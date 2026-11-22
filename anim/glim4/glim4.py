"""Glim explains v4 – Renderer mit 60 fps, Markenschriften und Stil-Varianten.
Aufruf:  GLIM_FPS=60 GLIM_STYLE=night python3 glim4.py <topic> <tl.json> <frames_dir> [offset step]
Themen liegen als eigene Dateien in topics/<topic>.py (werden per exec geladen) und definieren
  SC(i, P, t, u)  – Illustration je Satz (i = Satz, u = Sekunden seit Satzbeginn)
  PAL = (oben, unten)  – Hintergrundverlauf,  HI = {Schlüsselwörter}
Stile: classic | night | sunny | paper.  Basiert auf glim3.py (Glim v3, Kinetic-Text, Weißblitze).
Neu in v4: FPS frei wählbar (Standard 60), Bricolage Grotesque/Manrope (Fallback DejaVu),
Stil-Varianten mit Schattenebene (paper/sunny), Sternenhimmel (night), Mythos-Stempel („MYTH“/„FACT“)."""
import json, math, os, random, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, S = 1080, 1920, 2
FPS = int(os.environ.get("GLIM_FPS", "60"))
STYLE = os.environ.get("GLIM_STYLE", "classic")
TOPIC, TL, OUT = sys.argv[1], json.load(open(sys.argv[2])), sys.argv[3]
os.makedirs(OUT, exist_ok=True)
L, DUR = TL["lines"], TL["total"]
T = [l["start"] for l in L]
NIGHT = (14, 26, 51); GLIM = (255, 194, 51); HOPE = (35, 193, 122); HOOK = (255, 91, 74); CLOUD = (246, 244, 238)

def _fontfile(name, fallback):
    for p in (os.path.join(HERE, "fonts", name), os.path.join(HERE, "..", "fonts", name)):
        if os.path.exists(p): return p
    return fallback
DEJ = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
F_HEAD = _fontfile("bricolage-grotesque-latin-800-normal.woff", DEJ)
F_BODY = _fontfile("manrope-latin-800-normal.woff", DEJ)
_F = {}
def font(px, kind="body"):
    px = max(4, int(px)); key = (px, kind)
    if key not in _F:
        if len(_F) > 10: _F.clear()   # Cache begrenzen: animierte Schriftgrößen ließen den Speicher sonst um GB wachsen (OOM)
        _F[key] = ImageFont.truetype(F_HEAD if kind == "head" else F_BODY, px)
    return _F[key]
def clamp(t, a=0., b=1.): return max(a, min(b, t))
def lerp(a, b, t): return a + (b - a) * t
def lc(c1, c2, t): t = clamp(t); return tuple(int(lerp(a, b, t)) for a, b in zip(c1, c2))
def eio(t): t = clamp(t); return t * t * (3 - 2 * t)
def eout(t): t = clamp(t); return 1 - (1 - t) ** 3
def back(t, c=2.2): t = clamp(t); return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2
def seg(t, a, b): return clamp((t - a) / (b - a))
def mul(c, k): return tuple(int(clamp(v * k / 255) * 255) for v in c)
def scene_of(t):
    i = 0
    for k, s in enumerate(T):
        if t >= s - 0.25: i = k
    return i

class Cam:
    def __init__(s, z=1., cx=W / 2, cy=H / 2): s.z, s.cx, s.cy = z, cx, cy
    def p(s, x, y): return (((x - s.cx) * s.z + W / 2) * S, ((y - s.cy) * s.z + H / 2) * S)
    def r(s, v): return v * s.z * S
class Pen:
    def __init__(s, d, g, cam): s.d, s.g, s.c = d, g, cam
    def ell(s, x, y, rx, ry, fill, glow=None, outline=None, w=0):
        X, Y = s.c.p(x, y); RX, RY = abs(s.c.r(rx)), abs(s.c.r(ry))
        if glow: s.g.ellipse([X - RX * 1.5, Y - RY * 1.5, X + RX * 1.5, Y + RY * 1.5], fill=glow)
        s.d.ellipse([X - RX, Y - RY, X + RX, Y + RY], fill=fill, outline=outline, width=int(s.c.r(w)) if w else 0)
    def circ(s, x, y, r, fill, glow=None, outline=None, w=0): s.ell(x, y, r, r, fill, glow, outline, w)
    def poly(s, pts, fill, outline=None, w=0):
        s.d.polygon([s.c.p(x, y) for x, y in pts], fill=fill, outline=outline, width=int(s.c.r(w)) if w else 0)
    def line(s, pts, col, w, glow=None):
        P = [s.c.p(x, y) for x, y in pts]
        if glow: s.g.line(P, fill=glow, width=int(s.c.r(w * 2.6)), joint="curve")
        s.d.line(P, fill=col, width=max(1, int(s.c.r(w))), joint="curve")
    def rrect(s, x0, y0, x1, y1, r, fill, outline=None, w=0):
        A, B = s.c.p(x0, y0), s.c.p(x1, y1)
        s.d.rounded_rectangle([min(A[0], B[0]), min(A[1], B[1]), max(A[0], B[0]), max(A[1], B[1])], int(s.c.r(r)), fill=fill, outline=outline, width=int(s.c.r(w)) if w else 0)
    def arc(s, x, y, r, a0, a1, col, w):
        X, Y = s.c.p(x, y); R = abs(s.c.r(r))
        s.d.arc([X - R, Y - R, X + R, Y + R], a0, a1, fill=col, width=max(1, int(s.c.r(w))))
    def text(s, x, y, txt, size, col, anchor="mm", kind="head"):
        if size < 3: return
        X, Y = s.c.p(x, y)
        s.d.text((X, Y), txt, font=font(s.c.r(size), kind), fill=col, anchor=anchor, stroke_width=int(s.c.r(6)), stroke_fill=NIGHT)
    def heart(s, x, y, r, col):
        s.circ(x - r * .5, y - r * .2, r * .55, col); s.circ(x + r * .5, y - r * .2, r * .55, col)
        s.poly([(x - r * 1.02, y - r * .05), (x + r * 1.02, y - r * .05), (x, y + r * 1.1)], col)
    def badge(s, x, y, txt, size, bg, fg=CLOUD, k=1.):
        """Abgerundetes Schild mit Text (k = Pop-Skalierung 0..1)."""
        if k <= .02: return
        f = font(s.c.r(size * k), "head"); w = s.d.textlength(txt, font=f) / S / s.c.z
        s.rrect(x - w / 2 - 34 * k, y - size * .78 * k, x + w / 2 + 34 * k, y + size * .78 * k, size * .5 * k, bg)
        X, Y = s.c.p(x, y); s.d.text((X, Y), txt, font=f, fill=fg, anchor="mm")
    def stamp(s, x, y, txt, k, col=HOOK, rot=-10):
        """Stempel „MYTH“/„FACT“ – fällt mit Overshoot ein."""
        if k <= .02: return
        size = 120 * (2.2 - 1.2 * eout(k))
        f = font(s.c.r(size), "head"); tw = s.d.textlength(txt, font=f)
        pad = s.c.r(30); bw, bh = int(tw + pad * 2), int(s.c.r(size) * 1.35)
        im = Image.new("RGBA", (bw, bh), (0, 0, 0, 0)); dd = ImageDraw.Draw(im)
        dd.rounded_rectangle([4, 4, bw - 4, bh - 4], int(s.c.r(22)), outline=col + (255,), width=int(s.c.r(12)))
        dd.text((bw / 2, bh / 2), txt, font=f, fill=col + (255,), anchor="mm")
        im = im.rotate(rot, expand=True, resample=Image.BICUBIC)
        a = int(255 * clamp(k * 3)); im.putalpha(im.getchannel("A").point(lambda v: v * a // 255))
        X, Y = s.c.p(x, y); s.layer.alpha_composite(im, (int(X - im.width / 2), int(Y - im.height / 2)))
    def cross(s, x, y, r, col=HOOK, k=1.):
        r *= k; s.line([(x - r, y - r), (x + r, y + r)], col, 26 * k); s.line([(x - r, y + r), (x + r, y - r)], col, 26 * k)
    def check(s, x, y, r, col=HOPE, k=1.):
        r *= k; s.line([(x - r, y), (x - r * .3, y + r * .7), (x + r, y - r * .8)], col, 26 * k)

def waves(P, x, y, t, col, n=3, r0=60, dr=55, speed=1.2, a0=-60, a1=60):
    for k in range(n):
        q = (t * speed + k / n) % 1
        P.arc(x, y, r0 + q * dr * n, a0, a1, lc(col, (0, 0, 0), q * .8), 10 * (1 - q) + 3)

# ---------- Glim v3 (unverändert, flüssiger durch 60 fps) ----------
def glim(P, x, y, sc, t, mood="happy", talk=0., wave=0., squash=0.):
    r = 95 * sc; rot = math.sin(t * 2.0) * .1
    sx, sy = 1 + squash * .22, 1 - squash * .22
    def pt(px, py):
        c, s_ = math.cos(rot), math.sin(rot)
        return (x + (px * c - py * s_) * sx, y + (px * s_ + py * c) * sy)
    def star(rr, inner=.56):
        return [pt(rr * (1 if i % 2 == 0 else inner) * math.cos(i * math.pi / 5 - math.pi / 2),
                   rr * (1 if i % 2 == 0 else inner) * math.sin(i * math.pi / 5 - math.pi / 2)) for i in range(10)]
    la = math.radians(200 + math.sin(t * 3) * 8); ra = math.radians(-35 - wave * (40 + 30 * math.sin(t * 12)))
    for a, side in ((la, -1), (ra, 1)):
        bx, by = pt(side * r * .55, r * .25)
        ex, ey = bx + math.cos(a) * r * .8, by + math.sin(a) * r * .8
        P.line([(bx, by), (ex, ey)], (214, 140, 20), r * .18)
        P.circ(ex, ey, r * .14, GLIM, outline=(170, 105, 15), w=4)
    P.g.polygon([P.c.p(*q) for q in star(r * 1.42)], fill=(120, 80, 10))
    P.poly(star(r * 1.36), (190, 120, 15))
    P.poly(star(r * 1.28), GLIM)
    P.poly([pt(px * .85, py * .85 - r * .05) for px, py in [(0, -r * 1.05), (r * .2, -r * .4), (-r * .2, -r * .4)]], (255, 226, 140))
    cx, cy = pt(0, r * .08)
    P.ell(cx, cy + r * .06, r * .62, r * .58, (255, 214, 100))
    blink = (t % 3.1) > 2.98
    for ex in (-.25, .25):
        exx, eyy = pt(ex * r, -r * .04)
        if mood == "joy" or blink:
            P.arc(exx, eyy + r * .04, r * .13, 200, 340, NIGHT, r * .06)
        else:
            h = r * (.19 if mood == "wow" else .15)
            P.ell(exx, eyy, r * .11 * (1.2 if mood == "wow" else 1), h, NIGHT)
            P.circ(exx + r * .04, eyy - h * .45, r * .045, (255, 255, 255))
    for ex in (-.45, .45):
        bx, by = pt(ex * r, r * .2); P.ell(bx, by, r * .1, r * .055, (255, 140, 100))
    mx, my = pt(0, r * .25); m = .05 + .14 * talk + (.1 if mood in ("wow", "joy") else 0)
    if mood == "wow": P.ell(mx, my + r * .05, r * .08, r * (.06 + m * .6), (140, 40, 40))
    else:
        X, Y = P.c.p(mx, my); R = P.c.r(r * .2)
        P.d.chord([X - R, Y - R * .4, X + R, Y + R * (.5 + m * 3)], 0, 180, fill=(140, 40, 40))

# ---------- Thema laden ----------
SC = None; PAL = ((30, 40, 80), (80, 110, 160)); HI = set(); WOW = (2,)
exec(open(os.path.join(HERE, "topics", f"{TOPIC}.py")).read(), globals())

def kinetic(d, t, line, y, size):
    words = line["text"].split(); n = len(words); a0 = line["start"]; span = line["dur"] * .85
    isk = lambda w: w.lower() in HI or w.strip(".,!?").lower() in HI
    f = font(size * S); fk = font(int(size * S * 1.12), "head")
    rows, cur, curw = [], [], 0
    for i, w in enumerate(words):
        ww = d.textlength(w + " ", font=fk if isk(w) else f) + size * S * .16
        if curw + ww > (W - 150) * S and cur: rows.append(cur); cur, curw = [], 0
        cur.append((i, w, ww)); curw += ww
    rows.append(cur)
    lh = size * 1.22 * S; y0 = y * S - (len(rows) - 1) * lh / 2
    fade = 1 - seg(t, a0 + line["dur"] + .15, a0 + line["dur"] + .45)
    for ri, row in enumerate(rows):
        x = (W * S - sum(r[2] for r in row) + d.textlength(" ", font=f)) / 2
        for i, w, ww in row:
            k = back((t - (a0 + span * i / n)) / .22)
            if k > .01 and fade > 0:
                key = isk(w); fs = int(size * S * (0.6 + .4 * k) * (1.12 if key else 1))
                col = lc(NIGHT, GLIM if key else CLOUD, fade)
                d.text((x, y0 + ri * lh + (1 - k) * 40 * S + (size * S * (1.12 if key else 1) - fs) * .5), w,
                       font=font(fs, "head" if key else "body"), fill=col, stroke_width=int(7 * S), stroke_fill=NIGHT)
            x += ww

# ---------- Stil-Hintergründe (vorberechnet) ----------
random.seed(3)
LIGHT = STYLE in ("sunny", "paper")
if STYLE == "night":
    TOP, BOT = lc((6, 10, 28), PAL[0], .35), lc((10, 16, 40), PAL[1], .45)
elif STYLE == "sunny":
    TOP, BOT = lc(PAL[0], (255, 246, 228), .62), lc(PAL[1], (255, 236, 214), .5)
elif STYLE == "paper":
    TOP, BOT = (243, 236, 222), lc((236, 226, 206), PAL[1], .12)
else:
    TOP, BOT = PAL
BG = Image.new("RGBA", (W * S, H * S)); bd = ImageDraw.Draw(BG)
for yy in range(0, H * S, 8): bd.rectangle([0, yy, W * S, yy + 8], fill=lc(TOP, BOT, yy / (H * S)))
if STYLE == "paper":   # Papierfasern + zwei farbige Papierbögen
    noise = Image.effect_noise((W // 2, H // 2), 22).resize((W * S, H * S), Image.BILINEAR).convert("RGBA")
    noise.putalpha(28); BG.alpha_composite(noise)
    bd.ellipse([-W * .5 * S, H * .78 * S, W * 1.5 * S, H * 1.6 * S], fill=lc(PAL[1], (240, 230, 210), .55))
    bd.ellipse([-W * .3 * S, -H * .25 * S, W * 1.3 * S, H * .12 * S], fill=lc(PAL[1], (240, 230, 210), .78))
if STYLE == "sunny":   # weiche Sonnenstrahlen oben rechts
    for k in range(12):
        a = k / 12 * 2 * math.pi
        bd.polygon([(W * .85 * S, H * .08 * S), (W * .85 * S + math.cos(a) * 2600 * S, H * .08 * S + math.sin(a) * 2600 * S),
                    (W * .85 * S + math.cos(a + .14) * 2600 * S, H * .08 * S + math.sin(a + .14) * 2600 * S)], fill=lc(TOP, (255, 255, 255), .25))
    BG = BG.filter(ImageFilter.GaussianBlur(6 * S))
STARS = [(random.random() * W, random.random() * H * .9, random.random() * 2.6 + 1, random.random() * 6.28) for _ in range(150 if STYLE == "night" else 60)]
VIG = Image.new("L", (W, H), 0); vd = ImageDraw.Draw(VIG)
for i in range(40): vd.ellipse([-W * .35 + i * 6, -H * .2 + i * 8, W * 1.35 - i * 6, H * 1.2 - i * 8], fill=int(i * 6.3))
VIG = VIG.filter(ImageFilter.GaussianBlur(60)).point(lambda v: min(255, (130 if STYLE == "night" else 160) + v)); DARK = Image.new("RGB", (W, H), (5, 8, 20))
GLOW_GAIN = {"night": .8, "classic": .5, "sunny": .25, "paper": .15}.get(STYLE, .5)

def frame(t):
    base = BG.copy(); lay = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0)); glow = Image.new("RGB", (W * S, H * S))
    d, g = ImageDraw.Draw(lay), ImageDraw.Draw(glow)
    i = scene_of(t); u = t - T[i]
    cam0 = Cam(); Pb = Pen(ImageDraw.Draw(base), g, cam0)
    for x, y, r, ph in STARS:
        tw = .5 + .5 * math.sin(t * 1.5 + ph)
        if STYLE == "night":
            Pb.circ(x, y, r * (.6 + .5 * tw), lc(TOP, (255, 250, 220), .35 + .65 * tw))
        elif STYLE == "classic":
            Pb.circ(x, (y - t * 20 * r) % H, r, lc(TOP, CLOUD, .25 * tw))
        else:
            Pb.circ(x, (y - t * 12 * r) % H, r * 1.6, lc(TOP, (255, 255, 255), .45 * tw))
    pop = back(seg(t, T[i] - .25, T[i] + .35)); z = (0.92 + .08 * pop) * (1 + .03 * math.sin(t * .6))
    P = Pen(d, g, Cam(z, W / 2, H / 2 + 40)); P.layer = lay
    SC(i, P, t, u)
    talking = 0
    for l in L:
        if l["start"] <= t < l["start"] + l["dur"]: talking = .5 + .5 * math.sin(t * 22)
    last = i == len(L) - 1
    mood = "joy" if last else ("wow" if i in WOW and u < 1.5 else "happy")
    gp = back(seg(t, .1, .6)); hop = abs(math.sin(t * 3)) * 22 if last else math.sin(t * 2.2) * 10
    Pg = Pen(d, g, cam0); Pg.layer = lay
    gx, gy, gs = (760, 1660, .8) if last else (900, 1700, .62)
    glim(Pg, gx, gy - hop, max(.02, gp) * gs, t, mood, talking, wave=1 if (last or t < 2) else 0, squash=max(0, 1 - gp) * .5)
    if LIGHT:   # weicher Schatten unter allen Figuren (Papier-/Sonnen-Look)
        sh = lay.getchannel("A").resize((W // 4, H // 4), Image.BILINEAR).filter(ImageFilter.GaussianBlur(4 if STYLE == "paper" else 7))
        sh = sh.point(lambda v: int(v * (.42 if STYLE == "paper" else .3))).resize((W * S, H * S), Image.BILINEAR)
        shadow = Image.new("RGBA", (W * S, H * S), (40, 30, 20, 0)); shadow.putalpha(sh)
        base.alpha_composite(shadow, (int(10 * S), int(14 * S)))
    base.alpha_composite(lay)
    td = ImageDraw.Draw(base)
    for k, l in enumerate(L):
        if l["start"] - .1 <= t < l["start"] + l["dur"] + .5: kinetic(td, t, l, 330 if k else 380, 86 if k == 0 else 64)
    end = seg(t, DUR - 1.7, DUR - 1.3)
    if end > 0:
        f = font(54 * S, "head"); s_ = "Follow for more WHY?"; w = td.textlength(s_, font=f); k = back(end)
        td.rounded_rectangle([(W * S - w) / 2 - 40 * S, (1540 - 50 * k) * S, (W * S + w) / 2 + 40 * S, (1540 + 50 * k) * S], 50 * S, fill=HOOK)
        if k > .5: td.text((W * S / 2, 1540 * S), s_, font=f, fill=CLOUD, anchor="mm")
    small = glow.point(lambda v: int(v * GLOW_GAIN)).resize((W // 4, H // 4), Image.BILINEAR).filter(ImageFilter.GaussianBlur(8))
    img = ImageChops.add(base.convert("RGB"), small.resize((W * S, H * S), Image.BILINEAR)).resize((W, H), Image.LANCZOS)
    fl = max([0] + [1 - abs(t - (s - .25)) / .16 for s in T[1:]])
    if fl > 0: img = Image.blend(img, Image.new("RGB", (W, H), (255, 255, 255)), clamp(fl) * (.35 if LIGHT else .55))
    return img if LIGHT else Image.composite(img, DARK, VIG)

if __name__ == "__main__":
    off = int(sys.argv[4]) if len(sys.argv) > 4 else 0; step = int(sys.argv[5]) if len(sys.argv) > 5 else 1
    only = os.environ.get("GLIM_ONLY")   # Testframes: Liste von Sekunden, z. B. "1,6,12"
    if only:
        for s in only.split(","): frame(float(s)).save(f"{OUT}/t{float(s):05.1f}.png")
    else:
        a = int(os.environ.get("GLIM_FROM", 0)); b = int(os.environ.get("GLIM_TO", int(DUR * FPS)))   # Teilbereich nachrendern
        for fi in range(a + off, b, step): frame(fi / FPS).save(f"{OUT}/f{fi:05d}.png")
