# YouTube Outlier Ads and Brand Videos from English / Language-Learning Apps (as of 24 Nov 2026)

Builds on `research_notes/Outlier ads English IELTS leadership/english_apps.md`, which covers the Meta ad library, TikTok and the Praktika "Gustavo" story.

**Labels used throughout**
- **[VERIFIED]**: pulled directly from YouTube data on 2026-11-24 (view count, likes, publish date, length, public/unlisted status, transcript). Source: the Firecrawl Alexandria `youtube-com` provider (`video_details`, `video_transcript`, `channel_shorts`).
- **[3P-DATA]**: third-party scrape. ScrapeCreators channel listings give relative dates such as "2 years ago", shown below as "~", and view counts. Ads Transparency Center data came through a Firecrawl scrape.
- **[OBSERVATION]**: my own inference.

**How outliers were measured**
- **Outlier ratio** = video views ÷ the channel's median views.
  - Where I pulled a "latest" upload list, the median comes from the last 30 uploads: Preply ≈1,000 and Duolingo ≈105,600.
  - Otherwise I used the median of the channel's top 30 "Popular" videos (marked "pop-median"). This median is inflated, so those ratios are conservative.
  - For Shorts with no median available, I used views ÷ subscribers.
- **Like-to-view ratio**: organic YouTube videos usually get roughly 1–4% likes per view. Paid in-stream or skippable views rarely produce likes. A ratio below about 0.05% is therefore a strong sign that most views were paid. **[OBSERVATION / heuristic]**

---

## Q1. Which brand-channel videos have outlier view counts (likely ad-boosted)?

### Takeaway
- **Preply is the stand-out paid YouTube advertiser in the category.** Its channel has 67.4K subscribers and a typical upload gets about 1,000 views, yet its 15–36-second "Better Duo" / "Progress takes two" spots carry 10M–172M views each with almost no likes. The largest is "So... Preply 🩷 | Better Duo": 171.7M views and 1,550 likes, a ~170,000× outlier.
- **Talkpal** (4.3K subscribers) runs the same playbook. Its 30–53-second AI-avatar spots, localized into roughly 15 languages, reach 0.3M–7.5M views each.
- **Cambly and Busuu** each have one or two boosted brand spots in the 4.7M–9.7M range.
- **Praktika's** top YouTube asset is different: the 7.4M-view "Gustavo" Short has a 1.8% like rate, so it is an organic viral video, not a paid one. It is the creative the CEO credits for the $1M→$10M+ ARR jump.
- None of the checked outliers is unlisted. All are public uploads on the brand channel.

### Cited Findings

**Catalogue of specific videos (sorted by app)**

| # | App | Video (URL) | Views | Upload date | Length | Format | Hook (first ~5s, verbatim where transcript exists) | Angle | Offer / CTA | Outlier signal |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Preply | [So... Preply 🩷 \| Better Duo](https://www.youtube.com/watch?v=SfT57zeE4HE) | 171,697,371 | 2025-05-07 | 0:36 | TV-style spot (animated character vs. human tutor) | "So why should I learn the language with either of you?" | Comparative: "We have animated characters. We have humans. You get the real human connection." Implicit jab at app-only rivals (an animated mascot) | "Discover the better duo." | ~170,000× channel median; 1,550 likes = 0.0009% **[VERIFIED]** |
| 2 | Preply | [Your Super Tutor + you = the better duo](https://www.youtube.com/watch?v=zzR8tXICfoo) | 52,295,444 | ~2025 | 0:28 | TV-style spot | "The dog is in the fridge. The boy eats the moon." (absurd textbook sentences) | Apps teach useless sentences; a tutor gets you to "real talk" | "Find your super tutor today and make real progress with the better duo for you." | ~52,000× **[VERIFIED transcript; 3P views/date]** |
| 3 | Preply | [Language Learning Lab \| Better Duo](https://www.youtube.com/watch?v=T9_F7zYDdJA) | 37,436,049 | ~Jan 2026 | 0:31 | TV-style spot | (no transcript pulled) | Better Duo series | Better Duo | ~37,000× **[3P-DATA]** |
| 4 | Preply (ES market) | [Cómo NO hablar inglés.](https://www.youtube.com/watch?v=Ii7X_wCzmYY) | 29,154,392 | 2026-03-04 | 0:15 | Bumper-length skit | "My... red malet is lost. I need..." (a traveller freezes in broken English) | Embarrassment at the airport; "hablar inglés pro" | "Busquen al tutor de Preply más cercano… Preply, la prep para hablar inglés pro y progresar tres veces más rápido" ("Find the nearest Preply tutor… Preply, the prep to speak pro English and progress three times faster") | **5 likes** on 29M views **[VERIFIED]** |
| 5 | Preply | [Super Tutor vs. self-learning app](https://www.youtube.com/watch?v=Sajl1Ki9oAI) | 27,635,353 | ~2025 | 0:29 | TV-style spot | (title = hook) | Tutor vs. self-learning app | Better Duo | ~27,600× **[3P-DATA]** |
| 6 | Preply | [Based on a true story: Iryna & Chantelle](https://www.youtube.com/watch?v=OBP-2E2cy3U) | 23,878,086 | 2026-04-09 | 0:34 | Testimonial mini-doc | "Irina studied English her whole life, but when strangers heard her speak, she froze…" | Career transformation: "co-founder of a startup, negotiating, presenting, and raising investment… in English" | "You can also find the best tutor for you and progress with Preply." | 36 likes on 23.9M views. The long cuts of the same stories (1:30+) get only 700–3,100 views **[VERIFIED]** |
| 7 | Preply | [Who wants to be fluent \| Better Duo](https://www.youtube.com/watch?v=yg6wE252dj0) | 20,415,319 | ~Jan 2026 | 0:30 | TV-style game-show parody | (title) | Quiz-show parody | Better Duo | ~20,000× **[3P-DATA]** |
| 8 | Preply | [Based on a true story: Chris & Luis](https://www.youtube.com/watch?v=p9A_KzM9a6I) | 19,822,095 | ~Apr 2026 | 0:35 | Testimonial | — | Learner–tutor story | Progress takes two | ~19,800× **[3P-DATA]** |
| 9 | Preply (ES) | [¿Qué hablan en Londres?](https://www.youtube.com/watch?v=-n3L1G0K-FY) (+ variants [c8eYNEsPrhw](https://www.youtube.com/watch?v=c8eYNEsPrhw), [98v6U62XXjQ](https://www.youtube.com/watch?v=98v6U62XXjQ)) | 15.3M / 10.95M / 10.3M | ~Mar 2026 | 0:15 each | Bumper-length skit, 3 cut-downs | "What do they speak in London?" | Accent and comprehension anxiety | Preply tutor | Three near-identical 15s edits each above 10M points to A/B creative testing **[3P-DATA]** |
| 10 | Preply (ES) | [¿Y si tu ascenso dependiese de tu nivel de inglés?](https://www.youtube.com/watch?v=rMFVq8Ec_kw) | 2,153,992 | ~Sep 2026 | 0:20 | Skit | "What if your promotion depended on your English level?" | Career / promotion | Preply | ~2,100× and recent: Preply is still buying in Q3–Q4 2026 **[3P-DATA]** |
| 11 | Preply | [The card mix-up that turned into a language lesson](https://www.youtube.com/watch?v=U1NEA3n49Kw) | 1,794,707 | ~Sep 2026 | 0:33 | Story skit | — | Serendipity / human connection | Preply | ~1,800× **[3P-DATA]** |
| 12 | Talkpal | [Talkpal AI - Language Learning Platform](https://www.youtube.com/watch?v=wl-_FJms5wg) | 7,485,926 | 2025-03-24 | 0:42 | AI-avatar tutor demo | "Learn languages faster with AI. Hi, I'm Emma, your personal AI language teacher…" | AI corrects mistakes in real time; chat, call mode, role-plays, debates | "Join over a million other learners… the most efficient way to learn a language" | 79 likes (0.001%) on a 4.3K-subscriber channel **[VERIFIED]** |
| 13 | Talkpal | [Say Goodbye To Boring Language Learning](https://www.youtube.com/watch?v=89sPuu7yjSs) | 6,304,990 | ~2025 | 0:30 | AI-avatar demo | (title) | Anti-boredom | Free sign-up | **[3P-DATA]** |
| 14 | Talkpal | Localized cuts: [FR](https://www.youtube.com/watch?v=Wp5pMYYQUxI) 4.22M, [DE](https://www.youtube.com/watch?v=fjPbWOUpKGk) 2.90M, [PT](https://www.youtube.com/watch?v=kvcsxBIx-m0) 0.75M, [ES](https://www.youtube.com/watch?v=TSDwfYEZEFc) 0.69M, [IT](https://www.youtube.com/watch?v=V5zG3dCv_pQ) 0.33M, [HU](https://www.youtube.com/watch?v=IXl3Pd36gCg) 0.29M, [CZ](https://www.youtube.com/watch?v=54XAQB0ZzD4) 0.29M | as listed | ~2025 | 0:50–0:55 | Same AI-avatar demo, dubbed | — | Same | Same | The median of the channel's top 30 is 252K on a 4.3K-subscriber channel, so the whole channel is ad inventory **[3P-DATA]** |
| 15 | Talkpal | Shorts "Talkpal AI Review": [EN](https://www.youtube.com/shorts/3tUQK1PigwQ) 1.2M, [FR](https://www.youtube.com/shorts/Hh1XDLVLBP4) 1.1M, [ES](https://www.youtube.com/shorts/ZSZ_ODKNy_w) 495K, [DE](https://www.youtube.com/shorts/aReW0LmYPe0) 448K | as listed | n/a | Short | Faux-review / UGC-style Short | "Talkpal AI Review…" | Review framing | Free | 250–280× subscribers **[VERIFIED list]** |
| 16 | Praktika | [Praktika AI Tutor Corrects Mistake Live!](https://www.youtube.com/shorts/_qQhFyDqFXI) | 7,395,074 | 2024-01-23 | 0:36 | Short; human learner and AI tutor correction | "Let's practice your English. What's your name? / My name is Gustavo. / How old are you? / I have 22. / Do you mean I am 22?" | Coach corrects mistakes. Then: "I don't have money to pay for a tutor." "Did you know that an AI tutor is much cheaper than a human tutor?" | "Just download the Praktika app and practice anytime and anywhere you want." | 133,260 likes (1.8%), so **organic viral**. About 790× the channel's 9.37K subscribers **[VERIFIED]** |
| 17 | Praktika | [Do you like coffee? - Practice your English with Dwayne](https://www.youtube.com/shorts/PB9OP2t6ves) | 3.8M | n/a | Short | Same correction template, different avatar ("Dwayne") | "Do you like coffee? / Yes, I like. / Do you mean yes, I do?" | Grammar correction; then the "I don't have time" objection | "You can learn and practice anytime and anywhere… I'll download Praktika right now." | Replica of #16 **[VERIFIED transcript]** |
| 18 | Praktika | [Learn English with Praktika App](https://www.youtube.com/shorts/n36SYNrRKc0) (3M), [Learn English with Praktika](https://www.youtube.com/shorts/iq0_Kfcn4GA) (1.5M) | 3M / 1.5M | n/a | Shorts | Template replicas | — | — | Download | **[VERIFIED list]** |
| 19 | Praktika | [Omg - Learn and Practice English with Praktika](https://www.youtube.com/watch?v=ZF_VmBHfkYo) | 791,007 | 2024-03-11 | 1:05 | Long-form version of creator skit | (no description) | — | Download | ~126× pop-median (6,284); 0.18% likes. Probably partly boosted **[VERIFIED]** |
| 20 | Praktika | [Introducing Praktika's Next Gen Avatars](https://www.youtube.com/watch?v=o23kWbBWBXQ) / [Praktika 4.0 Launched](https://www.youtube.com/watch?v=7TF7kSVygRw) | 476K / 329K | ~2023 / ~Apr 2026 | 1:40 / 0:43 | Product-launch demo | — | Avatar realism / new features | Download | ~76× / ~52× pop-median **[3P-DATA]** |
| 21 | ELSA Speak | [🧅🥬🍅 #learnenglish #elsaspeak](https://www.youtube.com/shorts/KcfzwCzUC9A) | 31,135,148 | 2023-10-07 | 0:16 | Pronunciation Short (audio-led) | "onion… onion… lettuce… lettuce… tomato" | Hear and repeat tricky words | Description: "7 day free trial" link | 329,026 likes (1.06%), so **organic viral**. About 320× the 97.3K subscribers on ELSA Speak Global **[VERIFIED]** |
| 22 | ELSA Speak | [Can you pronounce these? 💐](https://www.youtube.com/shorts/FuARGeAKNlE) 16M; [Chocolate Chip!](https://www.youtube.com/shorts/l7_AKnSNlrQ) 8.5M; [Say goodbye to those embarrassing mispronunciations with ELSA now](https://www.youtube.com/shorts/42KNZ_mdKKw) 5.2M | as listed | ~2023–24 | Shorts | Pronunciation challenge | "Can you pronounce these?" | Embarrassment / challenge | ELSA download | **[VERIFIED list]** |
| 23 | Cambly (Arabic) | [عشان ما تلعب بك اللغة، العب فيها انت - سجّل بكامبلي](https://www.youtube.com/watch?v=lVHRQSHoGgU) ("So the language doesn't play you, play it yourself. Sign up for Cambly") | 9,674,086 | 2021-10-19 | 1:21 | TV-style Gulf spot | Description hook: "Yes… No… Of course… ما تمشّيك!" ("won't get you far!") | Stop relying on 3 stock English words; make English "your game" (#الإنقليزي_لعبتك, "#EnglishIsYourGame") | "سجل بكامبلي" ("Sign up at Cambly") + link | 7,983 likes (0.08%), so mostly paid **[VERIFIED]** |
| 24 | Cambly | [Meet the new Cambly](https://www.youtube.com/watch?v=JCWju3zEPoo) | 4,924,337 | 2024-09-16 | 1:45 | Brand manifesto / rebrand film | "Learning English isn't quiet. Or easy. Or by the book. Or a straight line." | Mistakes are progress | "Progress, not perfection. Cambly." | **296 likes on 4.9M views (0.006%)**. Captions in 8 languages point to a global paid launch **[VERIFIED]** |
| 25 | Cambly | [What is Cambly Pro?](https://www.youtube.com/watch?v=fevhLx6i7DU) | 556,578 | ~Mar 2026 | 0:10 | Bumper | (title) | New Pro tier | Cambly Pro | 10s bumper length **[3P-DATA]** |
| 26 | Busuu | [🗣️ Speak confidently with our new video bites!](https://www.youtube.com/watch?v=85fsHGH4zQA) | 4,666,846 | 2023-10-03 | 0:24 | Feature spot (real people speaking) | Japanese learner lines: "毎日漢字を書いています" ("I write kanji every day") | Learn from real native-speaker clips | "Download today" (Adjust tracking links) | ~12.5× the channel's next-best video (372K); ~300× pop-median; 0.026% likes **[VERIFIED]** |
| 27 | Lingoda | [Learn a language with Lingoda \| Wrong haircut \| TV Commercial](https://www.youtube.com/watch?v=p-e3bFownr0) / [Focus at the office](https://www.youtube.com/watch?v=IFXfL3ibZVw) | 944,559 / 433,262 | ~2021 | 0:16 | TV-style comedy spot | "Wrong haircut" (a misunderstanding gag) | Language mistakes cause real-life mishaps | Lingoda | ~33× pop-median **[3P-DATA]** |
| 28 | Duolingo | [Duo's Work Day \| behind the scenes of notifications](https://www.youtube.com/watch?v=IEHiY8scAKI) | 32,873,206 | ~2024 | 1:30 | Animation (brand film) | (title) | Mascot humour: notification guilt | Brand | ~311× the latest-30 median (105.6K) **[3P-DATA]** |
| 29 | Duolingo (PT-BR) | [Como o Duolingo mudou minha vida. Histórias reais.](https://www.youtube.com/watch?v=gzVG2M7szrc) ("How Duolingo changed my life. Real stories.") / [How I Learned French With Duolingo - Real Learner Stories](https://www.youtube.com/watch?v=FtcNTRVxB-s) | 22.6M / 19.5M | ~2022 | 1:01 / 0:41 | Learner testimonial | "Real learner stories" | Proof it works | Download | ~200× median. These are classic in-stream testimonial ads **[3P-DATA]** |
| 30 | Duolingo | [Korean or Get Eaten - Duolingo x Squid Game](https://www.youtube.com/watch?v=bN2rUoX7540) / [Duo joins Squid Game](https://www.youtube.com/watch?v=o3ftECYtkf0) | 14.9M / 11.2M | ~2025 | 2:49 / 0:30 | IP collab, animation / music | (title) | Pop-culture tie-in | Brand | ~140× / ~107× **[3P-DATA]** |

**Supporting data points**
- **Preply channel**: 67.4K subscribers, 455 videos **[VERIFIED]** ([channel](https://www.youtube.com/@preply)).
  - The last 30 uploads have a median of about 1,000 views. Recent podcast and tutor-tips uploads get 300–3,000 views.
  - In the same feed, the 15–35s ad cuts get 1.4M–29M views. Example: [U1NEA3n49Kw](https://www.youtube.com/watch?v=U1NEA3n49Kw) at 1.79M sits next to [bjrOhaNiwYw](https://www.youtube.com/watch?v=bjrOhaNiwYw) at 593. **[3P-DATA]**
- **Talkpal channel**: 4.34K subscribers, 127 videos. Its description says "Learn 5x Faster" and lists 130+ languages. — [Talkpal channel](https://www.youtube.com/@Talkpal) **[VERIFIED]**
- **Praktika channel**: "Speaking English Praktika" (@praktikaai), 9.37K subscribers, 380 videos. The median of its top 30 popular long-form videos is 6,284. — [channel](https://www.youtube.com/@praktikaai) **[VERIFIED]**
- **ELSA channels**:
  - "ELSA Speak Global" (@ELSAspeakglobal): 97.3K subscribers, 535 videos. — [channel](https://www.youtube.com/@ELSAspeakglobal)
  - "ELSA Speak Official": only 39 subscribers. Its top long-form video is "Salma Hayek Thought Her Husband Was Having an Affair with ELSA App" ([QK2Kpn3fv6k](https://www.youtube.com/watch?v=QK2Kpn3fv6k), 92K, ~2023). **[VERIFIED / 3P]**
- **Cambly**: the global channel is @CamblyGlobal and the Arabic channel is @camblyar. The handle @cambly belongs to an unrelated personal account. **[VERIFIED]**
- **Unlisted check**: every video checked with `video_details` returned `is_unlisted: false`. That covers Preply ×3, Talkpal, Praktika ×2, Cambly ×2, Busuu and ELSA. **[VERIFIED]**

### Inferences
- **Two YouTube growth modes stand apart.**
  - **(a) Paid in-stream / Shorts-ad inventory** parked publicly on the brand channel, with near-zero likes: Preply, Talkpal, Cambly, Busuu and Duolingo's testimonial ads.
  - **(b) Organic viral Shorts** with roughly 1–2% like rates: Praktika's Gustavo correction skit, ELSA's pronunciation Shorts and Duolingo's mascot Shorts.

  The AI-tutor upstarts that went viral (Praktika, ELSA) did it with **organic Shorts**. The tutor marketplaces (Preply, Cambly) bought reach with **TV-style brand spots**. **[OBSERVATION]**
- **Preply's 2025–26 YouTube creative system has three parts:**
  - (1) "Better Duo", which positions a human tutor against mascot or app learning;
  - (2) "Progress takes two", true-story testimonials cut to 34–38s from roughly 1:30 masters;
  - (3) Spanish-market 15–20s skits on embarrassment and career (airport, London, promotion), cut into several near-identical variants.

  This is the most investable template in the category by observed view volume (more than 450M cumulative views across the top 20 cuts). **[OBSERVATION]**
- **Praktika's 7.4M-view Short (Jan 2024) almost certainly is the "Gustavo" video** CEO Adam Turaev credits for the $1M→$10–12M ARR jump. The learner says "My name is Gustavo" and "I'm from Brazil", which matches the Brazil go-to-market and the "AI tutor is much cheaper than a human tutor" price angle described on the [Sub Club podcast](https://subclub.com/episode/how-praktika-built-a-profitable-50m-arr-ai-business-adam-turaev-praktika). Its structure: (1) a fragment of small talk, (2) an error in the learner's English ("I have 22"), (3) a gentle "Do you mean…?" correction, (4) an objection ("no money for a tutor" / "no time"), (5) the AI-is-cheaper reveal, (6) "I'll download Praktika right now". **[OBSERVATION, strong match]**

### Gaps
- **Speak** (@usespeak, channel ID UCrtzNjrz0r0EcTU-hYo6WSQ) resolved, but its popular and Shorts listings failed or returned nothing. No Speak YouTube outlier could be confirmed. The @speakapp handle is an unrelated payments brand.
- **Babbel**: no official channel handle resolved (@babbel and @BabbelOfficial both returned errors). The Babbel commercials found were re-uploads by third parties, e.g. ["Babbel Commercial - Spanish Passion"](https://www.youtube.com/watch?v=6dTN6UWbEKA) with 266K views (~2017). These are not brand-channel data.
- **Thin or no YouTube presence**:
  - Promova: 2 videos.
  - Loora: 2 subscribers.
  - Learna: 2 subscribers, 2 videos.
  - Falou: only third-party reviews plus ["The Falou Method"](https://www.youtube.com/watch?v=Lx3K_Kcg3-Q) at 38.9K, ~2021.
  - These apps appear to run ads from unlisted or non-channel assets, or not on YouTube at all.
- **Engoo and Memrise** were not analysed in depth. Memrise's top video is ["I love you x 100"](https://www.youtube.com/watch?v=P5f1Y3CWTc0) at 982K, about 14 years old, which is outside the useful window.
- **Missing details**:
  - Exact upload dates for rows marked "~" come from relative timestamps.
  - Hooks for rows without transcripts are inferred from titles only.
  - Truly unlisted ad videos cannot be found from channel listings by design. The Ads Transparency Center is the route, and it was only partly checked (see Q2).

---

## Q2. Are any listed in Google Ads Transparency Center, and what creatives appear?

### Takeaway
Only Preply was checked before Firecrawl credits ran out. The domain preply.com shows **about 1K video ads** across advertiser accounts. The main verified advertiser is **"Preply Inc"** (AR14659449058922332161), whose video creatives are served from YouTube video IDs. A second verified advertiser named as an individual ("Ivan Kolupaev") also points to preply.com, most likely an affiliate or tutor-side advertiser.

### Cited Findings
- Ads Transparency Center, preply.com, format = Video, region = anywhere: "This domain includes results for multiple advertiser accounts… **~1K ads**." **[3P-DATA: scrape of the live page]** — [Ads Transparency: preply.com video](https://adstransparency.google.com/?region=anywhere&domain=preply.com&format=VIDEO)
- The first creatives shown, all from "Preply Inc, Verified", use YouTube thumbnails for these video IDs **[3P-DATA]**:
  - g19ZtK_pVZM — [creative CR09188199527465615361](https://adstransparency.google.com/advertiser/AR14659449058922332161/creative/CR09188199527465615361?region=anywhere&format=VIDEO)
  - NJEpsv3R_ZE — [CR07269103136252362753](https://adstransparency.google.com/advertiser/AR14659449058922332161/creative/CR07269103136252362753?region=anywhere&format=VIDEO)
  - EkbdULRKOnc — [CR03399666631410974721](https://adstransparency.google.com/advertiser/AR14659449058922332161/creative/CR03399666631410974721?region=anywhere&format=VIDEO)
- These three IDs do **not** appear in Preply's public top-30 popular or latest-30 lists. They are probably unlisted ad uploads or older or other-channel assets. **[OBSERVATION]**
- A second verified advertiser, "Ivan Kolupaev", also runs a video creative to preply.com. — [CR15923758006320234497](https://adstransparency.google.com/advertiser/AR10241869500412592129/creative/CR15923758006320234497?region=anywhere&format=VIDEO) **[3P-DATA]**

### Inferences
- Preply's huge public view counts (Q1) and its roughly 1K Google video creatives are consistent with Preply being the category's heaviest YouTube and Google video buyer. **[OBSERVATION]**

### Gaps
- Firecrawl credits ran out. The prepared Ads Transparency queries for speak.com, praktika.ai, talkpal.ai, babbel.com, cambly.com, elsaspeak.com and promova.com were not run. The structured provider `adstransparency-google-com/ad-transparency/list_ads` with `format: VIDEO, region: anywhere` is the next step.
- The Transparency Center does not show impressions or spend for commercial (non-political) ads, so creative-level performance cannot be compared there.

---

## Q3. What are the top-viewed Shorts from these brands?

### Takeaway
- **Duolingo** dominates in absolute views: mascot and meme Shorts of 9M–82M each, on 7.11M subscribers.
- **Relative to channel size**, the standouts are:
  - ELSA Speak Global's pronunciation Shorts: 31M on 97K subscribers.
  - Praktika's AI-correction Shorts: 7.4M on 9.4K subscribers.
- **Preply's** Shorts tab is small (top 454K). Its reach goes through 15–36s landscape and vertical spots in the main video feed instead.

### Cited Findings
**Top Shorts by brand (views as of 2026-11-24) [VERIFIED list via `channel_shorts`, sort = popular]**

**Duolingo** ([@duolingo](https://www.youtube.com/@duolingo), 7.11M subscribers, 1.1K videos)

| Short | Views |
|---|---|
| [duo levels😱 which is best???? #roblox](https://www.youtube.com/shorts/nppDkHubAUY) | 82M |
| [Pour one out for the bear. #RIPDuo](https://www.youtube.com/shorts/J8efz1F8Ts8) | 45M |
| [BTS of my BBL for game day #SuperbOwl](https://www.youtube.com/shorts/aH-85nmkHHE) | 43M |
| [Stop reading this caption and go do your lessons](https://www.youtube.com/shorts/uo5PfiJznzs) | 34M |
| [Sharing is caring💋](https://www.youtube.com/shorts/zDemiJmV5lM) | 26M |

**ELSA Speak Global** ([@ELSAspeakglobal](https://www.youtube.com/@ELSAspeakglobal), 97.3K subscribers)

| Short | Views |
|---|---|
| [🧅🥬🍅](https://www.youtube.com/shorts/KcfzwCzUC9A) | 31M |
| [Can you pronounce these? 💐](https://www.youtube.com/shorts/FuARGeAKNlE) | 16M |
| [Chocolate Chip!](https://www.youtube.com/shorts/l7_AKnSNlrQ) | 8.5M |
| [Do you know how to pronounce these words?🤔](https://www.youtube.com/shorts/4WoYyX4DDig) | 7M |
| [Choose your favourite Olympic sport!](https://www.youtube.com/shorts/H89kLIkdykk) | 6.6M |
| [Say goodbye to those embarrassing mispronunciations with ELSA now](https://www.youtube.com/shorts/42KNZ_mdKKw) | 5.2M |
| [Where is the train station? 🗣️](https://www.youtube.com/shorts/54hd6c64EVE) | 3.4M |

**Praktika** ([@praktikaai](https://www.youtube.com/@praktikaai), 9.37K subscribers)

| Short | Views |
|---|---|
| [Praktika AI Tutor Corrects Mistake Live!](https://www.youtube.com/shorts/_qQhFyDqFXI) | 7.3M |
| [Do you like coffee? (Dwayne)](https://www.youtube.com/shorts/PB9OP2t6ves) | 3.8M |
| [Learn English with Praktika App](https://www.youtube.com/shorts/n36SYNrRKc0) | 3M |
| [Learn English with Praktika](https://www.youtube.com/shorts/iq0_Kfcn4GA) | 1.5M |
| [Learn and Practice English with Praktika](https://www.youtube.com/shorts/2hP1EBbqqLE) | 318K |
| [Speak English with Praktika (Stories in Portuguese 1)](https://www.youtube.com/shorts/WScSSWvrKFo) | 153K |

Everything after the top four drops below 100K.

**Talkpal** ([@Talkpal](https://www.youtube.com/@Talkpal), 4.34K subscribers)

| Short | Views |
|---|---|
| [Talkpal AI Review - AI Language Learning](https://www.youtube.com/shorts/3tUQK1PigwQ) | 1.2M |
| [Avis sur Talkpal AI](https://www.youtube.com/shorts/Hh1XDLVLBP4) (French: "Talkpal AI review") | 1.1M |
| [Reseña de Talkpal AI](https://www.youtube.com/shorts/ZSZ_ODKNy_w) (Spanish: "Talkpal AI review") | 495K |
| [Talkpal AI Bewertung](https://www.youtube.com/shorts/aReW0LmYPe0) (German: "Talkpal AI review") | 448K |

**Preply** ([@preply](https://www.youtube.com/@preply), 67.4K subscribers)

| Short | Views |
|---|---|
| [Messi vs Bellingham: We got the transcript 🫪](https://www.youtube.com/shorts/hHDsEhdTUaY) | 454K |
| [It's official, we've reinvented the Preply brand! #PracticeMakesPossible](https://www.youtube.com/shorts/OE5aI3vlToQ) | 77K |
| [Learn on Preply and watch yourself progress. Innit, mate? 😏](https://www.youtube.com/shorts/VFZzn4tmcHQ) | 66K |

The brand-refresh Short names a new tagline, **"Practice Makes Possible"**.

**ELSA Speak Official** ([channel](https://www.youtube.com/channel/UCNsGcqUpJCFxucZYFcZRYhw), 39 subscribers): top Short has 747 views. This is a dormant secondary channel.

### Inferences
- **Shorts outliers relative to subscribers**:
  - Praktika's correction skit: about 790×.
  - ELSA's pronunciation Shorts: about 320×.
  - Talkpal's "AI Review" Shorts: about 280×.

  Shorts-feed distribution (or Shorts ads) is decoupled from subscriber count, so small AI-tutor brands can reach Duolingo-scale views per asset. **[OBSERVATION]**
- **Two Shorts formats win for AI-tutor apps:**
  - (1) the **mistake → "Do you mean…?" correction** skit (Praktika);
  - (2) the **"Can you pronounce these?"** word-repeat challenge (ELSA).

  Both deliver a micro-lesson within 3 seconds and need no brand context to be watchable. **[OBSERVATION]**
- Talkpal titles its Shorts "AI Review". That faux-review packaging makes branded assets look like third-party UGC. **[OBSERVATION]**

### Gaps
- No Shorts data for Speak, Babbel, Cambly, Promova, Busuu, Loora or Learna: listings failed, the channel was not found, or the channel was empty.
- Shorts publish dates and likes were only pulled for the two Shorts in Q1 (Praktika and ELSA).

---

## Q4. Creator sponsorships: which apps sponsor English-teaching YouTubers, and which sponsor reads appear most?

### Takeaway
- In the **latest 30 uploads** of five major English-teaching channels, no description linked to a third-party app sponsor:
  - English with Lucy (14M+ subscribers)
  - mmmEnglish
  - Speak English With Vanessa
  - Learn English With TV Series
  - Rachel's English
- Instead, the biggest creators now promote **their own products**. Lucy pushes her own "Langua" AI conversation partner (code LUCY20) and her own English programmes.
- Historical brand–creator partnerships are visible mainly as **Lingoda** content featuring English with Lucy and other creators (2018–2020).

### Cited Findings
- **English with Lucy**, description of [GE8qKjV2fpU](https://www.youtube.com/watch?v=GE8qKjV2fpU) (2026-11-19), with the same block on 29 of 30 recent uploads:
  - "Explore Langua, the world's most advanced AI for language learning. You can now chat with your own Lucy AI conversation partner (yes, it's my real voice)! Try it here and then save 20% on the Unlimited Annual Plan with the code LUCY20."
  - Also: "BLACK FRIDAY: 50% OFF my B1–C2 English programmes" and "Want to find your perfect tutor? … https://ewl.info".
  - **[VERIFIED: description text via ScrapeCreators]**
- **mmmEnglish**: 14 of 30 recent descriptions mention "partners and practise in real conversations". This appears to be the creator's own speaking-partner offer, not a third-party sponsor. **[3P-DATA; OBSERVATION on interpretation]** — [mmmEnglish channel](https://www.youtube.com/@mmmEnglish_Emma)
- **Speak English With Vanessa, Learn English With TV Series, Rachel's English**: no description mentions of Speak, Preply, Cambly, Babbel, Lingoda, ELSA, Praktika, Busuu, Promova, Talkpal, Loora, Engoo or Memrise in the last 30 uploads. **[3P-DATA]**
  - One false positive: "Elsa" in [Learn English with FROZEN](https://www.youtube.com/watch?v=wZjGV_VwIt4) refers to the Disney character.
- **Lingoda creator partnerships, hosted on Lingoda's own channel** **[3P-DATA]**:
  - ["Why English with Lucy loves Lingoda"](https://www.youtube.com/watch?v=XChBwA2I81A): 10,154 views, ~2020.
  - ["Superholly meets Lingoda"](https://www.youtube.com/watch?v=NKdPd5EE924): 7,484 views, ~2020.
  - ["Zoey Arielle on Business English with the Lingoda Language Sprint"](https://www.youtube.com/watch?v=VxEWUe__fUU): 58,529 views, ~2018.
- **Busuu** cross-channel collab: ["Guessing HARD English Words: @LearnGermanFast vs English Speaker"](https://www.youtube.com/watch?v=MUWvFW11tWg), 5,754 views, ~2022. **[3P-DATA]**
- **Speak** runs a referral program that creators use. A referral page reads "John Fotheringham sent you $10.00 off a Speak membership" (John Fotheringham is a language-learning creator). — [Speak referral page](https://app.speak.com/us-en/i/DZVPSM) **[3P-DATA]**
- From the earlier notes: Preply runs 511 Meta **creator partnership ads** with "Use the link in my BIO and get 50% OFF on your first lesson" codes, which is the largest creator-sponsorship footprint observed. That program lives on Meta and TikTok, not in English-teacher YouTube descriptions. — [AdManage: Preply](https://admanage.ai/ad-library/preply)

### Inferences
- **The top English-teacher YouTubers have shifted from app sponsorships to their own products**, including their own AI tutors (Lucy's Langua). That removes the biggest English-education inventory from sponsors like Lingoda, which partnered with Lucy around 2020. Brands now reach learners through:
  - (a) paid in-stream on those channels' audiences;
  - (b) smaller mid-tier teacher creators;
  - (c) Meta/TikTok creator partnership ads (Preply's model).

  **[OBSERVATION]**
- No "most frequent sponsor read" could be established from this sample. If one dominates historically, Lingoda is the best-evidenced English-teacher sponsor and Preply the best-evidenced creator-ad sponsor overall. **[OBSERVATION, low confidence]**

### Gaps
- Only video **descriptions** were checked, and only for the last 30 uploads per channel. Spoken mid-roll sponsor reads without a description link, and older sponsorships (2021–2025), were not captured.
- The YouTube "paid promotion" disclosure flag was not checked.
- A sponsorship tracker (e.g. Sponsors.Tube or SponsorBlock-based data) was not reached before credits ran out.
- Not checked: Learn English with EnglishClass101, Linguamarina, BBC Learning English (pulled, but no sponsor mentions as expected for the BBC), Arnel's Everyday English, Bob the Canadian. Mid-tier channels are more likely to carry Speak, Cambly or Preply reads.
