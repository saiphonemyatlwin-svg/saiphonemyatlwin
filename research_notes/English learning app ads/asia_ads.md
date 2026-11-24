# Outlier ads from English-learning apps targeting Asian learners (Meta, TikTok), as of 24 Nov 2026

These notes extend `Outlier ads English IELTS leadership/english_apps.md` and `myanmar_market.md`. They do not repeat the ELSA/Airbridge, Praktika, Speak-France or "Never say I'm fine, thank you" material already there.

**Labels**
- **[VERIFIED]**: stated by the company or the platform.
- **[3P-DATA]**: pulled on 24 Nov 2026 through Firecrawl Alexandria. Meta ads come from the Adyntel Meta Ad Library scrape and TikTok ads from the AnyAPI TikTok Creative Center "Top Ads" scrape. These are third-party snapshots.
- **[OBSERVATION]**: my own reading.

**How to read the numbers**
- **"Days active"** for Meta is the scrape's `start_date` to `end_date`, which is the last day the ad was seen. Most ads were still active on 24 Nov 2026. Meta does not publish spend or results for commercial ads, so run length is only a proxy for a winning ad.
- **"Coll"** is Meta's collation count: how many near-identical versions of the ad are grouped together.
- **TikTok "likes"** and CTR rank (0 to 1, where lower is a better rank) are TikTok Creative Center's own figures for each Top Ad. They cover roughly the last 180 days.
- **TikTok links** are built from the Creative Center ad ID in this pattern: `ads.tiktok.com/business/creativecenter/topads/<id>/pc/en`. Viewing them needs a TikTok for Business login, and I have not opened them individually.
- **Video length** is available for TikTok ads only. The Meta scrape gives a format (VIDEO, IMAGE and so on) but no duration.
- **Country filter caveat.** Adyntel's country filter is loose. "ELSA Speak" with country IN, ID or PH returned unrelated Spanish and English short-drama ads. Each ad's country below is inferred from its language and page name, not from Meta's reach data. The `targeted_or_reached_countries` field came back empty for every ad.

---

## Q1. Which localized English-app ads in Asia are outliers (longest-running, most versions, top-ranked on TikTok Creative Center)?

### Takeaway
The longest-running localized ads in Asia rarely come from the famous AI apps. They come from:
- **tutoring and kids' brands with a click-to-Messenger funnel**: Engoo Thailand (799 days), Monkey Junior Vietnam (470 days, two versions; plus a separate 365-day ad), Langmaster (217 days);
- **exam apps running catalogue ads**: Santa TOEIC Korea, 511 days;
- **Burmese English schools**: GYS (764 days) and LEL School (743 days).

On TikTok, the clearest outlier is EF (EFEINDONESIA). Its single hook, "HANYA 50 RIBU / BULAN JAGO BAHASA INGGRIS" ("Only 50 thousand rupiah a month to be great at English"), appears in at least 11 different Top Ads with up to 305,718 likes each. A Burmese TikTok ad from GYS ranks in Creative Center with 26,522 likes.

ELSA Vietnam ads are numerous but short-lived. Most are 4–82 days old. ELSA keeps changing its KOL (influencer) creatives and flash-sale prices instead of running one long-lived ad.

### Cited Findings

**Catalogue: Meta ads (Facebook, Instagram, Messenger)**

1. **Engoo, Thailand (Thai), image ad. Longest-running localized ad found, 799 days.**
   - Ran 2024-09-16 to 2026-11-24 and was still active.
   - Hook: "เก่งภาษาอังกฤษได้ตอนนี้" ("Be good at English now"). Body bullets: "ให้ลูกได้ฝึกสนทนาแบบตัวต่อตัว" ("Let your child practise one-to-one conversation"), "เรียนได้ทุกที่ทุกเวลา" ("Learn anywhere, anytime"), "✅ ทดลองเรียนฟรี" ("Free trial lesson").
   - Angle: parent/child, convenience. CTA: Send message (Messenger). **[3P-DATA]**
   - [Meta Ad Library 3508205502811027](https://www.facebook.com/ads/library/?id=3508205502811027)

2. **Engoo, Thailand (Thai), image ads, 522 days (two near-identical ads).**
   - Title: "ผู้ช่วยภาษาอังกฤษในการทำงาน" ("Your English assistant at work").
   - Hook: "อยากคุยภาษาอังกฤษได้ไหลลื่น ต้องฝึกกับเจ้าของภาษาตัวจริง" ("Want to speak English fluently? You must practise with real native speakers").
   - Angle: work, native-speaker tutor. CTA: Contact us. **[3P-DATA]**
   - [776586944717751](https://www.facebook.com/ads/library/?id=776586944717751); [576310432216089](https://www.facebook.com/ads/library/?id=576310432216089)

3. **Engoo, Thailand (Thai), video ad, 377 days.**
   - Copy: "เรียนสด ตัวต่อตัว กับครูต่างชาติทุกคลาส เริ่มเพียง 2,400 บาท เลือกเรียนได้ 24 ชม. ไม่ต้องโหลดแอพ" ("Live one-to-one with a foreign teacher every class, from only 2,400 baht, book any of 24 hours, no app download needed").
   - Angle: price anchor plus friction removal. CTA: Send message. **[3P-DATA]**
   - [1386462366367807](https://www.facebook.com/ads/library/?id=1386462366367807)
   - Engoo also runs Taiwan dynamic catalogue ads on the page "Engoo 線上英文", running 405 and 288 days. **[3P-DATA]** — [1121930416761648](https://www.facebook.com/ads/library/?id=1121930416761648)

4. **Monkey Junior, Vietnam (Vietnamese), video ads, 470 days (two versions: one with collation count 2, plus a near-identical ad).**
   - Ran 2025-08-11 to 2026-11-24.
   - Hook: "VỪA HỌC VỪA CHƠI CON VẪN GIỎI TIẾNG ANH CHỈ SAU 100 NGÀY" ("Learning while playing, your child still becomes good at English after just 100 days").
   - Proof: "15 triệu phụ huynh trên thế giới lựa chọn Monkey" ("15 million parents worldwide chose Monkey"). Promise: "Nói tiếng Anh chuẩn Mỹ" ("Speak standard American English").
   - Title/offer: "Nhận quà tặng trị giá 2.000.000đ" ("Get a gift worth 2,000,000 VND"). CTA: Send message.
   - Angle: parent, time-bound outcome. **[3P-DATA]**
   - [1457794848590457](https://www.facebook.com/ads/library/?id=1457794848590457); [1206682851218351](https://www.facebook.com/ads/library/?id=1206682851218351)

5. **Monkey Junior, Vietnam, video ad, 365 days.**
   - Hook: "BIẾN TIẾNG ANH TRỞ THÀNH PHẢN XẠ TỰ NHIÊN CỦA CON CHỈ SAU 90 NGÀY" ("Turn English into your child's natural reflex in just 90 days").
   - Offer: "Giảm ngay 50% học phí - Chỉ còn 1399k/trọn đời (giá gốc 2799k)" ("50% off, only 1,399K VND for lifetime; originally 2,799K") plus a free Monkey Math course. Title: "Nhắn tin nhận ngay học bổng 50%" ("Message to get a 50% scholarship").
   - Angle: parent, lifetime-price anchor. CTA: Send message. **[3P-DATA]**
   - [1694676904825739](https://www.facebook.com/ads/library/?id=1694676904825739)

6. **Monkey Junior, Vietnam, video ad, 76 days (with a 48-day version that has 4 variants).**
   - Hook: "🚨 [CHUYÊN GIA CẢNH BÁO] Rất nhiều ba mẹ Việt đã vô tình bỏ lỡ 'giai đoạn vàng' tiếp thu ngôn ngữ của con mà không hề hay biết!" ("[EXPERT WARNING] Many Vietnamese parents have unknowingly missed their child's 'golden period' for language acquisition!").
   - Angle: parent fear of missing out plus expert authority. CTA: Apply now / Sign up. **[3P-DATA]**
   - [1721598085763161](https://www.facebook.com/ads/library/?id=1721598085763161); [1679325340288238](https://www.facebook.com/ads/library/?id=1679325340288238)

7. **Santa (Riiid), Korea (Korean), dynamic catalogue ads, 511, 461, 365 and 356 days.**
   - Page "산타 - AI 토익" ("Santa – AI TOEIC"). The search returned 152 ads, and many are long-lived catalogue (DCO) units. Creative text is templated (`{{product.name}}`), so no hook text was captured.
   - Angle: exam (TOEIC/TOEFL). CTA: Learn more. **[3P-DATA]**
   - [1118080450372050](https://www.facebook.com/ads/library/?id=1118080450372050); [780663260987722](https://www.facebook.com/ads/library/?id=780663260987722)

8. **Speak (스픽), Korea (Korean), DCO ad, 10 days, new.**
   - Title: "당신을 말하게 하는 영어 앱" ("The English app that makes you speak").
   - Hook: "🔥당신을 영어로 말하게 하는 앱🔥 올해 영어 공부 다짐하셨다면 제발 놓치지 마세요." ("The app that makes you speak English. If you resolved to study English this year, please don't miss this.").
   - Angle: New-Year resolution, output over input. **[3P-DATA]**
   - [1868781161222251](https://www.facebook.com/ads/library/?id=1868781161222251)
   - In the same week (Nov 2026), Speak Korea is promoting a Japanese course: "엔저일 때 떠나는 일본 여행, 이번엔 손가락 말고 입으로 주문해보세요" ("Travelling to Japan while the yen is weak: this time order with your mouth, not by pointing"). Not English, but it shows the brand pivoting its Korean user base. **[3P-DATA]** — [2227783424801209](https://www.facebook.com/ads/library/?id=2227783424801209)

9. **Babbayoung (바빠영), a Korean English-speaking academy and competitor of Speak, carousel ad, 186 days.**
   - Hook: "영어, 왜 말이 안 나올까? 영어 학원도 다녀보고, 스피킹 앱도 써봤는데… 정작 실전에서는 말문이 막히는 경험" ("English: why won't it come out? You've tried academies and speaking apps… but in real life you freeze").
   - This is an anti-app angle. CTA: See details. **[3P-DATA]**
   - [962779543266974](https://www.facebook.com/ads/library/?id=962779543266974)

10. **Praktika, multi-market (English copy also served in Japan; the JP search returned 2,859 ads), video ads, 145–161 days (many duplicates).**
    - Title: "⭐️⭐️⭐️⭐️⭐️ Try Now". Copy: "Learn English, German, Japanese… with AI Tutors… ✅ No boring grammar drills!"
    - A Portuguese version, "Experimente Agora" ("Try it now"), runs in parallel. CTA: Install now. **[3P-DATA]**
    - [2052039062056405](https://www.facebook.com/ads/library/?id=2052039062056405)
    - Earlier notes cite a Japanese hook, "シャドーイングって知ってる？" ("Do you know shadowing?"), which ran only 9 days.

11. **ELSA Speak Vietnam, video ad, 82 days (the longest-running live ELSA VN video in this scrape).**
    - Hook: "Học nói tiếng Anh mãi mà vẫn chưa nói như người bản xứ?" ("Been learning to speak English forever and still don't sound like a native?").
    - Offer: 7-day free Premium trial. CTA: Install now (App Store). **[3P-DATA]**
    - [962257616901503](https://www.facebook.com/ads/library/?id=962257616901503)

12. **ELSA Speak Vietnam, video ad, 79 days (with a 9-day copy of the same text).**
    - Hook: "Học tiếng Anh bao năm rồi mà vẫn 'mất gốc' ngữ pháp với thiếu từ vựng?" ("Studied English for years but still have 'lost your foundation' in grammar and lack vocabulary?").
    - Angle: years-of-failure. It pitches new Vocab Coach and Grammar Tutor features. **[3P-DATA]**
    - [2340931470056804](https://www.facebook.com/ads/library/?id=2340931470056804)

13. **ELSA Speak Vietnam, KOL video series, 4–29 days.** The series features creator Khánh Vy (a well-known Vietnamese English MC).
    - "Muốn bứt phá thu nhập và thăng tiến trong công việc, đừng để kỹ năng Nói tiếng Anh cản bước bạn!" ("Want to break through on income and promotion? Don't let English speaking hold you back!"). It promotes an AI interview tutor that "chấm điểm khả năng đậu phỏng vấn" ("scores your chance of passing the interview"). — [1130166843237567](https://www.facebook.com/ads/library/?id=1130166843237567); [2819013038495082](https://www.facebook.com/ads/library/?id=2819013038495082)
    - Image ad: "Premium 1 Năm - Gói học yêu thích nhất của Khánh Vy… GIẢM CHỈ CÒN 699K" ("1-year Premium, Khánh Vy's favourite plan… now only 699K VND"). Version count 2, 29 days. — [4963986483831712](https://www.facebook.com/ads/library/?id=4963986483831712)
    - KOL Hải My: "Học thuộc lòng đáp án văn mẫu sẽ khiến bạn 'đứng hình' ngay khi nhà tuyển dụng hỏi bẻ lái" ("Memorised model answers will make you freeze the moment the recruiter asks a curveball"). Its UTM reads `FA1_WC_JUL26_ASC_KOL`, which suggests the KOL creatives run inside Advantage+ campaigns. — [1134991842279479](https://www.facebook.com/ads/library/?id=1134991842279479)
    - Labels: **[3P-DATA]**; the UTM reading is **[OBSERVATION]**.

14. **ELSA Speak Vietnam, flash-sale image ads, 6 days.**
    - Hook: "🚨 FLASH SALE CHỚP NHOÁNG: ELSA PREMIUM CHỈ TỪ 659K! … Giới hạn đúng 10 suất!" ("Lightning flash sale: ELSA Premium from just 659K… limited to exactly 10 slots!").
    - Lifetime plan "2.699K (GIẢM GẦN 3,4 TRIỆU so với giá gốc)" ("2,699K, almost 3.4M off"). Code INFVN. **[3P-DATA]**
    - [1629443242200352](https://www.facebook.com/ads/library/?id=1629443242200352); [1871008040738032](https://www.facebook.com/ads/library/?id=1871008040738032)

15. **ELSA Speak Vietnam, role-play demo video, 17 days.**
    - Hook: "Tự tin order cà phê bằng tiếng Anh cực mượt chỉ sau vài phút luyện tập! ☕" ("Confidently order coffee in English, super smoothly, after just a few minutes of practice!").
    - Angle: everyday scenario. **[3P-DATA]**
    - [1650825803089995](https://www.facebook.com/ads/library/?id=1650825803089995)

16. **Langmaster, Vietnam (Vietnamese), image ads on the page "30 Phút Tiếng Anh Mỗi Ngày" ("30 minutes of English every day"), 216–217 days.**
    - "BỎ RA 0Đ – NHẬN LẠI GIÁ TRỊ CẢ TRIỆU ĐỒNG TỪ BUỔI HỌC THỬ IELTS ONLINE" ("Spend 0 VND, get back millions in value from a free IELTS trial class").
    - "FREE TEST IELTS 4 KỸ NĂNG… Thi thử ở đâu cũng chỉ loanh quanh 4.5 - 5.0 mãi" ("Free 4-skill IELTS test… wherever you mock-test you're stuck around 4.5–5.0").
    - Angle: exam plateau. CTA: Apply now. **[3P-DATA]**
    - [1317763810237250](https://www.facebook.com/ads/library/?id=1317763810237250); [1989213918333928](https://www.facebook.com/ads/library/?id=1989213918333928)

17. **Langmaster, Vietnam, video ad, 105 days.**
    - Hook: "ĐÓNG HỌC PHÍ 1 LẦN THẤY 'ĐAU VÍ'? … Nhìn bạn bè đổi việc lương ngàn đô mà phát thèm?" ("Paying tuition in one go hurts your wallet? … Envious watching friends switch to thousand-dollar-salary jobs?").
    - Offer: 0% instalments. Angle: career envy plus price. **[3P-DATA]**
    - [2326932638049959](https://www.facebook.com/ads/library/?id=2326932638049959)

18. **Prep (prep.vn), Vietnam, VSTEP exam ads, 87–108 days.**
    - Video hook: "VSTEP là gì?" ("What is VSTEP?"), 108 days.
    - Image ad: "HỌC NHANH - THI GỌN - MÀ THI 1 LẦN LÀ CHẮC CHẮN ĐẠT… 🧑‍🎓 Sinh viên → Cần VSTEP để xét tốt nghiệp… 👩‍💼 Người đi làm → Cần VSTEP để xét nâng ngạch/tăng lương" ("Learn fast, test once and surely pass… Students need VSTEP to graduate; workers need it for grade promotion and pay rises").
    - Angle: the national exam as a gate. CTA: Send message. **[3P-DATA]**
    - [1455916363040507](https://www.facebook.com/ads/library/?id=1455916363040507); [1063680006266317](https://www.facebook.com/ads/library/?id=1063680006266317)

19. **Kyna English (1-on-1), Vietnam, image ads, 109 and 63 days (ran Aug–Dec 2025).**
    - Hook: "⛔️ Học ĐỦ CHỖ - ĐỦ PHƯƠNG PHÁP - TỐN TIỀN TRIỆU mà vẫn 'dở' tiếng Anh" ("Studied everywhere, tried every method, spent millions, and still bad at English").
    - Offer: "1 KÈM 1… chỉ với 800K/THÁNG" ("1-on-1… only 800K VND a month"). Title: "204.961 học viên đã đăng ký" ("204,961 learners registered").
    - Angle: sunk cost plus price. **[3P-DATA]**
    - [2305053839927205](https://www.facebook.com/ads/library/?id=2305053839927205)

20. **Globish, Thailand (Thai), video ads, 60–62 days. At least 14 live ads in the same template; one has 7 versions and another 5.**
    - Title: "วัดระดับภาษาฟรี! พร้อมรับคำปรึกษา" ("Free level test! Plus a consultation").
    - Promise: "การันตีผลลัพธ์ ทำได้ใน 3 เดือน! 🏆 กว่า 100,000+ นักเรียนวัยทำงานไว้วางใจ 🏆 กว่า 800 องค์กรชั้นนำ" ("Results guaranteed in 3 months! 100,000+ working-adult learners, 800+ leading organisations").
    - Testimonial variant (23 days): "ตั้งเป้าว่าปีนี้จะพูดอังกฤษให้ได้ จากที่เคยฟังออกแต่ตอบไม่ได้" ("I set a goal to speak English this year. I used to understand but couldn't answer").
    - Angle: working adults, "understand but can't speak". CTA: Sign up / Send message. **[3P-DATA]**
    - [1067175972991701](https://www.facebook.com/ads/library/?id=1067175972991701); [1380590020454676](https://www.facebook.com/ads/library/?id=1380590020454676); [1074994648917479](https://www.facebook.com/ads/library/?id=1074994648917479)

21. **Generic AI-English apps seen in the Philippines and Myanmar searches (English copy).**
    - LunaSpeak "Speak English Fluently with this app!", video, 218 days. — [1250208760626569](https://www.facebook.com/ads/library/?id=1250208760626569)
    - LunaSpeak in Hindi: "अंग्रेज़ी बोलते समय अटक जाते हैं?" ("Do you get stuck when speaking English?"), 112 days. — [1429801495640342](https://www.facebook.com/ads/library/?id=1429801495640342)
    - Glite "🧠 Native speakers average 75% on this English test, 90%+ is genius level", 179 days. — [1251034110439597](https://www.facebook.com/ads/library/?id=1251034110439597)
    - Labels: **[3P-DATA]**.

**Catalogue: TikTok Creative Center Top Ads**

22. **EF (EFEINDONESIA), Indonesia (Indonesian). Same hook across at least 11 Top Ads, so this is the biggest TikTok outlier found.**
    - Hook / title: "HANYA 50 RIBU / BULAN JAGO BAHASA INGGRIS" ("Only 50K rupiah a month to be great at English").
    - Ad versions:
      - 7203356948988395521: 305,718 likes, 17s, conversion objective.
      - 7316152862780735490: 280,686 likes, 24s, product sales.
      - 7115076952277073922: 255,335 likes, 13s, lead gen.
      - 7237144335270150145: 125,190 likes, 18s.
      - 7316152451328540673: 123,729 likes, 22s.
      - 7299095131584167938: 114,197 likes, 14s.
    - Format: short (10–29s). Angle: price anchor against tutor or course cost. **[3P-DATA]**
    - [Creative Center 7203356948988395521](https://ads.tiktok.com/business/creativecenter/topads/7203356948988395521/pc/en); [7115076952277073922](https://ads.tiktok.com/business/creativecenter/topads/7115076952277073922/pc/en)

23. **GYS (Grab Your Success) online classes, Myanmar (Burmese), TikTok Top Ads, video-view objective.**
    - "အင်္ဂလိပ်သင်တန်း #TelegramChannel #gysonlineclasses" ("English class"): 26,522 likes, 74s, CTR rank 0.43. — [7667329273791561735](https://ads.tiktok.com/business/creativecenter/topads/7667329273791561735/pc/en)
    - "အင်္ဂလိပ်စကားပြောက အခုထိ ခက်နေတုန်းလား" ("Is English speaking still hard for you?"): 6,775 likes, 86s. — [7580037363944079376](https://ads.tiktok.com/business/creativecenter/topads/7580037363944079376/pc/en)
    - "အချိန်မရလို့ အင်္ဂလိပ်စာ မလေ့လာရဘူးဆိုရင်" ("If you can't study English because you have no time"): 91 likes, 56s. — [7582460247706599441](https://ads.tiktok.com/business/creativecenter/topads/7582460247706599441/pc/en)
    - Labels: **[3P-DATA]**.

24. **Wall Street English, Vietnam, lead-gen video, 11,338 likes, 111s.**
    - Copy: "Nhắn tin ngay cho Wall Street English để nhận ưu đãi lên đến 10 triệu và lộ trình học phù hợp" ("Message Wall Street English now for up to 10 million VND off and a suitable study path"). **[3P-DATA]**
    - [7346160000665010177](https://ads.tiktok.com/business/creativecenter/topads/7346160000665010177/pc/en)

25. **Vietnamese IELTS crash-course centres on TikTok (lead gen; course providers, not apps), included as the top performers for the VN "tiếng Anh" query.**
    - "LUYỆN THI IELTS CẤP TỐC DÀNH CHO NGƯỜI MẤT GỐC TIẾNG ANH. CAM KẾT 7.0+ IELTS - HỌC THỬ MIỄN PHÍ" ("Express IELTS prep for people who've lost their English foundation; 7.0+ guaranteed; free trial class"): **53,881 likes**, 52s. — [7497108879487336466](https://ads.tiktok.com/business/creativecenter/topads/7497108879487336466/pc/en)
    - "IELTS IKES CÙNG CON CHINH PHỤC 8.0 IELTS" ("Conquer IELTS 8.0 with your child"): 17,817 likes, 59s. — [7450037010951602177](https://ads.tiktok.com/business/creativecenter/topads/7450037010951602177/pc/en)
    - Parent-testimonial hook: "Con đã làm được rồi đấy, con đã 7.0 IELTS cho mẹ thấy" ("I did it, Mum, I got IELTS 7.0 to show you"): 914 likes, 107s. — [7511535550299258881](https://ads.tiktok.com/business/creativecenter/topads/7511535550299258881/pc/en)
    - Labels: **[3P-DATA]**.

26. **Thailand: Kru P'Ann / Perfect English (course creator), 99,700 likes, 119s.**
    - Hook: "น้องนุ่น ฮะสะมะฮ้าย โชว์สกิลสัมภาษณ์ภาษาอังกฤษครั้งแรก!!!" ("Comedian Noon Hasamahai shows off English interview skills for the first time!!!").
    - Format: celebrity plus teacher entertainment. **[3P-DATA]**
    - [7226603548325724162](https://ads.tiktok.com/business/creativecenter/topads/7226603548325724162/pc/en)
    - TCAS university-entrance English ads, "DEK69 อัพคะแนน TGAT ENG & A-level ENG 80+" ("Class of 2026: raise TGAT/A-level English to 80+"), drew 16,263 likes, 35s. — [7490795931236286471](https://ads.tiktok.com/business/creativecenter/topads/7490795931236286471/pc/en)

27. **Japan, TikTok English-lesson subscription ads.** Example copy: "今なら英語レッスン受け放題が7日間無料！" ("Unlimited English lessons free for 7 days right now!"), 239 likes, 32s. The brand name was not returned. **[3P-DATA]** — [7537510050157953031](https://ads.tiktok.com/business/creativecenter/topads/7537510050157953031/pc/en)

28. **Busuu (English learners in the Gulf/Asia), TikTok conversion ad.**
    - Copy: "Hey Jazz Users! Discover personalised lessons with busuu made just for you!" 6,303 likes, 22s.
    - Angle: a telco partner bundle (Jazz is a Pakistani mobile operator). **[3P-DATA]**
    - [7467550401957838849](https://ads.tiktok.com/business/creativecenter/topads/7467550401957838849/pc/en)

**Context and case studies**
- ELSA's Meta case study: more than 90M downloads. ELSA paired click-to-Messenger ads with Meta Business Agent in markets without a local service team, which produced "more leads and higher average order value". No figures were given. **[VERIFIED, qualitative]** — [Meta for Business](https://www.facebook.com/business/success/elsa-speak-bm-success-story)
- ELSA's official TikTok bio: "DOWNLOAD FOR FREE… get 50% off now!" — [TikTok @elsaspeak](https://www.tiktok.com/@elsaspeak)
- Airbridge says ELSA sells "through Vietnamese Meta ads about workplace fears and through 13 TikTok videos, 5 from a single Italian tutor", with a $129.99 annual plan. **[3P-DATA]** — [Airbridge](https://www.airbridge.io/en/app-revenue/elsa-speak)
- Apple Search Ads also has an ELSA success story. I did not open it. — [Apple Ads: ELSA](https://ads.apple.com/app-store/success-stories/elsa)

### Inferences
- **Two kinds of outlier, by advertiser type** **[OBSERVATION]**:
  - Tutor, kids and exam brands (Engoo, Monkey, Santa, Langmaster, GYS) run one evergreen Messenger-lead or catalogue ad for 1–2 years.
  - App-install brands with KOL pipelines (ELSA, Speak) rotate creatives every 1–4 weeks around price events: "flash sale", "11.11", Black Friday-style "GIÁ SỐC THÁNG 11" ("November shock price").
  - So for ELSA, "outlier" means template volume, not the lifespan of any one ad.
- **The Messenger CTA dominates in Southeast Asia.** Engoo, Monkey, Langmaster, Prep, Kyna, Globish and every Myanmar advertiser use Send message as the CTA, not Install. This matches the Messenger-led sales funnel described in `myanmar_market.md`.
- **EF Indonesia's single price-anchor line** reused across many short (10–29s) cuts is the most replicable "outlier template" in the dataset.
- Many of the highest-engagement Top Ads are from tutor centres and course creators (EF, Wall Street English, IELTS crash courses, Kru P'Ann) rather than pure apps. App brands appear in Top Ads mostly when searched by name (Busuu).

### Gaps
- **TikTok creative length and views.** Creative Center gives likes and CTR rank, not views. Exact run dates for TikTok ads were not returned.
- **Meta ad formats.** The scrape gives no video lengths, and DCO/catalogue ads (Santa, Engoo Taiwan) expose no hook text. Open the Meta Ad Library links to see the creative.
- **No ads found.** Keyword searches found nothing for Cake (the "Cake English" VN query returned bakeries), Cakap (the word is generic in Indonesian and Malay), Englishdee, Engoo Japan, Ruangguru English, Kampus, Langgo, Eiken apps or Cambly Thailand (that query returned "English in Brazil"). The next step is to pull these by Page ID with the Adyntel `meta-ads/library/advertiser` capability.
- **Country-level reach.** Not available from this scrape, so markets are inferred from language.
- **YouTube ads.** None were catalogued. No YouTube ad-library provider was available, and Google's Ads Transparency Center was not queried.

---

## Q2. What culturally specific hooks work (exam, job, children/parent, embarrassment with foreigners, price vs tutor centre)?

### Takeaway
Five hook families recur across markets, and each has a market where it is strongest:
1. **Exam as a life gate**: VSTEP for graduation and pay grade (VN), TOEIC (KR), TCAS/TGAT (TH), IELTS 7.0 (VN).
2. **Parent and child "golden period"**: Monkey Junior's 90/100-day promises and Starfish Academy in Myanmar.
3. **Career and income anxiety**: ELSA's interview and meeting ads, Langmaster's "friends earning thousand-dollar salaries".
4. **Price anchor**: EF's 50K rupiah a month, Monkey's lifetime 1,399K VND, Engoo's 2,400 baht, Kyna's 800K a month.
5. **"Years of study, still can't speak" or "understand but can't answer"**: ELSA, Kyna, Globish, Babbayoung, LEL School.

Fear of speaking in front of people (embarrassment) is explicit in Burmese and Thai copy. "Embarrassment with foreigners" appears mainly as the "native speaker" benchmark.

### Cited Findings
- **Exam gate (Vietnam):** Prep's VSTEP ad: "Sinh viên → Cần VSTEP để xét tốt nghiệp… Người đi làm → Cần VSTEP để xét nâng ngạch/tăng lương" ("Students need VSTEP to graduate; workers need it for promotion or a raise"). — [1063680006266317](https://www.facebook.com/ads/library/?id=1063680006266317) **[3P-DATA]**
- **Exam plateau (Vietnam):** Langmaster: "Thi thử ở đâu cũng chỉ loanh quanh 4.5 - 5.0 mãi" ("Stuck around 4.5–5.0 in every mock test"). — [1989213918333928](https://www.facebook.com/ads/library/?id=1989213918333928) **[3P-DATA]**
- **Exam (Korea):** Santa's AI TOEIC catalogue ads have run 1–1.4 years. — [1118080450372050](https://www.facebook.com/ads/library/?id=1118080450372050) **[3P-DATA]**
- **Exam (Thailand):** TikTok Top Ads for university entrance ("DEK69… TGAT ENG & A-level ENG 80+", 16,263 likes) and civil-service English books ("ผ่าน ก.พ. ขอแค่ 2 เล่มนี้", "To pass the civil-service exam you only need these 2 books", 30,347 likes). — [7490795931236286471](https://ads.tiktok.com/business/creativecenter/topads/7490795931236286471/pc/en); [7478616735827460097](https://ads.tiktok.com/business/creativecenter/topads/7478616735827460097/pc/en) **[3P-DATA]**
- **Parent, golden period / fear of missing out (Vietnam):** Monkey Junior: "[CHUYÊN GIA CẢNH BÁO]… bỏ lỡ 'giai đoạn vàng'" ("[Expert warning]… missed the 'golden period'"). — [1721598085763161](https://www.facebook.com/ads/library/?id=1721598085763161) **[3P-DATA]**
- **Parent, child's success shown to Mum (Vietnam TikTok):** "Con đã 7.0 IELTS cho mẹ thấy" ("I got IELTS 7.0 to show you, Mum"). — [7511535550299258881](https://ads.tiktok.com/business/creativecenter/topads/7511535550299258881/pc/en)
- **Parent, coffee-price anchor (Vietnam TikTok):** "Đầu tư khóa học giúp con giao tiếp tiếng Anh thành thạo chỉ với chi phí 2 ly Phúc Long/buổi" ("Invest in a course for your child's fluent English for the price of 2 Phúc Long coffees a session"). — [7657417648604037138](https://ads.tiktok.com/business/creativecenter/topads/7657417648604037138/pc/en) **[3P-DATA]**
- **Parent, study abroad (Indonesia TikTok):** "'Papa, Mama… nanti aku mau sekolah di luar negeri ya!'" ("Papa, Mama… I want to study abroad later!"). — [7587773658195181569](https://ads.tiktok.com/business/creativecenter/topads/7587773658195181569/pc/en) **[3P-DATA]**
- **Career (Vietnam):**
  - ELSA × Khánh Vy: "Muốn bứt phá thu nhập và thăng tiến…" ("Want a breakthrough in income and promotion…"). — [1130166843237567](https://www.facebook.com/ads/library/?id=1130166843237567)
  - Langmaster: "Nhìn bạn bè đổi việc lương ngàn đô mà phát thèm?" ("Envious watching friends switch to thousand-dollar jobs?"). — [2326932638049959](https://www.facebook.com/ads/library/?id=2326932638049959)
  - Aten English (TikTok): "Học tiếng Anh để xin việc, deal lương hay nhảy việc…" ("Learn English to get a job, negotiate salary or switch jobs…"). — [7586346320749150224](https://ads.tiktok.com/business/creativecenter/topads/7586346320749150224/pc/en)
  - Labels: **[3P-DATA]**.
- **Price vs tutor or centre:**
  - EF Indonesia "HANYA 50 RIBU / BULAN" ("Only 50K a month"), up to 305,718 likes per ad. — [7203356948988395521](https://ads.tiktok.com/business/creativecenter/topads/7203356948988395521/pc/en)
  - Kyna: "TỐN TIỀN TRIỆU mà vẫn 'dở' tiếng Anh" ("Spent millions and still bad at English"). — [2305053839927205](https://www.facebook.com/ads/library/?id=2305053839927205)
  - Engoo: "เริ่มเพียง 2,400 บาท" ("From only 2,400 baht"). — [1386462366367807](https://www.facebook.com/ads/library/?id=1386462366367807)
  - Labels: **[3P-DATA]**.
- **Native-speaker benchmark:**
  - ELSA: "vẫn chưa nói như người bản xứ?" ("still don't speak like a native?"). — [962257616901503](https://www.facebook.com/ads/library/?id=962257616901503)
  - Monkey: "Nói tiếng Anh chuẩn Mỹ" ("Speak standard American English"). — [1457794848590457](https://www.facebook.com/ads/library/?id=1457794848590457)
  - Engoo: "ต้องฝึกกับเจ้าของภาษาตัวจริง" ("must practise with real native speakers"). — [776586944717751](https://www.facebook.com/ads/library/?id=776586944717751)
  - Labels: **[3P-DATA]**.
- **Fear of speaking in public:** LEL School (Myanmar): "အင်္ဂလိပ်စကားပြောရတော့မယ်ဆိုကြောက်ပြီး လူတောမတိုးတော့ဘဲ… broken ပုံစံတွေပဲဖြစ်နေလို့ လူအများကြားထဲ ကိုယ့်ကိုကိုယ်ယုံကြည်မှုပျောက်ဆုံးနေပြီလား?" ("Scared when you have to speak English, so you avoid people… losing self-confidence in public because it comes out broken?"). — [1076277824128273](https://www.facebook.com/ads/library/?id=1076277824128273) **[3P-DATA]**
- **Entertainment / celebrity:** Thai Kru P'Ann's comedian-interview ad (99,700 likes) and a Vietnamese pun ad, "Ô ăn quan là Umbrella Eat Quan chứ còn gì nữa 😌". The pun is a deliberately wrong literal translation of the folk game "ô ăn quan". — [7226603548325724162](https://ads.tiktok.com/business/creativecenter/topads/7226603548325724162/pc/en); [7496786920028340240](https://ads.tiktok.com/business/creativecenter/topads/7496786920028340240/pc/en) **[3P-DATA]**

### Inferences
- **Each market has a dominant hook** **[OBSERVATION]**:
  - Vietnam: the densest market, every family present, with exam and career the most frequent.
  - Thailand: work-adult speaking (Globish, Engoo) and exam on TikTok.
  - Korea: exam (TOEIC) and "academies and apps didn't work" (output training).
  - Indonesia: price.
- **Myanmar:** "fear and embarrassment" and "time-poor" hooks, plus "Burmese-language explanation".
- **Common structure.** Asian hooks tie English to a concrete institutional gate (graduation, civil-service grade, university entrance, interview) or to the parent's duty. Western AI-app ads lean on speed or method instead. This extends the earlier note that ads in Asia lean on career, income and family.
- **Time-bound promises are everywhere:** Monkey's 90/100 days, Globish's 3 months, ELSA's "a few minutes", 30Days Learning's 30 days.

### Gaps
- **Hook performance.** No CTR or CPA by hook is published. Run length and Creative Center likes are proxies only.
- **Japan and the Philippines.** No localized Japanese or Filipino-language hooks from major brands were captured beyond the generic "7-day free unlimited lessons" ad. Engoo Japan returned 0 ads.

---

## Q3. Are any English-app ads running in Burmese or targeting Myanmar and the Burmese diaspora?

### Takeaway
Yes, but almost all come from **local Burmese course providers and edtech pages**, not international apps.
- **Burmese-language advertisers:** GYS, LEL School, 30days Learning, LearnMyanmar Book, English for Life (EFL), ESL, WEBS International and Starfish Academy (which has an app).
- **Run lengths are long:** 180 to 764 days.
- **The funnel:** almost universally Messenger. Most videos are captioned in Burmese with English terms mixed in ("Speaking", "4 skills", "Vocabulary").
- **Format:** a Burmese TikTok ad from GYS ranks in Creative Center Top Ads.
- **International apps:** LunaSpeak, Glite, Fluzy, LingoSpeak, Preply and "Instant Speak Translator" appear in the Myanmar-filtered results, but only with English (or Hindi) copy. No Burmese-localized ad from ELSA, Praktika, Speak, Cambly or Duolingo was found.
- **Diaspora:** no ad explicitly targeted the diaspora (for example in Thailand or Japan).

### Cited Findings
- **GYS (Grab Your Success), video, 764 days** (2024-10-21 to 2026-11-24).
  - Title: "✅အင်္ဂလိပ်စာကို 4 skills လုံး ပိုင်နိုင်အောင် ဘယ်လို လေ့လာရမလဲ" ("How do you study English to master all 4 skills?").
  - The body asks viewers to "39 Second လောက်ပေးပြီး ဆုံးအောင်ဖတ်ပေးပါ" ("give it about 39 seconds and read to the end"). Classes run "ABC မှ စတင်" ("starting from ABC"). CTA: Send message. **[3P-DATA]**
  - [8684058498298989](https://www.facebook.com/ads/library/?id=8684058498298989)
- **LEL School, video, 743 days.**
  - Hook: the fear-of-speaking line quoted in Q2. Offer: "One Month English Speaking Class". CTA: Send message. **[3P-DATA]**
  - [1076277824128273](https://www.facebook.com/ads/library/?id=1076277824128273)
- **30days Learning, video, 505 days.**
  - Hook: "💡ဒီနှစ်ထဲမှာ အင်္ဂလိပ်စာ စလေ့လာဖို့ စိတ်ကူးထားတာရှိလား? နေ့ရွေ့ညရွေ့နဲ့ဆိုရင် ပန်းတိုင်ရောက်ဖို့ အလှမ်းဝေးနေမယ်" ("Planning to start English this year? If you keep putting it off day after day, the goal will stay far away").
  - Offer: a one-time purchase with no expiry, 24/7 access. CTA: message "30" to m.me. **[3P-DATA]**
  - [590048494161590](https://www.facebook.com/ads/library/?id=590048494161590)
- **LearnMyanmar Book (LMB English), video, 467 days.**
  - Hook: "Vocabulary တွေခဏခဏမေ့နေလို့ အင်္ဂလိပ်စာမတိုးတက်ဘူးဖြစ်နေလား" ("Not improving at English because you keep forgetting vocabulary?").
  - USP: "မြန်မာလိုရှင်းပြချက်အသေးစိတ်ပါ" ("includes detailed explanations in Burmese"). **[3P-DATA]**
  - [1769207160371108](https://www.facebook.com/ads/library/?id=1769207160371108)
- **WEBS International, video, 386 days.** "Early Bird Discounts… Special Discount for (10) Persons" for General English and IELTS weekend classes, online or on campus. **[3P-DATA]** — [4072035313060184](https://www.facebook.com/ads/library/?id=4072035313060184)
- **English Classes by GYS, video, 376 days.** Hook: "အင်္ဂလိပ်လို မွှတ်နေအောင် ပြောနိုင်ဖို့ အဓိကလိုအပ်နေတာ သေချာလေ့ကျင့်ဖို့ပါ" ("To speak English fluently, the key is proper practice"). Offer: lifetime-access classes. **[3P-DATA]** — [1464811477937562](https://www.facebook.com/ads/library/?id=1464811477937562)
- **English for Life (EFL Myanmar), video, 288 days.** Hook: "Grammar မပိုင်နိုင်လို့ အင်္ဂလိပ်စာ level တခုထဲမှာပဲ တဝဲလည်လည်ဖြစ်နေတဲ့သူတွေ ရှိကြလား" ("Anyone stuck circling at one English level because you haven't mastered grammar?"). **[3P-DATA]** — [2991682317889111](https://www.facebook.com/ads/library/?id=2991682317889111)
- **ESL program, video, 235 days.** A creator ("Chan") endorses it: "Self study ပဲလုပ်ပြီး English စာကို Native Speakers တစ်ယောက်လိုပြောနိုင်တဲ့ထိ… Chan ကိုယ်တိုင် ညွှန်းပေးထားတဲ့ ESL" ("Recommended by Chan himself, who self-studied to speak like a native"). Format: KOL endorsement. **[3P-DATA]** — [1658654615585831](https://www.facebook.com/ads/library/?id=1658654615585831)
- **Starfish Academy (Burmese kids' English app), image ads, 103 days.**
  - Hook: "⏰ တစ်နေ့ ၁၅ မိနစ် အချိန်ပေးရုံနဲ့ ကလေးတို့ရဲ့ English ကို တစ်ဆင့်ပြီးတစ်ဆင့် တိုးတက်စေဖို့" ("Just 15 minutes a day to improve your child's English step by step").
  - "📱 Starfish Academy App မှာ Grade 1 မှ Grade 12 အထိ ကျောင်းစာ English" ("Starfish Academy App: school-curriculum English from Grade 1 to Grade 12").
  - A sister ad offers "August Special Promotion – 30% OFF". This is the only Burmese-language *app* ad found. **[3P-DATA]**
  - [2759123277807075](https://www.facebook.com/ads/library/?id=2759123277807075); [1526671215436589](https://www.facebook.com/ads/library/?id=1526671215436589)
- **GYS on TikTok.** Burmese Top Ads with 26,522 / 6,775 / 91 likes, 56–86s, video-view objective. They funnel to a Telegram channel (#TelegramChannel). **[3P-DATA]** — [7667329273791561735](https://ads.tiktok.com/business/creativecenter/topads/7667329273791561735/pc/en)
- **International AI apps in the Myanmar-filtered results, all non-Burmese copy:**
  - LunaSpeak (218 days): [1250208760626569](https://www.facebook.com/ads/library/?id=1250208760626569)
  - Glite "Free 3-Minute English Speaking Test": [2046115340120233](https://www.facebook.com/ads/library/?id=2046115340120233)
  - Fluzy: [1075994231559397](https://www.facebook.com/ads/library/?id=1075994231559397)
  - "Instant Speak Translator" (title "🗣️ English Speaking App ⭐4.8 12M+", Play Store link): [1088990320282788](https://www.facebook.com/ads/library/?id=1088990320282788)
  - Labels: **[3P-DATA]**. Whether these actually reached Myanmar is uncertain, given the loose country filter.
- **Scale of the query.** The Burmese-script keyword "အင်္ဂလိပ်စာ" (English language) returned 291 Meta ads; "English" with Myanmar selected returned 7,792. **[3P-DATA]**

### Inferences
- **A gap for apps.** No international English app runs Burmese-localized ads. The Burmese market is served by local course pages with long-running Messenger and Telegram lead ads, so a Burmese-language app ad would face little direct app competition. **[OBSERVATION]**
- **Long-running Burmese ads share a pattern** **[OBSERVATION]**:
  - a pain-question opener ("Is English speaking still hard?", "keep forgetting vocabulary?", "afraid to speak in public?");
  - Burmese body text with English skill terms mixed in;
  - a long benefit list;
  - an m.me or Telegram CTA.
- **Telegram is used as a delivery channel on TikTok (GYS).** This is consistent with Myanmar's VPN and Facebook restrictions described in `myanmar_market.md`.
- **Payment offers in Burmese ads avoid card subscriptions.** They use one-time purchases, early-bird group discounts and lifetime access. This fits the KBZPay/WavePay Messenger checkout norm.

### Gaps
- **No Myanmar-targeted ads from ELSA, Praktika, Cambly or Preply.** I could not confirm whether any of them run Myanmar-targeted ads. The scrape's reach-country data is empty.
- **No diaspora-targeted ads found.** I did not find Burmese-language English-learning ads aimed at the diaspora, such as Burmese workers in Thailand or Japan learning English. Searching in Thai or Japanese with Burmese keywords, plus Page-ID lookups, would be needed.
- **No Play Store data on Burmese English apps.** Download counts were not researched.
- **No TikTok data beyond Top Ads.** TikTok's Myanmar ad library (Commercial Content Library) has EU-only coverage, so Myanmar TikTok ads are visible only through Creative Center Top Ads.
