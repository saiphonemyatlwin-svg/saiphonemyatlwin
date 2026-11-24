---
name: dr-sai-video
description: The Dr. Sai video craft system for short-form reels (Facebook/Instagram/TikTok, 30–90s) and long-form talking-head video. It covers the platform signals a great video earns, the 10 components every video is built from, a 20-point scorecard for auditing any video (yours or a reference), a flop-diagnosis tree, and the shot/audio/edit/text standards. Use it when planning, scripting, shooting, editing or reviewing a Dr. Sai video, when the user shares a reel and asks "what makes this good / what is it lacking", or says "audit this video", "score this reel", "why did this flop", or "make this video better". It inherits voice from dr-sai-voice, visuals from dr-sai-studio and strategy from Dr_Sai_Content_Playbook_4_Pillars.md.
---

# Dr. Sai — Video Craft System

A video is good when it **earns the signals** the platform rewards **from the right viewer**.
Ideas and hooks get people to start watching. Craft keeps them watching. The payoff gets them to share.
This skill is the craft-and-measurement layer. The idea and script layer lives in
`Dr_Sai_Content_Playbook_4_Pillars.md` (4C hook, short/long skeletons). Don't duplicate it; use both.

---

## 1. The signals (what "good" means, measured)

Platforms rank on viewer behaviour, not on production value. Work towards these, in this order:

| # | Signal | What it proves | Where it's won |
|---|---|---|---|
| 1 | **3-second hold** (people who don't swipe away) | The hook works | Frame 1, line 1, on-screen text |
| 2 | **Average % watched / completion** | The middle doesn't sag | Pacing, open loops, cutting fluff |
| 3 | **Rewatches** (watch time > length) | It's dense or has a satisfying loop | Fast insight, a loopable ending |
| 4 | **Sends / shares per reach** | "This is about you, friend." The strongest reach signal on Reels | A specific, tag-a-person idea; a tattoo line |
| 5 | **Saves** | Useful later | A framework, list or steps on screen |
| 6 | **Comments (real ones)** | It started a thought | A contrarian frame, a question, a comment keyword |
| 7 | **Follows / profile visits per view** | People want *more of you* | Distinct POV, consistent series format |
| 8 | **Owned conversion** (Telegram/email signups) | The authority game is working | CTA aligned to the same pain |

Rule: **#8 is the north star. #1–#4 are the fuel.** A viral video with zero follows or signups is a miss.
Heuristic targets for Reels (check against your own baseline, not someone else's):
3-sec hold ≥ 60%, average watched ≥ 50% for a 60s reel, sends ≥ saves ≥ 1% of reach.

---

## 2. The 10 components of every video

Every video is built from these. When a video underperforms, one of them is missing.

1. **Idea (topic + angle):** a validated topic plus a non-obvious angle. (Playbook §3)
2. **Hook stack:** three hooks fire together in the first 1.5s:
   - *Visual hook:* movement, an unusual frame, a prop, or a face mid-sentence (never a logo or "hi everyone")
   - *Spoken hook:* the first line (see 4C / familiar pain / reversal)
   - *Text hook:* ≤ 7 words on screen that **add** to the spoken line rather than repeat it
3. **Promise:** the viewer knows in < 5s what they'll get and why to stay.
4. **Retention architecture:** open loops ("the third one is the one nobody does…"), a pattern interrupt every 3–6s (cut, zoom, b-roll, graphic, angle change), and no dead air.
5. **Payoff:** the light-bulb moment arrives *before* the viewer gives up, by about 60% of runtime.
6. **Proof / credibility:** one contextual, real proof point. Show it, don't just claim it (number, screenshot, place, scar).
7. **Visual craft:** clean frame, eye-level, light on the face, an intentional background, brand palette.
8. **Audio craft:** clear voice first, music second. Sound effects mark the beats. **Bad audio kills a video faster than bad video.**
9. **Text and captions:** burned-in captions (most people watch with the sound off), readable, inside the safe zone.
10. **Close and CTA:** a tattoo line plus one action aligned to the pain, and an ending that loops back to the start where possible.

Details for 7–9 are in `references/craft-standards.md`.

---

## 3. Auditing a video (yours or a reference reel)

When the user shares a video and asks what's good or what's lacking:

1. **Get the actual video.** Public Facebook/Instagram/TikTok/YouTube links: download with `yt-dlp` into the scratchpad,
   then `ffmpeg` frames at 2fps → contact sheets (`tile=5x2`), plus `volumedetect` for audio levels. Burned-in captions give the script.
   If the download fails (private / login-walled), ask for the mp4 or a description. **Never invent what a video contains.**
   Save each audit to `audits/` so the skill learns from every reference.
2. Write a **timeline breakdown**: 0–1.5s / 1.5–5s / middle beats / payoff / close. Note what is seen, heard and on screen.
3. Score it with `references/scorecard.md` (10 components × 0–2 = /20).
4. Report in this order:
   - **What works (keep/steal):** the 3 strongest signals it earns and *why*
   - **What's lacking:** the 3 lowest-scoring components, each with the exact fix
   - **Dr. Sai remix:** how to take the *structure* (not the content) into one of the 4 pillars, in Dr. Sai's voice
5. If it's the user's own video and analytics exist, run the **flop-diagnosis tree** below first.

---

## 4. Flop-diagnosis tree (debug in this order, always)

```
Low reach overall?
 └─ Is the TOPIC validated (outliers exist in the niche)?          no → change topic
     └─ Is the ANGLE non-obvious?                                    no → sharpen the angle
         └─ 3-sec hold < 50%?                                        yes → fix the HOOK STACK (visual + spoken + text)
             └─ Big drop-off in the middle?                          yes → cut fluff, add pattern interrupts, open a loop
                 └─ Good watch time but few sends/saves?             yes → payoff too vague; make it specific and shareable
                     └─ Good engagement but no follows/signups?      yes → POV not distinct / CTA misaligned to the pain
                         └─ All good, still small?                   → audience ring too broad or too narrow; post consistently
```
Never fix editing first. Topic, angle and hook cause most flops.

### Read the retention graph first (when you have analytics)
| Graph shape | Diagnosis | Fix |
|---|---|---|
| Steep cliff in the first 1–3s, then flat near zero | **Bad hook** | Rebuild the hook stack; start on the 2nd sentence |
| Steady straight-line decline from start to end | **Weak topic / angle**: nobody cares enough | Re-validate the topic; sharpen the angle |
| Early cliff, then flat but low | **Weak content overall**: hook *and* body | Re-plan from the idea |
| Holds well, then a sharp drop near the end | **Weak close / CTA**: people leave before the ask | Move the payoff earlier; shorter, aligned CTA |
| Mid-video dip | **Sagging middle** | Cut fluff, add a pattern interrupt or open loop there |
| Small early dip, then nearly flat and high (or above 100% with rewatches) | **The goal** | Repeat this format as a series |
(Learned from an audited reference reel: `audits/2026-11_retention-graph-reel.md`.)

---

## 5. Production workflow (one reel)

1. **Plan (10 min):** pillar → topic → angle → write the one-sentence *payoff* first.
2. **Script:** Playbook §3.7 skeleton. Read it aloud; cut every line that doesn't move to the payoff.
3. **Shot list:** A-roll (talking head) + 3–5 B-roll / graphic inserts mapped to beats.
4. **Shoot:** `references/craft-standards.md` setup checklist. Do the first line 3 times with different energy.
5. **Edit:** hook-first cut → remove pauses/breaths → pattern interrupt every 3–6s → captions → SFX on beats → music at −20 to −25 dB under voice.
6. **Package:** cover frame (dr-sai-studio), caption first line = a second hook, comment keyword.
7. **Score before publishing:** ≥ 15/20 to ship. 12–14: fix the lowest component. < 12: re-cut or re-shoot the hook.
8. **Review after 48h:** log the signals in `references/scorecard.md`, then run the diagnosis tree.

---

## 6. Brand guardrails (inherited)

- Calm authority, no hype. No fake urgency, no clickbait the video doesn't pay off.
- Real proof only; never invent numbers or stories.
- Burmese voice rules from dr-sai-voice (no "မင်း/ငါ", stacked short lines).
- Visual: one gold, one figure, one light, one line (dr-sai-studio).
- Human, first-person expertise. Avoid AI-avatar-only content for core videos.
