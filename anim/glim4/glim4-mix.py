"""Ton + Encode für Glim v4:  python3 glim4-mix.py <topicdir> <musik.wav> <startsekunde> [fps]
Wie glim3-mix.py (Soundeffekte, Stimme, Musik 0.45 mit Ducking, loudnorm -14 LUFS), aber fps frei
(Standard 60) und Frames im Format f%05d.png. Ergebnis: glim_<topic>.mp4 (1080x1920, libx264 slow crf 18)."""
import json, sys, subprocess, numpy as np, wave, os
k, music, mstart = sys.argv[1], sys.argv[2], sys.argv[3]
fps = sys.argv[4] if len(sys.argv) > 4 else "60"
tl = json.load(open(f"{k}/tl.json")); SR = 44100; D = tl["total"]; N = int(D * SR); T = [l["start"] for l in tl["lines"]]
rng = np.random.default_rng(len(k)); sfx = np.zeros(N)
def add(sig, t, g):
    i = int(t * SR); j = min(N, i + len(sig))
    if j > i: sfx[i:j] += sig[:j - i] * g
def env(n, a, r): t = np.arange(n) / SR; return np.minimum(1, t / a) * np.exp(-t / r)
def whoosh(d=.6):
    n = int(d * SR); x = rng.standard_normal(n); t = np.arange(n) / n
    return (np.convolve(x, np.ones(25) / 25, 'same') - np.convolve(x, np.ones(220) / 220, 'same')) * np.sin(np.pi * t) ** 2 * 3
def tone(f, d, a=.003, r=.1, sweep=0):
    n = int(d * SR); t = np.arange(n) / SR; fr = f * (1 + sweep * np.exp(-t * 30))
    return np.sin(2 * np.pi * np.cumsum(fr) / SR) * env(n, a, r)
def thud():   # Stempel-Aufprall für MYTH/FACT
    n = int(.35 * SR); t = np.arange(n) / SR
    return (np.sin(2 * np.pi * 70 * t) * np.exp(-t * 14) + rng.standard_normal(n) * np.exp(-t * 60) * .3)
add(tone(480, .2, r=.05, sweep=2), .12, .45)
for s in T[1:]: add(whoosh(), s - .45, .3); add(tone(1400, .4, r=.08), s - .2, .1)
for st in tl.get("stamps", []): add(thud(), st, .55)
for j, f in enumerate([1568, 2093, 2637, 3136]): add(tone(f, .6, r=.12), T[-1] + .3 + j * .09, .16)
add(tone(600, .2, r=.05, sweep=2), D - 1.65, .35)
w = wave.open(f"{k}/sfx.wav", "wb"); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((np.clip(sfx, -1, 1) * .8 * 32767).astype(np.int16).tobytes()); w.close()
ins = []; fc = []
for i, l in enumerate(tl["lines"]):
    ins += ["-i", f"{k}/l{i}.wav"]; ms = int(l["start"] * 1000); fc.append(f"[{i}:a]aresample=44100,adelay={ms}|{ms},apad[v{i}]")
n = len(tl["lines"])
fc.append("".join(f"[v{i}]" for i in range(n)) + f"amix=inputs={n}:normalize=0,atrim=0:{D},highpass=f=70,acompressor=threshold=-18dB:ratio=3,volume=1.6,asplit=2[vo][sc]")
fc.append(f"[{n}:a]atrim=0:{D},afade=t=in:d=0.5,afade=t=out:st={D-1.2}:d=1.2,volume=0.45[m]")
fc.append("[m][sc]sidechaincompress=threshold=0.03:ratio=6:release=300[md]")
fc.append(f"[vo][md][{n+1}:a]amix=inputs=3:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]")
subprocess.run(["ffmpeg", "-y", "-loglevel", "error"] + ins + ["-ss", mstart, "-i", music, "-i", f"{k}/sfx.wav",
    "-filter_complex", ";".join(fc), "-map", "[a]", "-ar", "44100", "-ac", "2", f"{k}/mix.wav"], check=True)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", fps, "-i", f"{k}/frames/f%05d.png", "-i", f"{k}/mix.wav",
    "-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p", "-r", fps, "-c:a", "aac", "-b:a", "192k",
    "-movflags", "+faststart", "-shortest", f"glim_{os.path.basename(k.rstrip('/'))}.mp4"], check=True)
print(k, "ok")
