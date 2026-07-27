# Character library — permanent identity assets

Generated on the Higgsfield 3-day MCP trial (2026-07-27), ~1 credit each. **These outlive the
trial.** After it expires you reuse these PNGs as reference images for
`fal.ai` → `bytedance/seedance-2.0` reference-to-video at $0.18/s — no Higgsfield subscription
needed. That's why they were worth generating before the credits expired.

Model: `soul_2`, 3:4, 2k. Built from `prompts/07-seedance-ugc-prompt-anatomy.md` +
the Higgsfield `ugc-saas-flow` character rules (variety roll, beauty floor, modesty language,
cool-daylight-only, anti-editorial bans, iPhone-selfie closing block).

## The roster

| File | Persona | Identity | Job ID |
|---|---|---|---|
| `p1-creator-bedroom.png` | **Persona / engine** | late 20s W · chestnut shoulder-length wavy · athletic · nose stud · bold liner · warm Mediterranean · sporty-jersey · bedroom | `705d1de4-43fc-4342-83cb-152412c357eb` |
| `p1-creator-kitchen.png` | same identity, 2nd setting | ↑ same face · clean-minimalist bone knit · kitchen counter | `bb96a46d-42c0-46fb-9af1-ffdf2cbe43d8` |
| `p2-selfimprovement-guy.png` | **Self-improvement / "lock in"** | late 20s M · ash-blonde short crop · average build · eyebrow piercing · East Asian · Y2K track jacket · kitchen | `f3b0cd4e-7f6a-41a5-a203-8ca96a1632a0` |
| `p3-doomscroll-normie.png` | **Doomscroll-guilt normie** | early 20s W · soft brown pixie · soft natural · freckles · winged liner · Middle Eastern · oversized crewneck · student flat couch | `df5c6446-ca59-49de-aef4-027dd6b78255` |

`p1-creator-bedroom.png` is the one used in `reel01-lockin-ugc.mp4`.

## How to reuse

**Same identity, new video** — pass the PNG (or the job ID, while on Higgsfield) as the
reference image. Never re-describe the person in the video prompt; the reference carries the face.

```
fal: bytedance/seedance-2.0 reference-to-video
  reference_image: p1-creator-bedroom.png
  prompt: <framing + setting + delivery + spoken line + audio + the no-screens ban>
```

**Two settings per identity** (p1 has bedroom + kitchen) means the account doesn't look like the
same shot every post while still being recognisably one creator — that recognition is the whole
point of the persona account (`strategy/04`).

## Rules that produced these (keep them)

- Variety roll before every new identity so faces don't converge
- Cool neutral daylight only, direction stated — **golden hour is banned**, it reads as AI
- Modesty language on every outfit — prevents downstream NSFW rejections on the video step
- One mid-action expression, never "warm smile at camera"
- Close every prompt with the iPhone-selfie block verbatim
- Never repeat the previous identity's age + hair + build combo

## Reminder
Any video built on these contains a synthetic human → **turn on the AI-generated label** when
posting (`strategy/04`).
