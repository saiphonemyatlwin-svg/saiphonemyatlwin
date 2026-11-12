#!/usr/bin/env python3
"""Render a "motion talking-head" reel from one plain clip + an edit plan.

    python3 render.py plan.json [--preview]   # --preview = half-res, fast

The plan (JSON) lists captions and beats; see ../reference/plan-schema.md.
Paths inside the plan are resolved relative to the plan file.

Looks produced (all from the reference style):
  - two-tier captions: small tracked caps "kicker" + big italic-serif "emphasis"
  - text_behind:  giant chrome keyword placed BEHIND the speaker (needs matte)
  - keyword_card: full-screen dark ribbed card, chrome keyword, optional
                  people-network diagram with glowing accent node
  - counter_card: odometer number roll (e.g. 450 -> 600) + label
  - broll:        cutaway clip with chrome keyword over it
  - slow push-in on the speaker that resets at every cutaway, crossfades,
    diagonal light sweep, vignette.

Needs: pip install pillow numpy ; ffmpeg on PATH.
"""
import argparse, json, math, os, random, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "..", "fonts")
F_DISPLAY = os.path.join(FONTS, "BebasNeue-Regular.ttf")
F_SERIF_IT = os.path.join(FONTS, "InstrumentSerif-Italic.ttf")
F_SANS = os.path.join(FONTS, "Inter-SemiBold.ttf")
F_MY = os.path.join(FONTS, "NotoSansMyanmar-Regular.ttf")
F_MY_B = os.path.join(FONTS, "NotoSansMyanmar-Bold.ttf")


# ---------------------------------------------------------------- helpers
def is_myanmar(s):
    return any("က" <= c <= "႟" or "ꩠ" <= c <= "ꩿ" for c in s)


_font_cache = {}
def font(path, size):
    k = (path, int(size))
    if k not in _font_cache:
        _font_cache[k] = ImageFont.truetype(path, int(size))
    return _font_cache[k]


def hex2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def ease_out(x):  # cubic
    x = min(max(x, 0.0), 1.0)
    return 1 - (1 - x) ** 3


def ease_in_out(x):
    x = min(max(x, 0.0), 1.0)
    return x * x * (3 - 2 * x)


def env(t, start, end, fade=0.2):
    """0..1 envelope: fade in after start, fade out before end."""
    if t < start or t > end:
        return 0.0
    return min(1.0, (t - start) / fade, (end - t) / fade) if fade > 0 else 1.0


def probe(path):
    out = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries",
                                   "format=duration", "-of", "json", path])
    return float(json.loads(out)["format"]["duration"])


class Reader:
    """Sequential cover-fit frame reader (repeats last frame when exhausted)."""
    def __init__(self, path, W, H, fps, gray=False, start=0.0):
        self.W, self.H, self.gray = W, H, gray
        self.n = W * H * (1 if gray else 3)
        vf = (f"scale={W}:{H}:force_original_aspect_ratio=increase,"
              f"crop={W}:{H},fps={fps}")
        self.p = subprocess.Popen(
            ["ffmpeg", "-v", "error", "-ss", str(start), "-i", path, "-vf", vf,
             "-f", "rawvideo", "-pix_fmt", "gray" if gray else "rgb24", "-"],
            stdout=subprocess.PIPE)
        self.last = None

    def read(self):
        buf = self.p.stdout.read(self.n)
        if len(buf) == self.n:
            shape = (self.H, self.W) if self.gray else (self.H, self.W, 3)
            self.last = Image.fromarray(np.frombuffer(buf, np.uint8).reshape(shape),
                                        "L" if self.gray else "RGB")
        elif self.last is None:
            self.last = Image.new("L" if self.gray else "RGB", (self.W, self.H))
        return self.last

    def close(self):
        try:
            self.p.kill()
        except Exception:
            pass


# ---------------------------------------------------------------- text art
def text_size(txt, f, tracking=0):
    if tracking and not is_myanmar(txt):
        return sum(f.getlength(c) for c in txt) + tracking * (len(txt) - 1), f.getbbox("Hg")[3]
    b = f.getbbox(txt)
    return b[2] - b[0], b[3]


def draw_text(d, xy, txt, f, fill, tracking=0):
    x, y = xy
    if tracking and not is_myanmar(txt):
        for c in txt:
            d.text((x, y), c, font=f, fill=fill)
            x += f.getlength(c) + tracking
    else:
        d.text((x, y), txt, font=f, fill=fill)


_chrome_cache = {}
def chrome_text(txt, size, max_w=None):
    """Silver brushed-metal text (RGBA) with soft shadow. Auto-shrinks to max_w."""
    key = (txt, size, max_w)
    if key in _chrome_cache:
        return _chrome_cache[key]
    path = F_MY_B if is_myanmar(txt) else F_DISPLAY
    f = font(path, size)
    while max_w and f.getbbox(txt)[2] > max_w and size > 20:
        size = int(size * 0.94)
        f = font(path, size)
    b = f.getbbox(txt)
    pad = int(size * 0.25)
    w, h = b[2] - b[0] + 2 * pad, b[3] - b[1] + 2 * pad
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).text((pad - b[0], pad - b[1]), txt, font=f, fill=255)
    # vertical metal gradient + faint horizontal brushing
    ys = np.linspace(0, 1, h)[:, None]
    stops = np.interp(ys, [0, .30, .48, .52, .75, 1], [250, 215, 150, 205, 175, 120])
    rng = np.random.default_rng(len(txt))
    streak = rng.normal(0, 6, (h, 1))
    g = np.clip(stops + streak + np.zeros((h, w)), 0, 255).astype(np.uint8)
    metal = Image.merge("RGB", (Image.fromarray(g),) * 3)
    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    sh = mask.filter(ImageFilter.GaussianBlur(size * 0.06)).point(lambda v: int(v * 0.55))
    out.paste((0, 0, 0, 255), (0, int(size * 0.03)), sh)
    out.paste(metal, (0, 0), mask)
    _chrome_cache[key] = out
    return out


def paste_center(base, im, cx, cy, alpha=1.0, scale=1.0):
    if alpha <= 0.01:
        return
    if abs(scale - 1) > 0.002:
        im = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))),
                       Image.BILINEAR)
    if alpha < 0.999:
        a = im.getchannel("A").point(lambda v: int(v * alpha))
        im = im.copy(); im.putalpha(a)
    base.alpha_composite(im, (int(cx - im.width / 2), int(cy - im.height / 2)))


# ---------------------------------------------------------------- renderer
class Renderer:
    def __init__(self, plan, base_dir, preview=False):
        self.plan, self.dir = plan, base_dir
        W, H = plan.get("size", [1080, 1920])
        if preview:
            W, H = W // 2, H // 2
        self.W, self.H, self.s = W, H, W / 1080.0
        self.fps = plan.get("fps", 30)
        th = plan.get("theme", {})
        self.accent = hex2rgb(th.get("accent", "#5ec8ff"))
        self.card_bg = hex2rgb(th.get("card_bg", "#121214"))
        self.text_col = hex2rgb(th.get("text", "#f2f2f2"))
        self.push = plan.get("push_in", 0.06)
        self.beats = sorted(plan.get("beats", []), key=lambda b: b["start"])
        self.caps = plan.get("captions", [])
        self.src = self.p(plan["source"])
        self.dur = plan.get("duration") or probe(self.src)
        self.cuts = sorted({0.0} | {b["start"] for b in self.beats if b["type"] != "text_behind"}
                           | {b["end"] for b in self.beats if b["type"] != "text_behind"})
        self._mk_static()

    def p(self, rel):
        return rel if os.path.isabs(rel) else os.path.join(self.dir, rel)

    # precomputed layers
    def _mk_static(self):
        W, H = self.W, self.H
        xs = np.arange(W)[None, :]
        rib = 18 * self.s
        stripes = 10 * np.sin(xs / rib * 2 * np.pi) ** 2 + 6 * np.sin(xs / (rib * 7.3)) ** 2
        base = np.array(self.card_bg, np.float32)[None, None, :]
        ys = np.linspace(-1, 1, H)[:, None]
        shade = (1 - 0.35 * ys ** 2)[..., None]
        card = (base + stripes[..., None]) * shade
        self.card = Image.fromarray(np.clip(np.broadcast_to(card, (H, W, 3)), 0, 255).astype(np.uint8))
        yy, xx = np.mgrid[0:H, 0:W]
        self.u = ((xx * 0.57 + yy * 0.82) / (W * 0.57 + H * 0.82)).astype(np.float32)  # diagonal coord
        r = np.sqrt(((xx - W / 2) / (W * 0.75)) ** 2 + ((yy - H / 2) / (H * 0.75)) ** 2)
        self.vig = Image.fromarray(np.clip(255 * (1 - 0.45 * np.clip(r, 0, 1) ** 2.2), 0, 255).astype(np.uint8))

    def sheen(self, img, pos, strength=0.10, width=0.10):
        m = np.exp(-((self.u - pos) / width) ** 2) * strength
        arr = np.asarray(img).astype(np.float32)
        arr = arr + (255 - arr) * m[..., None]
        return Image.fromarray(arr.astype(np.uint8))

    # ---- layers
    def speaker(self, t, frame, matte):
        cut = max(c for c in self.cuts if c <= t + 1e-6)
        z = 1 + self.push * ease_in_out((t - cut) / 4.0)
        if z > 1.001:
            W, H = self.W, self.H
            cw, ch = W / z, H / z
            box = (int((W - cw) / 2), int((H - ch) * 0.35), int((W + cw) / 2), int((H - ch) * 0.35 + ch))
            frame = frame.crop(box).resize((W, H), Image.BILINEAR)
            if matte is not None:
                matte = matte.crop(box).resize((W, H), Image.BILINEAR)
        tb = [b for b in self.beats if b["type"] == "text_behind" and b["start"] <= t <= b["end"]]
        if not tb or matte is None:
            return frame
        b = tb[0]
        k = env(t, b["start"], b["end"], 0.18)
        layer = frame.convert("RGBA")
        # darken background slightly so the keyword reads
        layer.alpha_composite(Image.new("RGBA", layer.size, (0, 0, 0, int(70 * k))))
        if b.get("gauge"):
            self.gauge(layer, t - b["start"], k, b.get("y", 0.2))
        size = int(b.get("size", 300) * self.s)
        im = chrome_text(b["text"].upper(), size, int(self.W * 0.92))
        sc = 1.12 - 0.12 * ease_out((t - b["start"]) / 0.45)
        paste_center(layer, im, self.W / 2, self.H * b.get("y", 0.2), k, sc)
        return Image.composite(frame, layer.convert("RGB"), matte)  # speaker on top

    def gauge(self, layer, lt, k, y):
        d = ImageDraw.Draw(layer)
        cx, cy, r = self.W / 2, self.H * (y + 0.07), self.W * 0.36
        sweep = 180 * ease_out(lt / 0.8)
        for i in range(0, 37):
            a = math.radians(180 + i * 5)
            if i * 5 > sweep:
                break
            r1 = r * (0.93 if i % 6 else 0.86)
            d.line([(cx + r1 * math.cos(a), cy + r1 * math.sin(a)),
                    (cx + r * math.cos(a), cy + r * math.sin(a))],
                   fill=(230, 230, 230, int(170 * k)), width=max(1, int(3 * self.s)))
        d.arc([cx - r * 1.04, cy - r * 1.04, cx + r * 1.04, cy + r * 1.04], 180, 180 + sweep,
              fill=(*self.accent, int(220 * k)), width=max(2, int(5 * self.s)))

    def kicker(self, img, txt, y, alpha=1.0, size=34):
        d = ImageDraw.Draw(img)
        f = font(F_MY if is_myanmar(txt) else F_SANS, size * self.s)
        tr = 0 if is_myanmar(txt) else 2.2 * self.s
        w, h = text_size(txt, f, tr)
        draw_text(d, ((self.W - w) / 2, y), txt, f, (*self.text_col, int(255 * alpha)), tr)
        return h

    def keyword_card(self, t, b):
        lt, L = t - b["start"], b["end"] - b["start"]
        img = self.sheen(self.card, -0.2 + 1.4 * lt / L, 0.07, 0.12).convert("RGBA")
        if b.get("kicker"):
            self.kicker(img, b["kicker"].upper(), self.H * 0.30, ease_out(lt / 0.3))
        im = chrome_text(b["text"].upper(), int(b.get("size", 190) * self.s), int(self.W * 0.86))
        paste_center(img, im, self.W / 2, self.H * 0.37, ease_out(lt / 0.25),
                     1.08 - 0.08 * ease_out(lt / 0.4))
        if b.get("network", False):
            self.network(img, lt, L, b.get("seed", 7))
        return img.convert("RGB")

    def person_icon(self, d, x, y, s, col):
        d.ellipse([x - s * .32, y - s, x + s * .32, y - s * .36], fill=col)
        d.rounded_rectangle([x - s * .55, y - s * .26, x + s * .55, y + s * .45], radius=s * .3, fill=col)

    def network(self, img, lt, L, seed):
        rnd = random.Random(seed)
        W, H, s = self.W, self.H, self.s
        cx, cy = W / 2, H * 0.58
        nodes = []
        for i in range(14):
            a = rnd.uniform(0, 2 * math.pi); r = rnd.uniform(0.12, 0.38) * W
            nodes.append((cx + r * math.cos(a), cy + r * math.sin(a) * 1.25, rnd.uniform(0.15, 0.9)))
        d = ImageDraw.Draw(img)
        for i, (x, y, delay) in enumerate(nodes):
            k = ease_out((lt - delay * 0.8) / 0.35)
            if k <= 0:
                continue
            if i < 6:  # links to hub
                d.line([(cx, cy), (cx + (x - cx) * k, cy + (y - cy) * k)],
                       fill=(200, 200, 200, int(50 * k)), width=max(1, int(2 * s)))
            self.person_icon(d, x, y, 26 * s, (190, 190, 195, int(230 * k)))
        # glowing hub
        pulse = 0.5 + 0.5 * math.sin(lt * 5)
        glow = Image.new("RGBA", img.size, (0, 0, 0, 0))
        gd = ImageDraw.Draw(glow)
        R = (34 + 10 * pulse) * s
        gd.ellipse([cx - R, cy - R, cx + R, cy + R], fill=(*self.accent, 150))
        glow = glow.filter(ImageFilter.GaussianBlur(18 * s))
        img.alpha_composite(glow)
        d.ellipse([cx - 13 * s, cy - 13 * s, cx + 13 * s, cy + 13 * s], fill=(*self.accent, 255))
        ring = 60 * s + 30 * s * ((lt * 0.8) % 1)
        d.ellipse([cx - ring, cy - ring, cx + ring, cy + ring],
                  outline=(*self.accent, int(120 * (1 - (lt * 0.8) % 1))), width=max(1, int(2 * s)))

    def counter_card(self, t, b):
        lt, L = t - b["start"], b["end"] - b["start"]
        img = self.sheen(self.card, -0.2 + 1.4 * lt / L, 0.07, 0.12).convert("RGBA")
        W, H, s = self.W, self.H, self.s
        if b.get("kicker"):
            self.kicker(img, b["kicker"].upper(), H * 0.24, ease_out(lt / 0.3))
        a, z = float(b["from"]), float(b["to"])
        roll = b.get("roll", min(1.6, L * 0.6))
        v = a + (z - a) * ease_out(lt / roll)
        step = b.get("step") or max(1, round(abs(z - a) / 10))
        base = math.floor(v / step) * step
        ph = (v - base) / step if v < z else 0.0
        row = 230 * s
        cy = H * 0.44
        fmt = b.get("format", "{:,.0f}")
        size = int(b.get("size", 200) * s)
        for k, val in ((-1, base - step), (0, base), (1, base + step)):
            if val < min(a, z) or val > max(a, z):
                continue
            y = cy + (k - ph) * row
            al = {-1: 0.15 * (1 - ph), 0: 1.0 - 0.8 * ph, 1: 0.18 + 0.82 * ph}[k]
            im = chrome_text(fmt.format(val) + b.get("suffix", ""), size)
            paste_center(img, im, W / 2, y, al)
        d = ImageDraw.Draw(img)
        for yy in (cy - row / 2, cy + row / 2):
            d.line([(W * 0.2, yy), (W * 0.8, yy)], fill=(255, 255, 255, 28), width=max(1, int(2 * s)))
        d.ellipse([W / 2 - 9 * s, cy + 92 * s, W / 2 + 9 * s, cy + 110 * s], fill=(*self.accent, 255))
        if b.get("label"):
            k = ease_out((lt - roll * 0.9) / 0.35)
            im = chrome_text(b["label"].upper(), int(b.get("label_size", 130) * s), int(W * 0.86))
            paste_center(img, im, W / 2, H * 0.66 + 30 * s * (1 - k), k)
        return img.convert("RGB")

    def broll(self, t, b):
        if b.get("_reader") is None:
            b["_reader"] = Reader(self.p(b["src"]), self.W, self.H, self.fps,
                                  start=b.get("src_start", 0.0))
        fr = b["_reader"].read()
        lt = t - b["start"]
        z = 1.04 + 0.06 * (lt / (b["end"] - b["start"]))
        cw, ch = self.W / z, self.H / z
        fr = fr.crop((int((self.W - cw) / 2), int((self.H - ch) / 2),
                      int((self.W + cw) / 2), int((self.H + ch) / 2))).resize((self.W, self.H))
        img = fr.convert("RGBA")
        img.alpha_composite(Image.new("RGBA", img.size, (0, 0, 0, 60)))
        if b.get("text"):
            im = chrome_text(b["text"].upper(), int(b.get("size", 200) * self.s), int(self.W * 0.9))
            paste_center(img, im, self.W / 2, self.H * b.get("y", 0.52), ease_out(lt / 0.3),
                         1.1 - 0.1 * ease_out(lt / 0.5))
        return img.convert("RGB")

    def captions(self, img, t):
        for c in self.caps:
            if not (c["start"] <= t <= c["end"]):
                continue
            k = env(t, c["start"], c["end"], 0.12)
            lt = t - c["start"]
            d = ImageDraw.Draw(img)
            y = self.H * c.get("y", 0.70)
            if c.get("kicker"):
                y += self.kicker(img, c["kicker"].upper(), y + 14 * self.s * (1 - ease_out(lt / 0.2)), k, 30) + 6 * self.s
            if c.get("emphasis"):
                txt = c["emphasis"]
                my = is_myanmar(txt)
                f = font(F_MY_B if my else F_SERIF_IT, (70 if my else 96) * self.s)
                w = f.getlength(txt)
                kk = ease_out((lt - 0.08) / 0.22) * k
                col = (*self.accent, int(255 * kk)) if (my or c.get("accent")) else (*self.text_col, int(255 * kk))
                # soft shadow for legibility on busy footage
                sh = Image.new("RGBA", img.size, (0, 0, 0, 0))
                ImageDraw.Draw(sh).text(((self.W - w) / 2, y + 4 * self.s), txt, font=f, fill=(0, 0, 0, int(160 * kk)))
                img.alpha_composite(sh.filter(ImageFilter.GaussianBlur(6 * self.s)))
                d.text(((self.W - w) / 2, y + 10 * self.s * (1 - kk)), txt, font=f, fill=col)

    # ---- main loop
    def run(self, out):
        W, H, fps = self.W, self.H, self.fps
        src = Reader(self.src, W, H, fps)
        mt = Reader(self.p(self.plan["matte"]), W, H, fps, gray=True) if self.plan.get("matte") else None
        enc = subprocess.Popen(
            ["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
             "-r", str(fps), "-i", "-", "-i", self.src, "-map", "0:v", "-map", "1:a?",
             "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
             "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out],
            stdin=subprocess.PIPE)
        N = int(self.dur * fps)
        XF = self.plan.get("crossfade", 0.22)
        for i in range(N):
            t = i / fps
            frame, matte = src.read(), (mt.read() if mt else None)
            img = self.speaker(t, frame, matte)
            for b in self.beats:
                if b["type"] == "text_behind" or not (b["start"] - XF <= t <= b["end"]):
                    continue
                fn = {"keyword_card": self.keyword_card, "counter_card": self.counter_card,
                      "broll": self.broll}[b["type"]]
                layer = fn(max(t, b["start"]), b)
                a = min(1.0, (t - b["start"] + XF) / XF, (b["end"] - t) / XF)
                img = Image.blend(img, layer, max(0.0, min(1.0, a)))
            img = img.convert("RGBA")
            on_card = any(b["type"] in ("keyword_card", "counter_card") and b["start"] <= t <= b["end"]
                          for b in self.beats)
            if not on_card:
                self.captions(img, t)
            if self.plan.get("logo_bug", True):
                self.bug(img)
            rgb = img.convert("RGB")
            rgb = Image.composite(rgb, Image.new("RGB", rgb.size), self.vig)
            enc.stdin.write(rgb.tobytes())
            if i % fps == 0:
                print(f"\r{t:5.1f}/{self.dur:.1f}s", end="", file=sys.stderr)
        enc.stdin.close(); enc.wait()
        src.close(); mt and mt.close()
        for b in self.beats:
            b.get("_reader") and b["_reader"].close()
        print(f"\nwrote {out}", file=sys.stderr)

    def bug(self, img):
        """Small rounded-square brand mark, top-right (accent asterisk)."""
        s = self.s
        x1, y1 = self.W - 110 * s, 70 * s
        d = ImageDraw.Draw(img)
        d.rounded_rectangle([x1, y1, x1 + 56 * s, y1 + 56 * s], radius=14 * s, fill=(20, 20, 22, 200),
                            outline=(255, 255, 255, 40))
        cx, cy = x1 + 28 * s, y1 + 28 * s
        for k in range(4):
            a = k * math.pi / 4
            d.line([(cx - 13 * s * math.cos(a), cy - 13 * s * math.sin(a)),
                    (cx + 13 * s * math.cos(a), cy + 13 * s * math.sin(a))],
                   fill=(*self.accent, 255), width=max(2, int(4 * s)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plan")
    ap.add_argument("--preview", action="store_true", help="half resolution, faster")
    ap.add_argument("--out")
    a = ap.parse_args()
    plan = json.load(open(a.plan, encoding="utf-8"))
    base = os.path.dirname(os.path.abspath(a.plan))
    r = Renderer(plan, base, a.preview)
    out = a.out or os.path.join(base, plan.get("out", "edit.mp4"))
    r.run(out)


if __name__ == "__main__":
    main()
