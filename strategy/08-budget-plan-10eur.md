# The €10/month Plan — 50 reels, verified July 2026

Target: **~50 finished 15s vertical reels per month for ≤ €10/month** = **€0.20 per reel.**
Output of a 12-agent research + adversarial-verification workflow (28 July 2026). Every price below was
re-checked against a live vendor page; the ones that failed verification are listed as ❌ with the correction.

FX used: **1 USD = 0.878 EUR** (ECB reference, 27 Jul 2026). The old `research/02` figures used 0.92 — every
USD price in this repo was overstated by ~4.6%.

---

## 1. The answer in one table

Cost of ONE finished 15s vertical reel. "All-AI" = 3× 5s generated clips. "Hybrid" = 1 AI clip + your own footage.

| Path | €/reel | 50 reels/mo | Fits €10? | Honest quality |
|---|---:|---:|:---:|---|
| **Your phone + iOS screen recording** | **€0.00** | **€0.00** | ✅ | Best-performing format available to you |
| **Freepik/Magnific Premium** (annual) | €0.126 | €6.00/mo* | ✅ | Kling 2.5 720p — genuinely postable |
| **WaveSpeed InfiniteTalk Fast** (8s AI hook + 7s real) | €0.11 | €5.52/mo | ✅ | 480p, plasticky — reads as AI |
| **WaveSpeed Wan 2.2 480p Ultra Fast** (silent B-roll) | €0.147 | €7.36/mo | ✅ | B-roll only, no faces |
| **fal.ai** `ltx-2-19b/distilled/audio-to-video` + fal TTS | €0.117 | €5.84/mo | ⚠️ | Cheapest talking head anywhere — **lipsync unproven**, see §4b |
| **fal.ai** same, hybrid (5s AI hook + your screen rec) | **€0.039** | **€1.95/mo** | ✅ | Only variant with real retry headroom |
| RunPod RTX 4090 self-host, 480p | ~€0.19 | ~€10/mo | ⚠️ | Only with zero wasted GPU minutes |
| HeyGen API, Avatar III | €0.24 (+€0.88/avatar) | €12/mo | ❌ | 2023-era corporate presenter |
| Kling AI Standard (annual) | — | €5.79/mo but only **~11 reels** | ❌ | Good quality, fails on volume |
| Novita Vidu Q3 Turbo 720p (off-peak) | €0.37 | €18.50/mo | ❌ | Postable; 1.9× over |
| **openshorts** on fal, as shipped | €0.80 | ~€40/mo | ❌ | 4× over — see §4b. Its own cost figures are guesses |
| **Higgsfield** | €1.38 (API) | €69/mo — or €39/mo floor, annual-only | ❌ | Your read was right. ~7× over |
| Replicate | €0.97–3.45 | €48–172/mo | ❌ | Same weights as fal, 25–180% markup |
| Bought human UGC (Billo/Fiverr) | €91–143 | €4,550+/mo | ❌ | 455–715× over |

\* €72 charged upfront for 12 months. Month-to-month is €16/mo — over budget.

**The budget is achievable. Three separate paths clear it.** But see §2 before you pick one.

---

## 2. The three things that actually decide this

**a) Every AI path that fits €10 assumes ZERO retries.** UGC needs 2–3 takes per usable shot. Freepik's
nominal 47 reels/month becomes ~16–24 keepers. WaveSpeed's 90 becomes ~30–45. Kling's own consumer app
burns credits on failed generations with no refund (the API refunds; the app doesn't). Halve or third
every AI number in the table above before planning against it.

**b) At €0.20/reel you cannot buy good AI — only cheap AI.** €0.11/reel buys a 480p, step-distilled,
Wan-2.1-era talking avatar in mid-2026, aimed at the most AI-literate cohort alive. The cheapest point
where an AI face stops reading as AI is WaveSpeed InfiniteTalk 720p at €0.83/reel — **4.1× over budget.**
That gap is the whole story.

**c) The binding constraint is time, not money.** 50 reels/month ≈ **20–24 h/month (~5–6 h/week)**:
~2h scripting, ~2h capturing a reusable B-roll library, ~5–8h assembly, ~1.5h/wk queue refills, ~2h
analytics, ~8h replying to comments (the least skippable — reply engagement is where TikTok reach
compounds). [Confidence: LOW–MEDIUM — derived estimate, not a sourced benchmark.]
Opal's "Olivia Unplugged" — the direct-competitor proof point — was a full-time social manager's job.

---

## 3. Recommended stack — €0/month

Spend nothing on video generation. Build all 50 reels from real footage. For LockIn specifically this is
not a compromise: the product's entire claim is that **real friends** hold your key. A labelled AI avatar
delivering a fake testimonial about beating doomscrolling is a self-refuting ad.

| Stage | Tool | Cost | Licence note |
|---|---|---:|---|
| Capture | iPhone camera + iOS screen recording | €0 | — |
| Edit | **Instagram Edits** (4K, no watermark) | €0 | Preferred over CapCut |
| Slides/carousels | Canva Free + TikTok Photo Mode | €0 | — |
| Script/hooks | Claude or Gemini free tier | €0 | AI-written scripts are **exempt** from TikTok's label rule |
| Voiceover (if not your own) | **Kokoro-82M** local | €0 | Apache-2.0, no audio watermark, #1 TTS-Arena Jan 2026 |
| Voiceover (hosted alt) | Google Cloud TTS WaveNet | €0 | 1M chars/mo free ≈ 4,500 reels. [Confidence: MEDIUM] |
| Captions | whisper.cpp large-v3-turbo + ffmpeg ASS burn-in | €0 | MIT, ~8s/reel on M-series |
| Stills / thumbnails | FLUX.1 **schnell** via Draw Things | €0 | Apache-2.0 — `dev` is non-commercial, don't use it |
| Batch rendering | **Remotion** | €0 | Free License covers orgs ≤ 3 people; jumps to $100/mo at 4 |
| Scheduling | **Buffer Free** | €0 | 3 channels, rolling 10-post queue, direct TikTok/IG publish |
| Analytics | **PostHog Free** (EU cloud, already provisioned) | €0 | 1M events/mo |
| Automation glue | Make Free (1,000 ops) or n8n Community | €0 | Never automate the edit, comments, or DMs |
| **Total** | | **€0.00/mo** | |

**Format mix for 50/month:** ~25 photo-mode carousels (real Screen Time screenshots + text slides,
5–10 min each) · ~15 founder talking-heads (batch-film 12 in one 90-min session) · ~10 screen-recording
"app flash" moments (1–2s of LockIn inside otherwise non-promotional content — not full demos).

**Spend the €10 once, not monthly:** a phone tripod/clamp. It's the only purchase here with positive ROI.

---

## 4. If you want an AI layer anyway

Only after the free stack is running, and only as a **B-roll / hero-shot layer** — never the main engine.

**Option A — Freepik/Magnific Premium, €72/year (€6/mo).** Best AI value found, by a distance.
240,000 credits/yr, natively EUR-billed from a Slovak IP (no FX drift, no card conversion fees). One credit
pool, and you pick per shot: 140 credits for a cheap Kling 2.5 720p filler clip, 2,080 for a Veo 3.1 hero
shot. Kling 2.5 720p = 140 cr/5s → **142 clips/month = ~47 three-clip reels at €0.126 each.**
Catch: €72 upfront, 12-month commitment. The "60% off, offer ends July 27" banner is an evergreen rolling
timer with stale hardcoded copy — it was still purchasable on 28 July. "Unlimited" applies to Premium+ only.

**Option B — WaveSpeed pay-as-you-go, no commitment.** Top up $5, spend what you spend.
- `infinitetalk-fast` — **$0.015/s flat, resolution-independent** (verified: the API schema has no
  resolution parameter at all). 8s talking hook = €0.11. Min billed 5s, max 600s.
- `wan-2.2/i2v-480p-ultra-fast` — **$0.01/s**, the cheapest verified per-second video anywhere. 5s or 8s
  only, silent, 480×832 vertical. Two 8s clips = €0.147. Use for atmospheric B-roll under heavy text
  overlay, where 480p softness reads as moody phone footage rather than cheap AI.
- **$1 free signup credit, no card** = ~13 five-second talking hooks. **Do this test before spending
  anything.** If the output looks like slop to you, this whole lane is dead and no price-hunting fixes it.

Recommendation: **Option A if you'll commit for a year, Option B if you won't.** Not both.

### 4b. fal.ai — corrected, and the openshorts verdict

**Correction to §1's original figure.** "fal's floor is €0.40–0.55/reel" was **too pessimistic** — it came from
third-party comparison tables, because fal.ai/pricing sits behind a Vercel checkpoint returning HTTP 429. A
full sweep of fal's live catalogue (1,394 models, 35 pages of `https://fal.ai/api/models?keywords=&page=N`,
631 exposing `pricingInfoOverride`) found a cheaper tier that no per-second price list surfaces:

| Endpoint | Real price | 15s vertical reel |
|---|---|---|
| `fal-ai/ltx-2-19b/distilled/audio-to-video` | $0.0008 **per megapixel** (w × h × frames) | 480×854 × 375f = 153.7 MP = **$0.123** |
| `fal-ai/vibevoice` (TTS) | $0.04/generated minute | $0.010 |
| `async/tts-pro/v1.0` (TTS) | $0.01 / 1,000 chars | $0.0022 |
| `fal-ai/longcat-video/distilled/i2v/480p` | $0.005/s — **half of WaveSpeed** | $0.075 (silent) |
| `fal-ai/wan/v2.2-a14b/i2v/turbo` | $0.05 flat per 480p video (~5.06s) | ≈ $0.0099/s |

So a complete talking-head reel is **$0.133 = €0.117**, in a single call that takes image + audio → lip-synced
video (no separate lipsync stage), and **ElevenLabs disappears entirely.**

Two corrections that follow: **WaveSpeed is not meaningfully cheaper than fal** — its `wan-2.2 ultra-fast`
$0.01/s and fal's `wan/v2.2-a14b/turbo` $0.0099/s are within 1%, and fal's LongCat distilled tier at $0.005/s
undercuts both. WaveSpeed's only real edge is billing up to 8s in one call. And **fal's `deprecated` flag is
useless** — it is `false` on all 1,394 models; obsolete endpoints are left published with pricing stripped.
Read `publishedAt` instead.

⚠️ **The load-bearing unknown:** LTX-2 distilled audio-to-video is a general *audio-conditioned* model
("generate video with audio from audio, text and images"), **not** a purpose-built lipsync model like
`fal-ai/latentsync` or `fal-ai/kling-video/lipsync`. Fifteen seconds of close-up mouth accuracy is exactly
where such models break. **Smoke-test one reel (~$0.15) before building anything on this number.**

**Retries decide pass/fail.** Break-even is a **1.77× retry factor** on the 15s pure-AI route — at a realistic
2× you land at €11.24/mo and miss budget. The **hybrid** route (5s AI hook + your own screen recording,
assembled with local ffmpeg) is **€0.039/reel = €1.95 for 50** and survives **5.1× retries**. Only the hybrid
has genuine headroom.

**openshorts (`mutonby/openshorts`) — verdict: don't run it.** Not because it's broken:

- ✅ **Alive and healthy** — 2,771★, 772 forks, 100+ commits in 30 days, a commit on 28 Jul 2026, maintainer
  triaging issues with real technical detail. No GPU, no DB, no Redis; Docker Compose, 3 containers, S3 optional.
- ✅ **Licence resolved — and `research/01` overstated it.** Root `LICENSE` is plain **MIT**. The commercial
  carve-out applies *only* to `cloud/`, which holds Stripe billing/managed-key code that never runs
  (`BILLING_ENABLED` defaults off; `require_managed_entitlement()` is an explicit no-op). Its own Clarifications
  section says everything outside `cloud/` is MIT and the app "runs fully without the Commercial Software."
  Making marketing reels for your own commercial app is unambiguously permitted.
- ❌ **~€0.80/reel as shipped ≈ €40/mo — 4× over.** Default "Low Cost" chain, all four model IDs verified live:
  Hailuo 2.3 Fast 6s ($0.19, vendor-confirmed) + VEED Lipsync + Flux 2 Pro actor + 2× Flux 2 Pro b-roll
  ≈ $0.47 fal-only. Its landing page quotes ~$0.65/video all-in.
- ❌ **Its cost figures are hardcoded Python constants, not measurements.** `saasshorts.py` returns
  `cost_estimate` literals including `veed_lipsync: 0.20`. But `veed/lipsync/v2` prices at **$0.07/output-second**,
  and the pipeline hard-mandates an 18–22s narration → ~$1.40, **7× the constant**. The repo calls v1, which
  publishes no price and is GPU-time billed — genuinely unknowable without spending money.
- ❌ **ElevenLabs is hardcoded and not pluggable.** `generate_voiceover()` posts straight to a hardcoded
  `api.elevenlabs.io` base; no provider interface, no registry; grep for kokoro/piper/edge_tts/Google TTS
  returns **zero hits**; `app.py` hard-fails with HTTP 400 without the key. And the maintainer closed issue
  **#17 ("support local AI models") as not planned** — a pluggable provider layer is off the roadmap.
- ❌ **Scripts are hardcoded to 18–25s** ("EXACTLY 5 segments"), with no duration knob, and the low-cost path
  loops a 6s Hailuo clip across ~20s of audio — visible motion repetition.
- ❌ **Adapting it is 25–40h** (TTS swap 3–5h, provider adapter 6–10h + your own S3/R2 bucket for public input
  URLs, hook-format rewrite 5–8h because `composite_video()` derives the whole timeline from the talking-head
  duration and the hybrid topology is its inverse, plus reading a 159 KB `app.py` and 58 KB `saasshorts.py`).
  Then you maintain a fork of a repo that gets pushed to daily.

**The configuration that fits €10 makes exactly one paid API call per reel.** That is a ~120–150 line script
(~6–10h to write, 1–2h/month after), not a framework. openshorts earns nothing you'd use — you'd inherit the
Clip Generator, YOLOv8/MediaPipe reframing, a React dashboard and an S3 gallery to use ~5% of it.

**The strongest evidence is negative.** Two independent signals:
1. No genuine, verifiable case study exists of an automated AI-UGC pipeline run at volume in 2026 with published
   installs, views *and* cost. Every result was a vendor blog, an affiliate/SEO farm, or a course funnel. The
   widely-quoted "350% higher engagement / 2.8× more views / $43,700 April 2026" numbers have **no reachable
   primary source.** If solo founders were reliably winning at this, the retrospectives would be findable.
2. openshorts' own issue tracker: of 51 issues/PRs, essentially every user-reported problem concerns the **free
   Clip Generator**, not the fal-based AI Shorts path. Nobody has filed "my fal bill was higher than the README
   said" — which is what you'd expect from an active userbase on the money-burning path. **People star it and
   run the free clipper.**

**And the part no engineering fixes:** automation changes cost-per-unit and time-per-unit. It does not change
one frame of what the viewer sees. €0.20/reel buys 480p, a distilled avatar, and unclonened free TTS — soft
against native-camera footage on a 2026 OLED phone, smeared mouth interiors, over-regular blinking, no gaze
tracking, and TTS with no breath or false starts. That is the single fastest AI tell, read instantly by the
most AI-literate cohort alive. For a *focus app* selling authenticity, a synthetic creator is a credibility
own-goal, and 50 templated reels can drag account-level distribution rather than merely underperforming.

---

## 5. Do not buy — verified traps

| Tool | Why |
|---|---|
| **Higgsfield** | PLUS is annual-**only** at €39/mo (€468 upfront); ULTRA €129/mo monthly. No cheap tier exists. Per-credit economics are fine — the floor is the problem. |
| **ElevenLabs** | Creator is now **$22/mo for 100K chars** (~239% YoY increase) = 2.2× your entire budget for voice alone. `research/02`'s "$6 Starter" is dead. |
| **Akool** | Starter/Pro/Pro Max grant a **Personal licence only** — commercial use starts at Business, ~€137–160/mo. Free tier has a *full-screen* watermark. Strike entirely. |
| **HeyGen** | Avatar III at $0.0167/s is the closest near-miss, but add **$1.00 per avatar creation** (your 4-identity character library = €3.52) and realistic retakes → 14–21 finished reels for €10. No free API credits since Feb 2026. |
| **Creatify / Arcads / Synthesia / Argil** | €36–101/mo floors; Creatify still watermarks at €36 (clean exports need €91). |
| **Replicate** | 20–180% more expensive than fal for literally the same model weights. |
| **PiAPI / ModelsLab / Segmind** | Monthly floors of €13.80 / €19.32 / $10-minimum-topup blow the budget before a frame renders. ModelsLab's "unlimited" excludes premium video by its own FAQ. |
| **Kie.ai / Atlas Cloud "$0.022/s"** | 403s on pricing pages, 30–70%-below-official claims. The $0.022/s was a **misattributed Seedance v1.5 price**, not 2.0. Grey-market signature — an account ban mid-campaign costs more than the saving. |
| **Later / Metricool / Postiz Cloud / Plausible** | €17.25 / €16–20 / €26.68 / €8.28 per month for what Buffer Free + PostHog Free do at €0. Metricool Free caps at **20 posts/month** — structurally can't do the job. |
| **Self-hosted Postiz** | Requires *your own* TikTok dev app. Unaudited clients can only post **SELF_ONLY (private)** video, max 5 users/24h. A month of platform bureaucracy to save €0 vs Buffer. |
| **Local video gen on Mac** | M1 Max measured at **82 min for a 2s 480p Wan 2.2 clip**. Even a generous 3.5–6× for M4 Max = **1.7–2.9 h per 15s reel**, laptop pinned throughout. LTX-2 fails on Metal outright. |
| **HunyuanVideo** | Fastest open model, but the Tencent licence states in capitals that it **"DOES NOT APPLY IN THE EUROPEAN UNION, UNITED KINGDOM AND SOUTH KOREA."** Multiple 2026 blogs falsely list it as Apache-2.0. You're in Slovakia. |
| **Wav2Lip** | "Any form of commercial use is strictly prohibited." It's bundled into most open UGC pipelines — check before you inherit it. |

---

## 6. Corrections to claims circulating in this repo and elsewhere

❌ **"fal.ai is 5–9× over budget"** → stale. Cheapest usable fal route is now €0.40–0.55/reel, **2–2.8× over**.
But the specific fal model prices in circulation are also wrong, nearly all optimistically: Kling v3 Standard
is **$0.084/s, not $0.029/s**; LTX-2.3 Fast is **$0.06/s at 1080p, not $0.04/s**. (fal.ai/pricing is behind a
Vercel checkpoint returning HTTP 429; `https://fal.ai/api/models?keywords=<term>` returns unauthenticated
vendor-authoritative JSON and is the way to read real prices.)

❌ **"Kling Standard = 44 clips/month"** → Kling's own page says 660 credits = **33 720p videos**. ~11 all-AI
reels. Also: the $6.99 monthly price is a first-subscription teaser; standing monthly is $8.80. The $79.20
annual rate *does* persist at renewal.

❌ **"Hailuo Standard $7.99/mo"** → that's the **annual-equivalent** ($95.99 upfront). Month-to-month is $9.99.
And it's **40 clips/month, not 57** (2.3 at 768p/6s = 25 credits, read off the live generation panel).

❌ **"Vidu Standard ≈ €0.14/reel, best-in-class"** → Vidu Q3 is metered **per second**, not per clip. A 15s
720p Q3-turbo reel = 165 credits = **€0.72**. 50 reels = €36/mo. One of the more expensive options, not the cheapest.

❌ **"Midjourney Basic = 100 clips = 50 reels"** → 100 clips is 33 three-clip reels (€0.21/reel), and 50 reels
needs 300 GPU minutes against 200 available, with no Relax overflow on Basic. Basic is also **SD video only**.

❌ **"CapCut's ToS grants ByteDance a perpetual biometric licence"** → the word *biometric* does not appear in
the ToS. The perpetual/sublicensable licence is a standard User Content clause scoped to what you **upload or
submit** — it does not attach to local editing. (Still prefer Instagram Edits: CapCut publishes no prices at
all and capcut.com/pricing 404s.)

❌ **"TikTok Photo Mode gets 5× the reach"** and **"carousels +81% engagement (698,000 posts)"** → both
unsourced. The real comparable study (Socialinsider, 35M Instagram posts) shows carousels beating Reels by
**~6%**. The 5× claim's own author says the window closes in 6–12 months.

❌ **"Real human UGC delivers 2.1–2.8× the ROAS of AI"** → the figure exists on the cited page but is
unsourced, and the publisher sells human UGC. Don't cite it. The defensible version is the one in §2b: at this
budget you can't buy good AI, and slop loses to a real face regardless of labelling.

❌ **"TikTok suppresses AI content 73% / cuts reach 80%"** → no primary source; don't plan around it. What
TikTok actually shipped (10 Mar 2026): 1.3B videos labelled, invisible watermarks on AI Editor Pro and C2PA
uploads, and an **AIGC toggle in Manage Topics** letting viewers dial AI content down in their own FYP. Meta
states its "AI info" label carries no algorithmic penalty. The real exposure is **retroactive C2PA flagging**,
which lands after the first-6-hour engagement window and rarely recovers.

❌ **"TikTok Creator Marketplace"** → discontinued as a standalone product (fully shut down 1 Apr 2025) and
absorbed into **TikTok One**. `creatormarketplace.tiktok.com` 302-redirects. Slovakia availability is
unverifiable because TikTok publishes no country list.

❌ **"Chatterbox's PerTh watermark gets you detected by TikTok"** → TikTok's published stack is C2PA + its own
invisible watermark + its own classifiers. PerTh is nowhere in it. (Kokoro is still the cleaner pick — no
watermark at all, Apache-2.0.)

---

## 7. Distribution & measurement — €0

- **Cadence:** 25 reels/mo TikTok main + 15 TikTok secondary persona + 10 **materially re-edited** to IG Reels.
  Two accounts, one device, no proxies, no automated engagement, never the same file twice.
- **TikTok CREATOR account, not Business** — Business is locked to the Commercial Music Library, i.e. no
  trending sounds. For a 16–30 doomscroll audience that loses more than the bio-link convenience gains.
- **Volume pays on TikTok; it is penalised on IG and YouTube.** Instagram's Original Content Guidelines strip
  recommendation eligibility from accounts primarily posting unoriginal or materially-unedited content and
  require no visible watermarks. YouTube's Jul 2025 "inauthentic content" policy targets mass-produced
  templated video. Never raw-repost a watermarked TikTok.
- **Attribution:** PostHog Free + one static landing page per channel; waitlist email submit is the pre-launch
  conversion event. App Store Connect campaign links (free) take over at launch.
- **Seeding (€0):** Apple offer codes allow 1M redemptions per app per quarter, shared across subscriptions
  (max 10 active offers per SKU; one-time codes expire ≤ 6 months). Note the separate *app-download promo
  codes* are capped at **100 per version, valid 4 weeks** — that's a friends-and-family list, not a programme.
  IAP promo codes were phased out on 26 Mar 2026; free-download promo codes continue.
  Seed whole **friend groups** — LockIn's 2–4-approver mechanic needs a group anyway. Expect 10–30 usable
  clips per 100 codes.
- **Rev-share instead of paying creators does not work pre-launch** — 25% of zero revenue is worth zero.

---

## 8. Expectations

Set them low and keep going anyway. TikTok engagement rate by views slid to **3.85% in Q2 2026**; an account
under 5K followers averages **~350 views/post**, so month one of 50 reels ≈ 17,500 views, not a viral break.
Install lift in this niche typically appears at **months 3–6**. Cal AI's founder needed **281 videos** for
2.1M views. Opal's persona account hit ~402K followers and ~8M views in 30 days — on a whiteboard and a phone.

Measure **waitlist signups → installs. Never views.**
