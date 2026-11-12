#!/usr/bin/env python3
"""Make a person matte video (white = speaker, black = background).

The matte lets render.py place big keywords BEHIND the speaker
("text-behind-subject" depth effect).

    python3 segment.py talking_head.mp4 matte.mp4 [--model selfie_segmenter.tflite]

Needs: pip install mediapipe numpy ; ffmpeg on PATH.
The model downloads automatically on first run (~250 KB) from
storage.googleapis.com if --model is not given.
"""
import argparse, json, os, subprocess, sys, urllib.request
import numpy as np

MODEL_URL = ("https://storage.googleapis.com/mediapipe-models/image_segmenter/"
             "selfie_segmenter/float16/latest/selfie_segmenter.tflite")


def probe(path):
    out = subprocess.check_output([
        "ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
        "stream=width,height,r_frame_rate", "-of", "json", path])
    s = json.loads(out)["streams"][0]
    n, d = s["r_frame_rate"].split("/")
    return s["width"], s["height"], float(n) / float(d)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("out")
    ap.add_argument("--model", default=None)
    ap.add_argument("--smooth", type=float, default=0.6,
                    help="temporal smoothing 0..0.95 (higher = steadier edge)")
    a = ap.parse_args()

    model = a.model or os.path.join(os.path.dirname(os.path.abspath(a.out)), "selfie_segmenter.tflite")
    if not os.path.exists(model):
        print("downloading segmentation model ->", model, file=sys.stderr)
        urllib.request.urlretrieve(MODEL_URL, model)

    import mediapipe as mp
    from mediapipe.tasks import python as mpt
    from mediapipe.tasks.python import vision

    seg = vision.ImageSegmenter.create_from_options(vision.ImageSegmenterOptions(
        base_options=mpt.BaseOptions(model_asset_path=model),
        running_mode=vision.RunningMode.VIDEO,
        output_confidence_masks=True))

    w, h, fps = probe(a.src)
    dec = subprocess.Popen(["ffmpeg", "-v", "error", "-i", a.src, "-f", "rawvideo",
                            "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "gray",
                            "-s", f"{w}x{h}", "-r", str(fps), "-i", "-",
                            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "12", a.out],
                           stdin=subprocess.PIPE)
    prev, i, fsz = None, 0, w * h * 3
    while True:
        buf = dec.stdout.read(fsz)
        if len(buf) < fsz:
            break
        frame = np.frombuffer(buf, np.uint8).reshape(h, w, 3)
        res = seg.segment_for_video(mp.Image(image_format=mp.ImageFormat.SRGB, data=frame),
                                    int(i * 1000 / fps))
        conf = np.squeeze(res.confidence_masks[-1].numpy_view()).astype(np.float32)  # person prob
        if conf.shape != (h, w):
            from PIL import Image
            conf = np.array(Image.fromarray((conf * 255).astype(np.uint8), "L")
                            .resize((w, h), Image.BILINEAR), np.float32) / 255
        prev = conf if prev is None else a.smooth * prev + (1 - a.smooth) * conf
        # soft but tight edge
        m = np.clip((prev - 0.35) / 0.3, 0, 1)
        enc.stdin.write((m * 255).astype(np.uint8).tobytes())
        i += 1
    seg.close()
    enc.stdin.close(); enc.wait(); dec.wait()
    print(f"matte: {i} frames -> {a.out}")


if __name__ == "__main__":
    main()
