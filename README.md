# UGC Marketing Videos — Knowledge Base

Everything researched about building an **AI UGC / content-marketing machine** for short-form video (TikTok / Instagram Reels). Consolidated from a deep research + multi-agent workflow effort in July 2026.

The goal: a repeatable, cheap pipeline to produce and distribute UGC-style short video content at scale — and the *strategy* to make it actually convert, not just rack up views.

## Index

| File | What's in it |
|------|--------------|
| [`research/01-tooling-and-repos.md`](research/01-tooling-and-repos.md) | Open-source UGC-generation repos, ranked. Winner: **openshorts**. What to fork, what to avoid. |
| [`research/02-api-pricing-and-free-trials.md`](research/02-api-pricing-and-free-trials.md) | Real cost per video. Gemini / ElevenLabs / fal.ai pricing, subscriptions vs pay-per-use, free trials. |
| [`research/03-platforms-and-funnels.md`](research/03-platforms-and-funnels.md) | UGCdrop, Higgs Field, "550 slideshows/day" — what's a real tool vs an affiliate/lead-gen funnel. |
| [`strategy/04-content-strategy-playbook.md`](strategy/04-content-strategy-playbook.md) | **The verified 2026 playbook.** Persona-led education accounts, TikTok's AI-labeling constraint, hook templates, budget benchmarks, 30/60/90 plan. Cited + adversarially verified. |
| [`case-studies/05-lockin-case-study.md`](case-studies/05-lockin-case-study.md) | Worked example: applying all of this to LockIn (a focus/screen-time app). 6 angles, hook bank, a fully-spec'd reel. |
| [`prompts/06-ugc-reels-agent-kickoff.md`](prompts/06-ugc-reels-agent-kickoff.md) | The kickoff prompt to run a dedicated "UGC Reels" agent that continues building the machine. |
| [`prompts/07-seedance-ugc-prompt-anatomy.md`](prompts/07-seedance-ugc-prompt-anatomy.md) | The Shlabu/Arcads Seedance 2.0 workflow, deconstructed into reusable templates: character sheets, frame chaining, the 4-section video mega-prompt, batch automation — on fal at ~$1.50–2.50/video instead of Arcads' $11. |
| [`content/reel-01-screen-time-confession.md`](content/reel-01-screen-time-confession.md) | **First produced reel.** Complete copy-paste package: script, Higgsfield stills chain, the full Seedance mega-prompt, real-screenshot B-roll list, captions, ship checklist. ~$1.60. |

## TL;DR — the machine in one paragraph

Produce **human / screen-recording-first** video (AI only writes the hooks & scripts — TikTok now reach-suppresses unlabeled AI *video*). Run it through the cheapest viable stack (**Gemini** free for scripts, **ElevenLabs** ~$6/mo for voice, **fal.ai** ~$1/video for any AI visuals, or **$0** real screenshots). Distribute through a **persona-led education account** (the proven 2026 pattern), not overt product ads or 550-post volume spam. Measure **signups / installs, never views.**

## Cost reality
- Script (Gemini): ~$0 (free tier)
- Voice (ElevenLabs): ~$0.08/video, or a $6/mo sub
- AI video (fal.ai): ~$1/video, unavoidably metered (no subscription option)
- Real screen-recording / screenshot content: **$0** and no AI-labeling penalty ← often the best format

> Full budget math and per-model pricing in `research/02`.

## Status
Research complete and verified (confidence levels noted per claim). Next step: run the UGC Reels agent (`prompts/06`) to start producing the first test batch.
