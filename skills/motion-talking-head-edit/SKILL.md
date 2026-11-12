---
name: motion-talking-head-edit
description: Turn one plain talking-head clip into a premium "motion-graphics" short (Reels/TikTok/Shorts, 9:16) — giant chrome keywords placed BEHIND the speaker, two-tier caption (small caps + big italic serif), dark ribbed full-screen keyword cards with icon-network diagrams, odometer number rolls, B-roll with keyword overlays, push-ins and crossfades. Use when the user wants a talking-head, podcast or interview clip "edited like that motion-graphics reel", "text behind me", "premium/cinematic captions", "make my clip look like a high-end creator edit", or hands over a raw clip + transcript and asks for an edit plan or a rendered video. Works for English and Burmese (Myanmar script) text.
---

# Motion Talking-Head Edit

One raw clip + its transcript → a 9:16 reel where a new visual idea lands
every ~1.5 s. The full look breakdown is in `reference/style-breakdown.md`;
the plan format is in `reference/plan-schema.md`.

## Pipeline

```
raw clip ──► 1. transcript (word or phrase timings)
         ──► 2. scripts/segment.py   → matte.mp4   (person mask, for text-behind)
         ──► 3. YOU write plan.json  (the creative part — rules below)
         ──► 4. scripts/render.py plan.json --preview   → check frames
         ──► 5. scripts/render.py plan.json             → final 1080×1920
```

Setup once: `pip install pillow numpy mediapipe`, ffmpeg on PATH. On headless
Linux MediaPipe also needs `apt-get install -y libegl1 libgles2`. segment.py
downloads its ~250 KB model from storage.googleapis.com on first run.

**Transcript:** use one the user supplies, or a transcription tool you have
(e.g. a local Whisper). You need start/end seconds per phrase. For
Burmese, ask the user to check the transcript — auto-transcription of
Myanmar speech is often wrong.

**Study a new reference reel first:** `scripts/analyze_reference.sh <video>`
makes a contact sheet, cut list and per-second frames. Read the sheet before
changing the style.

## Writing the plan — the editorial rules

These rules carry the look. The renderer only executes them.

1. **Hook in the first 1.5 s.** Open on the speaker with a caption at 0.1 s,
   then a `text_behind` keyword by ~1 s. Never start on a card.
2. **One idea per beat, ~1.2–2.2 s each.** Every beat is triggered by a
   spoken word. Pick the noun or number that carries each sentence:
   - a **status/identity noun** ("INTERVIEWS", "FAME", "EVERYTHING") →
     `text_behind`, 1–2 words, ≤ 12 characters;
   - a **category/concept** the viewer must remember ("ENTERPRISE") →
     `keyword_card`, `network: true` if it is about people/teams/markets;
   - a **number** ("a 600-page textbook") → `counter_card`, rolling from
     ~75 % of the value up to it, with the unit as `label`;
   - a **concrete place/thing** you can show ("call centers") → `broll`
     with the keyword over it.
3. **Rhythm:** speaker → speaker+keyword → card → b-roll → card → speaker.
   Don't put two cards back to back more than once, and don't stay on the
   bare speaker longer than ~3 s.
4. **Captions are two-tier, not word-by-word karaoke.** `kicker` holds the
   3–6 lead-in words in small caps; `emphasis` holds the 1–3 words that land,
   in big italic serif. Lowercase emphasis reads as voice, so keep it that way.
   Captions hide automatically on cards (cards carry their own kicker line).
5. **Card text = the spoken words.** The card's kicker is the setup phrase
   verbatim; the keyword is the payoff word. Never write text that isn't said.
6. **Restraint:** one accent colour (default ice-blue `#5ec8ff`), everything
   else greyscale/chrome. Use `gauge: true` at most once per video, on the
   final or biggest `text_behind`.
7. **End on the speaker** with a strong `text_behind` + gauge, holding to the
   last word.

## Rendering & QA

- Always run `--preview` first (half res, about 2× faster), then grab frames:
  `ffmpeg -ss <t> -i edit.mp4 -frames:v 1 f.png` at the middle of every beat.
  Check that keywords aren't clipped, text sits behind the head and not over
  the face, captions are readable, and the counter ends on the right number.
- `text_behind` needs the speaker's head to sit lower than the keyword. The
  default `y: 0.2` suits a typical mid-shot. If the head is high in the frame,
  lower `size` or use a `keyword_card`.
- A poor matte (busy background, low light) shows as a halo. Raise
  `--smooth` in segment.py to 0.8, or swap that beat for a card.
- About 5 s of render time per 1 s of 1080p video on CPU. Audio comes from
  the source clip untouched.

## Burmese / Dr. Sai adaptation

- Myanmar text is detected automatically and set in Noto Sans Myanmar
  (Bold for keywords/emphasis). Italic serif has no Myanmar form, so Myanmar
  `emphasis` is drawn in the accent colour instead.
- Keep Myanmar keywords short (1 word, roughly ≤ 6 syllables); the renderer
  shrinks anything wider than the frame.
- For the Dr. Sai brand, set `theme.accent` and `theme.card_bg` from the
  dr-sai-design / dr-sai-studio palette, and pull keywords from his
  stacked-line punchlines (dr-sai-voice).

## Files

- `scripts/segment.py` — person matte via MediaPipe selfie segmenter.
- `scripts/render.py` — plan → video (PIL + numpy + ffmpeg).
- `scripts/analyze_reference.sh` — study any reference reel.
- `reference/style-breakdown.md` — beat-by-beat teardown of the reference.
- `reference/plan-schema.md` — every field, with defaults.
- `examples/plan.example.json` — full working plan.
- `fonts/` — Bebas Neue, Instrument Serif Italic, Inter, Noto Sans Myanmar
  (all SIL OFL; licences included).
