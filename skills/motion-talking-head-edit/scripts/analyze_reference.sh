#!/usr/bin/env bash
# Study a reference reel: metadata, cut list, silences, contact sheet, frames.
#   analyze_reference.sh <video-file-or-URL> [outdir]
# A URL is fetched with yt-dlp (pip install yt-dlp). Facebook/Instagram may
# need their CDN hosts allowed on the network.
set -euo pipefail
IN="$1"; OUT="${2:-ref_analysis}"; mkdir -p "$OUT"
if [[ "$IN" =~ ^https?:// ]]; then
  yt-dlp -q -o "$OUT/ref.%(ext)s" --write-info-json --merge-output-format mp4 "$IN"
  IN="$OUT/ref.mp4"
fi
ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate:format=duration \
  -of default=nw=1 "$IN" | tee "$OUT/probe.txt"
echo "--- hard cuts (scene > 0.25)"; ffmpeg -hide_banner -i "$IN" \
  -vf "select='gt(scene,0.25)',showinfo" -f null - 2>&1 | grep -o "pts_time:[0-9.]*" | tee "$OUT/cuts.txt" || true
echo "--- silences"; ffmpeg -hide_banner -i "$IN" -af silencedetect=n=-35dB:d=0.3 -f null - 2>&1 \
  | grep silence_ | tee "$OUT/silences.txt" || true
ffmpeg -hide_banner -loglevel error -i "$IN" -vf "fps=2,scale=180:-1,tile=7x6" -frames:v 1 -y "$OUT/contact_sheet.png"
mkdir -p "$OUT/frames"
ffmpeg -hide_banner -loglevel error -i "$IN" -vf "fps=2,scale=540:-1" -y "$OUT/frames/f_%03d.png"
echo "done → $OUT (read contact_sheet.png first; frames are every 0.5 s)"
