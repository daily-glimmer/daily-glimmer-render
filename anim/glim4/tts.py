"""Sprechertext -> Piper-WAVs + tl.json.   python3 tts.py <topic> [stamp_lines] [pause]
Liest <topic>/lines.txt (6 Zeilen Englisch). stamp_lines z. B. "1" -> Stempel-Sound 0,35 s nach Beginn von Satz 1.
Timing wie glim3: erster Satz bei 0,4 s, Abstand = pause (Standard 0,5 s), total = Ende + 1,8 s."""
import json, subprocess, sys, wave, os
k = sys.argv[1]; stamps = [int(x) for x in sys.argv[2].split(",")] if len(sys.argv) > 2 and sys.argv[2] else []
pause = float(sys.argv[3]) if len(sys.argv) > 3 else .5
V = os.path.join(os.path.dirname(os.path.abspath(__file__)), "voice", "ljs.onnx")
lines = [l.strip() for l in open(f"{k}/lines.txt") if l.strip()]
out, t = [], .4
for i, txt in enumerate(lines):
    subprocess.run(["python3", "-m", "piper", "-m", V, "-f", f"{k}/l{i}.wav", "--length-scale", "1.0", "--sentence-silence", "0.1"],
                   input=txt.encode(), check=True, capture_output=True)
    w = wave.open(f"{k}/l{i}.wav"); d = w.getnframes() / w.getframerate(); w.close()
    out.append({"start": round(t, 3), "dur": round(d, 3), "text": txt}); t += d + pause
total = round(out[-1]["start"] + out[-1]["dur"] + 1.8, 3)
json.dump({"lines": out, "total": total, "stamps": [out[i]["start"] + .35 for i in stamps]}, open(f"{k}/tl.json", "w"), indent=1)
print(k, "total", total, "chars", sum(len(l) for l in lines))
