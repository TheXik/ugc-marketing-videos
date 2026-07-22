# UGC Generation Tooling — Open-Source Repos, Ranked

Multi-agent workflow evaluated 23 candidate repos, deep-dived 16. Goal: the best open-source foundation for generating AI UGC video ads at scale.

## 🏆 Winner: `mutonby/openshorts` (8/10)

The **only repo that generates an AI UGC ad end-to-end in one codebase**:

> product URL → Gemini writes a hook-problem-solution-CTA script → generates an AI actor (Flux 2 Pro) or picks an avatar → voices it (ElevenLabs) → animates + lip-syncs (Hailuo / Kling) → adds B-roll + ASS subtitles → assembles in FFmpeg → publishes to TikTok/IG/YT. Self-hosted, no watermarks.

Every other repo covers **at most one stage**.

**Caveats:**
- It's a UI/job-queue app, not API-first bulk — for volume you script its queue headlessly (bump `MAX_CONCURRENT_JOBS`).
- Depends on paid APIs (~$0.50–1.50/video).
- Source-available license with a commercial carve-out — **verify before building a business on it.**

## Full ranking

| # | Repo | Score | What it actually is |
|---|------|-------|---------------------|
| 1 | **mutonby/openshorts** | 8 | Full AI-actor UGC pipeline, self-hosted, no watermark |
| 2 | TMElyralab/MuseTalk | 6 | MIT, real-time lip-sync — best **free** avatar stage (commercial-OK) |
| 3 | OpenTalker/SadTalker | 5 | Apache-2.0 photo+audio talking-head, but frozen since 2024, dated 256/512px |
| 4 | harry0703/MoneyPrinterTurbo | 4.5 | ~98k⭐ MIT batch/API faceless generator — wrong format (stock+TTS, no avatars) but strong render/caption backend |
| 5 | FujiwaraChoki/MoneyPrinter | 4 | Faceless Shorts gen w/ DB-queue/Docker skeleton — good bones to fork |
| 6 | SamurAIGPT/AI-Youtube-Shorts-Generator | 4 | Repurposes long-form → vertical hook clips; generates no net-new UGC; no license |
| 7 | elebumm/RedditVideoMakerBot | 3.5 | Canonical faceless Reddit-story maker; GPL-3.0 blocks commercial embedding |
| 8 | gyoridavid/short-video-maker | 3.5 | MIT TS MCP+REST faceless gen; stock+robotic-TTS only, English-only, ~1yr stale |
| 9 | vishnuhimself/UGCVidGen | 3 | On-topic vertical UGC-ad **assembler but ZERO AI** — human supplies every clip; abandoned same-day, no license |
| 10 | RayVentura/ShortGPT | 3 | Well-known MIT faceless pipeline reference, unmaintained since Feb 2025 |
| 11 | Rudrabha/Wav2Lip | 3 | Famous but low-res 2020 lip-sync; **non-commercial license = hard blocker for ads** |

## Ruled out (were floated in UGC-guru tweets, are NOT UGC tools)

All confirmed HIGH confidence — category mismatches:

- **facebook/tribev2** — Meta brain-encoding/fMRI *prediction* research model; generates nothing; CC-BY-NC-4.0 non-commercial
- **Narcooo/inkos** — novel/long-form text writing agent, no video
- **xberg-io/xberg** — document extraction framework (the inverse of a generator)
- **BinarCode/laravel-restify** — Laravel REST-API framework, no media capability
- **zendev-sh/goai** — generic Go LLM SDK, text + static images only

## Recommendation

- **Fastest path:** deploy **openshorts** (Docker Compose), wire Gemini + fal.ai + ElevenLabs keys. Budget ~$1/video. Verify the license.
- **Cheaper at volume:** self-host the avatar stage with **MuseTalk** (MIT, real-time, commercial-OK) + a faceless skeleton like **MoneyPrinterTurbo** (MIT, batch + REST) for render/caption/TTS — but you build the orchestration yourself.
- **Honest gap:** no repo is a turnkey, license-clean, API-first bulk UGC-ad farm. The content-complete option (openshorts) has a non-OSI license; the clean-MIT options each cover only part of the pipeline.

> ⚠️ Strategy note: for **organic TikTok**, AI-generated talking heads now trigger AI-labeling + reach suppression (see `strategy/04`). Reserve these tools for paid-ad creative or B-roll, and prefer human/screen-recording video organically.
