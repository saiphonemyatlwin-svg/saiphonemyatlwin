# plan.json schema

Paths are relative to the plan file. Times are in seconds on the source clip's
timeline. Cards and B-roll cover the speaker while the source audio keeps playing.

```jsonc
{
  "source": "talk.mp4",        // required: the raw talking-head clip (any aspect; cover-cropped to 9:16)
  "matte": "matte.mp4",        // from segment.py; omit to disable text_behind
  "out": "edit.mp4",
  "size": [1080, 1920], "fps": 30,
  "duration": null,            // default: source length
  "push_in": 0.06,             // slow zoom on the speaker, resets after each cutaway
  "crossfade": 0.22,           // seconds, in/out of cards & b-roll
  "logo_bug": true,            // accent mark top-right
  "theme": { "accent": "#5ec8ff", "card_bg": "#121214", "text": "#f2f2f2" },

  "captions": [
    { "start": 0.1, "end": 1.6,
      "kicker": "There's a strong",   // small tracked caps (auto-uppercased)
      "emphasis": "pull to",          // big italic serif (Myanmar → bold, accent colour)
      "y": 0.70,                      // optional, fraction of height
      "accent": false }               // optional: emphasis in accent colour
  ],

  "beats": [
    { "type": "text_behind", "start": 0.9, "end": 2.4, "text": "Interviews",
      "y": 0.2, "size": 300, "gauge": false },

    { "type": "keyword_card", "start": 3.6, "end": 5.8,
      "kicker": "But there's also a really strong", "text": "Enterprise",
      "size": 190, "network": true, "seed": 7 },

    { "type": "broll", "start": 5.8, "end": 7.6, "src": "broll.mp4",
      "src_start": 0, "text": "Call centers", "y": 0.52, "size": 200 },

    { "type": "counter_card", "start": 7.6, "end": 9.8,
      "kicker": "They'll read, like, a", "from": 450, "to": 600,
      "step": null, "format": "{:,.0f}", "suffix": "", "roll": null,
      "label": "Page textbook", "size": 200, "label_size": 130 }
  ]
}
```

Sizes are in px at 1080 wide and scale with the output size. Over-wide
keywords shrink automatically to fit.
