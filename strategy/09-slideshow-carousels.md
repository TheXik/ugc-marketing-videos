# Slideshow Carousels — the researched plan (29 Jul 2026)

Output of a 12-agent research + adversarial-verification workflow. Supersedes several claims made
earlier in this repo and in conversation. Every load-bearing number below was checked against a
primary source; the ones that failed are listed in §6 with the correction.

---

## 1. Verdict on cadence

**3 posts/day on Instagram (2 carousels + 1 Reel) + 1–2/day video-only on TikTok. One account each. Not 10.**

Ramp: weeks 1–4 at 2/day IG while the footage pipeline gets built → weeks 5+ at 3/day → 5/day only if
median reach/post AND saves/post held flat or rose over the prior 14 days. Hard stop at 5.

**Why not 10–20/day** (the guru number):
- No dataset exists above ~1.5 posts/day on IG. The three largest studies top out at 1.4/day (Buffer,
  2.1M posts), 3.5/day (Socialinsider) and 5/day (Buffer/BuzzSumo FB, 43M posts). The measured TikTok
  ecosystem average is **3.34 posts per WEEK**. [HIGH]
- The only way a solo founder reaches 10/day is near-duplicate variants — exactly what TikTok's
  25 Sep 2025 bulk-repetitive-content enforcement removes from the FYP and what Instagram's
  30 Apr 2026 unoriginal-content rule de-recommends **at account level**. [HIGH]
- The largest measured effect in the literature is not daily volume but **consistency across weeks**:
  posting in 20+ of 26 weeks → ~450% more engagement per post than ≤4 weeks. [HIGH]

**Why frequency itself is NOT the problem** (this corrects our own earlier note): Buffer's 2.1M-post /
102k-account dataset shows reach *per post* rising monotonically with frequency (+12% / +18% / +24% at
3–5, 6–9, 10+ posts per week vs a 1–2/week baseline). Instagram has stated on record it does not
downrank for posting frequency. The industry-wide −31% reach collapse is **ecosystem saturation, not a
per-account penalty**. [HIGH]

**One account, not three.** Device/IP linking makes a TikTok shadowban network-wide; Meta's CIB policy
covers "multiple assets working in concert" (1.5M+ IG accounts removed in Q4 2024). And three accounts
triples the original-footage burden — the one thing already in shortest supply. [MEDIUM on enforcement,
HIGH on the capacity argument]

**Kill metric, pre-declared:** waitlist signups per post in PostHog over 2-week windows. If 2→3/day does
not raise weekly signups, the extra posts are cost with no return.

---

## 2. Platform allocation — carousels are pointed the wrong way by default

| | Instagram | TikTok |
|---|---|---|
| **Carousels** | ✅ 4.7× the views of the same format on TikTok | ❌ video beats photo 5–5.6× on reach |
| **Video** | repost from TikTok, 1/day | ✅ primary, ~30% more views than IG Reels |

**Carousels are a conversion instrument, not a discovery engine.** At <1k followers, IG Reels get
**134 median reach vs carousels' 56** (700M-post study). The carousel advantage is an audience-size
effect that only crosses over around 50k followers. Judge carousels on **saves, sends, profile visits
and waitlist clicks — never reach.** [HIGH]

---

## 3. The €0 stack (as verified)

| Stage | Tool | Catch |
|---|---|---|
| **Slide rendering** (~90% of slides) | Python + Pillow → 1080×1350 JPEG | Benchmarked on this M2: **80 slides in 2.08s** (26ms/slide). Brand-exact, ~1000× faster than any model. You own the template quality. **Must be JPEG** — the Graph API rejects PNG. |
| **Picture slides** (1–2/carousel) | **Cloudflare Workers AI** `@cf/black-forest-labs/flux-1-schnell` | Free plan = 10,000 neurons/day ≈ **173 images/day** at 1024² / 4 steps. Apache-2.0 *because it's schnell* — anything with `dev` in the name is non-commercial and banned. |
| **Hosting** | Cloudflare R2 + Worker | Graph API cURLs your URL; it will not accept local files. JPEG ≤8MB, public HTTPS, **no query string** (Postiz #1584 fails to encode them). Aspect 4:5 → 1.91:1. A 1080×1920 still is **rejected** as a feed image. |
| **Publishing (primary)** | Instagram native scheduler | 25/day, 75 days ahead, carousels + Reels. Zero setup, zero API risk, and the only path where **attaching music to a carousel is guaranteed to work**. Manual, phone-first. |
| **Publishing (automated)** | Self-hosted Postiz + own Meta app | Three catches — see §5. |
| **Video** | Phone + Instagram Edits / CapCut, whisper.cpp captions | Always `-movflags +faststart` — "moov atom at the front" is a hard Graph API requirement and the #1 cause of silent Reel-publish failure. |
| **Attribution** | PostHog + unique bio slug per weekly batch | IG/TikTok referrer data is unreliable; without per-batch slugs you cannot attribute at all. |

**Banned — licence / watermark / volume traps:** FLUX `[dev]` (non-commercial) · Gemini & Imagen API
(**no free tier for any image model**) · Draw Things FLUX on this 8GB M2 (needs ~6.5GB vs ~6–7GB usable)
· Bing/Copilot Image Creator (personal use only) · Leonardo & Ideogram free (public generations, paid API)
· HF Inference free ($0.10/month ≈ 30 images) · Pollinations (watermark, refuses to state a licence)
· Metricool Free (20 posts/**month**) · Later (free plan discontinued) · Make free (1,000 credits dies
instantly — one carousel is 12+ API calls).

---

## 4. Instagram API — no review needed

The "2–4 week App Review blocker" was a **phantom**. None of steps 1–7 are review-gated:

1. Convert the IG account to **Professional**. (5 min, in-app)
2. Create a **Facebook Page**, link it to the IG account.
3. developers.facebook.com → Create App → type **BUSINESS**. Business apps get **Standard Access on all
   permissions automatically**.
4. Add the Instagram product. Use the **Facebook Login for Business** route (it's the only one exposing
   `audioSearch`/trending music in Postiz; standalone login has an open 409 bug). Request:
   `instagram_basic`, `pages_show_list`, `pages_read_engagement`, `business_management`,
   `instagram_content_publish`, `instagram_manage_comments`, `instagram_manage_insights`.
5. App Dashboard → Roles → add your IG account as an **Instagram Tester**, then accept the invite in
   Instagram → Settings → Apps and Websites → Tester Invites. **Nothing publishes until you accept.**
6. **Leave the app in Development Mode permanently.** Standard Access covers publishing for anyone holding
   a role on the app. [HIGH on the documented mechanism; MODERATE that Meta hasn't tightened it in 2026 —
   validate with one real test post.]
7. Set `FACEBOOK_APP_ID` / `FACEBOOK_APP_SECRET` in Postiz `.env`, restart, connect the channel.
8. Publish **one test carousel end-to-end** before anything else: N item containers with
   `is_carousel_item=true` → one `media_type=CAROUSEL&children=…` container → `media_publish`.
   That's 12 API calls for a 10-slide carousel.
9. Read your real quota every run: `GET /{IG_ID}/content_publishing_limit?fields=config,quota_usage`.
   Meta documents 100 posts/rolling 24h (carousels count as one; 50 carousels/24h); a vendor still reports
   25. Stop guessing — read the number. At 3–5/day you're nowhere near either.
10. Build media containers **at publish time** — they expire after 24h.

**Advanced Access / App Review is required ONLY** if you ever let third parties connect their own accounts.
Not part of this plan.

---

## 5. Known failure modes

- 🔴 **No authentic footage.** LockIn has never run a real multi-person pact; 0 device installs. Every
  high-value angle needs a live pact producing real denials. **Fix in week 1** — run a real 3-person pact
  on real devices and capture it. Optimising cadence before this is optimising an empty pipe. [HIGH]
- **Postiz single point of failure:** `integrationList` returns `[]` today (zero channels connected), 15
  open upstream IG issues, and **#1724 — posts created via `/public/v1/posts` get stuck in QUEUE forever**
  with no GET or PUT to inspect or retry. A silent failure looks exactly like a quiet day. Keep the native
  scheduler as fallback; alert on anything still queued after 5 minutes. [HIGH]
- **Music may not survive automation.** If the Graph API path can't attach audio to a carousel, automated
  carousels lose Reels-tab eligibility — most of the reason to run them on IG. Verify with one test post
  before building the pipeline around it. [MEDIUM]
- **Undocumented Graph API limit:** calls/24h = 4800 × impressions, with a documented minimum-impressions
  floor for Threads but **not** Instagram — a zero-follower account is precisely the undefined case. Seed
  with a few manual posts first, read `X-Business-Use-Case-Usage` on every call, cap polling at 1/min for
  5 min. [MEDIUM]
- **Slideshows have a ceiling.** The best-documented precedent (Blake Anderson's Cal AI / Umax) plateaued
  organically and moved to $1M+/month in paid ads. Treat slideshows as a zero-cost hook-discovery engine
  for 90 days, not as the App Store launch channel. [MEDIUM]

---

## 6. Corrections to claims in this repo and in circulation

| Claim | Status |
|---|---|
| "2–4 weeks of Meta App Review before you can publish" | ❌ **Phantom blocker.** Dev-Mode + Tester role needs no review. |
| "One quality account always beats volume" *(ours)* | ⚠️ **Too strong.** Frequency doesn't hurt reach. The real ceilings are original-content supply and originality enforcement. |
| "Gemini free tier for images" *(ours)* | ❌ **False.** Google's pricing page: "Free Tier: Not available" for every image model. Gemini free is **text only**. |
| "FLUX schnell locally via Draw Things" *(ours)* | ❌ Not viable on an 8GB M2. Route volume to Cloudflare Workers AI. |
| "TikTok Photo Mode gets 5× more reach than video" | ❌ **Backwards.** Video gets 5–5.6× the reach (Metricool, 2.3M posts). Every "5×" claim traces to blogs selling carousel tools. |
| "Scratch AI: 20k users in 2 weeks off 20 posts/day" | ❌ **Doesn't survive checking.** ~25,000 *lifetime* downloads over 10 months; reviews spread evenly Oct→Apr; zero corroboration anywhere. |
| TikTok's own "2.9× comments / 1.9× likes / 2.6× shares" for photos | ❌ Feb 2024 in-app **promotional** messaging, no method, no sample, no reach claim. Fanpage Karma (~698k posts) found carousel shares ~⅓ **lower** than video. |
| "8–12 slides optimal / 72% first-slide retention / 3.5× dwell" | ❌ Fabricated SEO from carousel-tool vendors. The one real signal (Socialinsider) points the other way: using **all** available slides had the highest ER. |
| "Post 20×/day" | ❌ Untested. No dataset covers it. |

---

## 7. Slide format rules (only the grounded ones)

1. **1080×1350 (4:5), JPEG, ≤8MB, public HTTPS, no query string.** Not 9:16 — a 1080×1920 still is rejected.
2. **Hard cap 10 slides** (API limit; the app allows 20). Fix at 8 for the first 20 posts, log
   reach/saves/profile-visits, *then* vary deliberately.
3. **Slide 1 = the moment itself**, as a real product screenshot + one line of punchline. No logo, no
   brand intro. Real screenshots are also the safest input under the Apr 2026 originality policy.
4. **Slide 2 = a second standalone cold-open hook**, not a continuation. Mosseri (Oct 2024): if a viewer
   doesn't swipe, Instagram will often re-serve the carousel **starting at slide 2**. Never put setup there.
5. **≤12 words per slide**, one idea, two type sizes max. Must read at thumbnail size in the Reels tab.
6. **Always attach music** — it's what makes a carousel eligible for the Reels tab. Non-skippable step.
7. **Final slide CTA = "send this to the friend who'd hold your key."** Sends-per-reach is among Mosseri's
   stated top-three 2026 ranking signals, weighted several times a like — and it is literally the product
   mechanic. Waitlist link goes **second**, in the caption.
8. **≤3 hashtags, or none.** Metricool 2026 (24.3M posts): posts with hashtags got **31.7% fewer views**.
9. **Originality:** every post must differ in footage or in claim — not just caption. Never re-upload the
   same asset; never publish the same asset from two accounts. Self-designed slides are original; a
   third-party screenshot with a caption bolted on is not.

## 8. Angles — ranked

| # | Angle | Needs a live pact? |
|---|---|:---:|
| 1 | **The denial** — real push notification: "Marek denied your unlock. 4h 12m remaining." Slide 2: the group chat reacting. *This is the ad.* | 🔴 yes |
| 2 | **The beg** — the actual message you sent, and the reply. Names blurred. | 🔴 yes |
| 3 | **The 4-second objection** — "every screen-time app you tried, you deleted in 4 seconds." Why self-imposed limits fail and a second person doesn't. | ✅ no |
| 4 | **Objection carousels** — "what if my friend's asleep", "what if I need Maps", "what if I just delete the app". Highest-save format. | ✅ no |
| 5 | **Founder's own screen time**, weekly, including the bad weeks. | ✅ no (needs your real screenshot) |
| 6 | **The friend's side** — what it looks like when someone asks *you* for a key. | 🔴 yes |
| 7 | **Waitlist counter** — once the number isn't embarrassing. | ✅ no |

**Never make:** generic "dopamine detox" listicles, AI stock imagery, "top 5 focus apps" roundups, or
anything an account that doesn't own this product could post. No moat, and it walks straight into both
platforms' originality enforcement.
