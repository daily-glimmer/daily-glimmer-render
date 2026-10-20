#!/usr/bin/env python3
"""Daily Glimmer – weekly long video renderer.
Reads a manifest JSON, downloads each clip, places vertical clips on a blurred 16:9
background, concatenates everything and writes out.mp4 + chapters.txt."""
import json, subprocess, sys, urllib.request, pathlib

W, H, FPS = 1920, 1080, 30

def run(cmd):
    print("+", " ".join(cmd), flush=True)
    subprocess.run(cmd, check=True)

def duration(path):
    out = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                   "-of", "default=nw=1:nk=1", str(path)])
    return float(out.strip())

def has_audio(path):
    out = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "a",
                                   "-show_entries", "stream=index", "-of", "csv=p=0", str(path)])
    return bool(out.strip())

def fmt(t):
    t = int(round(t))
    return f"{t//3600}:{t%3600//60:02d}:{t%60:02d}" if t >= 3600 else f"{t//60}:{t%60:02d}"

def main(manifest_path, workdir="work"):
    m = json.loads(pathlib.Path(manifest_path).read_text())
    wd = pathlib.Path(workdir); wd.mkdir(exist_ok=True)
    parts, chapters, t = [], [], 0.0
    for i, seg in enumerate(m["segments"]):
        src = wd / f"src_{i:02d}.mp4"
        if seg["url"].startswith("http"):
            req = urllib.request.Request(seg["url"], headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req) as r, open(src, "wb") as f:
                f.write(r.read())
        else:
            src = pathlib.Path(seg["url"])
        dst = wd / f"part_{i:02d}.mp4"
        vf = (f"[0:v]split=2[a][b];"
              f"[a]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=30:5,eq=brightness=-0.08[bg];"
              f"[b]scale={W}:{H}:force_original_aspect_ratio=decrease[fg];"
              f"[bg][fg]overlay=(W-w)/2:(H-h)/2,fps={FPS},format=yuv420p[v]")
        cmd = ["ffmpeg", "-y", "-i", str(src)]
        if not has_audio(src):
            cmd += ["-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo"]
        cmd += ["-filter_complex", vf, "-map", "[v]", "-map", "0:a" if has_audio(src) else "1:a",
                "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
                "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2", "-shortest", str(dst)]
        run(cmd)
        chapters.append(f"{fmt(t)} {seg.get('title', f'Part {i+1}')}")
        t += duration(dst)
        parts.append(dst)
    lst = wd / "list.txt"
    lst.write_text("".join(f"file '{p.resolve()}'\n" for p in parts))
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy",
         "-movflags", "+faststart", "out.mp4"])
    pathlib.Path("chapters.txt").write_text("\n".join(chapters) + "\n")
    print(f"done: {fmt(t)} total, {len(parts)} parts")

if __name__ == "__main__":
    main(sys.argv[1])
