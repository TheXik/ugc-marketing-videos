# UGC Generation Tooling — Open-Source Repos, Ranked

**Re-swept 28 Jul 2026.** All star counts, push dates and licences below were pulled live from the GitHub API
that day, not from memory. The previous version of this file ranked by an internal fit-score; this one ranks by
stars **because that is what was asked for** — and the whole point of the exercise turned out to be that
**ranking by stars puts you on dead repos and licence violations.** Read the right-hand columns, not the left.

---

## ⚠️ Read this before using the ranking

**Stars are inversely correlated with usefulness in this category.** Everything above 10k is either a
*component* (Whisper, TTS, ComfyUI) or the wrong format (faceless stock-footage printers). The five
highest-star pipeline repos — MoneyPrinterTurbo, Deep-Live-Cam, MoneyPrinter, RedditVideoMakerBot, ShortGPT —
total **~229,000 stars and not one produces a creator-face UGC ad for an app.** Stars measure how much people
enjoy the *idea* of an automated video printer.

**Four places a stars-descending list actively misleads:**

| Trap | Higher stars | Actually current |
|---|---|---|
| Archived vs alive | `rhasspy/piper` **11,270** ⚠️ ARCHIVED, 419 stranded issues | `OHF-Voice/piper1-gpl` **4,930**, 39 commits/90d |
| Adjacent versions | `Wan-Video/Wan2.1` **16,667** | `Wan-Video/Wan2.2` **16,869** — a 202-star gap, so they interleave with no hint which is newer |
| README says go elsewhere | `Lightricks/LTX-Video` **10,770** — last commit is literally *"Readme: Add notice directing users to LTX-2"* | `LTX-2` **8,428** |
| Monotonic decay toward life | `hallo` **8,658** (dead 2024-09) → `hallo2` **3,726** (dead 2025-02) → `hallo3` **1,395** (dead 2025-03) | `fudan-generative-vision/Hallo-Live` **337** — 25× fewer stars, the only one alive |

**Commit recency lies too — check *what* the commits are.** `SamurAIGPT/AI-Youtube-Shorts-Generator` looks
alive (pushed 2026-07-21) but recent commits include *"chore: add MuAPI powered-by badge"* and *"chore: add UTM
tracking to muapi.ai links"* — affiliate monetisation, not maintenance. `FujiwaraChoki/MoneyPrinter`'s last
commit is a sponsor swap. `gyoridavid/short-video-maker`'s last five are all README edits.

**Better health signals:** commits in the last 90 days (MoneyPrinterTurbo 100, piper1-gpl 39, Deep-Live-Cam 37,
chatterbox 3, kokoro **0**), and whether recent open issues are *feature requests* (healthy) or *"won't install
/ won't run on my GPU"* (rot). MoneyPrinterTurbo's **6 open issues on 99.6k stars** is the strongest health
signal in the sweep; SadTalker's 661 and LatentSync's 228 are the opposite.

---

## ⛔ Licence blockers — ranked by how hard they stop you

1. **`Rudrabha/Wav2Lip` (13,127★)** — **no LICENSE file at all.** README verbatim: *"This repository can only be
   used for personal/research/non-commercial purposes"* and *"any form of commercial use is strictly
   prohibited."* The authors sell the commercial version via Sync Labs. Also technically dead — pins
   `torch==1.1.0`, `numpy==1.17.1`, won't install on any 2026 Python. **It is bundled into most open UGC
   pipelines — check before you inherit it.**
2. **`hacksider/Deep-Live-Cam` (95,319★)** — double blocker. AGPL-3.0 *and* it depends on InsightFace weights,
   which are *"available for non-commercial research purposes only"*. The repo's own README admits this at line
   386. Also a category mismatch: deepfaking a real person's face into an app ad is a consent problem on
   Meta/TikTok regardless of licence. The repo is genuinely healthy — health is fine, legality isn't.
3. **`fishaudio/fish-speech` (31,394★)** — Fish Audio Research License (updated 2026-03-07): **research and
   non-commercial only.** *"Any use for a Commercial Purpose requires a separate written license agreement."*
   31k stars notwithstanding, this is out.
4. **`SamurAIGPT/AI-Youtube-Shorts-Generator` (4,402★)** — **no licence file**, which under default copyright is
   *more* restrictive than GPL, not less. All rights reserved. No granted right to use it commercially.

**NOASSERTION resolved (all in your favour, by reading the actual LICENSE files):**
- `TMElyralab/MuseTalk` → **MIT** + third-party notices appendix (the appendix is what confuses GitHub's
  detector). README: *"There is no limitation for both academic and commercial usage"* — weights included.
- `OpenTalker/SadTalker` → **Apache-2.0**. The old non-commercial restriction was **removed**.
- `remotion-dev/remotion` → two-tier licence, **free for individuals and for-profit orgs up to 3 employees,
  commercially.** A solo founder qualifies. Watch the 4-person threshold ($100/mo).
- `mutonby/openshorts` → **MIT**; carve-out covers only `cloud/` billing code. See below.

**GPL/AGPL is less scary than it sounds here.** GPL restricts distributing the *software*, not the MP4s and
WAVs it produces. Running piper or OpenMontage locally to make 50 reels/month is unrestricted. It only bites if
you bundle the code into the LockIn iOS app or expose it as a network service.

---

## 🆕 The category the first sweep missed entirely: 2026 "video-as-code"

All star counts below independently re-verified against the GitHub API. **These render locally via headless
Chrome + ffmpeg — zero marginal cost per reel, which is the only shape that survives a €10/month budget.**

| ★ | Repo | Created | Licence | Read |
|---:|---|---|---|---|
| **43,012** | `calesthio/OpenMontage` | 2026-03-29 | AGPL-3.0 | Agentic video studio — 12 pipelines, 700+ agent skill files, Python + Remotion + ffmpeg. Hit #1 GitHub Trending. **Its `docs/PROVIDERS.md` is the pluggable provider layer openshorts lacks** — every backend is an env var, with a documented free-first path (Pexels/Pixabay $0, Google TTS 1M chars/mo free, Piper local $0). ⚠️ 211 open issues, large surface area. |
| **38,251** | `heygen-com/hyperframes` | 2026-03-10 | Apache-2.0 | *"Write HTML. Render video."* HTML/CSS/GSAP → deterministic MP4 via Puppeteer + ffmpeg. Needs only Node 22 + ffmpeg, **no API key for the render path.** Pushed today. Note the vendor: HeyGen open-sourced it and the docs funnel toward their paid avatar API for the human-actor part. |
| **4,206** | `nexu-io/html-video` | 2026-05-27 | Apache-2.0 | *"Pluggable rendering engines, no per-render fees, no vendor lock-in."* 21 templates. ⚠️ Its own README admits the Remotion/Motion Canvas/Manim adapters *"aren't built yet"* — today it's a wrapper over HyperFrames. |
| **2,420** | `Vincentwei1021/video-shotcraft` | 2026-07-19 | Apache-2.0 | 9 days old at 2.4k stars. 106 shot recipe cards + 161 motion previews for **product/app promos** on Remotion. Closest thing to a marketing-specific Remotion library. |
| **416** | `xixihhhh/clipforge` | 2026-03-23 | AGPL-3.0 | **The only repo found with a documented genuinely-zero-key path**: free Openverse images + Wikimedia stock + Edge TTS + free BGM + local ffmpeg. Chinese-first, e-commerce-oriented, Douyin-tuned hooks. Clone it for the free-provider wiring even if you discard the templates. |
| **307** | `iart-ai/motion-skills` | 2026-06-22 | MIT | 50 MIT agent skills for motion graphics, incl. an explicit **TikTok/Reels pack** and kinetic typography. Modular — take two packs, ignore the rest. |

**Honest shared limit:** all of these make motion graphics, kinetic captions and screen-recording composites.
**None makes a human face talking to camera.** They cover maybe 60% of UGC ad formats — which, per
`strategy/08`, is the 60% you should be making anyway.

**The end-to-end UGC-ad category is still nearly empty.** The only true openshorts peer found is
`Anil-matcha/Open-AI-UGC` (207★, MIT) — and it repeats openshorts' exact mistake with a different vendor: every
model routes through muapi.ai, the repo is a lead-gen asset for that gateway, and *"add any MUAPI model in ~10
lines"* means extensible **within** MUAPI, not provider-agnostic. `tsensei/OpenReels` (150★, MIT) is
architecturally the closest match to "50 faceless reels/month, one command" with a credible free path (Kokoro
local TTS + Pexels + 25 bundled tracks), but it's 1 watcher, 1 maintainer, last push 2026-04-10 — a fragile
dependency.

---

## Full ranking by stars — with the verdict that matters

| ★ | Repo | Pushed | Licence | Verdict |
|---:|---|---|---|---|
| 122,572 | `Comfy-Org/ComfyUI` | 2026-07-28 | GPL-3.0 | SKIP — local gen, Mac too slow |
| 105,863 | `openai/whisper` | 2026-04-15 | MIT | superseded by whisper.cpp |
| 99,639 | `harry0703/MoneyPrinterTurbo` | 2026-07-28 | MIT | MAYBE — healthiest repo in the sweep (6 open issues), but faceless stock format. ⚠️ Pixabay provider broken (#1136, Cloudflare 429); default edge-tts throwing 503s and legally grey |
| 95,319 | `hacksider/Deep-Live-Cam` | 2026-07-27 | AGPL-3.0 | ⛔ licence — see above |
| 54,619 | `remotion-dev/remotion` | 2026-07-28 | Remotion (free ≤3 employees) | **USE** — batch-render 50 reels from one template |
| 52,374 | `ggml-org/whisper.cpp` | 2026-07-28 | MIT | **USE** — captions, 2–3× realtime on M-series ⚠️ moved from `ggerganov/` |
| 45,826 | `coqui-ai/TTS` | **2024-08-16** | MPL-2.0 | SKIP — company shut down; XTTS-v2 *weights* licence differs from the code and is reportedly non-commercial. Unverified — check before touching |
| 37,039 | `myshell-ai/OpenVoice` | 2025-04-19 | MIT | stale |
| 31,394 | `fishaudio/fish-speech` | 2026-07-26 | Fish Audio Research | ⛔ non-commercial |
| 25,730 | `resemble-ai/chatterbox` | 2026-07-21 | MIT | **USE** — best-sounding free TTS; Nano runs 3× realtime on CPU. ⚠️ PerTh watermark on every output |
| 24,591 | `SYSTRAN/faster-whisper` | 2025-11-19 | MIT | fine |
| 18,827 | `KlingAIResearch/LivePortrait` | 2026-06-01 | MIT | MAYBE — strongest open talking-head not previously listed. ⚠️ moved from `KwaiVGI/` |
| 18,467 | `jianchang512/pyvideotrans` | 2026-07-24 | GPL-3.0 | dubbing, not generation |
| 16,869 | `Wan-Video/Wan2.2` | 2026-03-17 | Apache-2.0 | MAYBE — S2V + Animate variants are the UGC-relevant ones. CUDA only |
| 16,667 | `Wan-Video/Wan2.1` | 2026-03-05 | Apache-2.0 | SKIP — superseded, 367 mostly-spam issues |
| 15,037 | `SWivid/F5-TTS` | 2026-07-23 | MIT | fine |
| 13,972 | `OpenTalker/SadTalker` | **2024-06-26** | Apache-2.0 | SKIP — **archetypal star zombie.** Last *code* commit 2023-10-10. 661 open issues, unpatched command injection (filed 2026-06-12, ignored). Licence is clean; pure rot kills it |
| 13,784 | `FujiwaraChoki/MoneyPrinter` | 2026-03-26 | MIT | SKIP — runtime depends on `gpt4free`, which reverse-engineers paid APIs and is rotting accordingly |
| 13,127 | `Rudrabha/Wav2Lip` | 2025-06-22 | **NONE** | ⛔ non-commercial |
| 12,510 | `elebumm/RedditVideoMakerBot` | 2026-07-20 | GPL-3.0 | SKIP — category mismatch, but healthy (27 issues, all feature requests) |
| 12,375 | `Tencent-Hunyuan/HunyuanVideo` | 2026-06-29 | Tencent Community | ⛔ **excludes the EU** |
| 11,270 | `rhasspy/piper` | 2025-08-26 | MIT | ⚠️ **ARCHIVED** → use `OHF-Voice/piper1-gpl` (4,930★, GPL-3.0) |
| 10,770 | `Lightricks/LTX-Video` | 2026-01-05 | Apache-2.0 | SKIP — README points to LTX-2 |
| 8,147 | `hexgrad/kokoro` | **2025-08-06** | Apache-2.0 (code **and** weights) | **USE** — cleanest licence of any TTS, no watermark. ⚠️ dormant: 0 commits/90d, 195 open issues, PyPI stuck at 0.9.4 since 2025-04. Pin Python 3.12 |
| 7,734 | `RayVentura/ShortGPT` | 2025-02-10 | MIT | SKIP — zombie, 18 months |
| 6,256 | `TMElyralab/MuseTalk` | 2025-09-26 | MIT (commercial OK) | MAYBE — licence resolved in your favour, but 10 months stale + CUDA only |
| 5,932 | `bytedance/LatentSync` | 2025-06-20 | Apache-2.0 | SKIP — zombie, 228 issues, no releases ever |
| 5,017 | `Zejun-Yang/AniPortrait` | **2024-07-02** | Apache-2.0 | SKIP — dead |
| 4,930 | `OHF-Voice/piper1-gpl` | 2026-07 | GPL-3.0-or-later | **USE** — the live piper. Too robotic for a human read; fine for captioned faceless |
| 4,622 | `antgroup/echomimic_v2` | 2026-02-23 | Apache-2.0 | audio-driven avatar |
| 4,402 | `SamurAIGPT/AI-Youtube-Shorts-Gen` | 2026-07-21 | **NONE** | ⛔ no licence + affiliate commits |
| 3,940 | `midrender/revideo` | 2026-07-15 | MIT | Remotion alt ⚠️ moved from `redotvideo/` |
| 3,726 | `fudan-generative-vision/hallo2` | 2025-02-27 | MIT | SKIP — two generations stale → `Hallo-Live` (337★) |
| 2,844 | `TMElyralab/MuseV` | **2024-06-28** | — | SKIP — dead |
| **2,771** | **`mutonby/openshorts`** | **2026-07-28** | **MIT** | See below — healthy, licence fine, **4× over budget** |
| 1,254 | `gyoridavid/short-video-maker` | 2025-06-21 | MIT | MAYBE — right stack (Kokoro + whisper.cpp + Pexels + Remotion), no maintainer. ⚠️ unpatched path-traversal filed 2026-04-20 |
| 837 | `IgorShadurin/app.yumcut.com` | 2026-07-20 | NOASSERTION | read LICENSE first |
| 416 | `xixihhhh/clipforge` | 2026-07-27 | AGPL-3.0 | **USE** for its zero-key provider wiring |
| 337 | `fudan-generative-vision/Hallo-Live` | 2026-06-24 | MIT | the current Hallo |
| 307 | `iart-ai/motion-skills` | 2026-06-30 | MIT | **USE** — TikTok/Reels + kinetic-typography packs |
| 207 | `Anil-matcha/Open-AI-UGC` | 2026-07-27 | MIT | MAYBE — reference implementation only; MUAPI-locked |
| 150 | `tsensei/OpenReels` | 2026-04-10 | MIT | MAYBE — closest architectural match, fragile |
| 73 | `vishnuhimself/UGCVidGen` | 2025-02-26 | NONE | abandoned same-day |

---

## 🏆 `mutonby/openshorts` — still the only end-to-end UGC generator, still unaffordable

**2,771★ · 772 forks · 100+ commits in 30 days · commit on 28 Jul 2026 · Docker Compose, no GPU/DB/Redis.**

> Product URL → Gemini script → AI actor (Flux 2 Pro) → ElevenLabs voice → Hailuo/Kling animate + lipsync →
> B-roll + ASS subtitles → ffmpeg → publish to TikTok/IG/YT. Self-hosted, no watermarks.

**✅ Licence resolved — the old "verify before building a business on it" caveat overstated it.** Root `LICENSE`
is plain **MIT**. The commercial carve-out covers *only* `cloud/` (Stripe billing / managed-key code), which
never runs — `BILLING_ENABLED` defaults off and `require_managed_entitlement()` is an explicit no-op. Its own
Clarifications section: everything outside `cloud/` is MIT and the app *"runs fully without the Commercial
Software."* Marketing reels for your own commercial app are unambiguously permitted.

**⛔ But it fails on cost, and its own numbers are unreliable:**
1. **~€0.41/reel fal-only, ~€40/mo for 50 — 4× over budget.**
2. **Its cost figures are hardcoded Python constants, not measurements.** `saasshorts.py` returns
   `veed_lipsync: 0.20` as a literal — but `veed/lipsync/v2` bills **$0.07/output-second**, and the pipeline
   hard-mandates an 18–22s narration → ~$1.40, **7× the constant.** It calls v1, which publishes no price.
3. **ElevenLabs is hardcoded and not pluggable** — no provider interface; grep for kokoro/piper/edge-tts/Google
   TTS returns **zero hits**; `app.py` hard-fails HTTP 400 without the key. Maintainer closed issue **#17
   ("support local AI models") as not planned.**
4. **Its own users don't run this path.** Of 51 issues/PRs, essentially every user-reported problem concerns the
   *free* Clip Generator. Nobody reports a surprise fal bill.

Adapting it is **25–40h**, after which you maintain a fork of a daily-pushed repo to use ~5% of it. Full
teardown and the alternative in [`strategy/08-budget-plan-10eur.md`](../strategy/08-budget-plan-10eur.md) §4b.

---

## Ruled out (floated in UGC-guru posts, are NOT UGC tools)

Category mismatches, all HIGH confidence: **facebook/tribev2** (fMRI prediction, CC-BY-NC), **Narcooo/inkos**
(long-form text), **xberg-io/xberg** (document extraction), **BinarCode/laravel-restify** (REST framework),
**zendev-sh/goai** (Go LLM SDK). Also excluded deliberately: desktop NLE editors (Shotcut 14,648★, Kdenlive,
OpenShot 6,113★, Blender) — real software, useless for automating 50 reels/month.

⚠️ **`Augani/openreel-video` (4,584★, MIT)** — self-described open-source CapCut alternative, would be a clean
free editor. But its README carries a **pump.fun Solana memecoin contract address**, and 4,584 stars against
**29 watchers** (158:1) is a textbook airdrop-farmed star profile. The editor may work; the star count is not
evidence that it does.

---

## Recommendation

**Hardware, not licence, is the real €10/month killer for half this list.** On macOS, MuseTalk, LatentSync,
SadTalker, Hallo-Live, LTX-Video/LTX-2 and Wan2.1/2.2 all assume CUDA; the Wan 14B models want 40GB+ VRAM.
Renting a GPU for 50 reels/month costs multiples of €10.

**The components that actually run inside the budget on your machine:**
`ggml-org/whisper.cpp` (captions) · `hexgrad/kokoro` or `resemble-ai/chatterbox` Nano (voice) ·
`remotion-dev/remotion` or `heygen-com/hyperframes` (render) · free stock B-roll.

**If you want a framework rather than your own script:** `heygen-com/hyperframes` (Apache-2.0, zero marginal
cost, pushed daily) as the render backbone, plus `iart-ai/motion-skills`' TikTok/Reels pack. That is
motion-graphics-and-screen-recording video — which is the format `strategy/08` recommends anyway.
