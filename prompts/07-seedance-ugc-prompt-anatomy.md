# Seedance 2.0 UGC Prompt Anatomy — the Shlabu/Arcads Workflow, Deconstructed

Source: "Arcads UGC Tutorial" by Shlabu (craft.do doc, July 2026). The tutorial itself is a funnel into his paid "A.I Creator School" skool community (see `research/03`) — but the technique is real and fully documented in the doc itself. **Nothing here requires Arcads.** Seedance 2.0 is officially on fal.ai (`bytedance/seedance-2.0`, incl. a reference-to-video endpoint), so the whole pipeline runs on our existing stack at pay-per-use instead of Arcads' ~$11/video.

⚠️ This produces **fully synthetic humans** → TikTok AI-labeling applies. Per `strategy/04`: paid-ads and B-roll lane only, not organic.

## The pipeline (5 stages)

```
1. Base image      → hyper-real "candid selfie" still  (Higgsfield Soul 2.0 / any realism model)
2. Character sheet → 4-panel identity reference          (GPT Image 2)
3. Scene stills    → base + sheet + product as refs      (GPT Image 2)
4. Frame chaining  → end-frame of clip N = start of N+1
5. Video           → Seedance 2.0 reference-to-video, one mega-prompt per clip
```

### Stage 1 — Base image: the realism checklist

What makes the still read as a real phone photo (from the tutorial's Higgsfield Soul 2.0 prompt, reusable with any image model):

- **Anti-beauty clauses, stated explicitly:** "completely bare face — no makeup", "visible pores, natural sebum sheen, subtle uneven tone, faint blemishes", "**zero skin smoothing, zero airbrushing, zero digital correction** — skin looks exactly as it would in an unfiltered front camera photo."
- **Named light source:** "ambient natural daylight through the panoramic windshield as primary light source, soft and diffused, no harsh shadows."
- **Phone-camera framing spec:** "horizontal selfie framing — camera held at arm's length or propped, near eye level", "frame shows shoulders up to mid chest."
- **A mundane, specific location:** driver's seat of a Tesla, white vegan leather, cabin softly out of focus.
- Closing vibe keyword: *"Authentic candid UGC energy."*

### Stage 2 — Character sheet (identity lock)

One GPT Image 2 generation, then reused as a reference in every later step:

> "Character reference sheet, four-panel layout on a pure white seamless studio background. Four head angles of the same young woman — [detailed identity: complexion, hair with highlight range, freckle placement, lip tone, brow shape, eye color, bone structure]. Panel 1 — front facing … Panel 2 — clean 90° left profile, hair swept back to reveal jaw/ear/neck … Panel 3 — right profile mirror … Panel 4 — back of head, hair texture and crown volume. All four panels shot with an 85mm studio lens, soft large diffused key light from front-above with gentle fill from below, clean separation from white background. Full visible skin texture — fine pores, natural freckle variation, zero retouching. Individual hair strand separation, natural flyaways. Fashion casting card aesthetic, clinical four-view character reference quality, 8K, tack-sharp on all panels."

### Stage 3 — Scene stills (identity + environment inheritance + product)

Inputs: character sheet + base photo + **product image**. The prompt has three mandatory blocks:

1. **Identity preservation clause:** "the woman from the multi-angle reference sheet — preserving her exact facial identity: [repeat the identity list verbatim]."
2. **Environment inheritance clause:** "Camera angle, framing, and environment taken **entirely from the car photo** — same low propped-camera perspective, same mid-chest-up framing, same white ribbed top, same cream leather interior with seatbelt visible left side, same foliage through rear window, same warm daylight."
3. **Pose micro-spec** (this is what stops AI-weirdness): hands ("both hands wrapped loosely around the cup, fingers curled naturally, condensation visible, straw pointing upward"), arms ("bent inward, elbows down, **no arm reaching forward**"), gaze ("upward and to one side — not at the camera"), expression written as behavior, not adjectives ("barely-there smile pulling at one corner — asymmetric, not posed … the kind of look that comes right before saying something she shouldn't").

Swap the product reference per variant → same shot, different product.

### Stage 4 — Frame chaining (seamless multi-shot)

Generate an **adjusted still that ends clip 1 and starts clip 2** (e.g., "add both hands visible in the lower frame, positioned as if she just finished propping the camera — mid-motion, just-settled, not posed"). Stitching two 4s clips at a shared frame reads as one continuous ~8s video.

### Stage 5 — The Seedance 2.0 mega-prompt (the core template)

Seedance rewards extreme specificity. The tutorial's structure, verbatim as a fill-in skeleton:

```
IMAGE REFERENCE MAP
Image 1 ([name]) → first frame / opening scene. [Who/what, role: "primary talent for Shot 1"]
Image 2 ([name]) → [character reference — face, hair, skin tone]
Image 3 ([name]) → [second character / product reference, when it enters]

SECTION 1: EFFECTS TIMELINE
SHOT 1 / MOMENT (0:00–1:20s) — [label, e.g. "Snap Open, Woman to Camera"]
EFFECT: [effect stack, e.g. jump-cut snap open + handheld selfie hold + fast push-in]
[Prose: what happens, the spoken line in quotes + delivery ("fast, punchy, no pause"),
 camera behavior with NUMBERS ("frame auto-pushes in ~8–10% scale over the line"),
 micro-realism ("handheld micro-bounce on every syllable — not shaky, but alive"),
 the transition out ("she physically FLIPS the camera — fast wrist snap, frame
 motion-blurs in the direction of the swing").]

SHOT 2 / MOMENT (1:20–2:20s) — [label]
EFFECT: whip pan (wrist flip) + motion blur smear + rack focus snap
[Designate ONE "SIGNATURE VISUAL EFFECT" per video. Spec it in frames:
 "~10–15 frames of directional smear, then snaps sharp on his face."
 Human details: "he's already looking toward the camera when it arrives — like he
 knew it was coming", "camera landing has a tiny overshoot and settle — natural
 phone physics, not mechanical."]

SHOT 3 / MOMENT (2:20–4:00s) — [label]
EFFECT: digital zoom (two pulses) + handheld bounce + natural hold
[Sync zooms to words: "~10–12% zoom-in over the first three words … second smaller
 pulse on the payoff word." End on a held human beat: "half-second hold on his
 profile, sun catching his hair, slight smile still visible."]

SECTION 2: MASTER EFFECTS INVENTORY
[Every effect, usage count, spec — e.g.:]
Snap open (jump-cut entry) — used 1x, Shot 1. No fade, no build — starts at full energy.
Digital zoom / push-in — used 3x. Each pulse is 8–12% scale increase. Emulates TikTok emphasis zoom.
Handheld selfie bounce — throughout. Micro-movement on every syllable. Wrist-held, not stabilized.
Whip pan — used 1x, Shot 1→2 transition. The signature kinetic moment.
Motion blur smear — used 1x, mid-whip. ~10–15 frames horizontal, resolves sharply.
Rack focus snap — used 1x, Shot 2 landing. Instant pull from blur to sharp lock.
Natural daylight interior exposure — throughout. Bright window overexposure, raw phone-camera skin. NO GRADE.
Shallow depth of field / bokeh — all shots. Background always softer than subject.

SECTION 3: EFFECTS DENSITY MAP
0:00–1:20s = MEDIUM DENSITY (3 effects)
1:20–2:20s = HIGH DENSITY (4 effects)   ← the peak
2:20–4:00s = MEDIUM DENSITY (3 effects)

SECTION 4: MOTION FLOW
Opening: [no warmup — clip snaps in hot, already talking]
Build: [name the peak kinetic moment; "everything before it is setup, everything after is payoff"]
Resolution: [energy drops "just enough to feel real … ends relaxed but still charged —
 you felt something and it didn't try too hard"]
```

**Why it works:** the four sections force (a) explicit image-to-role mapping, (b) per-shot camera physics with numbers, (c) a global consistency check (inventory), (d) pacing control (density map + flow arc). It's a shot list + edit spec, not a "vibe" prompt.

## Batch automation (the Arcads node trick, minus Arcads)

The tutorial's canvas automation = 10 nodes with different product refs → run all → 10 videos, same model, different products (or same product × 10 characters). On our stack that's a **loop over fal API calls**: fix character sheet + scene prompt, iterate the product reference (or fix the product, iterate character sheets). openshorts' queue or a 20-line script does the same job.

## Cost on our stack (fal.ai, verified July 2026)

| Endpoint (720p) | $/s | 8s two-shot video |
|---|---|---|
| Seedance 2.0 **reference-to-video** | $0.1814 | **~$1.45** |
| Seedance 2.0 fast (image-to-video) | $0.2419 | ~$1.94 |
| Seedance 2.0 standard | $0.3034 | ~$2.43 |
| Seedance 2.0 standard **1080p** | $0.682 | ~$5.46 ⛔ |

- - stills: a few cents (GPT Image 2 / Seedream). Budget **~$1.50–2.50 per shippable 720p video** before retries — vs **~$11/video on Arcads** (Starter $110/10 videos, regenerations burn full credits).
- Seedance 2.0 is a **premium tier**, 3–5× the Wan 2.5 / Kling workhorses ($0.05–0.07/s, see `research/02`). Use it when the multi-reference character/product consistency is the point; use the workhorses for everything else.
- Higgsfield Soul 2.0 (stage 1) is subscription-gated — see the Higgs Field funnel warning in `research/03`. The realism checklist transfers to any strong image model; the exact tool doesn't matter.
