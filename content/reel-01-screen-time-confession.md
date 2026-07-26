# Reel 01 — "Screen-Time Confession" (LockIn, pre-launch)

**Status:** ready to produce · **Lane:** AI-actor → paid/test (AI-label it) · **Organic twin:** §9 ($0, no label)
**Angle:** #1 screen-time reveal, education-led · **CTA:** waitlist (app is NOT on the App Store)
**Cost:** ~$1.60 (8s Seedance 720p ref-to-video $1.45 + stills + VO) · budget $3–5 with retries

## 0. Integrity rules baked into this script

- ❌ No claim that anyone's screen time dropped **using LockIn** — the app has never run a real pact. Fabricated result = fake testimonial.
- ❌ No "download it / it's free, link in bio" — it isn't downloadable. CTA is **early access**.
- ❌ No staged "my friend denied me" — that feature isn't wired yet (`case-studies/05`).
- ✅ What the actor CAN say: her own screen-time shame (generic, relatable), why self-blocking fails (education), and that an app doing X is coming.

---

## 1. Structure (28s, only 8s is paid AI video)

| Time | Source | Content |
|------|--------|---------|
| 0:00–0:08 | **AI actor** (Seedance, 2 shots) | Hook + the "just delete the apps" objection |
| 0:08–0:20 | **Real screenshots** + VO | The insight (you negotiate with yourself and lose) |
| 0:20–0:28 | **Real app screens** + VO + card | The concept + early-access CTA |

Keeping B-roll on real assets is what holds cost at ~$1.60 instead of ~$5.

---

## 2. Voiceover script (~500 chars, ~28s)

> **[Shot 1 — on camera]**
> "I checked my screen time this morning and I genuinely need to lie down. Nine hours. On my phone."
>
> **[Shot 2 — on camera]**
> "And before anyone says 'just delete the apps' — I've deleted Instagram six times. I redownload it the same night."
>
> **[B-roll]**
> "That's the part nobody says out loud. At 1am the person you're negotiating with is you. And you always lose that one."
>
> **[B-roll + product]**
> "So the only thing that's ever actually worked is when someone else holds the line. There's an app coming that does exactly that — your friends hold the key, you can't unlock without them. It's called LockIn. Link's in my bio if you want in early."

**ElevenLabs delivery:** casual, spoken-to-a-friend. Slightly defeated on the first two lines → flat/honest on the insight → quietly hopeful on the last. Real sigh before "Nine hours." Do **not** use announcer energy. Model: Flash/Turbo v2.5 (~0.5 credit/char).

---

## 3. Stage 1 — Base image (Higgsfield Soul 2.0)

```
Candid unfiltered front-camera selfie of a 20-year-old university student sitting at a
cluttered desk in a small bedroom, early morning. Completely bare face — no makeup, no
filter. Visible pores across nose and cheeks, natural sebum sheen on the forehead and
T-zone, subtly uneven skin tone, one faint blemish near the jaw, slight under-eye shadow
from a short night. Zero skin smoothing, zero airbrushing, zero digital correction — skin
looks exactly as it would in an unfiltered front camera photo. Messy dark-blonde hair in a
loose bun with flyaway strands. Oversized grey hoodie, collar slightly twisted. Ambient
natural daylight through a window to camera-left as the primary light source, soft and
diffused, no harsh shadows, slight window overexposure behind her. Vertical selfie framing
— phone held at arm's length, near eye level, slight downward tilt; frame shows shoulders
up to just above the head. Background softly out of focus: unmade bed, open laptop, half-
full water glass, textbooks stacked at the desk edge. Shot on a modern smartphone front
camera, natural lens softness, no color grade. Authentic candid UGC energy.
```

## 4. Stage 2 — Character sheet (identity lock)

```
Character reference sheet, four-panel layout on a pure white seamless studio background.
Four head angles of the same young woman — fair complexion with warm undertone, dark-
blonde hair with lighter sun-faded ends, light freckling across the nose bridge and upper
cheeks, muted rose lip tone, straight medium-thick brows, grey-green eyes, soft oval face
with a defined jaw. Panel 1 — front facing. Panel 2 — clean 90° left profile, hair swept
back to reveal jaw, ear and neck. Panel 3 — right profile mirror. Panel 4 — back of head,
hair texture and crown volume. All four panels shot with an 85mm studio lens, soft large
diffused key light from front-above with gentle fill from below, clean separation from the
white background. Full visible skin texture — fine pores, natural freckle variation, zero
retouching. Individual hair strand separation, natural flyaways. Fashion casting card
aesthetic, clinical four-view character reference quality, 8K, tack-sharp on all panels.
```

> Save this sheet. It's the identity anchor for **every** future reel with this creator — that's how you get a consistent recurring "face" instead of a new random person each video.

## 5. Stage 3 — Scene still + Stage 4 — chain frame

**Scene still (start frame of Shot 1):** base image + character sheet as refs.
```
The woman from the multi-angle reference sheet — preserving her exact facial identity:
fair warm complexion, dark-blonde hair with sun-faded ends, freckling across nose bridge
and upper cheeks, muted rose lips, straight medium-thick brows, grey-green eyes, soft oval
face with defined jaw. Camera angle, framing and environment taken entirely from the desk
selfie photo — same arm's-length near-eye-level perspective, same shoulders-up framing,
same oversized grey hoodie, same cluttered desk with laptop and textbooks, same window
daylight from camera-left with slight overexposure behind her. Pose: one hand out of frame
holding the phone, the other resting on the desk near a mug, fingers relaxed, no reaching
toward the camera. Gaze directly into the lens. Expression written as behaviour: eyebrows
lifted slightly and held, mouth just parted as if she's about to admit something she finds
embarrassing — not smiling, not performing.
```

**Chain frame (end of Shot 1 = start of Shot 2):** regenerate the same still with
```
...adjusted: her free hand now lifted into the lower frame, palm half-open in a small
resigned shrug, caught mid-motion — just-settled, not posed. Head beginning to tilt a few
degrees to her right. Same lighting, same framing, same wardrobe.
```

> ⚠️ **Do not** ask the image model to render the LockIn UI on a phone screen — it will garble it. Cut to the real screenshot full-frame in CapCut instead (§7).

---

## 6. Stage 5 — Seedance 2.0 mega-prompt

```
IMAGE REFERENCE MAP
Image 1 (scene_still_desk)  → first frame / opening scene. The student, primary talent for Shot 1.
Image 2 (char_sheet_4panel) → character reference — face, hair, skin tone, freckles, bone structure.
Image 3 (chain_frame_shrug) → start frame for Shot 2. Same woman, hand risen into lower frame.

SECTION 1: EFFECTS TIMELINE

SHOT 1 / MOMENT (0:00–4:00s) — "Snap Open, The Confession"
EFFECT: jump-cut snap open + handheld selfie hold + slow push-in + [SIGNATURE] flinch punch-in
No fade, no warmup — the clip starts with her already mid-sentence, talking straight into the
lens: "I checked my screen time this morning and I genuinely need to lie down." Delivery is
low-energy and embarrassed, not performative — the pace of someone confessing, with a real
audible breath before the next line. Frame pushes in slowly, ~6% scale over the first three
seconds, phone held in one hand so there is constant handheld micro-bounce on every syllable
— alive, not shaky. Then the SIGNATURE VISUAL EFFECT lands on the words "Nine hours": a hard
punch-in of ~12% scale over 4 frames combined with a 3-frame vertical dip of the whole frame,
as if her hand physically flinched. It resolves immediately and holds. Her eyes drop away from
the lens for roughly half a second on "On my phone", then come back up. Transition out: a hard
jump cut on the beat — no dissolve.

SHOT 2 / MOMENT (4:00–8:00s) — "The Objection"
EFFECT: jump-cut entry + handheld bounce + two digital zoom pulses + held human beat
She is already talking when the cut lands — mid-word, as if the boring part was trimmed out:
"And before anyone says 'just delete the apps' — I've deleted Instagram six times. I redownload
it the same night." Delivery is faster and flatter than Shot 1, slightly defensive, like she has
had this argument before. Her free hand rises into the lower frame in a small resigned shrug on
"six times" — natural, low, not a gesture performed for camera. First digital zoom pulse of
~10% over "just delete the apps", a second smaller pulse of ~6% snapping on the word "same
night". Head tilts a few degrees right as she says it. End on a held human beat: roughly half a
second of her just looking at the lens after the line, no smile, one slow blink, window light
blowing out slightly behind her shoulder.

SECTION 2: MASTER EFFECTS INVENTORY
Snap open (jump-cut entry) — used 2x, Shots 1 and 2. No fade, no build; starts at full energy.
Flinch punch-in — used 1x, Shot 1 on "Nine hours". ~12% scale over 4 frames + 3-frame vertical
  dip. THE signature moment of the video.
Digital zoom / push-in — used 3x total. Slow 6% in Shot 1; 10% and 6% pulses in Shot 2. Emulates
  TikTok emphasis zoom, synced to words not to time.
Handheld selfie bounce — throughout, both shots. Micro-movement on every syllable. Wrist-held,
  never stabilized.
Gaze break — used 2x. Half-second look-away in Shot 1, one slow blink in Shot 2. The human tell.
Natural window daylight — throughout. Slight overexposure behind the subject, raw phone-camera
  skin, visible pores and sebum sheen. NO COLOR GRADE.
Shallow depth of field — both shots. Desk and bed always softer than her face.

SECTION 3: EFFECTS DENSITY MAP
0:00–2:00s = MEDIUM DENSITY (3 effects) — settle in, let the confession land
2:00–4:00s = HIGH DENSITY (4 effects)   ← the peak, the flinch punch-in on "Nine hours"
4:00–8:00s = MEDIUM DENSITY (3 effects) — recover, end on a held human beat

SECTION 4: MOTION FLOW
Opening: no warmup — the clip snaps in hot, she is already mid-confession.
Build: everything runs toward the flinch punch-in on "Nine hours". That is the payoff; the whole
  first shot is setup for it and the second shot is the aftershock.
Resolution: energy drops just enough to feel real. Ends on her holding the lens after the line —
  slightly defeated, still charged. You felt the shame and it didn't try too hard.
```

**Settings:** Seedance 2.0 reference-to-video, 720p, 9:16, 8s (or 2× 4s stitched on the chain frame).

---

## 7. B-roll edit list (real assets — $0, no AI)

| Cut | Asset | Direction |
|-----|-------|-----------|
| 0:08–0:12 | **Your real iOS Screen Time screenshot** | Full-frame, slow 5% Ken Burns push-in. Red circle drawn on the total. |
| 0:12–0:16 | `screens/home.png` | Slow push-in on the focus ring with Petr + Jakub orbiting |
| 0:16–0:22 | `screens/locked.png` | Hold on **"The only way back in is to ask Petr or Jakub. They hold the key."** — this line IS the product; let it breathe |
| 0:22–0:28 | `screens/locked.png` → end card | Push to the "Request Unlock" button, then cut to a black card: **LockIn · early access · locked-in.dev** |

> 🔧 **Re-shoot the screenshots first.** Both currently read `0 apps` / `0 BLOCKED` — that looks broken on camera. Run a real lock with 4–5 apps selected and re-capture `home` and `locked` so the numbers are non-zero.

## 8. On-screen captions (key words only, native TikTok style)

`9 HOURS 😭` → `on my PHONE` → `"just delete the apps"` → `deleted IG 6 times` → `you always lose at 1am` → `your friends hold the key` → `LockIn` → `early access · link in bio`

---

## 9. The $0 organic twin (make this one too)

Same script, **you on camera** (or just voice), no AI actor:
your real screen-time screenshot → the same real app screens → same VO.
Cost $0, no AI label, no reach suppression — and per `strategy/04` this is the version that
should carry the **organic** account. Post the AI version as a paid/test creative or a
labeled variant, and compare signups, not views.

## 10. Ship checklist
- [ ] Re-capture `home.png` / `locked.png` with non-zero numbers
- [ ] Base image → character sheet → scene still → chain frame (Higgsfield)
- [ ] 8s Seedance render, 720p 9:16
- [ ] ElevenLabs VO, Flash v2.5, casual delivery
- [ ] Assemble in CapCut: AI 8s + B-roll + captions + trending audio bed low
- [ ] **Toggle the AI-generated label** before posting
- [ ] Bio link → locked-in.dev waitlist; verify the waitlist form actually records the signup
- [ ] Track: signups, not views
