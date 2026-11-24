# TikTok Outlier Ads and Viral Videos: English-Learning Apps and Programs (catalogue, as of 24 Nov 2026)

This file extends `research_notes/Outlier ads English IELTS leadership/english_apps.md`. That file already covers Praktika's "Gustavo" story, the Meta Ad Library long-runners, and the hook taxonomy, so none of that is repeated here. This file adds a ranked catalogue of specific TikTok ads with Creative Center IDs.

**Labels**
- **[VERIFIED]**: stated by the company, the platform or the founder.
- **[3P-DATA]**: TikTok Creative Center Top Ads records retrieved through the AnyAPI provider in Firecrawl Alexandria (`anyapi/tiktok/top-ads-search`), plus third-party trackers.
- **[OBSERVATION]**: my own reading or inference.

**How to read the Creative Center fields**
- **Link pattern.** Each ad links to its Creative Center detail page: `https://ads.tiktok.com/business/creativecenter/topads/{adId}/pc/en`. The source query was the Top Ads list at <https://ads.tiktok.com/business/creativecenter/inspiration/topads/>. TikTok's help page notes that Top Ads only shows ads the advertiser has authorized ([About Top Ads](https://ads.tiktok.com/help/article/top-ads)). So "absent from Top Ads" does not mean "not advertising."
- **`ctr` score.** Values run from 0 to 1. Across about 120 records, ads with very high likes consistently had low values (0.03–0.27), and low-like ads had high values (0.7–0.98). That pattern suggests the score is a CTR percentile position where lower is stronger, i.e. 0.17 ≈ "top 17%". **[OBSERVATION, unconfirmed]** The earlier notes read the score the other way round, so treat it as directional only.
- **`cost` field.** Values are 0, 1 or 2. This appears to be Creative Center's budget tier (low / medium / high). **[OBSERVATION, unconfirmed]**
- **Dates.** Ad creation dates were decoded from the TikTok ad ID (a snowflake ID; the upper 32 bits are a Unix timestamp). **[OBSERVATION: standard decoding method]**
- **Period filter.** The `period: 180` and `period: 30` filters still returned ads created in 2022–2023. The filter seems to mean "ranked or active in the window," not "created in the window."
- **No region field.** The provider returned no region, so the region in the catalogue is inferred from the ad language and the brand. **[OBSERVATION]**

---

## Which English-app ads rank top in TikTok Creative Center, and what are their metrics?

### Takeaway
The biggest outliers in Creative Center for English learning are not the global AI-tutor apps. They are **regional English-course brands**:
- **KaleAnders** (Spanish-language LatAm): "learn English in 3 months without grammar", up to **1.53M likes on one ad**.
- **EF English First Indonesia** ("EFEINDONESIA"): "ONLY 50K/month, master English", 14 ads at 2K–306K likes.
- **Thailand's Kru Pe Ann (ครูพี่แอน)**: celebrity English-interview clips, about 100K likes.
- A generic **"Free app to learn English"** app ad: 157K likes.

Among AI-tutor apps, only **Learna AI** (Arabic and Turkish markets, 47–96s demos, up to 43.8K likes) and **Busuu** (10–22s, up to 10.8K likes) show up. Keyword searches for Praktika, Speak, Duolingo, ELSA, Cambly, Babbel, Preply, Promova and Talkpal returned **no** authorized Top Ads.

### Cited Findings

**Ranked catalogue (by likes on Creative Center, an outlier-strength proxy).** All rows are **[3P-DATA]** from Creative Center via AnyAPI, retrieved 24 Nov 2026. Link = `https://ads.tiktok.com/business/creativecenter/topads/{ID}/pc/en`. "Ad title" is the verbatim ad text, which on TikTok is the caption and CTA text. The first 3 seconds of on-screen visuals could not be viewed (see Gaps).

| # | Brand / app | Ad ID (link) | Created | Likes | ctr score | Budget tier | Length | Objective | Region (inferred) | Ad title / hook text (verbatim) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | KaleAnders (online English method) | [7298751892956233730](https://ads.tiktok.com/business/creativecenter/topads/7298751892956233730/pc/en) | 2023-11-07 | **1,532,644** | 0.27 | 2 | 52s | Conversion | LatAm / Mexico | "Aprender Inglés En 3 Meses Sin Necesidad De Usar Gramatica" |
| 2 | KaleAnders | [7207848188903915521](https://ads.tiktok.com/business/creativecenter/topads/7207848188903915521/pc/en) | 2023-03-07 | 414,045 | 0.33 | 1 | 17s | Conversion | LatAm | "Aprende inglés en 3 meses, si no aprendes devolveremos el 100% de tu dinero" (money-back guarantee) |
| 3 | KaleAnders | [7444574931663437842](https://ads.tiktok.com/business/creativecenter/topads/7444574931663437842/pc/en) | 2024-12-04 | 388,334 | 0.33 | 1 | 53s | Conversion | LatAm | "Clase gratuita: descubre cómo aprender inglés en solo 3 meses, desde cero." (free class) |
| 4 | EF Indonesia (EFEINDONESIA) | [7203356948988395521](https://ads.tiktok.com/business/creativecenter/topads/7203356948988395521/pc/en) | 2023-02-23 | 305,718 | 0.17 | 2 | 16s | Conversion | Indonesia | "HANYA 50 RIBU / BULAN JAGO BAHASA INGGRIS" ("Only 50K rupiah/month, become good at English") |
| 5 | EF Indonesia | [7316152862780735490](https://ads.tiktok.com/business/creativecenter/topads/7316152862780735490/pc/en) | 2023-12-24 | 280,686 | 0.29 | 2 | 23s | Product sales | Indonesia | same headline |
| 6 | EF Indonesia | [7115076952277073922](https://ads.tiktok.com/business/creativecenter/topads/7115076952277073922/pc/en) | 2022-06-30 | 255,335 | 0.34 | 2 | 13s | Lead gen | Indonesia | same headline |
| 7 | KaleAnders | [7362148817624760327](https://ads.tiktok.com/business/creativecenter/topads/7362148817624760327/pc/en) | 2024-04-26 | 230,388 | 0.24 | 2 | 60s | Lead gen | LatAm | "Aprende inglés en 3 meses sin necesidad de usar GRAMÁTICA y con un método 100% validado" |
| 8 | KaleAnders | [7380470473539256328](https://ads.tiktok.com/business/creativecenter/topads/7380470473539256328/pc/en) | 2024-06-14 | 195,813 | 0.24 | 2 | 34s | Conversion | LatAm | same as #7 |
| 9 | "Learning English" (app; Education-app industry label) | [7581789529222643719](https://ads.tiktok.com/business/creativecenter/topads/7581789529222643719/pc/en) | 2025-12-09 | 157,305 | 0.14 | 2 | 33s | Conversion (app) | unknown (English title) | "Free app to learn English" |
| 10 | EF Indonesia | [7237144335270150145](https://ads.tiktok.com/business/creativecenter/topads/7237144335270150145/pc/en) | 2023-05-25 | 125,190 | 0.24 | 2 | 18s | Lead gen | Indonesia | "HANYA 50 RIBU / BULAN JAGO BAHASA INGGRIS" |
| 11 | EF Indonesia | [7316152451328540673](https://ads.tiktok.com/business/creativecenter/topads/7316152451328540673/pc/en) | 2023-12-24 | 123,729 | 0.17 | 2 | 21s | Conversion | Indonesia | same |
| 12 | EF Indonesia | [7299095131584167938](https://ads.tiktok.com/business/creativecenter/topads/7299095131584167938/pc/en) | 2023-11-08 | 114,197 | 0.27 | 2 | 14s | Conversion | Indonesia | same |
| 13 | Kru Pe Ann / PerfectEnglish (Thai school) | [7226603548325724162](https://ads.tiktok.com/business/creativecenter/topads/7226603548325724162/pc/en) | 2023-04-27 | 99,700 | 0.12 | — | 118s | Product sales | Thailand | "น้องนุ่น ฮะสะมะฮ้าย โชว์สกิลสัมภาษณ์ภาษาอังกฤษครั้งแรก!!!" ("Noon [comedian/celebrity] shows off English interview skills for the first time!!!") |
| 14 | "online english classes" | [7514218731033968648](https://ads.tiktok.com/business/creativecenter/topads/7514218731033968648/pc/en) | 2025-06-10 | 95,143 | 0.11 | — | 26s | Conversion | unknown | "Learn Anytime, Anywhere!" (sister ad [7514222313643163655](https://ads.tiktok.com/business/creativecenter/topads/7514222313643163655/pc/en): 28,669 likes, 21s) |
| 15 | EF Indonesia | [7137678533966905346](https://ads.tiktok.com/business/creativecenter/topads/7137678533966905346/pc/en) | 2022-08-30 | 71,413 | 0.36 | — | 13s | Conversion | Indonesia | same headline |
| 16 | KaleAnders | [7276796292675223553](https://ads.tiktok.com/business/creativecenter/topads/7276796292675223553/pc/en) | 2023-09-09 | 63,970 | 0.33 | 2 | 50s | Conversion | LatAm | "Pon a prueba tu inglés y aprende el método que te hará dominarlo en solo 3 meses." (test-your-English quiz hook) |
| 17 | Kru Pe Ann | [7317085184725565442](https://ads.tiktok.com/business/creativecenter/topads/7317085184725565442/pc/en) | 2023-12-27 | 63,060 | 0.08 | — | 88s | Product sales | Thailand | "ปลื้มใจสุดๆ ลูกศิษย์สปีคอิงลิชรัวเป็นไฟ ดังจนได้เป็นดารา 💖🥹" ("So proud, my student speaks English rapid-fire, became a star") |
| 18 | Vietnamese IELTS centre (unnamed) | [7497108879487336466](https://ads.tiktok.com/business/creativecenter/topads/7497108879487336466/pc/en) | 2025-04-25 | 53,881 | 0.33 | — | 51s | Lead gen | Vietnam | "LUYỆN THI IELTS CẤP TỐC DÀNH CHO NGƯỜI MẤT GỐC TIẾNG ANH. CAM KẾT 7.0+ IELTS- HỌC THỬ MIỄN PHÍ" ("Express IELTS for people who've lost their English foundation. 7.0+ guaranteed. Free trial class") |
| 19 | **Learna AI** (AI-tutor app) | [7608964404739932178](https://ads.tiktok.com/business/creativecenter/topads/7608964404739932178/pc/en) | 2026-02-20 | **43,802** | 0.19 | 2 | 47s | Conversion | Arabic-speaking (MENA) | "تحدّث مع معلّم بالذكاء الاصطناعي، حمّل Learna AI" ("Talk with an AI teacher, download Learna AI") |
| 20 | Kru Pe Ann | [7584067976091009025](https://ads.tiktok.com/business/creativecenter/topads/7584067976091009025/pc/en) | 2025-12-15 | 34,510 | **0.06** | — | 106s | Reach | Thailand | "ครูพี่แอนอยากให้ทุกคนไม่ต้องคิดมากเรื่องสำเนียงนะคะ ตอนเริ่มเรียนภาษาอังกฤษ…" ("I want everyone not to overthink their accent when starting to learn English…") |
| 21 | Join in English | [7480331947774328840](https://ads.tiktok.com/business/creativecenter/topads/7480331947774328840/pc/en) | 2025-03-10 | 22,940 | 0.38 | 2 | 45s | Lead gen | LatAm | "Programa de Inglés 100% Online en solo 12 Meses" |
| 22 | **Learna AI** | [7575147188188971026](https://ads.tiktok.com/business/creativecenter/topads/7575147188188971026/pc/en) | 2025-11-21 | 22,031 | 0.19 | 2 | 50s | Conversion | **Turkey** | "AI Tutor ile konuş, Learna AI'yi indir" ("Talk to the AI Tutor, download Learna AI") |
| 23 | IELTS IKES (VN) | [7450037010951602177](https://ads.tiktok.com/business/creativecenter/topads/7450037010951602177/pc/en) | 2024-12-19 | 17,817 | 0.32 | — | 59s | Lead gen | Vietnam | "KHAI GIẢNG LỚP HỌC TIẾNG ANH IELTS CẤP TỐC CAM KẾT ĐẦU RA 7.5+IELTS. ƯU ĐÃI HỌC PHÍ TỚI 50%" (7.5+ guarantee, up to 50% off) |
| 24 | Learna AI ("Speak & Learn English: Learna") | [7601182159202992135](https://ads.tiktok.com/business/creativecenter/topads/7601182159202992135/pc/en) | 2026-01-30 | 17,191 | 0.19 | 2 | 55s | Conversion | MENA | Arabic "talk with an AI teacher" CTA |
| 25 | KaleAnders | [7213038331020869634](https://ads.tiktok.com/business/creativecenter/topads/7213038331020869634/pc/en) | 2023-03-21 | 15,451 | 0.27 | 1 | 27s | Conversion | LatAm | "Conoce el método RAIO que te permitirá aprender inglés en solo 3 meses y sin usar gramática" (named-method hook) |
| 26 | Learna AI | [7604896355895033864](https://ads.tiktok.com/business/creativecenter/topads/7604896355895033864/pc/en) | 2026-02-09 | 12,236 | 0.20 | 1 | 68s | Conversion | MENA | Arabic AI-tutor CTA |
| 27 | Wall Street English (VN) | [7346160000665010177](https://ads.tiktok.com/business/creativecenter/topads/7346160000665010177/pc/en) | 2024-03-14 | 11,338 | 0.36 | — | 110s | Lead gen | Vietnam | "Nhắn tin ngay cho Wall Street English để nhận ưu đãi lên đến 10 triệu và lộ trình học phù hợp." ("Message WSE now for up to 10M VND off plus a personalised roadmap") |
| 28 | **Busuu** | [7439026035730219015](https://ads.tiktok.com/business/creativecenter/topads/7439026035730219015/pc/en) | 2024-11-19 | 10,756 | 0.38 | 1 | 10s | Conversion | global / EN | "Learn any language on the go with Busuu. Subscribe now." |
| 29 | Unnamed AI-tutor app | [7636417647860989972](https://ads.tiktok.com/business/creativecenter/topads/7636417647860989972/pc/en) | 2026-05-05 | 7,435 | 0.17 | — | 28s | Conversion | EN | "Unlock Your English Skills in Just 10 Minutes a Day" (same advertiser, same day: [7636417051226243092](https://ads.tiktok.com/business/creativecenter/topads/7636417051226243092/pc/en), "Speak English fluently with your AI English tutor", 60s, 442 likes) |
| 30 | **Busuu** (telco partnership) | [7467550401957838849](https://ads.tiktok.com/business/creativecenter/topads/7467550401957838849/pc/en) | 2025-02-04 | 6,303 | 0.58 | 1 | 22s | Conversion | **Pakistan** (Jazz is a Pakistani telco) | "Hey Jazz Users! Discover personalised lessons with busuu made just for you! Subscribe Now." |
| 31 | IIG Vietnam (TOEIC) | [7350215752920301569](https://ads.tiktok.com/business/creativecenter/topads/7350215752920301569/pc/en) | 2024-03-25 | 4,270 | 0.34 | — | 89s | Lead gen | Vietnam | "✅ 60 NGÀY - CHINH PHỤC 550+/700+/800+/4 kỹ năng TOIEC…" (60 days to 550–800+ TOEIC) |
| 32 | Busuu | [7437438977605255186](https://ads.tiktok.com/business/creativecenter/topads/7437438977605255186/pc/en) | 2024-11-15 | 3,600 | 0.54 | 1 | 10s | Conversion | EN | "learn and speak english fluently." |
| 33 | Learna AI | [7610077934175322120](https://ads.tiktok.com/business/creativecenter/topads/7610077934175322120/pc/en) | 2026-02-23 | 3,099 | 0.18 | 2 | 96s | Conversion | MENA | "تحدث إلى AI Tutor، وقم بتنزيل Learna AI" |
| 34 | ANGKRIZ (Thai) | [7421767655462666258](https://ads.tiktok.com/business/creativecenter/topads/7421767655462666258/pc/en) | 2024-10-04 | 2,716 | 0.34 | — | 37s | Conversion | Thailand | "เรียนภาษาอังกฤษ ต้องแองกริซ" ("Learn English? Must be Angkriz") |
| 35 | Busuu (3 more) | [7496856920419155985](https://ads.tiktok.com/business/creativecenter/topads/7496856920419155985/pc/en), [7464825637598576656](https://ads.tiktok.com/business/creativecenter/topads/7464825637598576656/pc/en), [7436821052847079442](https://ads.tiktok.com/business/creativecenter/topads/7436821052847079442/pc/en) | 2024–25 | 2,257 / 1,802 / 840 | 0.60 / 0.64 / 0.73 | 1/1/0 | 10s each | Conversion | EN | "Learn english with short lessons and speak with confidence. Subscribe now" / "Busuu's English Lessons: Speak Clearly & Confidently. Subscribe now" |

**Recent low-like but well-ranked "hook" ads**

These have few likes but strong (low) ctr scores, and show the hooks advertisers are testing in late 2026. **[3P-DATA]**
- **Brazil:** "Não estude inglês antes de conhecer essa história." ("Don't study English before you know this story."). 110s, conversion, created 2026-10-07. — [7693938687088771080](https://ads.tiktok.com/business/creativecenter/topads/7693938687088771080/pc/en). A second version, [7667247250951618578](https://ads.tiktok.com/business/creativecenter/topads/7667247250951618578/pc/en), runs 117s.
- **Turkey (travel pain):** "Tatile gidip İngilizce konuşamamak sandığından daha yorucu olabilir. Otelde check-in yaparken, restoranda sipariş verirken…" ("Going on holiday and not being able to speak English can be more tiring than you think. Checking in at the hotel, ordering at a restaurant…"). 28s, lead gen, 2026-06-02. — [7646949612527304712](https://ads.tiktok.com/business/creativecenter/topads/7646949612527304712/pc/en)
- **UAE (Egyptian-Arabic):** "الإنجليزي مش ميزة إضافية… ده شيء إجباري وانت في الإمارات" ("English isn't an extra skill… it's mandatory when you're in the UAE"). 15s version: 55 likes, 2026-11-06 — [7705027167017795605](https://ads.tiktok.com/business/creativecenter/topads/7705027167017795605/pc/en). 51s version: ctr 0.87 — [7677905267208028176](https://ads.tiktok.com/business/creativecenter/topads/7677905267208028176/pc/en).
- **Vietnam (career):** Aten: "Học tiếng Anh để xin việc, deal lương hay nhảy việc sẽ dễ hơn rất nhiều khi bạn luyện nói đúng cách." ("Learning English to get a job, negotiate salary or switch jobs is much easier when you practise speaking the right way."). 44s, 2025-12-21. — [7586346320749150224](https://ads.tiktok.com/business/creativecenter/topads/7586346320749150224/pc/en)
- **Vietnam (parent price-anchor):** "Đầu tư khóa học giúp con giao tiếp tiếng Anh thành thạo chỉ với chi phí 2 ly Phúc Long/buổi" ("A course for your child's fluent English for the price of 2 Phuc Long coffees per session"). — [7657417648604037138](https://ads.tiktok.com/business/creativecenter/topads/7657417648604037138/pc/en)
- **Indonesia:** "Makin Lancar Ngomong Inggris Dengan Belajar Di Kampung Inggris Lc" ("Speak English more fluently by studying at Kampung Inggris LC"). 45s, 1,227 likes. — [7596892202649419794](https://ads.tiktok.com/business/creativecenter/topads/7596892202649419794/pc/en)

**Searches that returned no English-app Top Ads**

Keyword searches (180 days) for "praktika", "duolingo", "ELSA Speak", "cambly", "babbel", "preply", "promova", "talkpal" and "İngilizce" returned either unrelated advertisers or `not_found`. **[3P-DATA]** Earlier keyword hits for "praktika" matched German "Praktikum" and Malay "praktikal". Searches for Falou, Loora, Memrise, Lingoda, Engoo and Speak (as a brand) were not run because Firecrawl credits ran out.

**Benchmark from outside English learning:** Teuida (Korean-learning app) "Speak Korean from day one. Practice everyday conversations with TEUIDA." 15s, 214,621 likes, ctr 0.16. — [7400248811224088583](https://ads.tiktok.com/business/creativecenter/topads/7400248811224088583/pc/en) **[3P-DATA]**

**Platform case study:** TikTok's only language-app success story found is Mondly (Pearson). It credits three things: the App Profile Page, App Event Optimization for subscriptions, and Maximum Delivery bidding. — [TikTok for Business: Mondly](https://ads.tiktok.com/business/en/inspiration/Mondly-app) **[VERIFIED, platform]**

### Inferences
- **Paid outliers on TikTok are dominated by local course brands with one blunt promise:**
  - a time box ("3 meses", "60 ngày", "12 Meses");
  - a price anchor ("50 RIBU / BULAN", "2 ly Phúc Long");
  - or a guarantee ("devolveremos el 100%", "CAM KẾT 7.0+").
  
  These ads are short (13–23s for EF Indonesia) or mid-length talking-head explainers (50–60s for KaleAnders). **[OBSERVATION]**
- **AI-tutor apps on TikTok paid run long.** Learna's ads run 47–96s. Its best ad (43.8K likes) is the shortest at 47s. Busuu runs ultra-short 10s product cuts but gets an order of magnitude fewer likes than the local course brands. **[OBSERVATION]**
- **Praktika, Speak and Duolingo's TikTok growth runs through organic and creator content, not authorized Top Ads.** This is consistent with the founder statements in the earlier notes. **[OBSERVATION]**
- **SEA pattern:** Thailand rewards teacher-personality and celebrity content (Kru Pe Ann, ครูหวาน books: 30,347 likes on [7478616735827460097](https://ads.tiktok.com/business/creativecenter/topads/7478616735827460097/pc/en)). Vietnam is test-score driven (IELTS 7.0+/7.5+, TOEIC). Indonesia is price-driven. **[OBSERVATION]**

### Gaps
- **Region and views are missing.** The provider gave no region and no impressions or view count. Likes are the only engagement metric.
- **First 3 seconds not checked.** The `videoUrl` CDN links could not be watched, so verbatim on-screen first-3-second text is not confirmed. The "hook text" above is the ad caption/title.
- **Searches cut short.** Firecrawl credits ran out ("Your Firecrawl credits ran out. Daily MCP credits refresh in 6h 39m. Add credits or upgrade to keep going: https://www.firecrawl.dev/billing/99cpn3srse63awbm43wmvdm9cajy9d3r"). This blocked further searches for Speak, Falou, Loora, Memrise, Lingoda, Engoo, Philippines, Hindi-language queries, and page 2 of results.
- **Hosts blocked.** tiktok.com, pipiads.com, gethandler.ai and virlo.ai are not allowed in this session's network, so organic video stats and PiPiAds ad pages could not be fetched.

---

## Which creator-partnership and organic videos went viral (Praktika, Speak, Duolingo and others)?

### Takeaway
- **Praktika:** The breakout "Gustavo" coach-correction video (about 10M views each on Instagram, TikTok and YouTube) is still unlinked publicly. Several identifiable Praktika creator-partnership TikToks exist, and they use the same "mistake ❌ / correct ✅" format with an Adjust tracking link. Praktika's own TikTok handle is **@praktika.app**, not @praktika.ai.
- **Duolingo:** Its top organic TikTok passed 32M views (Oct 2023).
- **Third-party outliers:** A tracker lists AI English-tutor "app demo" TikToks from the creator "englishgurukat" at 1.1M–7.6M views, 162–2,121× that account's median.

### Cited Findings
- **Praktika breakout video.** About 10M views each on Instagram, TikTok and YouTube; ARR went from about $1M to $12M that month. The video "wasn't about the app at all." It was found through a discovery platform filtered for creators with under 5,000 followers whose views far exceeded their audience. Winners were re-shot by the paid team's creator roster. **[VERIFIED: founder claim]** — [RevenueCat blog: Adam Turaev, Sub Club 2026](https://www.revenuecat.com/blog/growth/adam-turaev-praktika-sub-club-podcast-2026)
- **Praktika's TikTok handle.** The official TikTok is **praktika.app** and the Instagram is @praktika.ai. **[VERIFIED: company blog]** — [Praktika Challenge 2025](https://praktika.ai/blog/praktika-challenge-2025)
- **Praktika creator-partnership TikToks** (URLs and captions from search index; view counts not retrievable) **[3P-DATA]**:
  - **@nesly.english**, 2024-05-14 (date decoded from video ID). Caption: "I am Türkiye ❌ I am from Türkiye ✅ Download @Speaking English Praktika and get your AI tutor ⬇️ https://app.adjust.com/1chg2o36_1crafqao #ad". Format: creator UGC, mistake-correction, Turkey. — [tiktok.com/@nesly.english/video/7368875747450031365](https://www.tiktok.com/@nesly.english/video/7368875747450031365)
  - **@englishwcilemakar**, 2024-09-21. Caption: "Yapay zekayla İngilizce @Praktika.ai #işbirliği #fy #fyp" ("English with AI… #collaboration"). Turkey. — [link](https://www.tiktok.com/@englishwcilemakar/video/7417153886315646228)
  - **@giuliachilin**, 2023-01-18. Caption: "Aprende ingles para trabajar remoto con @praktika.ai ❤️📚 #trabajoremoto #asistentevirtual". Remote-work/career angle, Spanish-speaking market. This early-2023 date fits the 2023 breakout timing. — [link](https://www.tiktok.com/@giuliachilin/video/7189819328655527174)
  - **@spencersabe**, 2024-04-03. Caption tags "@Speaking English Praktika". — [link](https://www.tiktok.com/@spencersabe/video/7353725490739318021)
  - **@englishwithtsar**, 2024-01-25. An organic critical review: "no es perfecta… a veces, no detecta errores que hago a propósito" ("it's not perfect… sometimes it doesn't catch mistakes I make on purpose"); notes 10 free minutes a day. — [link](https://www.tiktok.com/@englishwithtsar/video/7327832441257790725)
- **Learna AI creator partnership.** **@englishteacherclaire**, 2025-01-09: "New Year, New Language Goals! Learna AI is your personal tutor… Start your English learning journey with @learna.ai today. Link in my bio for a special discount ✨ #learnaai". Format: teacher-creator UGC, New-Year angle, discount CTA. **[3P-DATA]** — [link](https://www.tiktok.com/@englishteacherclaire/video/7458024969969224982)
- **Call Annie (AI tutor).** Official account: "Learn English with your personal AI tutor 🙋‍♀️ #callannie #englishteacher #ai". **[3P-DATA]** — [link](https://www.tiktok.com/@call_annie_ai/video/7309203483914145066)
- **Loora on TikTok.** PiPiAds lists a TikTok ad, "Improve your spoken English by practicing with AI tutor!", at about 1.5M impressions (per search snippet; page blocked). **[3P-DATA]** — [PiPiAds: Speak English with Loora AI](https://www.pipiads.com/tiktok-ads-examples/SpeakEnglishwithLooraAI-tiktok-ads-1774830647939073). PiPiAds also tracks a "TalkOn - Learn English with AI" advertiser. — [PiPiAds: TalkOn](https://www.pipiads.com/tiktok-ads-examples/talkonlearnenglishwithai-tiktok-ads-1789581665003538)
- **Organic AI-tutor "app demo" outliers (gethandler.ai, account "englishgurukat").** These are views per search snippet, with the multiple measured against the account's median. One snippet described a video that "opens directly on a mobile app interface featuring an interactive English tutor." Pages could not be opened, and the brand shown is unconfirmed. **[3P-DATA]**

  | Views | Multiple | Page |
  |---|---|---|
  | ~7.6M | 2,121× | [link](https://gethandler.ai/outliers/language-learning-tiktok-app-demo-2121x/) |
  | ~2.9M | 162× | [link](https://gethandler.ai/outliers/language-learning-ai-tiktok-app-demo-162x/) |
  | ~2.4M | 1,851× | [link](https://gethandler.ai/outliers/language-learning-tiktok-app-demo-1851x/) |
  | ~1.6M | 478× | [link](https://gethandler.ai/outliers/language-learning-ai-tiktok-app-demo-478x/) |
  | ~1.3M | 590× | [link](https://gethandler.ai/outliers/language-learning-tiktok-app-demo-590x/) |
  | ~1.1M | 329× | [link](https://gethandler.ai/outliers/language-learning-tiktok-app-demo-329x/) |
  | ~536K | 31× | [link](https://gethandler.ai/outliers/language-learning-tiktok-app-demo-31x/) |
  | ~255K | 76× | [link](https://gethandler.ai/outliers/language-learning-tiktok-app-demo-76x/) |

- **Duolingo.**
  - Highest-viewed TikTok passed **32M views** as of Oct 2023, per Duolingo data cited in an academic study. Its first real hit was a Sept 2021 post teasing Duo. **[3P-DATA citing company]** — [Elon Journal, Spring 2024](https://www.elon.edu/u/academics/communications/journal/archive/spring-2024/spring-2024-sadie-wiswall/)
  - Well-known viral formats: Duo calling Dua Lipa "mommy", twerking to Adele's "Easy on Me", chasing Google Translate users. **[VERIFIED: press]** — [NBC News](https://www.nbcnews.com/pop-culture/pop-culture-news/duo-big-green-owl-became-tiktok-star-rcna4445)
  - Account had about 7M followers and 147M likes at the time of writing (undated). — [HubSpot](https://blog.hubspot.com/marketing/duolingo-unhinged-content)
- **Speak.** No viral TikTok video or view data was found in search. Speak's English product targets Asian markets, and its US app teaches other languages to English speakers. — [speak.com](https://www.speak.com/)
- **ELSA Speak.** No TikTok campaign with view data was found. VnExpress reports more than 50M users. — [VnExpress](https://e.vnexpress.net/news/tech/how-vietnamese-entrepreneur-utilizes-ai-to-teach-english-to-50-million-learners-worldwide-4849115.html)

### Inferences
- **The Praktika creator template visible on TikTok:**
  - Native-language teacher-creator.
  - A one-line mistake shown with ❌, then the correct version with ✅ ("I am Türkiye ❌ I am from Türkiye ✅").
  - Then "get your AI tutor" and an Adjust deep link plus #ad.
  
  This is the paid and partnership descendant of the Gustavo "coach corrects mistakes" video, and the same skeleton as Learna and Loora's "Never say 'I'm fine, thank you'" Meta ads. **[OBSERVATION]**
- **Turkey shows up across channels.** Praktika partnerships (nesly.english, englishwcilemakar), Learna's Turkish Top Ad (22K likes) and the Turkish travel-pain ad all point to Turkey as an active, competitive market for AI English tutors on TikTok. **[OBSERVATION]**

### Gaps
- The Gustavo video URL, verbatim hook and length remain unfound.
- No view or like counts for the Praktika, Learna or Call Annie creator videos (tiktok.com blocked; Oriane TikTok search was not run because credits ran out).
- No viral Speak, Cambly, Preply, Babbel, Promova, Falou or Talkpal TikTok videos were identified.

---

## What hooks and on-screen text repeat?

### Takeaway
Across the TikTok catalogue, six hook families repeat:
1. **Time-box promise:** "en 3 meses", "60 NGÀY", "en solo 12 Meses", "10 Minutes a Day".
2. **No-grammar / named method:** "Sin Necesidad De Usar Gramatica", "método RAIO".
3. **Price anchor:** "HANYA 50 RIBU / BULAN", "2 ly Phúc Long/buổi", "Free app".
4. **Guarantee / score commitment:** "devolveremos el 100%", "CAM KẾT 7.0+/7.5+".
5. **"Talk to an AI tutor" demo CTA:** Learna in Arabic and Turkish.
6. **Mistake ❌ → correct ✅** in creator partnerships.

Emerging 2026 hooks are context-of-pain ("English is mandatory in the UAE", "not speaking English on holiday is exhausting") and story-curiosity ("Don't study English before you know this story").

### Cited Findings
- **Time-box:**
  - KaleAnders, "3 meses": rows #1–3, #7–8, #16, #25. — [1,532,644-like ad](https://ads.tiktok.com/business/creativecenter/topads/7298751892956233730/pc/en)
  - IIG "60 NGÀY". — [7350215752920301569](https://ads.tiktok.com/business/creativecenter/topads/7350215752920301569/pc/en)
  - Join in English "12 Meses". — [7480331947774328840](https://ads.tiktok.com/business/creativecenter/topads/7480331947774328840/pc/en)
  - "10 Minutes a Day". — [7636417647860989972](https://ads.tiktok.com/business/creativecenter/topads/7636417647860989972/pc/en)
  
  **[3P-DATA]**
- **Price anchor:** EF Indonesia, 14 Top Ads with an identical headline. — e.g. [7203356948988395521](https://ads.tiktok.com/business/creativecenter/topads/7203356948988395521/pc/en). "Free app to learn English". — [7581789529222643719](https://ads.tiktok.com/business/creativecenter/topads/7581789529222643719/pc/en) **[3P-DATA]**
- **Guarantee:** KaleAnders 100% money-back. — [7207848188903915521](https://ads.tiktok.com/business/creativecenter/topads/7207848188903915521/pc/en). Vietnamese IELTS "CAM KẾT 7.0+". — [7497108879487336466](https://ads.tiktok.com/business/creativecenter/topads/7497108879487336466/pc/en) **[3P-DATA]**
- **AI-tutor CTA:** Learna's "Talk with an AI teacher, download Learna AI", 6 Top Ads. — [7608964404739932178](https://ads.tiktok.com/business/creativecenter/topads/7608964404739932178/pc/en) **[3P-DATA]**
- **Mistake ❌ / correct ✅:** "I am Türkiye ❌ I am from Türkiye ✅". — [nesly.english](https://www.tiktok.com/@nesly.english/video/7368875747450031365) **[3P-DATA]**
- **Celebrity or student transformation (Thailand):** "Noon shows off English interview skills for the first time!!!" — [7226603548325724162](https://ads.tiktok.com/business/creativecenter/topads/7226603548325724162/pc/en) **[3P-DATA]**
- **Accent reassurance:** "don't overthink your accent". ctr 0.06, the best score among English-learning ads in the sample. — [7584067976091009025](https://ads.tiktok.com/business/creativecenter/topads/7584067976091009025/pc/en) **[3P-DATA]**
- **Platform-level hooks:**
  - "Hey Jazz Users!" (Busuu × telco bundle, Pakistan). — [7467550401957838849](https://ads.tiktok.com/business/creativecenter/topads/7467550401957838849/pc/en)
  - The repeated "Subscribe now" end-CTA in all 7 Busuu ads. — [e.g. 7439026035730219015](https://ads.tiktok.com/business/creativecenter/topads/7439026035730219015/pc/en)
  
  **[3P-DATA]**

### Inferences
- **Format by ad type:**
  - The highest-like English ads are short-to-mid talking-head or teacher videos making one blunt promise.
  - AI-app demos are long (47–96s) because the demo itself is the proof.
  - The format mix seen: creator UGC (Praktika, Learna partnerships), teacher talking head (KaleAnders, Kru Pe Ann), AI-tutor screen demo (Learna, the unnamed "AI English tutor" app), celebrity skit (Kru Pe Ann/Noon), and product-cut (Busuu 10s).
  
  **[OBSERVATION]**
- **No examples of three requested formats.** Street-interview, green-screen and meme ads did not surface among English-app Top Ads in this sample. That may reflect the keyword-based search rather than real absence. **[OBSERVATION]**

### Gaps
- Verbatim on-screen text in the first 3 seconds was not checked for any ad (video CDN, TikTok and PiPiAds were unreachable). Captions and titles are used as a proxy.
- Not covered: CTR percentile bucket filtering (`top_1_20`) by country, and Philippines/India-specific queries.
