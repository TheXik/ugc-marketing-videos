# API Pricing, Subscriptions & Free Trials

Real cost to generate one AI UGC video, per API, verified against live pricing pages (July 2026).

> ⚠️ **Partially superseded (28 Jul 2026).** A re-verification pass found four material errors below.
> See [`strategy/08-budget-plan-10eur.md`](../strategy/08-budget-plan-10eur.md) for corrected numbers and
> the €10/month plan. Summary of what changed:
> 1. **ElevenLabs Starter $6/mo is gone** — Creator is now **$22/mo for 100K chars** (~239% YoY). Replace with
>    **Kokoro-82M** (local, Apache-2.0, no watermark) or **Google Cloud TTS WaveNet** (1M chars/mo free).
>    Voice is now a €0 line item, not a $6 subscription.
> 2. **fal is cheaper than stated** — the cheapest usable route is €0.40–0.55 per finished 15s reel, not
>    ~$1.00–1.85. But it is still 2–2.8× over a €0.20/reel budget. (fal.ai/pricing now 429s behind a Vercel
>    checkpoint; read `https://fal.ai/api/models?keywords=<term>` for vendor-authoritative JSON instead.)
> 3. **Cheaper hosts exist than fal** — WaveSpeed `wan-2.2/i2v-480p-ultra-fast` at **$0.01/s** and
>    `infinitetalk-fast` at **$0.015/s flat** are ~4× below fal's floor. 480p only.
> 4. **FX was wrong** — this file assumed 1 USD = 0.92 EUR. ECB reference on 27 Jul 2026 is **0.878**.

## Cost per video, by API

| API | Job | Cost/video | Billing | Subscription? |
|-----|-----|-----------|---------|---------------|
| **Gemini** | Writes the script | ~$0.001 (≈ free) | Pay-per-use / free tier | ❌ No (but doesn't matter) |
| **ElevenLabs** | Voiceover (~30s) | ~$0.08–0.09 | **Subscription** | ✅ Yes — this IS the model |
| **fal.ai** | AI actor image + talking video + B-roll | **~$0.75–1.75** | Pay-per-use only | ❌ No subs, ever |
| | **Total** | **~$1.00–1.85 typical** | | |

Add retries (UGC needs ~2–3 takes for a usable one) → budget **~$2–5 raw compute per *shippable* video.**

## 1. Gemini (script) — effectively free
- Gemini 2.5 Flash-Lite: **$0.10 / $0.40** per 1M input/output tokens. A ~500-token ad script = a fraction of a cent.
- **Free tier** via Google AI Studio: ~1,500 scripts/day, $0, permanent (not a trial). Catch: free-tier prompts may be used to train Google's models.
- ❌ Consumer subs (Google AI Pro $20/mo, Ultra) give **zero API access** — chat app only. Irrelevant since the API is ~free anyway.

## 2. ElevenLabs (voice) — subscription IS the model
- Tiers: Free (10k credits/mo), **Starter $6**, **Creator $22**, Pro $99, Scale $299.
- ~1,000 chars = 1 min audio; a 30s script ≈ 400–500 chars.
- API draws from the **same monthly credit pool** as the web app — so a flat sub *replaces* usage billing.
- **Free tier = testing only** (requires attribution, **no commercial rights** — can't run as ads).
- Cheapest viable commercial plan: **Starter $6/mo** (~60 videos), step to **Creator $22/mo** (~240) at volume.

## 3. fal.ai (video) — 90%+ of your bill, always metered
Live pricing:

| Model | Unit | Price | Notes |
|-------|------|-------|-------|
| Qwen / Seedream V4 (image) | image | $0.02–0.03 | Actor image — rounding error |
| Wan 2.5 (video) | second | $0.05 | Workhorse |
| Kling 2.5 Turbo Pro (video) | second | $0.07 | Workhorse |
| Seedance 2.0 reference-to-video (720p) | second | $0.18 | Multi-reference character/product consistency (see `prompts/07`) |
| Seedance 2.0 fast / standard (720p) | second | $0.24 / $0.30 | Premium mid-tier; 1080p is $0.68/s ⛔ |
| **Veo 3 (video)** | second | **$0.40** | ⛔ Premium cinematic — AVOID for cheap-at-scale |
| Kling AI Avatar / VEED Fabric (talking) | second | $0.05–0.15 | Audio-driven avatar for true talking-head |
| Kling LipSync | ~5s block | $0.014 | Lip-sync onto existing video (near-free) |

- **Cheapest build:** image $0.03 + 8s talking $0.40 + 5s B-roll $0.25 ≈ **$0.70–0.85/video**.
- **Billing:** strictly prepaid credits. **No subscriptions, no bundles, ever.** GPU rental also available ($1.10–4.49/hr) for self-hosting.
- **Why video ≫ image/text:** an image is 1 frame (~1s GPU). A 6s clip is ~150–180 frames with temporal attention linking every frame → ~2 min GPU occupancy → ~100–200× the compute. You rent GPU-seconds; there's no way around it.

## Free trials — can you test for $0?

| API | Free to test? | Free to ship commercially? |
|-----|:---:|:---:|
| **Gemini** | ✅ permanent free tier (~1,500 scripts/day) | ✅ yes |
| **ElevenLabs** | ✅ 10k credits/mo | ❌ free tier = no commercial rights |
| **fal.ai** | ⚠️ one-time signup credit (~$1–20, no card) | ❌ then strictly metered |

**Repeated free video testing:** skip fal, use the native web apps — recurring daily free credits but **watermarked** and UI-only (not API):
- **Kling (kling.ai):** ~6 short watermarked videos/day, resets daily — best recurring free option.
- **Hailuo (hailuo.ai):** ~200 signup credits + daily login bonuses.

## Monthly cost model
- **30 videos/mo:** ElevenLabs Starter $6 + ~$30–55 fal ≈ **$40–60/mo**
- **100 videos/mo:** ElevenLabs Creator $22 + ~$100–185 fal ≈ **$120–210/mo**
- Gemini: ~$0

**Lever for cheaper unit economics at volume:** self-host the video/lip-sync stage (MuseTalk on a rented GPU ~$1.10–4.49/hr) instead of per-second fal fees — flips $1+/video to fractions of a cent once rendering in bulk, but you build & babysit the pipeline.

**Cheapest format of all:** real screen recording / screenshot + text hook + trending audio = **$0** and no AI-labeling penalty. Often the best-converting format for app content (see `strategy/04`).
