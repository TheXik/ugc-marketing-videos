# UGC Marketing Videos — Knowledge Base

Everything researched about building an **AI UGC / content-marketing machine** for short-form video (TikTok / Instagram Reels). Consolidated from a deep research + multi-agent workflow effort in July 2026.

The goal: a repeatable, cheap pipeline to produce and distribute UGC-style short video content at scale — and the *strategy* to make it actually convert, not just rack up views.

## Index

| File | What's in it |
|------|--------------|
| [`research/01-tooling-and-repos.md`](research/01-tooling-and-repos.md) | **43 open-source repos ranked by live star count (28 Jul 2026)** — plus why ranking by stars puts you on 3 dead repos and 4 licence violations. Includes the 2026 "video-as-code" wave the first sweep missed (OpenMontage 43k★, HyperFrames 38k★). |
| [`research/02-api-pricing-and-free-trials.md`](research/02-api-pricing-and-free-trials.md) | Real cost per video. Gemini / ElevenLabs / fal.ai pricing, subscriptions vs pay-per-use, free trials. |
| [`research/03-platforms-and-funnels.md`](research/03-platforms-and-funnels.md) | UGCdrop, Higgs Field, "550 slideshows/day" — real tool vs affiliate funnel. **+ the X/Twitter sweep:** the 5-second bait diagnostic, the fake-free-repo archetype, and the only founder posting audited numbers (0.076% view→install). |
| [`strategy/04-content-strategy-playbook.md`](strategy/04-content-strategy-playbook.md) | **The verified 2026 playbook.** Persona-led education accounts, TikTok's AI-labeling constraint, hook templates, budget benchmarks, 30/60/90 plan. Cited + adversarially verified. |
| [`case-studies/05-lockin-case-study.md`](case-studies/05-lockin-case-study.md) | Worked example: applying all of this to LockIn (a focus/screen-time app). 6 angles, hook bank, a fully-spec'd reel. |
| [`prompts/06-ugc-reels-agent-kickoff.md`](prompts/06-ugc-reels-agent-kickoff.md) | The kickoff prompt to run a dedicated "UGC Reels" agent that continues building the machine. |
| [`prompts/07-seedance-ugc-prompt-anatomy.md`](prompts/07-seedance-ugc-prompt-anatomy.md) | The Shlabu/Arcads Seedance 2.0 workflow, deconstructed into reusable templates: character sheets, frame chaining, the 4-section video mega-prompt, batch automation — on fal at ~$1.50–2.50/video instead of Arcads' $11. |
| [`content/reel-01-screen-time-confession.md`](content/reel-01-screen-time-confession.md) | **First produced reel.** Complete copy-paste package: script, Higgsfield stills chain, the full Seedance mega-prompt, real-screenshot B-roll list, captions, ship checklist. ~$1.60. |
| [`strategy/08-budget-plan-10eur.md`](strategy/08-budget-plan-10eur.md) | **⭐ The costed plan: 50 reels/month for ≤€10.** Every path priced per reel, verified 28 Jul 2026. The €0 stack, the two AI options worth buying, the traps, and 12 corrections to claims elsewhere in this repo. **Start here.** |

## TL;DR — the machine in one paragraph

Produce **human / screen-recording-first** video (AI only writes the hooks & scripts — TikTok now reach-suppresses unlabeled AI *video*). Run it through the cheapest viable stack (**Gemini** free for scripts, **ElevenLabs** ~$6/mo for voice, **fal.ai** ~$1/video for any AI visuals, or **$0** real screenshots). Distribute through a **persona-led education account** (the proven 2026 pattern), not overt product ads or 550-post volume spam. Measure **signups / installs, never views.**

## Cost reality (re-verified 28 Jul 2026)
- Script (Gemini / Claude): **€0** (free tier) — and AI-written scripts are exempt from TikTok's AI-label rule
- Voice: **€0** — Kokoro-82M local (Apache-2.0) or Google Cloud TTS WaveNet free tier. ~~ElevenLabs $6~~ is now $22/mo
- AI video: **€0.11–0.15/reel** at the absolute floor (WaveSpeed, 480p) · **€0.126/reel** for genuinely postable
  720p (Freepik/Magnific, €72/yr) · **€0.40–0.55/reel** on fal · **€1.38/reel** on Higgsfield
- Real screen-recording / founder-shot content: **€0**, no AI-label penalty, and the best-converting format ← **do this**

> The €10/month budget is achievable three different ways — but every AI path assumes zero retries, and
> at €0.20/reel you can only buy cheap AI. Full math, traps and corrections in `strategy/08`.

## Status
Research complete and verified (confidence levels noted per claim). Next step: run the UGC Reels agent (`prompts/06`) to start producing the first test batch.
