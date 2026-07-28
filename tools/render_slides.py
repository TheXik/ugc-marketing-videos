#!/usr/bin/env python3
"""Render Instagram carousel slides from a JSON deck.

Why Pillow and not an image model: ~90% of carousel slides are typography on a flat
background. Benchmarked on an M2/8GB this renders 80 slides in ~2s (26ms/slide) — about
1000x faster than any generative model, brand-exact, and free forever. Reserve AI image
generation for the 1-2 genuine picture slides per carousel (Cloudflare Workers AI,
flux-1-schnell, Apache-2.0).

Output is 1080x1350 (4:5) JPEG. NOT 9:16 — the Instagram feed API rejects 1080x1920
stills. JPEG, not PNG — the Graph API rejects PNG.

Usage:
    python3 render_slides.py deck.json -o out/carousel-01
    python3 render_slides.py deck.json -o out/x --bench
"""

import argparse
import json
import pathlib
import sys
import time

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
MARGIN = 96

# LockIn "Ember" tokens — same values as lockin-web/src/app/tokens.css
INK = "#F7F4ED"
INK_2 = "#ABA398"
INK_3 = "#8A8175"
FLAME = "#FFD60A"
EMBER = "#FF8A34"
GROUND = "#0B0A09"
RAISED = "#17140F"
ACCENT_INK = "#17140F"

# macOS system faces. Helvetica is present on every macOS install; the heavy weights
# carry the display voice without shipping a font file.
FONT_CANDIDATES = {
    "heavy": [
        "/System/Library/Fonts/Supplemental/Helvetica.ttc",
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/Library/Fonts/Arial Black.ttf",
    ],
    "mono": [
        "/System/Library/Fonts/Menlo.ttc",
        "/System/Library/Fonts/SFNSMono.ttf",
    ],
}


def load_font(kind: str, size: int) -> ImageFont.FreeTypeFont:
    for path in FONT_CANDIDATES[kind]:
        if pathlib.Path(path).exists():
            try:
                # index 1 of Helvetica.ttc is Bold; harmless if the face has no such index
                return ImageFont.truetype(path, size, index=1 if kind == "heavy" else 0)
            except Exception:
                try:
                    return ImageFont.truetype(path, size)
                except Exception:
                    continue
    return ImageFont.load_default(size)


def wrap(draw, text, font, max_w):
    """Greedy wrap on real measured width."""
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=font) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def fit_block(draw, text, kind, max_w, max_h, start, floor=44):
    """Shrink until the wrapped block fits the box. Returns (font, lines, line_h)."""
    size = start
    while size >= floor:
        font = load_font(kind, size)
        lines = wrap(draw, text, font, max_w)
        line_h = int(size * 1.14)
        if len(lines) * line_h <= max_h:
            return font, lines, line_h
        size -= 4
    font = load_font(kind, floor)
    return font, wrap(draw, text, font, max_w), int(floor * 1.14)


def draw_slide(slide, index, total):
    template = slide.get("template", "statement")
    bg = RAISED if template == "answer" else GROUND
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)

    # Warm hearth glow at the top, matching the app's lockInScreenBackground
    for y in range(0, 520):
        t = 1 - (y / 520)
        d.line(
            [(0, y), (W, y)],
            fill=(
                int(int(bg[1:3], 16) + 26 * t * t),
                int(int(bg[3:5], 16) + 16 * t * t),
                int(int(bg[5:7], 16) + 4 * t * t),
            ),
        )

    inner = W - MARGIN * 2

    # Two passes: measure the whole block, then draw it optically centred. Top-aligning
    # short slides leaves a dead lower half, which reads as an unfinished template.
    blocks = []  # (kind, payload, height)

    kicker = slide.get("kicker")
    if kicker:
        blocks.append(("kicker", (load_font("mono", 27), kicker.upper()), 62))

    head = slide.get("headline", "")
    if head:
        hf, lines, lh = fit_block(d, head, "heavy", inner, 700, 106)
        blocks.append(("lines", (hf, lines, lh, INK), len(lines) * lh))

    if accent := slide.get("accent"):
        af, alines, alh = fit_block(d, accent, "heavy", inner, 320, 96)
        blocks.append(("gap", None, 10))
        blocks.append(("lines", (af, alines, alh, FLAME), len(alines) * alh))

    if body := slide.get("body"):
        bf, blines, blh = fit_block(d, body, "heavy", inner, 340, 44, floor=34)
        blocks.append(("gap", None, 34))
        blocks.append(("lines", (bf, blines, blh, INK_2), len(blines) * blh))

    total_h = sum(b[2] for b in blocks)
    # Sit slightly above true centre — the CTA and rail live in the lower third.
    top = MARGIN + 8
    avail = (H - 150) - top
    y = top + max(0, (avail - total_h) // 2 - 40)

    for kind, payload, height in blocks:
        if kind == "gap":
            y += height
        elif kind == "kicker":
            kf, text = payload
            x = MARGIN
            for ch in text:
                d.text((x, y), ch, font=kf, fill=INK_3)
                x += d.textlength(ch, font=kf) + 3.4
            y += height
        else:
            font, lines, lh, colour = payload
            for line in lines:
                d.text((MARGIN, y), line, font=font, fill=colour)
                y += lh

    # CTA pill, bottom-left
    cta = slide.get("cta")
    if cta:
        cf = load_font("heavy", 42)
        tw = d.textlength(cta, font=cf)
        bx0, by0 = MARGIN, H - MARGIN - 96
        d.rounded_rectangle(
            [bx0, by0, bx0 + tw + 76, by0 + 92], radius=46, fill=FLAME
        )
        d.text((bx0 + 38, by0 + 22), cta, font=cf, fill=ACCENT_INK)

    # Progress rail — tells the viewer there is more to swipe to
    rail_y = H - 54
    seg = (W - MARGIN * 2) / total
    for i in range(total):
        x0 = MARGIN + seg * i
        d.rounded_rectangle(
            [x0, rail_y, x0 + seg - 10, rail_y + 7],
            radius=4,
            fill=FLAME if i == index else "#3A3227",
        )

    return img


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck", help="JSON file: {caption, slides:[{kicker,headline,...}]}")
    ap.add_argument("-o", "--outdir", required=True)
    ap.add_argument("--bench", action="store_true", help="print timing")
    args = ap.parse_args()

    deck = json.loads(pathlib.Path(args.deck).read_text())
    slides = deck["slides"]
    if len(slides) > 10:
        sys.exit(f"error: {len(slides)} slides — the Instagram carousel API caps at 10")

    out = pathlib.Path(args.outdir)
    out.mkdir(parents=True, exist_ok=True)

    t0 = time.perf_counter()
    for i, slide in enumerate(slides):
        # JPEG q92: the Graph API rejects PNG outright
        draw_slide(slide, i, len(slides)).save(
            out / f"{i + 1:02d}.jpg", "JPEG", quality=92, optimize=True
        )
    dt = time.perf_counter() - t0

    if caption := deck.get("caption"):
        (out / "caption.txt").write_text(caption)

    print(f"{len(slides)} slides -> {out}")
    if args.bench:
        print(f"{dt * 1000:.0f}ms total, {dt / len(slides) * 1000:.1f}ms/slide")


if __name__ == "__main__":
    main()
