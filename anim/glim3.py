"""Glim explains v3.1 – Themen-Renderer (Natur & Tiere). Aufruf:
FPS=60 STYLE=classic python3 glim3.py <topic> <tl.json> <frames_dir> [offset step]
Themen: cats, bees, beavers, flamingos, turtles, octopuses, whales, migration, zebras, fireflies. Neue Themen: Szenenfunktion sc_<thema> + SCENES/PAL/HI.
v3.1 (Nachtlauf 14./15.11.): FPS per Umgebungsvariable (Standard 60), STYLE = classic | paper | night | sunny,
Glim mit weichem Blinzeln, Atmen, Blickrichtung und Funkeln beim Jubeln; weiche (geglättete) Weißblitz-Übergänge.
Testframe-Nummern beziehen sich auf FPS (bei 60 fps: Sekunde x 60)."""
import json, math, os, random, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

W, H, S = 1080, 1920, 2
FPS = int(os.environ.get("FPS", "60"))
STYLE = os.environ.get("STYLE", "classic")
TOPIC, TL, OUT = sys.argv[1], json.load(open(sys.argv[2])), sys.argv[3]
os.makedirs(OUT, exist_ok=True)
L, DUR = TL["lines"], TL["total"]
T = [l["start"] for l in L]
NIGHT = (14, 26, 51); GLIM = (255, 194, 51); HOPE = (35, 193, 122); HOOK = (255, 91, 74); CLOUD = (246, 244, 238)
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
_F = {}
def font(px):
    px = max(1, int(px))
    if px not in _F: _F[px] = ImageFont.truetype(FB, px)
    return _F[px]
def clamp(t, a=0., b=1.): return max(a, min(b, t))
def lerp(a, b, t): return a + (b - a) * t
def lc(c1, c2, t): t = clamp(t); return tuple(int(lerp(a, b, t)) for a, b in zip(c1, c2))
def eio(t): t = clamp(t); return t * t * (3 - 2 * t)
def eout(t): t = clamp(t); return 1 - (1 - t) ** 3
def back(t, c=2.2): t = clamp(t); return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2
def seg(t, a, b): return clamp((t - a) / (b - a))
def mul(c, k): return tuple(int(clamp(v * k / 255) * 255) for v in c)
def hsv(h, s=.8, v=1.):
    i = int(h * 6) % 6; f = h * 6 - int(h * 6); p, q, r = v * (1 - s), v * (1 - s * f), v * (1 - s * (1 - f))
    return tuple(int(c * 255) for c in [(v, r, p), (q, v, p), (p, v, r), (p, q, v), (r, p, v), (v, p, q)][i])
def scene_of(t):
    i = 0
    for k, s in enumerate(T):
        if t >= s - 0.25: i = k
    return i

# ---------- Zeichen-Helfer (Design-Koordinaten 1080x1920, Kamera mit Zoom) ----------
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
        s.d.rounded_rectangle([A[0], A[1], B[0], B[1]], int(s.c.r(r)), fill=fill, outline=outline, width=int(s.c.r(w)) if w else 0)
    def arc(s, x, y, r, a0, a1, col, w):
        X, Y = s.c.p(x, y); R = s.c.r(r)
        s.d.arc([X - R, Y - R, X + R, Y + R], a0, a1, fill=col, width=max(1, int(s.c.r(w))))
    def text(s, x, y, txt, size, col, anchor="mm"):
        X, Y = s.c.p(x, y)
        s.d.text((X, Y), txt, font=font(s.c.r(size)), fill=col, anchor=anchor, stroke_width=int(s.c.r(6)), stroke_fill=NIGHT)
    def heart(s, x, y, r, col):
        s.circ(x - r * .5, y - r * .2, r * .55, col); s.circ(x + r * .5, y - r * .2, r * .55, col)
        s.poly([(x - r * 1.02, y - r * .05), (x + r * 1.02, y - r * .05), (x, y + r * 1.1)], col)
    def twinkle(s, x, y, r, col):
        s.poly([(x, y - r), (x + r * .25, y - r * .25), (x + r, y), (x + r * .25, y + r * .25), (x, y + r), (x - r * .25, y + r * .25), (x - r, y), (x - r * .25, y - r * .25)], col)

def waves(P, x, y, t, col, n=3, r0=60, dr=55, speed=1.2, a0=-60, a1=60):
    for k in range(n):
        q = (t * speed + k / n) % 1
        P.arc(x, y, r0 + q * dr * n, a0, a1, lc(col, (0, 0, 0), q * .8), 10 * (1 - q) + 3)

# ---------- Glim v3.1: Kontur, Ärmchen, Winken, Stimmungen, weiches Blinzeln ----------
def glim(P, x, y, sc, t, mood="happy", talk=0., wave=0., squash=0.):
    sc *= 1 + .025 * math.sin(t * 2.4)                       # Atmen
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
    P.poly(star(r * 1.36), (190, 120, 15))                     # Kontur
    P.poly(star(r * 1.28), GLIM)
    P.poly([pt(px * .85, py * .85 - r * .05) for px, py in [(0, -r * 1.05), (r * .2, -r * .4), (-r * .2, -r * .4)]], (255, 226, 140))  # Glanz
    cx, cy = pt(0, r * .08)
    P.ell(cx, cy + r * .06, r * .62, r * .58, (255, 214, 100))
    bp = (t % 3.3) - 3.12; close = math.sin(math.pi * clamp(bp / .18)) if bp > 0 else 0   # weiches Blinzeln
    look = math.sin(t * .7) * .03 * r
    for ex in (-.25, .25):
        exx, eyy = pt(ex * r, -r * .04)
        if mood == "joy" or close > .75:
            P.arc(exx, eyy + r * .04, r * .13, 200, 340, NIGHT, r * .06)
        else:
            h = r * (.19 if mood == "wow" else .15) * (1 - close)
            P.ell(exx + look, eyy, r * .11 * (1.2 if mood == "wow" else 1), max(h, r * .02), NIGHT)
            if close < .3: P.circ(exx + look + r * .04, eyy - h * .45, r * .045, (255, 255, 255))
    for ex in (-.45, .45):
        bx, by = pt(ex * r, r * .2); P.ell(bx, by, r * .1, r * .055, (255, 140, 100))
    mx, my = pt(0, r * .25); m = .05 + .14 * talk + (.1 if mood in ("wow", "joy") else 0)
    if mood == "wow": P.ell(mx, my + r * .05, r * .08, r * (.06 + m * .6), (140, 40, 40))
    else:
        X, Y = P.c.p(mx, my); R = P.c.r(r * .2)
        P.d.chord([X - R, Y - R * .4, X + R, Y + R * (.5 + m * 3)], 0, 180, fill=(140, 40, 40))
    if mood == "joy":
        for k in range(4):
            q = (t * .8 + k / 4) % 1; a = k * 1.6 + 0.6
            P.twinkle(x + math.cos(a) * r * (1.6 + q * .6), y + math.sin(a) * r * (1.6 + q * .6) - r * .3, r * .16 * math.sin(math.pi * q), (255, 240, 170))

# ---------- Tiere ----------
def cat(P, x, y, s, t, eyes="closed", tail=True, col=(244, 160, 80), stripe=(214, 120, 50)):
    if tail:
        tw = math.sin(t * 2) * 25 * s
        P.line([(x + 110 * s, y + 120 * s), (x + 190 * s, y + 60 * s + tw), (x + 200 * s, y - 40 * s + tw)], col, 34 * s)
    P.ell(x, y + 110 * s, 140 * s, 130 * s, col)
    P.ell(x, y + 160 * s, 90 * s, 70 * s, (252, 220, 180))
    for dx in (-60, 60): P.ell(x + dx * s, y + 225 * s, 40 * s, 24 * s, col)
    P.poly([(x - 120 * s, y - 70 * s), (x - 105 * s, y - 190 * s), (x - 30 * s, y - 120 * s)], col)
    P.poly([(x + 120 * s, y - 70 * s), (x + 105 * s, y - 190 * s), (x + 30 * s, y - 120 * s)], col)
    P.poly([(x - 100 * s, y - 95 * s), (x - 98 * s, y - 160 * s), (x - 55 * s, y - 120 * s)], (250, 170, 170))
    P.poly([(x + 100 * s, y - 95 * s), (x + 98 * s, y - 160 * s), (x + 55 * s, y - 120 * s)], (250, 170, 170))
    P.ell(x, y - 40 * s, 135 * s, 115 * s, col)
    for dx in (-40, 0, 40): P.line([(x + dx * s, y - 150 * s), (x + dx * s * .8, y - 115 * s)], stripe, 12 * s)
    for ex in (-48, 48):
        if eyes == "closed": P.arc(x + ex * s, y - 45 * s, 24 * s, 200, 340, NIGHT, 9 * s)
        else:
            P.ell(x + ex * s, y - 45 * s, 20 * s, 26 * s, NIGHT); P.circ(x + ex * s + 7 * s, y - 55 * s, 7 * s, (255, 255, 255))
    P.poly([(x - 13 * s, y - 10 * s), (x + 13 * s, y - 10 * s), (x, y + 4 * s)], (240, 110, 120))
    P.arc(x - 14 * s, y + 4 * s, 14 * s, 20, 160, NIGHT, 6 * s); P.arc(x + 14 * s, y + 4 * s, 14 * s, 20, 160, NIGHT, 6 * s)
    for side in (-1, 1):
        for k in (-1, 0, 1):
            P.line([(x + side * 45 * s, y + 5 * s + k * 12 * s), (x + side * 150 * s, y - 5 * s + k * 26 * s)], (255, 245, 230), 4 * s)

def bee(P, x, y, s, t, flap=True, glow_belly=0.):
    wa = math.sin(t * 40) if flap else 0.3
    for dx in (-1, 1):
        P.ell(x + dx * 30 * s, y - 55 * s - wa * 8 * s, 42 * s, 60 * s * (0.6 + .4 * abs(wa)), (220, 240, 255), outline=(150, 190, 230), w=3)
    if glow_belly: P.ell(x + 20 * s, y + 5 * s, 70 * s, 50 * s, (255, 200, 60), glow=mul((255, 190, 40), 200 * glow_belly))
    P.ell(x, y, 80 * s, 55 * s, (255, 200, 40), outline=NIGHT, w=5)
    for dx in (-25, 10, 45): P.line([(x + dx * s, y - 50 * s), (x + dx * s, y + 50 * s)], NIGHT, 16 * s)
    P.circ(x - 80 * s, y - 5 * s, 38 * s, (40, 40, 60))
    P.circ(x - 92 * s, y - 15 * s, 9 * s, (255, 255, 255))
    P.line([(x - 95 * s, y - 38 * s), (x - 115 * s, y - 80 * s)], NIGHT, 5 * s); P.circ(x - 115 * s, y - 80 * s, 7 * s, NIGHT)
    P.poly([(x + 78 * s, y - 8 * s), (x + 110 * s, y), (x + 78 * s, y + 8 * s)], NIGHT)

def flower(P, x, y, s, t, col=(255, 110, 160)):
    P.line([(x, y), (x + math.sin(t) * 6 * s, y + 260 * s)], (60, 160, 80), 14 * s)
    P.ell(x + 40 * s, y + 150 * s, 50 * s, 18 * s, (60, 170, 90))
    for k in range(6):
        a = k / 6 * 2 * math.pi + t * .3
        P.ell(x + math.cos(a) * 55 * s, y + math.sin(a) * 55 * s, 42 * s, 42 * s, col)
    P.circ(x, y, 38 * s, (255, 210, 60))

def hexcell(P, x, y, r, fill, outline=(200, 130, 20)):
    P.poly([(x + r * math.cos(math.pi / 3 * k + math.pi / 6), y + r * math.sin(math.pi / 3 * k + math.pi / 6)) for k in range(6)], fill, outline, 5)

def beaver(P, x, y, s, t, stick=False, swim=False, flip=1):
    f = flip
    P.ell(x + f * 150 * s, y + 40 * s, 95 * s, 38 * s, (90, 70, 60))
    for k in range(3): P.line([(x + f * (100 + k * 35) * s, y + 15 * s), (x + f * (100 + k * 35) * s, y + 65 * s)], (70, 55, 50), 4 * s)
    P.ell(x, y, 140 * s, 95 * s, (150, 95, 55))
    P.ell(x - f * 120 * s, y - 40 * s, 80 * s, 70 * s, (160, 105, 62))
    P.circ(x - f * 95 * s, y - 100 * s, 18 * s, (130, 85, 50))
    P.ell(x - f * 185 * s, y - 25 * s, 30 * s, 24 * s, (190, 140, 100))
    P.circ(x - f * 205 * s, y - 35 * s, 10 * s, NIGHT)
    P.rrect(x - f * 190 * s - 9 * s, y - 8 * s, x - f * 190 * s + 9 * s, y + 18 * s, 3 * s, (255, 150, 60))
    P.circ(x - f * 135 * s, y - 60 * s, 11 * s, NIGHT); P.circ(x - f * 131 * s, y - 64 * s, 4 * s, (255, 255, 255))
    if not swim:
        for dx in (-50, 50): P.ell(x + dx * s, y + 85 * s, 30 * s, 18 * s, (120, 75, 45))
    if stick:
        P.line([(x - f * 280 * s, y - 10 * s), (x - f * 100 * s, y + 10 * s)], (120, 80, 40), 16 * s)
        P.ell(x - f * 270 * s, y - 25 * s, 22 * s, 12 * s, (80, 170, 80))

def log(P, x0, y0, x1, y1, w):
    P.line([(x0, y0), (x1, y1)], (125, 85, 45), w); P.circ(x1, y1, w * .5, (175, 130, 80), outline=(125, 85, 45), w=3)

def fish(P, x, y, s, col):
    P.ell(x, y, 50 * s, 26 * s, col); P.poly([(x + 45 * s, y), (x + 80 * s, y - 25 * s), (x + 80 * s, y + 25 * s)], col)
    P.circ(x - 25 * s, y - 6 * s, 6 * s, NIGHT)

def frog(P, x, y, s):
    P.ell(x, y, 60 * s, 40 * s, (90, 190, 80))
    for dx in (-28, 28): P.circ(x + dx * s, y - 38 * s, 18 * s, (90, 190, 80)); P.circ(x + dx * s, y - 40 * s, 8 * s, NIGHT)
    P.arc(x, y - 5 * s, 30 * s, 20, 160, (30, 90, 40), 5 * s)

def bird(P, x, y, s, t):
    fl = math.sin(t * 8) * 25 * s
    P.line([(x - 60 * s, y - fl), (x, y), (x + 60 * s, y - fl)], (250, 250, 250), 10 * s)

def wolf(P, x, y, s):
    col = (95, 100, 115)
    P.ell(x, y, 120 * s, 60 * s, col); P.ell(x - 120 * s, y - 50 * s, 55 * s, 45 * s, col)
    P.poly([(x - 160 * s, y - 45 * s), (x - 230 * s, y - 25 * s), (x - 160 * s, y - 15 * s)], col)
    P.poly([(x - 140 * s, y - 85 * s), (x - 125 * s, y - 135 * s), (x - 105 * s, y - 85 * s)], col)
    for dx in (-80, -40, 50, 90): P.line([(x + dx * s, y + 30 * s), (x + dx * s, y + 110 * s)], col, 18 * s)
    P.line([(x + 110 * s, y - 10 * s), (x + 190 * s, y - 50 * s)], col, 22 * s)
    P.circ(x - 130 * s, y - 55 * s, 7 * s, (255, 220, 120))

# ---------- Szenen (jede bekommt lokale Zeit u ab Satzbeginn und Fortschritt) ----------
CENTER = 1050
def sc_cats(i, P, t, u):
    if i == 0:
        cat(P, 540, CENTER, 1.5, t); waves(P, 540, CENTER + 120, t, (255, 200, 120), r0=260, dr=60, a0=-30, a1=30)
        waves(P, 540, CENTER + 120, t, (255, 200, 120), r0=260, dr=60, a0=150, a1=210)
        P.text(540, CENTER + 470, "purrrr...", 70, GLIM)
    elif i == 1:
        cat(P, 540, CENTER - 60, 1.2, t)
        P.ell(540, CENTER + 120, 70, 45, (255, 120, 120), glow=mul(HOOK, 180))
        pts = [(220 + k * 8, CENTER + 330 + math.sin(k * .55 - t * 25) * 38 * eout(u * 2)) for k in range(81)]
        P.line(pts, GLIM, 9, glow=mul(GLIM, 200))
        k = back(seg(u, .4, .9))
        if k > 0: P.text(540, CENTER + 470, "20–30 x per second", 62 * k, CLOUD)
    elif i == 2:
        k = eout(u * 1.3)
        for side in (-1, 1):
            P.rrect(540 + side * (40 + 140 * (1 - k * .2)) - 110, CENTER - 160, 540 + side * (40 + 140 * (1 - k * .2)) + 110, CENTER + 160, 80, (230, 120, 130))
        P.ell(540 - 140, CENTER, 45, 120 * k, GLIM, glow=mul(GLIM, 220)); P.ell(540 + 140, CENTER, 45, 120 * k, GLIM, glow=mul(GLIM, 220))
        P.text(540, CENTER - 260, "vocal folds", 52, CLOUD); P.text(540, CENTER + 260, "special pad", 60, GLIM)
        waves(P, 540, CENTER, t, (255, 220, 160), r0=260, dr=60, a0=-30, a1=30, speed=1.8)
        waves(P, 540, CENTER, t, (255, 220, 160), r0=260, dr=60, a0=150, a1=210, speed=1.8)
    elif i == 3:
        cat(P, 420, CENTER, 1.15, t, col=(200, 200, 210), stripe=(150, 150, 165))
        cat(P, 720, CENTER + 170, .6 * back(u / .6), t, eyes="closed", tail=False, col=(250, 190, 120), stripe=(220, 150, 80))
        for k in range(4):
            q = (u * .6 + k / 4) % 1
            P.heart(600 + math.sin(k * 2 + t) * 60, CENTER - 100 - q * 300, 26, lc((255, 120, 150), (40, 40, 80), q))
        P.text(540, CENTER + 470, "a few days old", 62, GLIM)
    elif i == 4:
        cat(P, 540, CENTER, 1.3, t)
        P.rrect(600, CENTER + 60, 690, CENTER + 95, 12, (255, 235, 200), outline=(220, 180, 140), w=3)
        for k in range(3):
            q = (t * .5 + k / 3) % 1
            P.arc(540, CENTER + 60, 280 + q * 260, 200, 340, lc(HOPE, (0, 0, 0), q), 9 * (1 - q) + 3)
        P.text(540, CENTER + 470, "self-soothing?", 62, HOPE)
    else:
        cat(P, 420, CENTER + 40, 1.0, t, eyes="open")
        P.text(540, CENTER - 300, "LOUD or soft?", 84, GLIM)

def sc_bees(i, P, t, u):
    if i == 0:
        P.rrect(380, CENTER + 60, 700, CENTER + 420, 60, (255, 190, 60), outline=(200, 130, 20), w=8)
        P.rrect(400, CENTER + 20, 680, CENTER + 90, 25, (180, 120, 60))
        P.text(540, CENTER + 260, "HONEY", 70, (140, 80, 10))
        bx = 540 + math.sin(t * 1.4) * 260; by = CENTER - 200 + math.sin(t * 2.8) * 80
        bee(P, bx, by, 1.2, t)
    elif i == 1:
        flower(P, 360, CENTER - 40, 1.4, t)
        bk = eout(u / 1.2); bx = lerp(900, 520, bk); by = CENTER - 160
        bee(P, bx, by, 1.15, t, glow_belly=seg(u, 1.5, 3.5))
        if 1.0 < u < 4:
            for k in range(3):
                q = ((u - 1) * .8 + k / 3) % 1
                P.circ(lerp(380, bx + 20, q), lerp(CENTER - 40, by + 10, q), 14, (255, 220, 120), glow=mul(GLIM, 200))
        P.text(540, CENTER + 470, "honey stomach", 62, GLIM)
    elif i == 2:
        for k in range(3): bee(P, 230 + k * 310, CENTER + (k % 2) * 60, .95, t + k)
        q = (u * .7) % 1; seg_i = int(u * .7 * 2) % 2
        x0 = 230 + seg_i * 310; P.circ(lerp(x0 + 60, x0 + 250, q), CENTER - 40 + (seg_i % 2) * 60 * q, 18, (255, 200, 80), glow=mul(GLIM, 230))
        for k in range(10):
            a = k * 1.7 + t * 2; P.text(540 + math.cos(a) * 380, CENTER - 300 + math.sin(a * 1.3) * 60, "✦", 34, (190, 230, 255))
        P.text(540, CENTER + 470, "+ enzymes", 66, (190, 230, 255))
    elif i == 3:
        for r_ in range(3):
            for c_ in range(4):
                x = 270 + c_ * 180 + (r_ % 2) * 90; y = CENTER + 80 + r_ * 156
                fillk = eout(u / 3)
                hexcell(P, x, y, 95, lc((255, 230, 150), (240, 160, 30), fillk))
        bee(P, 540, CENTER - 260, 1.3, t * 2)
        for k in range(5):
            q = (t * 1.5 + k / 5) % 1
            P.line([(330 + k * 100, CENTER - 120 + q * 120), (360 + k * 100, CENTER - 80 + q * 120)], lc((220, 240, 255), (40, 60, 100), q), 8)
        P.text(540, CENTER + 560, "thick & sweet", 62, GLIM)
    elif i == 4:
        for r_ in range(3):
            for c_ in range(4):
                x = 270 + c_ * 180 + (r_ % 2) * 90; y = CENTER - 120 + r_ * 156
                hexcell(P, x, y, 95, (240, 160, 30))
                k = seg(u, .3 + (r_ * 4 + c_) * .18, .6 + (r_ * 4 + c_) * .18)
                if k > 0: hexcell(P, x, y, 95 * eout(k), (255, 245, 210), (220, 200, 160))
        P.text(540, CENTER + 420, "sealed with wax ❄", 62, CLOUD)
    else:
        P.ell(540, CENTER + 60, 260, 90, (230, 235, 245), outline=(170, 180, 200), w=8)
        P.rrect(780, CENTER + 40, 1040, CENTER + 80, 20, (230, 235, 245), outline=(170, 180, 200), w=6)
        P.ell(540, CENTER + 60, 260 * eout(u / 2) * .29, 90 * eout(u / 2) * .29, (255, 190, 40), glow=mul(GLIM, 220))
        P.text(540, CENTER - 200, "1/12", 150, GLIM); P.text(540, CENTER - 60, "of a teaspoon", 56, CLOUD)
        bee(P, 300 + math.sin(t) * 40, CENTER + 330, .9, t)

def sc_beavers(i, P, t, u):
    WATER = CENTER + 100
    def water(level=WATER, col=(40, 120, 200)):
        P.poly([(0, level + math.sin(t * 2) * 6), (W, level + math.sin(t * 2 + 2) * 6), (W, H), (0, H)], col)
        for k in range(6): P.line([(k * 200 + (t * 40) % 200 - 100, level + 30), (k * 200 + (t * 40) % 200, level + 30)], (120, 190, 240), 6)
    if i == 0:
        water(); beaver(P, 540, WATER - 60, 1.3, t, stick=True)
    elif i == 1:
        P.poly([(0, CENTER - 40), (520, CENTER - 40), (600, H), (0, H)], (70, 140, 70))
        water(CENTER - 40, (30, 90, 170)); P.poly([(0, CENTER - 40), (430, CENTER - 40), (520, H), (0, H)], (70, 140, 70))
        wolf(P, 230, CENTER - 150, .9)
        k = eout(seg(u, .5, 2.2)); beaver(P, lerp(560, 820, k), lerp(CENTER - 80, CENTER + 330, k), .8, t, swim=True)
        P.text(800, CENTER + 560, "safe in deep water", 54, (180, 230, 255))
    elif i == 2:
        lvl = lerp(CENTER + 260, CENTER - 20, eout(u / 4)); water(lvl)
        P.poly([(0, CENTER + 330), (W, CENTER + 330), (W, H), (0, H)], (40, 120, 200))
        n = int(clamp(u / 3.5) * 9) + 1
        for k in range(n):
            y = CENTER + 300 - (k // 3) * 70; x = 380 + (k % 3) * 110 + (k // 3) * 20
            log(P, x - 120, y + 10, x + 140, y - 10, 34)
        P.ell(540, CENTER + 330, 280, 40, (110, 80, 50))
        beaver(P, 860, CENTER - 80 + (lvl - CENTER) * .3, .7, t, stick=True, flip=1)
        P.text(540, CENTER + 560, "branches + mud + stones", 50, CLOUD)
    elif i == 3:
        water(CENTER - 40)
        P.poly([(250, CENTER - 40), (540, CENTER - 330), (830, CENTER - 40), (830, CENTER + 300), (250, CENTER + 300)], (125, 85, 45))
        for k in range(8): log(P, 280 + k * 70, CENTER - 60 - (k % 3) * 60, 330 + k * 70, CENTER - 160 - (k % 3) * 60, 18)
        P.ell(540, CENTER - 90, 140, 90, (60, 40, 30))
        P.poly([(420, CENTER + 120), (500, CENTER + 120), (520, CENTER - 40), (450, CENTER - 40)], (25, 70, 140))
        k = (u * .35) % 1; beaver(P, lerp(980, 470, k), CENTER + 180 - k * 60, .45, t, swim=True)
        P.text(540, CENTER + 470, "underwater door", 62, GLIM)
    elif i == 4:
        water(CENTER - 20)
        k = lambda d: back(seg(u, d, d + .5))
        if k(0.2) > 0: frog(P, 230, CENTER - 60, 1.2 * k(0.2))
        if k(0.8) > 0: fish(P, 520 + math.sin(t) * 40, CENTER + 250, 1.4 * k(0.8), (255, 150, 80))
        if k(1.4) > 0: bird(P, 760, CENTER - 420 + math.sin(t * 2) * 30, 1.4 * k(1.4), t)
        if k(2.0) > 0:
            P.line([(820, CENTER - 160), (930, CENTER - 160)], (60, 200, 220), 10)
            for dx in (-20, 20): P.ell(875 + dx, CENTER - 175, 30, 10, (200, 240, 255))
        fish(P, 300 - math.sin(t) * 40, CENTER + 420, .9, (120, 200, 255))
    else:
        water(); beaver(P, 540, WATER - 60, 1.2, t)
        P.rrect(170, CENTER - 420, 910, CENTER - 270, 70, HOPE)
        P.text(540, CENTER - 345, "ECOSYSTEM ENGINEER", 54, CLOUD)


# ---------- Flamingos & Meeresschildkröten (14.11.) ----------
PINK = (255, 120, 160)
def flamingo(P, x, y, s, t, col=PINK, chick=False):
    if chick:
        P.ell(x, y, 70 * s, 60 * s, col); P.circ(x - 55 * s, y - 55 * s, 38 * s, col)
        P.circ(x - 65 * s, y - 62 * s, 7 * s, NIGHT)
        P.poly([(x - 92 * s, y - 55 * s), (x - 125 * s, y - 45 * s), (x - 92 * s, y - 40 * s)], (60, 60, 70))
        for dx in (-15, 20): P.line([(x + dx * s, y + 50 * s), (x + dx * s, y + 120 * s)], (90, 90, 100), 8 * s)
        return
    sway = math.sin(t * 1.5) * 10 * s
    P.line([(x + 10 * s, y + 70 * s), (x + 10 * s, y + 330 * s)], col, 12 * s)
    P.line([(x - 15 * s, y + 70 * s), (x - 10 * s, y + 190 * s), (x + 10 * s, y + 200 * s)], col, 11 * s)
    P.ell(x + 30 * s, y, 130 * s, 85 * s, col)
    P.ell(x + 60 * s, y - 10 * s, 90 * s, 55 * s, lc(col, (255, 255, 255), .25))
    P.line([(x - 70 * s, y - 20 * s), (x - 110 * s + sway, y - 150 * s), (x - 60 * s + sway, y - 280 * s)], col, 26 * s)
    hx, hy = x - 60 * s + sway, y - 300 * s
    P.circ(hx, hy, 40 * s, col); P.circ(hx - 8 * s, hy - 10 * s, 8 * s, NIGHT)
    P.poly([(hx - 30 * s, hy - 5 * s), (hx - 95 * s, hy + 25 * s), (hx - 80 * s, hy + 45 * s), (hx - 25 * s, hy + 20 * s)], (250, 245, 235))
    P.poly([(hx - 75 * s, hy + 28 * s), (hx - 95 * s, hy + 25 * s), (hx - 82 * s, hy + 46 * s)], NIGHT)

def shrimp(P, x, y, s, t, col=(255, 150, 120)):
    for k in range(5): P.circ(x + k * 22 * s, y + math.sin(k * .8) * 14 * s, (22 - k * 2.5) * s, col)
    P.line([(x - 15 * s, y - 5 * s), (x - 70 * s, y - 40 * s + math.sin(t * 6) * 8 * s)], col, 4 * s)
    P.circ(x - 8 * s, y - 8 * s, 4 * s, NIGHT)

def carrot(P, x, y, s):
    P.poly([(x - 40 * s, y - 60 * s), (x + 40 * s, y - 60 * s), (x, y + 140 * s)], (255, 140, 40))
    for dx in (-20, 0, 20): P.line([(x, y - 60 * s), (x + dx * 1.6 * s, y - 130 * s)], (70, 170, 80), 12 * s)

def turtle(P, x, y, s, t, hatch=False):
    fl = math.sin(t * 3) * 20
    for sx, sy, a in ((-1, -1, 0), (1, -1, 0), (-1, 1, 0), (1, 1, 0)):
        P.ell(x + sx * 85 * s, y + sy * 65 * s + (fl if sy < 0 else -fl) * s * .4, 55 * s, 22 * s, (110, 170, 110))
    P.circ(x - 140 * s, y, 42 * s, (120, 180, 120)); P.circ(x - 158 * s, y - 10 * s, 7 * s, NIGHT)
    P.ell(x, y, 120 * s, 90 * s, (150, 100, 55), outline=(100, 65, 35), w=6)
    for dx, dy in ((-40, -25), (35, -25), (-40, 25), (35, 25), (0, 0)): hexcell(P, x + dx * s, y + dy * s, 26 * s, (175, 120, 65), (110, 75, 40))

def globe(P, x, y, r, t):
    P.circ(x, y, r, (40, 110, 200), glow=mul((60, 140, 255), 45))
    P.ell(x - r * .3, y - r * .25, r * .35, r * .22, (70, 170, 90)); P.ell(x + r * .35, y + r * .2, r * .28, r * .35, (70, 170, 90))
    for k in range(5):
        rr = r * (1.25 + k * .22)
        P.arc(x, y, rr, 200 + math.sin(t + k) * 4, 340 + math.sin(t + k) * 4, lc((150, 220, 255), (40, 60, 120), k / 5), 5)
        P.arc(x, y, rr, 20, 160, lc((150, 220, 255), (40, 60, 120), k / 5), 5)

def sc_flamingos(i, P, t, u):
    if i == 0:
        P.poly([(0, CENTER + 330), (W, CENTER + 330), (W, H), (0, H)], (60, 140, 190))
        flamingo(P, 520, CENTER - 20, 1.25, t)
    elif i == 1:
        flamingo(P, 640, CENTER - 60, 1.0, t)
        flamingo(P, 300, CENTER + 280, 1.3 * back(seg(u, .3, .9)), t, col=(170, 170, 180), chick=True)
        P.text(300, CENTER + 470, "gray chick", 56, CLOUD)
    elif i == 2:
        P.poly([(0, CENTER - 40), (W, CENTER - 40), (W, H), (0, H)], (60, 140, 190))
        for k in range(14):
            P.circ(120 + (k * 137) % 860, CENTER + 60 + (k * 89) % 380, 14 + (k % 3) * 5, (90, 200, 120))
        for k in range(4):
            shrimp(P, 200 + k * 200 + math.sin(t + k) * 30, CENTER + 120 + (k % 2) * 160, 1.3 * back(seg(u, .2 + k * .3, .6 + k * .3)), t + k)
        P.text(540, CENTER - 180, "algae + brine shrimp", 60, GLIM)
    elif i == 3:
        carrot(P, 300, CENTER, 1.3 * back(seg(u, 1.2, 1.7)))
        shrimp(P, 640, CENTER - 40, 2.2, t)
        for k in range(8):
            a = k / 8 * 2 * math.pi + t; P.circ(540 + math.cos(a) * 330, CENTER + math.sin(a) * 260, 12, (255, 150, 60), glow=mul((255, 140, 40), 220))
        P.text(540, CENTER + 400, "carotenoids", 72, (255, 160, 80))
    elif i == 4:
        k = eio(seg(u, .3, 4.0))
        flamingo(P, 520, CENTER - 20, 1.2, t, col=lc((235, 235, 240), PINK, k))
        for j in range(6):
            q = (u * .7 + j / 6) % 1
            P.circ(250 + j * 110, CENTER + 420 - q * 500, 12, (255, 150, 120), glow=mul((255, 120, 150), 200 * (1 - q)))
    else:
        flamingo(P, 450, CENTER - 20, 1.1, t)
        shrimp(P, 760, CENTER - 300, 1.6, t)
        P.text(700, CENTER - 420, "= dinner!", 70, GLIM)

def sc_turtles(i, P, t, u):
    if i == 0:
        P.poly([(0, CENTER + 120), (W, CENTER + 120), (W, H), (0, H)], (40, 120, 200))
        turtle(P, 540 + math.sin(t * .8) * 150, CENTER + 330, 1.3, t)
        P.circ(820, CENTER - 300, 70, (255, 230, 150), glow=mul(GLIM, 160))
    elif i == 1:
        P.poly([(0, CENTER + 150), (W, CENTER + 150), (W, H), (0, H)], (40, 120, 200))
        P.poly([(0, CENTER + 60), (460, CENTER + 60), (560, CENTER + 150), (0, CENTER + 150)], (235, 210, 160))
        k = eout(seg(u, .3, 3.5))
        turtle(P, lerp(220, 900, k), lerp(CENTER + 100, CENTER + 420, k), .55 + .5 * k, t)
        P.text(540, CENTER - 200, "across entire oceans", 60, GLIM)
    elif i == 2:
        P.poly([(0, CENTER + 150), (W, CENTER + 150), (W, H), (0, H)], (40, 120, 200))
        P.poly([(0, CENTER + 60), (700, CENTER + 60), (820, CENTER + 150), (0, CENTER + 150)], (235, 210, 160))
        k = eout(seg(u, .2, 3.0)); turtle(P, lerp(980, 420, k), lerp(CENTER + 380, CENTER + 60, k), 1.1, t)
        for j in range(5): P.ell(250 + j * 60, CENTER + 110, 20, 16, (250, 248, 240))
        P.text(540, CENTER - 200, "same beach, decades later", 56, GLIM)
    elif i == 3:
        P.poly([(0, CENTER + 60), (W, CENTER + 60), (W, H), (0, H)], (235, 210, 160))
        P.rrect(280, CENTER - 330, 800, CENTER - 110, 40, (255, 250, 235), outline=(200, 170, 120), w=6)
        P.text(540, CENTER - 260, "MAGNETIC", 54, HOOK); P.text(540, CENTER - 180, "ADDRESS", 54, HOOK)
        for k in range(3):
            q = (t * .6 + k / 3) % 1
            P.arc(540, CENTER + 160, 120 + q * 330, 200, 340, lc((150, 220, 255), (0, 0, 0), q), 9 * (1 - q) + 3)
        turtle(P, 540, CENTER + 260, .9, t)
    elif i == 4:
        globe(P, 540, CENTER, 260, t)
        for k in range(3): P.circ(540 + math.cos(t + k * 2) * 400, CENTER + math.sin(t + k * 2) * 330, 16, GLIM, glow=mul(GLIM, 220))
        P.text(540, CENTER + 470, "a built-in map", 64, GLIM)
    else:
        P.circ(540, CENTER - 40, 230, (240, 240, 250), outline=(180, 180, 200), w=10)
        a = math.sin(t * 2) * .4 - .6
        P.poly([(540 + math.cos(a) * 190, CENTER - 40 + math.sin(a) * 190), (540 + math.cos(a + 1.57) * 30, CENTER - 40 + math.sin(a + 1.57) * 30), (540 - math.cos(a + 1.57) * 30, CENTER - 40 - math.sin(a + 1.57) * 30)], HOOK)
        P.circ(540, CENTER - 40, 22, NIGHT)
        turtle(P, 540, CENTER + 330, .9, t)
        P.text(540, CENTER - 330, "TURTLE GPS", 70, GLIM)

# ---------- Oktopus, Buckelwal, Zugvogel (Nachtlauf 14./15.11.) ----------
def octopus(P, x, y, s, t, col=(230, 90, 110), spots=None, eyes=True):
    dark = mul(col, 190)
    for k in range(8):                                        # acht Arme, wellig, verjüngt
        a0 = math.pi * (.12 + .76 * k / 7); pts = []
        for j in range(14):
            q = j / 13; a = a0 + math.sin(t * 2.2 + k * .9 + q * 3) * .35 * q
            pts.append((x + math.cos(a) * (60 + 260 * q) * s, y + 40 * s + math.sin(a) * (40 + 230 * q) * s + q * q * 60 * s))
        for j in range(13):
            P.line([pts[j], pts[j + 1]], col if j % 2 == 0 else dark, (34 - j * 2.2) * s)
        for j in range(2, 12, 3): P.circ(pts[j][0], pts[j][1] + 6 * s, (8 - j * .4) * s, lc(col, CLOUD, .55))
    P.ell(x, y - 80 * s, 150 * s, 170 * s, col)                # Kopf/Mantel
    P.ell(x - 40 * s, y - 150 * s, 45 * s, 30 * s, lc(col, CLOUD, .3))
    if spots:
        for k, (dx, dy, r_, c_) in enumerate(spots): P.circ(x + dx * s, y + dy * s, r_ * s, c_)
    if eyes:
        for ex in (-55, 55):
            P.ell(x + ex * s, y + 10 * s, 30 * s, 26 * s, CLOUD); P.ell(x + ex * s, y + 12 * s, 22 * s, 9 * s, NIGHT)
        P.arc(x, y + 40 * s, 30 * s, 20, 160, NIGHT, 6 * s)

def whale(P, x, y, s, t, col=(70, 90, 130), flip=1, sing=0.):
    f = flip; belly = lc(col, CLOUD, .55); bob = math.sin(t * 1.3) * 8 * s
    y = y + bob; tail = math.sin(t * 1.6) * 30 * s
    P.poly([(x + f * 260 * s, y - 10 * s), (x + f * 380 * s, y - 40 * s + tail), (x + f * 420 * s, y - 110 * s + tail),
            (x + f * 360 * s, y - 20 * s + tail), (x + f * 430 * s, y + 50 * s + tail), (x + f * 370 * s, y + 20 * s + tail)], col)
    P.ell(x, y, 300 * s, 105 * s, col)
    P.ell(x - f * 30 * s, y + 45 * s, 250 * s, 55 * s, belly)
    for k in range(5): P.line([(x - f * (230 - k * 6) * s, y + (30 + k * 12) * s), (x + f * (60 - k * 15) * s, y + (40 + k * 12) * s)], mul(belly, 220), 4 * s)
    fa = math.sin(t * 1.6) * .2
    P.poly([(x - f * 60 * s, y + 40 * s), (x - f * (20 - 160 * math.sin(fa)) * s, y + 210 * s), (x + f * 40 * s, y + 220 * s), (x + f * 20 * s, y + 50 * s)], mul(col, 230))
    for k in range(4): P.circ(x - f * (150 - k * 45) * s, y - 85 * s + k * 4 * s, 9 * s, mul(col, 160))
    P.circ(x - f * 200 * s, y - 5 * s, 10 * s, NIGHT); P.circ(x - f * 203 * s, y - 9 * s, 3.5 * s, (255, 255, 255))
    if sing:
        for k in range(4):
            q = (t * .5 + k / 4) % 1
            P.text(x - f * (250 + q * 120) * s, y - (80 + q * 360) * s, "♪" if k % 2 else "♫", (70 + 30 * math.sin(math.pi * q)) * s, lc(GLIM, (20, 30, 60), q * q))

def flybird(P, x, y, s, t, col=(245, 245, 250), flip=1, wing=(200, 210, 225)):
    f = flip; fl = math.sin(t * 7)
    P.poly([(x + f * 10 * s, y), (x + f * 40 * s, y - (90 + 60 * fl) * s), (x + f * 90 * s, y - (60 + 70 * fl) * s), (x + f * 70 * s, y)], wing)
    P.ell(x, y, 85 * s, 30 * s, col, outline=mul(wing, 170), w=3)
    P.poly([(x + f * 70 * s, y - 5 * s), (x + f * 130 * s, y - 30 * s), (x + f * 120 * s, y + 20 * s)], col)
    P.circ(x - f * 80 * s, y - 18 * s, 26 * s, col); P.poly([(x - f * 100 * s, y - 24 * s), (x - f * 135 * s, y - 14 * s), (x - f * 100 * s, y - 8 * s)], (255, 150, 40))
    P.circ(x - f * 86 * s, y - 24 * s, 5 * s, NIGHT)
    P.poly([(x - f * 10 * s, y), (x - f * 30 * s, y + (60 + 60 * fl) * s), (x + f * 40 * s, y + (40 + 60 * fl) * s), (x + f * 40 * s, y)], mul(wing, 220))

def sc_octopuses(i, P, t, u):
    REEF = lambda: [P.ell(150 + k * 200, CENTER + 470 + (k % 2) * 30, 140, 70, lc((60, 90, 120), (90, 70, 110), k / 5)) for k in range(6)]
    if i == 0:
        REEF()
        octopus(P, 540, CENTER - 40, 1.25, t, col=hsv((t * .35) % 1, .65, .95))
        for k in range(6):
            q = (t * .4 + k / 6) % 1; P.circ(200 + k * 140, CENTER + 400 - q * 900, 10 + k % 3 * 4, lc((200, 230, 255), (30, 50, 90), q), outline=(220, 240, 255), w=2)
    elif i == 1:
        P.circ(540, CENTER, 380, (235, 180, 160), outline=(200, 140, 120), w=10)
        random.seed(7)
        for k in range(70):
            a = random.random() * 6.28; rr = math.sqrt(random.random()) * 340; ph = random.random() * 6
            r_ = 10 + 14 * (.5 + .5 * math.sin(t * 3 + ph)) * eout(seg(u, k * .02, k * .02 + .4))
            P.circ(540 + math.cos(a) * rr, CENTER + math.sin(a) * rr, r_, [(200, 40, 50), (240, 180, 40), (120, 70, 40), (40, 30, 30)][k % 4])
        P.text(540, CENTER - 460, "zoom into the skin", 50, CLOUD)
        P.text(540, CENTER + 470, "chromatophores", 70, GLIM)
    elif i == 2:
        cols = [(220, 50, 60), (245, 190, 40), (140, 85, 45), (35, 30, 35)]
        for k, c_ in enumerate(cols):
            x = 270 + (k % 2) * 540; y = CENTER - 200 + (k // 2) * 420; kk = back(seg(u, .2 + k * .35, .6 + k * .35))
            if kk <= 0: continue
            for m in range(10):
                a = m / 10 * 2 * math.pi + math.sin(t * 2) * .05
                P.line([(x + math.cos(a) * 95 * kk, y + math.sin(a) * 95 * kk), (x + math.cos(a) * 170 * kk, y + math.sin(a) * 170 * kk)], (240, 140, 150), 16 * kk)
            P.circ(x, y, 85 * kk, c_, outline=CLOUD, w=4)
        P.text(540, CENTER + 10, "pigment + muscles", 56, CLOUD)
    elif i == 3:
        P.ell(220, CENTER - 300, 130, 100, (240, 170, 190), outline=(200, 120, 150), w=6)
        for k in range(3): P.arc(220 + (k - 1) * 40, CENTER - 300, 50, 200, 340, (200, 120, 150), 6)
        prog = seg(u, .3, 1.6)
        pts = [(220 + q * 320, CENTER - 200 + math.sin(q * 9) * 30 + q * 200) for q in [j / 20 for j in range(21)]]
        P.line(pts, (120, 100, 140), 8)
        sp = pts[int(prog * 20)]
        if 0 < prog < 1: P.circ(sp[0], sp[1], 22, GLIM, glow=mul(GLIM, 240))
        k = eout(seg(u, 1.6, 2.6)); r_ = 40 + 230 * k
        for m in range(12):
            a = m / 12 * 2 * math.pi
            P.line([(620 + math.cos(a) * (r_ + 10), CENTER + 180 + math.sin(a) * (r_ + 10)), (620 + math.cos(a) * (r_ + 70), CENTER + 180 + math.sin(a) * (r_ + 70))], (240, 140, 150), 14)
        P.circ(620, CENTER + 180, r_, (220, 50, 60))
        for q in range(3):
            qq = (u * .8 + q / 3) % 1
            if k > .9: P.arc(620, CENTER + 180, r_ + 90 + qq * 120, 0, 360, lc((255, 160, 160), (0, 0, 0), qq), 6 * (1 - qq) + 2)
        if k > .3: P.text(620, CENTER + 180, "OPEN", 64 * back(seg(u, 1.9, 2.4)), CLOUD)
    elif i == 4:
        REEF()
        octopus(P, 540, CENTER - 40, 1.2, t, col=(90, 120, 200))
        for k in range(10):
            a = k / 10 * math.pi * 2 + t * .8; c_ = hsv((.45 + .1 * math.sin(t + k)) % 1, .5, 1)
            P.circ(540 + math.cos(a) * 170, CENTER - 100 + math.sin(a) * 180, 18 + 8 * math.sin(t * 4 + k), c_, glow=mul(c_, 200))
        for k in range(3):
            x0 = 260 + k * 280; q = seg(u, .3 + k * .3, 1.1 + k * .3)
            P.line([(x0 - 120, CENTER - 520), (x0 - 120 + 120 * q, CENTER - 520 + 300 * q)], (255, 250, 210), 8)
        P.text(540, CENTER + 470, "shimmer from reflected light", 50, (170, 230, 255))
    else:
        P.circ(820, CENTER - 420, 90, (255, 225, 120), glow=mul(GLIM, 200))
        for k in range(5):
            q = (t * .7 + k / 5) % 1; P.line([(780 - k * 40, CENTER - 340), (lerp(780 - k * 40, 600 - k * 50, q), lerp(CENTER - 340, CENTER - 120, q))], (255, 240, 170), 6)
        octopus(P, 480, CENTER + 40, 1.0, t, col=hsv((t * .5) % 1, .6, .95))
        P.text(540, CENTER + 480, "skin that senses light!", 56, GLIM)

def sc_whales(i, P, t, u):
    def sea(top=CENTER - 520):
        P.poly([(0, top), (W, top), (W, H), (0, H)], (20, 70, 130))
        for k in range(6):
            x0 = (k * 230 + t * 30) % 1300 - 120
            P.poly([(x0, top), (x0 + 60, top), (x0 + 220, H), (x0 + 100, H)], (35, 95, 160))
    if i == 0:
        sea(); whale(P, 540, CENTER, 1.2, t, sing=1)
    elif i == 1:
        sea(); whale(P, 560, CENTER + 120, 1.0, t, sing=1)
        k = back(seg(u, .3, .8))
        P.circ(800, CENTER - 330, 120 * k, CLOUD, outline=(180, 190, 210), w=8)
        if k > .2:
            a = -math.pi / 2 + seg(u, .5, 4.5) * 2 * math.pi
            P.line([(800, CENTER - 330), (800 + math.cos(a) * 90 * k, CENTER - 330 + math.sin(a) * 90 * k)], HOOK, 10)
            P.text(800, CENTER - 150, "up to 20 min", 50, GLIM)
        P.text(540, CENTER + 480, "only males sing", 60, CLOUD)
    elif i == 2:
        sea()
        whale(P, 360, CENTER - 140, .65, t, sing=1)
        whale(P, 700, CENTER + 260, .55, t + 1, col=(90, 100, 140), flip=-1)
        for k in range(3):
            q = (u * .6 + k / 3) % 1
            P.heart(560 + math.sin(t + k) * 40, CENTER + 100 - q * 260, 26 * (1 - q * .5), lc((255, 120, 150), (20, 70, 130), q))
        P.text(540, CENTER - 420, "impress females?", 56, GLIM)
        P.text(540, CENTER + 480, "or rival males?", 56, CLOUD)
    elif i == 3:
        sea()
        whale(P, 230, CENTER, .5, t, sing=0)
        for k in range(5):
            q = (t * .45 + k / 5) % 1
            P.arc(330, CENTER, 80 + q * 800, -35, 35, lc((170, 230, 255), (20, 70, 130), q), 12 * (1 - q) + 3)
        whale(P, 880, CENTER + 330, .3, t, flip=-1)
        k = eio(seg(u, .5, 3.5))
        P.line([(160, CENTER + 520), (160 + 760 * k, CENTER + 520)], GLIM, 10)
        P.text(540, CENTER + 600, "many kilometers", 56, GLIM)
    elif i == 4:
        sea()
        c_ = hsv((.12 + seg(u, 1, 4) * .5) % 1, .7, 1)
        for k in range(3):
            x = 270 + k * 270; y = CENTER - 280 + k * 300
            whale(P, x, y, .45, t + k * .7, flip=1 if k % 2 == 0 else -1)
            for j in range(3):
                q = (t * .5 + j / 3) % 1
                P.text(x - 100, y - 70 - q * 160, "♪", 56, lc(c_, (20, 70, 130), q))
        P.text(540, CENTER + 520, "same song · new versions", 52, GLIM)
    else:
        sea(CENTER - 380)
        P.ell(60, CENTER - 360, 140, 60, (90, 160, 90)); P.ell(1020, CENTER - 360, 140, 60, (90, 160, 90))
        for k in range(6):
            q = (t * .3 + k / 6) % 1
            P.text(lerp(140, 940, q), CENTER - 330 - math.sin(q * math.pi) * 130, "♫", 60, lc(GLIM, HOOK, k / 6))
        whale(P, 540, CENTER + 160, .9, t, sing=1)
        P.text(540, CENTER + 500, "whale pop hits!", 72, GLIM)

def sc_migration(i, P, t, u):
    def clouds(y0=CENTER - 520):
        for k in range(4):
            x = (k * 330 + t * 25) % 1400 - 160; y = y0 + (k % 2) * 110
            for dx, r_ in ((-60, 50), (0, 70), (60, 50)): P.circ(x + dx, y, r_, lc(CLOUD, (200, 215, 235), .3))
    if i == 0:
        clouds()
        for k in range(7):
            off = abs(k - 3); x = 540 + (k - 3) * 120 + math.sin(t * .8) * 40; y = CENTER - 60 + off * 90
            flybird(P, x, y + math.sin(t * 3 + k) * 10, .75 if k != 3 else 1.0, t + k * .3)
    elif i == 1:
        P.ell(380, CENTER + 260, 220, 80, (130, 90, 50))
        for k in range(6): P.line([(200 + k * 70, CENTER + 230), (260 + k * 60, CENTER + 300)], (100, 70, 40), 10)
        P.ell(380, CENTER + 180, 100, 85, (180, 170, 150)); P.circ(330, CENTER + 120, 55, (190, 180, 160))
        P.circ(315, CENTER + 105, 9, NIGHT); P.poly([(285, CENTER + 115), (250, CENTER + 125), (285, CENTER + 135)], (255, 150, 40))
        for j in range(16):                                 # DNA-Doppelhelix
            y = CENTER - 380 + j * 44; a = t * 2 + j * .6
            x1, x2 = 760 + math.sin(a) * 90, 760 - math.sin(a) * 90
            P.line([(x1, y), (x2, y)], lc(HOPE, CLOUD, .3), 6)
            P.circ(x1, y, 16, HOPE); P.circ(x2, y, 16, GLIM)
        k = eout(seg(u, .8, 2.2))
        P.line([(440, CENTER - 80), (440 + 140 * k, CENTER - 230 * k)], GLIM, 14)
        P.text(540, CENTER + 470, "born with a map", 62, GLIM)
    elif i == 2:
        P.rrect(60, CENTER - 520, 1020, CENTER - 40, 50, (130, 190, 240))
        P.rrect(60, CENTER, 1020, CENTER + 480, 50, (15, 22, 50))
        sx = lerp(180, 900, seg(u, 0, 3)); P.circ(sx, CENTER - 360 + abs(sx - 540) * .25, 70, (255, 220, 90), glow=mul(GLIM, 160))
        flybird(P, 540, CENTER - 160, .6, t)
        P.twinkle(540, CENTER + 240, 34, GLIM)
        random.seed(5)
        for k in range(22):
            rr = 50 + random.random() * 170; a0 = random.random() * 6.28 + t * .25
            P.circ(540 + math.cos(a0) * rr * 1.7, CENTER + 240 + math.sin(a0) * rr, 4 + (k % 3) * 2, (240, 240, 255))
        P.text(540, CENTER + 420, "North Star", 46, GLIM)
    elif i == 3:
        P.circ(380, CENTER, 230, (40, 110, 200)); P.ell(320, CENTER - 60, 90, 60, (70, 170, 90)); P.ell(450, CENTER + 80, 70, 90, (70, 170, 90))
        for k in range(4):
            rx = 260 + k * 60
            P.arc(380, CENTER, rx, 300, 420, lc((255, 120, 160), (40, 60, 120), k / 5), 5)
            P.arc(380, CENTER, rx, 120, 240, lc((255, 120, 160), (40, 60, 120), k / 5), 5)
        g = .5 + .5 * math.sin(t * 3)
        P.circ(800, CENTER - 150, 150, CLOUD, outline=(170, 180, 200), w=8)
        P.circ(800, CENTER - 150, 75, (60, 120, 90)); P.circ(800, CENTER - 150, 40, NIGHT, glow=mul((120, 255, 200), 120 + 100 * g))
        P.circ(820, CENTER - 170, 14, (255, 255, 255))
        P.text(800, CENTER + 60, "eye proteins", 50, HOPE)
        P.text(540, CENTER + 470, "magnetic sense", 66, GLIM)
    elif i == 4:
        P.poly([(0, CENTER + 100), (W, CENTER + 100), (W, H), (0, H)], (90, 160, 90))
        for x, h_ in ((200, 300), (380, 400), (560, 260)):
            P.poly([(x - 170, CENTER + 100), (x, CENTER + 100 - h_), (x + 170, CENTER + 100)], (120, 120, 140))
            P.poly([(x - 50, CENTER + 100 - h_ * .7), (x, CENTER + 100 - h_), (x + 50, CENTER + 100 - h_ * .7)], CLOUD)
        P.poly([(760, CENTER + 100), (W, CENTER + 100), (W, H), (880, H)], (40, 120, 200))
        P.line([(0, CENTER + 330), (300, CENTER + 280), (600, CENTER + 380), (800, CENTER + 330)], (80, 160, 230), 26)
        k = seg(u, 0, 4); flybird(P, lerp(980, 150, k), CENTER - 300 + math.sin(t * 2) * 30, .8, t)
        for j in range(4):
            q = (t * .6 + j / 4) % 1; P.circ(lerp(700, 860, q), CENTER - 80 - q * 140, 8 + 6 * q, lc((230, 200, 255), (40, 60, 100), q))
        P.text(540, CENTER + 520, "landmarks + smell", 60, GLIM)
    else:
        P.circ(540, CENTER - 20, 330, (40, 110, 200), glow=mul((60, 140, 255), 40))
        P.ell(470, CENTER - 230, 150, 70, CLOUD); P.ell(560, CENTER + 230, 160, 70, CLOUD)
        P.ell(400, CENTER - 40, 90, 120, (70, 170, 90)); P.ell(680, CENTER + 10, 80, 150, (70, 170, 90))
        k = eio(seg(u, .2, 4.5)); n = int(40 * k)
        pts = [(540 + math.sin(j / 40 * math.pi) * 230, CENTER - 300 + j * 15) for j in range(n + 1)]
        for a, b in zip(pts[::2], pts[1::2]): P.line([a, b], GLIM, 10)
        if pts: flybird(P, pts[-1][0], pts[-1][1], .5, t, flip=1)
        P.text(540, CENTER + 470, "70,000 km a year!", 72, GLIM)

# ---------- Zebras & Glühwürmchen (Nachtlauf 14./15.11., Lauf B 21:35) ----------
def dk(c, k): return tuple(int(clamp(v * k / 255, 0, 255)) for v in c)   # echtes Abdunkeln (k/255), mul() sättigt bei k>1
def equine(P, x, y, s, t, stripes=True, col=(250, 250, 250), coat=False, flip=1, run=0.):
    f = flip; blk = (30, 30, 36); body = col; mane = blk if stripes and not coat else dk(col, 140)
    sw = math.sin(t * (9 if run else 2)) * (22 if run else 4)
    for k, lx in enumerate((-120, -70, 90, 140)):          # Beine
        a = sw * (1 if k % 2 else -1) * s
        P.line([(x + f * lx * s, y + 40 * s), (x + f * lx * s + a, y + 230 * s)], body, 34 * s)
        if stripes and not coat:
            for j in range(3): P.line([(x + f * lx * s + a * (.3 + j * .25) - 17 * s, y + (95 + j * 45) * s), (x + f * lx * s + a * (.3 + j * .25) + 17 * s, y + (95 + j * 45) * s)], blk, 12 * s)
        P.rrect(x + f * lx * s + a - 19 * s, y + 222 * s, x + f * lx * s + a + 19 * s, y + 245 * s, 6 * s, blk)
    tw = math.sin(t * 3) * 20 * s                            # Schwanz
    P.line([(x + f * 175 * s, y - 40 * s), (x + f * 230 * s, y + 40 * s + tw), (x + f * 225 * s, y + 110 * s + tw)], body, 12 * s)
    P.ell(x + f * 225 * s, y + 120 * s + tw, 14 * s, 26 * s, blk)
    P.ell(x, y, 190 * s, 95 * s, body)
    if stripes:
        cx = x - (20 if coat else 0) * f * s; rx = (150 if coat else 185) * s
        if coat: P.ell(cx, y - 5 * s, rx, 88 * s, (250, 250, 250))
        for k in range(-6, 7):
            dx = k * 30 * s
            if abs(dx) > rx - 8 * s: continue
            hh = 95 * s * math.sqrt(max(0, 1 - (dx / (190 * s)) ** 2))
            w_ = 5 * s + 2 * s * (k % 2)
            P.poly([(cx + dx - w_, y - hh + 2 * s), (cx + dx + w_ + 6 * s, y - hh + 2 * s), (cx + dx + w_ - 4 * s, y + hh * .75), (cx + dx - w_ - 8 * s, y + hh * .75)], blk)
    if coat: P.line([(x - f * 170 * s, y - 60 * s), (x - f * 170 * s, y + 60 * s)], (200, 60, 60), 10 * s); P.line([(x + f * 135 * s, y - 75 * s), (x + f * 135 * s, y + 70 * s)], (200, 60, 60), 10 * s)
    nod = math.sin(t * 1.5) * 8 * s
    P.poly([(x - f * 120 * s, y - 60 * s), (x - f * 175 * s, y - 190 * s + nod), (x - f * 235 * s, y - 170 * s + nod), (x - f * 175 * s, y + 10 * s)], body)
    for k in range(5):
        P.circ(x - f * (135 + k * 20) * s, y - (85 + k * 26) * s + nod * k / 5, 16 * s, mane)
    if stripes and not coat:
        for k in range(4): P.line([(x - f * (130 + k * 22) * s, y - (40 + k * 30) * s), (x - f * (185 + k * 22) * s, y - (20 + k * 30) * s)], blk, 11 * s)
    hx, hy = x - f * 245 * s, y - 165 * s + nod
    P.ell(hx, hy, 70 * s, 42 * s, body)
    P.ell(hx - f * 52 * s, hy + 10 * s, 26 * s, 24 * s, (60, 60, 66) if stripes and not coat else dk(col, 150))
    P.poly([(hx + f * 25 * s, hy - 30 * s), (hx + f * 15 * s, hy - 85 * s), (hx + f * 45 * s, hy - 40 * s)], body, outline=dk(col, 150), w=3)
    P.circ(hx - f * 5 * s, hy - 12 * s, 9 * s, NIGHT); P.circ(hx - f * 8 * s, hy - 15 * s, 3 * s, (255, 255, 255))
    if stripes and not coat:
        for k in range(3): P.line([(hx + f * (5 + k * 18) * s, hy - 38 * s), (hx + f * (12 + k * 18) * s, hy + 34 * s)], blk, 7 * s)

def horsefly(P, x, y, s, t, ang=0.):
    fl = abs(math.sin(t * 40))
    for side in (-1, 1):
        P.ell(x + side * 26 * s, y - 22 * s - fl * 10 * s, 30 * s, 14 * s, (220, 235, 250), outline=(150, 170, 200), w=2)
    P.ell(x + 18 * s, y, 34 * s, 17 * s, (110, 95, 80))
    for k in range(3): P.line([(x + (8 + k * 12) * s, y - 15 * s), (x + (8 + k * 12) * s, y + 15 * s)], (70, 60, 50), 3 * s)
    P.circ(x - 18 * s, y, 18 * s, (80, 70, 60)); P.circ(x - 26 * s, y - 5 * s, 12 * s, (60, 190, 110))

def firefly(P, x, y, s, t, glow=1., col=(255, 235, 110), ang=0.):
    fl = math.sin(t * 30)
    for side in (-1, 1):
        P.ell(x + side * 30 * s, y - 25 * s - fl * 8 * s, 34 * s, 16 * s, (180, 200, 230), outline=(120, 140, 180), w=2)
    if glow > .02:
        P.ell(x + 46 * s, y + 2 * s, 30 * s, 24 * s, lc((90, 90, 50), col, glow), glow=dk(col, 150 * glow))
    else: P.ell(x + 46 * s, y + 2 * s, 30 * s, 24 * s, (90, 90, 50))
    P.ell(x + 8 * s, y, 32 * s, 20 * s, (70, 50, 40))
    P.circ(x - 26 * s, y, 18 * s, (220, 80, 60)); P.circ(x - 36 * s, y - 4 * s, 7 * s, NIGHT)
    P.line([(x - 34 * s, y - 14 * s), (x - 55 * s, y - 45 * s)], (60, 40, 30), 4 * s)
    P.line([(x - 30 * s, y - 16 * s), (x - 42 * s, y - 52 * s)], (60, 40, 30), 4 * s)

def sc_zebras(i, P, t, u):
    G = lambda: P.ell(540, CENTER + 330, 520, 70, (150, 200, 110))
    if i == 0:
        G(); equine(P, 560, CENTER + 60, 1.25, t)
        k = back(seg(u, .5, 1.0))
        if k > 0: P.text(820, CENTER - 300, "?", 180 * k, GLIM)
    elif i == 1:
        G(); equine(P, 320, CENTER + 120, .7, t, stripes=False, col=(170, 110, 70)); equine(P, 780, CENTER + 120, .7, t)
        for k in range(7):
            a = t * (2 + k * .3) + k
            horsefly(P, 540 + math.cos(a) * (180 + k * 30), CENTER - 120 + math.sin(a * 1.3) * 130, .9, t + k)
        P.text(540, CENTER + 480, "horseflies", 72, GLIM)
    elif i == 2:
        G(); equine(P, 560, CENTER + 120, 1.0, t, stripes=False, col=(170, 110, 70))
        q = eout(seg(u, .2, 2.2))                           # sanftes Abbremsen
        fx, fy = lerp(-60, 560, q), lerp(CENTER - 500, CENTER + 25, q)
        horsefly(P, fx, fy, 1.1, t)
        if q > .97:
            k = back(seg(u, 2.2, 2.6)); P.text(540, CENTER + 480, "smooth landing", 66 * k, HOPE)
    elif i == 3:
        G(); equine(P, 560, CENTER + 120, 1.0, t)
        q = seg(u, .2, 1.6); q2 = seg(u, 1.6, 3.0)
        if q < 1: fx, fy = lerp(-60, 600, q), lerp(CENTER - 500, CENTER + 10, q)
        else: fx, fy = 600 + 500 * eout(q2), CENTER + 10 - 400 * eout(q2) + math.sin(q2 * 20) * 30
        horsefly(P, fx, fy, 1.1, t)
        if q >= 1:
            k = back(seg(u, 1.6, 2.0)); P.text(540, CENTER + 480, "missed!", 84 * k, HOOK)
            for m in range(6): P.twinkle(600 + math.cos(m) * 60 * k, CENTER + 10 + math.sin(m) * 60 * k, 16 * (1 - q2), GLIM)
    elif i == 4:
        P.rrect(140, CENTER - 420, 940, CENTER + 380, 60, (250, 250, 250))
        for k in range(-6, 12):
            x0 = 140 + k * 110 + math.sin(t) * 10
            pts = [(clamp(x0 + j * 40 + math.sin(j * .9 + t * 1.5) * 40, 160, 920), CENTER - 400 + j * 78) for j in range(11)]
            P.line(pts, (30, 30, 36), 46)
        P.rrect(140, CENTER - 420, 940, CENTER + 380, 60, None, outline=(230, 220, 200), w=10)
        for k in range(3):
            a = t * 5 + k * 2.1; r_ = 120 + 60 * math.sin(t * 3 + k)
            horsefly(P, 540 + math.cos(a) * r_, CENTER - 20 + math.sin(a) * r_, 1.2, t + k)
            P.text(540 + math.cos(a) * r_ + 50, CENTER - 80 + math.sin(a) * r_, "?", 60, GLIM)
        P.text(540, CENTER + 480, "confusing up close", 62, CLOUD)
    else:
        G(); equine(P, 560, CENTER + 120, 1.0, t, stripes=True, col=(170, 110, 70), coat=True)
        for k in range(4):
            q = (u * .7 + k / 4) % 1; a = -1.2 + k * .8
            horsefly(P, 560 + math.cos(a) * (150 + q * 450), CENTER - 60 + math.sin(a) * (120 + q * 350), .9, t + k)
        k = back(seg(u, .4, .9))
        if k > 0: P.text(540, CENTER - 430, "striped coats work!", 62 * k, HOOK)

def sc_fireflies(i, P, t, u):
    def grass(n=26):
        for k in range(n):
            x = k * 44 + 10; h = 140 + (k * 37) % 90; sw = math.sin(t * 1.2 + k) * 14
            P.poly([(x - 10, CENTER + 520), (x + 10, CENTER + 520), (x + sw, CENTER + 520 - h)], lc((20, 60, 45), (40, 100, 60), (k % 3) / 2))
    def swarm(n=12, seed=5):
        random.seed(seed)
        for k in range(n):
            x0, y0, ph = random.random() * 1000 + 40, CENTER - 450 + random.random() * 900, random.random() * 6
            on = max(0, math.sin(t * 2.4 + ph)) ** 3
            x, y = x0 + math.sin(t * .6 + ph) * 40, y0 + math.cos(t * .5 + ph) * 30
            P.circ(x, y, 8 + 10 * on, lc((60, 60, 40), (255, 240, 120), on), glow=dk((255, 230, 90), 230 * on))
    if i == 0:
        swarm(); grass()
        on = .5 + .5 * math.sin(t * 2.5)
        firefly(P, 540, CENTER - 20, 3.2 * back(seg(u, 0, .5)), t, glow=on)
    elif i == 1:
        P.circ(540, CENTER, 360, (60, 55, 30), outline=GLIM, w=8)
        k1, k2 = back(seg(u, .4, .9)), back(seg(u, 2.0, 2.5))
        random.seed(2)
        for m in range(8):
            a = m / 8 * 6.28 + t * .3; x, y = 540 + math.cos(a) * 200, CENTER - 40 + math.sin(a) * 160
            if k1 > 0:
                P.poly([(x + math.cos(j * 1.047) * 34 * k1, y + math.sin(j * 1.047) * 34 * k1) for j in range(6)], (255, 220, 90), outline=(200, 150, 30), w=3)
        for m in range(3):
            a = m / 3 * 6.28 - t * .4; x, y = 540 + math.cos(a) * 90, CENTER - 40 + math.sin(a) * 70
            if k2 > 0: P.ell(x, y, 54 * k2, 40 * k2, HOPE, outline=(20, 120, 70), w=4); P.circ(x + 30 * k2, y - 5 * k2, 14 * k2, (60, 55, 30))
        if k1 > 0: P.text(540, CENTER - 450, "luciferin", 66 * k1, GLIM)
        if k2 > 0: P.text(540, CENTER + 450, "luciferase", 66 * k2, HOPE)
    elif i == 2:
        P.circ(540, CENTER, 300, (60, 55, 30), outline=GLIM, w=8)
        for m in range(8):
            q = (u * .6 + m / 8) % 1; a = m * .785
            x, y = 540 + math.cos(a) * (700 - 450 * q), CENTER + math.sin(a) * (700 - 450 * q)
            P.circ(x, y, 34, (120, 190, 255), outline=CLOUD, w=3); P.text(x, y, "O₂", 30, CLOUD)
        fl = eout(seg(u, .8, 2.2)); pul = .8 + .2 * math.sin(t * 6)
        P.circ(540, CENTER, 260 * fl * pul + 1, lc((60, 55, 30), (255, 238, 130), fl), glow=dk((255, 230, 100), 110 * fl))
        if fl > .3: P.text(540, CENTER + 450, "light!", 84 * back(seg(u, 1.2, 1.6)), GLIM)
    elif i == 3:
        P.circ(300, CENTER - 100, 130, (255, 220, 160), glow=(120, 50, 40)); P.rrect(250, CENTER + 20, 350, CENTER + 120, 14, (150, 150, 160))
        for k in range(3):
            q = (t * .8 + k / 3) % 1; x = 240 + k * 60
            P.line([(x, CENTER - 260 - q * 160), (x + 20 * math.sin(q * 9), CENTER - 300 - q * 160)], lc(HOOK, NIGHT, q), 12)
        P.text(300, CENTER + 230, "hot", 64, HOOK)
        firefly(P, 760, CENTER - 100, 2.2, t, glow=.8 + .2 * math.sin(t * 3))
        P.rrect(735, CENTER + 60, 785, CENTER + 300, 25, CLOUD); P.circ(760, CENTER + 310, 40, (120, 190, 255))
        P.rrect(748, CENTER + 230 - 30 * eio(seg(u, .3, 1.5)), 772, CENTER + 310, 12, (120, 190, 255))
        P.text(760, CENTER + 420, "cool", 64, (150, 210, 255))
        k = back(seg(u, 1.0, 1.4))
        if k > 0: P.text(540, CENTER - 460, "cold light", 84 * k, GLIM)
    elif i == 4:
        pats = [(1, 0, 1, 0, 0, 0), (1, 1, 1, 0, 0, 0), (1, 0, 0, 1, 0, 0)]
        for r_, pat in enumerate(pats):
            y = CENTER - 320 + r_ * 300; c = [(255, 235, 110), (170, 255, 120), (255, 190, 90)][r_]
            step = int(t * 4) % len(pat); on = pat[step]
            firefly(P, 200, y, 1.8, t + r_, glow=on, col=c)
            for j, v in enumerate(pat):
                x = 420 + j * 95; act = j == step
                if v: P.circ(x, y, 26 + (8 if act else 0), c if act else dk(c, 120), glow=dk(c, 200) if act else None)
                else: P.circ(x, y, 10, (70, 70, 90))
        P.text(540, CENTER + 480, "secret flash codes", 62, GLIM)
    else:
        swarm(8, 9); grass()
        on = 1 if (t * 1.2) % 1 < .5 else 0
        firefly(P, 470, CENTER - 60, 2.3, t, glow=on)
        for m in range(4):
            q = (u * .8 + m / 4) % 1
            if on: P.circ(700 + q * 200, CENTER - 140 + math.sin(m * 2) * 80 * q, 20, (120, 190, 255))
        P.rrect(720, CENTER + 130, 900, CENTER + 230, 50, HOPE if on else (90, 90, 110))
        P.circ(850 if on else 770, CENTER + 180, 40, CLOUD)
        P.text(810, CENTER + 300, "ON" if on else "OFF", 56, CLOUD)
        P.text(540, CENTER - 430, "oxygen = switch", 62, GLIM)


# ---------- Chamäleon, Elefant, Spinne (Nachtlauf A 14.11. 21:54) ----------
def chameleon(P, x, y, s, t, col=(90, 190, 90), tongue=0., tx=None, ty=None, flip=1):
    f = flip; dark = dk(col, 170); lite = lc(col, CLOUD, .35)
    cx = x + f * 170 * s                                                     # eingerollter Schwanz
    for k in range(3): P.arc(cx + f * 30 * s, y + 20 * s, (70 - k * 20) * s, 0, 360, col, (26 - k * 6) * s)
    P.ell(x, y, 160 * s, 95 * s, col)
    for k in range(5): P.poly([(x + f * (-90 + k * 45) * s, y - 85 * s), (x + f * (-70 + k * 45) * s, y - 120 * s), (x + f * (-50 + k * 45) * s, y - 85 * s)], dark)
    for k in range(4): P.arc(x + f * (-60 + k * 45) * s, y + 10 * s, 28 * s, 200, 340, lite, 6 * s)
    hx = x - f * 160 * s; hy = y - 25 * s
    P.poly([(hx + f * 60 * s, hy - 60 * s), (hx - f * 20 * s, hy - 110 * s), (hx - f * 90 * s, hy + 10 * s), (hx + f * 60 * s, hy + 60 * s)], col)
    mx, my = hx - f * 80 * s, hy + 15 * s
    P.line([(mx, my), (hx + f * 30 * s, hy + 30 * s)], dark, 5 * s)
    if tongue > 0:
        ex, ey = (tx, ty) if tx is not None else (mx - f * 300 * s, my)
        bx, by = lerp(mx, ex, tongue), lerp(my, ey, tongue)
        P.line([(mx, my), (bx, by)], (240, 120, 150), 16 * s); P.circ(bx, by, 26 * s, (255, 140, 170), outline=(200, 80, 110), w=3)
    ex_, ey_ = hx - f * 5 * s, hy - 20 * s
    P.circ(ex_, ey_, 38 * s, lite, outline=dark, w=4)
    a = t * 1.3; P.circ(ex_ - f * 12 * s + math.cos(a) * 8 * s, ey_ + math.sin(a) * 8 * s, 11 * s, NIGHT)
    for dx in (-80, 70):
        P.line([(x + f * dx * s, y + 60 * s), (x + f * (dx - 20) * s, y + 120 * s)], col, 22 * s)

def branch(P, y, x0=0, x1=W):
    P.line([(x0, y), (x1, y - 30)], (110, 75, 45), 34)
    for k in range(3): P.ell(x0 + 200 + k * 300, y - 30 - k * 10, 50, 22, (70, 160, 80))

def fly(P, x, y, s, t):
    wa = math.sin(t * 50)
    for dx in (-1, 1): P.ell(x + dx * 18 * s, y - 20 * s - wa * 5 * s, 22 * s, 14 * s, (220, 235, 255), outline=(150, 170, 200), w=2)
    P.ell(x, y, 26 * s, 18 * s, (60, 60, 70)); P.circ(x - 22 * s, y - 4 * s, 12 * s, (150, 40, 40))

def sc_chameleons(i, P, t, u):
    if i == 0:
        branch(P, CENTER + 260)
        fx, fy = 300 + math.sin(t * 3) * 60, CENTER - 140 + math.sin(t * 5) * 40
        k = seg(u, 1.3, 1.45) - seg(u, 1.6, 1.9)
        if u < 1.6: fly(P, fx, fy, 1.4, t)
        chameleon(P, 640, CENTER + 120, 1.15, t, tongue=k, tx=fx, ty=fy)
        if u > 1.6: P.text(320, CENTER - 300, "GOT IT!", 70 * back(seg(u, 1.6, 2.0)), GLIM)
    elif i == 1:
        P.rrect(240, CENTER - 40, 840, CENTER + 40, 40, (240, 225, 190), outline=(190, 170, 130), w=6)
        k = eout(seg(u, .2, 1.0))
        for j in range(5): P.rrect(280 + j * 105, CENTER - 90, 360 + j * 105, CENTER + 90, 30, (240, 120, 150), outline=(190, 80, 110), w=5)
        P.circ(240, CENTER, 70, (255, 140, 170), outline=(200, 80, 110), w=5)
        P.arc(540, CENTER + 420, 300 * k + 1, 200, 340, (150, 100, 60), 12)
        P.line([(300, CENTER + 340), (780, CENTER + 340)], (230, 230, 230), 4)
        P.line([(260, CENTER + 340), (800, CENTER + 340)], (150, 100, 60), 8); P.poly([(240, CENTER + 340), (280, CENTER + 320), (280, CENTER + 360)], HOOK)
        P.text(540, CENTER - 200, "tongue on a bone", 60, GLIM)
    elif i == 2:
        sq = .5 + .5 * math.sin(t * 2.5); sq = eio(seg(u, .3, 2.5)) * .6 + .1 * sq
        pts = []
        for j in range(25):
            q = j / 24; pts.append((lerp(200, 880 - 260 * sq, q), CENTER + math.sin(q * 30) * 70 * (1 + sq)))
        P.line(pts, (240, 120, 150), 14)
        for j in range(4): P.ell(620 - j * 30 - 200 * sq, CENTER, 40, 140, None, outline=HOOK, w=10)
        P.text(540, CENTER - 300, "loaded like a spring", 60, GLIM)
        P.text(540, CENTER + 300, "ring muscle squeezes", 52, CLOUD)
    elif i == 3:
        branch(P, CENTER + 120)
        k = eout(seg(u, .4, .6)) - eio(seg(u, 2.6, 3.4))
        chameleon(P, 780, CENTER - 20, .65, t, tongue=k, tx=150, ty=CENTER - 140)
        if u < 2.6: fly(P, 150, CENTER - 140, 1.0, t)
        P.line([(160, CENTER + 330), (900, CENTER + 330)], GLIM, 8); P.line([(160, CENTER + 300), (160, CENTER + 360)], GLIM, 8); P.line([(900, CENTER + 300), (900, CENTER + 360)], GLIM, 8)
        P.text(540, CENTER + 430, "up to 2x body length", 56, GLIM)
    elif i == 4:
        P.circ(540, CENTER - 20, 260, (255, 140, 170), outline=(200, 80, 110), w=10)
        for j in range(5):
            q = (u * .5 + j / 5) % 1
            P.ell(380 + j * 80, CENTER + 230 + q * 140, 14, 20 + q * 30, (255, 200, 220))
        fly(P, 540, CENTER - 60, 2.4 * back(seg(u, .3, .8)), 0)
        P.text(540, CENTER + 470, "super sticky", 70, GLIM)
    else:
        P.arc(540, CENTER + 60, 280, 180, 360, CLOUD, 30)
        for j in range(7):
            a = math.pi + j / 6 * math.pi; P.line([(540 + math.cos(a) * 230, CENTER + 60 + math.sin(a) * 230), (540 + math.cos(a) * 270, CENTER + 60 + math.sin(a) * 270)], NIGHT, 8)
        a = math.pi + eout(seg(u, .3, .45)) * math.pi * .95
        P.line([(540, CENTER + 60), (540 + math.cos(a) * 240, CENTER + 60 + math.sin(a) * 240)], HOOK, 14); P.circ(540, CENTER + 60, 22, NIGHT)
        P.text(540, CENTER + 150, "0 to 60 mph", 64, CLOUD)
        P.text(540, CENTER - 430, "in 1/100 second!", 70, GLIM)
        chameleon(P, 300, CENTER + 360, .45, t)

def elephant(P, x, y, s, t, ear=1., flap=0., col=(150, 150, 160), veins=False, cool=0.):
    dark = dk(col, 190); fl = 1 + .12 * math.sin(t * (3 + 6 * flap)) * (.3 + flap)
    for side in (-1, 1):
        ex = x + side * 190 * s * ear * fl
        P.ell(ex, y + 20 * s, 170 * s * ear * fl, 220 * s * ear, dark)
        P.ell(ex + side * 8 * s, y + 20 * s, 150 * s * ear * fl, 200 * s * ear, lc(col, (240, 170, 170), .35))
        if veins:
            vc = lc((220, 60, 70), (90, 140, 230), cool)
            for k in range(5):
                a = -1.1 + k * .55; pts = [(ex - side * 60 * s * ear, y + 20 * s)]
                for j in range(1, 5): pts.append((ex - side * 60 * s * ear + side * math.cos(a) * j * 32 * s * ear * fl, y + 20 * s + math.sin(a) * j * 40 * s * ear + math.sin(j + k) * 8 * s))
                P.line(pts, vc, 8 * s)
    P.ell(x, y - 20 * s, 150 * s, 170 * s, col)
    tw = math.sin(t * 1.5) * 30 * s
    P.line([(x, y + 60 * s), (x - 5 * s, y + 200 * s), (x + 10 * s + tw, y + 320 * s), (x + 50 * s + tw, y + 360 * s)], col, 70 * s)
    P.line([(x + 30 * s + tw, y + 330 * s), (x + 55 * s + tw, y + 365 * s)], dark, 20 * s)
    for side in (-1, 1):
        P.line([(x + side * 55 * s, y + 90 * s), (x + side * 80 * s, y + 190 * s), (x + side * 60 * s, y + 230 * s)], (250, 245, 230), 22 * s)
        P.circ(x + side * 60 * s, y - 40 * s, 14 * s, NIGHT); P.circ(x + side * 56 * s, y - 45 * s, 5 * s, (255, 255, 255))

def sc_elephants(i, P, t, u):
    def savanna(y0=CENTER + 300):
        P.poly([(0, y0), (W, y0), (W, H), (0, H)], (200, 170, 100))
        P.ell(880, y0 - 40, 120, 40, (90, 140, 70)); P.line([(880, y0 - 30), (880, y0 + 40)], (110, 80, 50), 14)
    if i == 0:
        savanna(); elephant(P, 540, CENTER - 40, 1.2, t, flap=.4)
    elif i == 1:
        savanna(); P.circ(840, CENTER - 420, 90, (255, 210, 80), glow=mul(GLIM, 150))
        for k in range(5):
            q = (t * .6 + k / 5) % 1; x = 200 + k * 170
            P.line([(x + math.sin(q * 12) * 15, CENTER + 280 - q * 300), (x + math.sin(q * 12 + 1) * 15, CENTER + 230 - q * 300)], lc((255, 160, 80), (40, 40, 60), q), 8)
        elephant(P, 460, CENTER - 20, .9, t, flap=.2)
        P.rrect(860, CENTER - 200, 920, CENTER + 200, 30, CLOUD, outline=(170, 170, 180), w=5)
        h = 120 + 220 * eout(seg(u, .3, 3))
        P.rrect(872, CENTER + 188 - h, 908, CENTER + 188, 18, HOOK)
        P.text(540, CENTER + 470, "few sweat glands", 60, GLIM)
    elif i == 2:
        P.ell(540, CENTER, 380, 460, (120, 120, 135)); P.ell(555, CENTER, 345, 425, (215, 165, 165))
        k = seg(u, .2, 2.5); pulse = .5 + .5 * math.sin(t * 6)
        for j in range(7):
            a = -1.4 + j * .47; pts = [(240, CENTER)]
            n = int(1 + 6 * k)
            for m in range(1, n + 1): pts.append((240 + math.cos(a) * m * 55, CENTER + math.sin(a) * m * 65 + math.sin(m * 1.3 + j) * 15))
            P.line(pts, lc((200, 40, 60), (255, 90, 100), pulse), 12, glow=dk((255, 60, 80), 120))
        P.text(540, CENTER + 560, "blood vessels", 66, GLIM)
    elif i == 3:
        savanna()
        elephant(P, 540, CENTER - 40, 1.0, t, flap=1., veins=True, cool=eio(seg(u, .5, 3.0)))
        for k in range(6):
            q = (t * 1.2 + k / 6) % 1; side = 1 if k % 2 else -1
            P.line([(540 + side * (330 + q * 150), CENTER - 150 + k * 40), (540 + side * (390 + q * 150), CENTER - 150 + k * 40)], lc((200, 240, 255), (40, 60, 90), q), 8)
        P.text(540, CENTER + 470, "flap = cooler blood", 62, (170, 230, 255))
    elif i == 4:
        savanna()
        e = 1 + .35 * back(seg(u, 1.5, 2.2))
        elephant(P, 540, CENTER - 40, .95, t, ear=e)
        for k in range(3):
            q = (t * .7 + k / 3) % 1
            P.arc(-150, CENTER - 40, 200 + q * 300, -40, 40, lc(GLIM, (40, 40, 60), q), 10 * (1 - q) + 3)
        P.text(540, CENTER + 470, "look bigger!", 70, GLIM)
    else:
        savanna(CENTER + 200)
        elephant(P, 230, CENTER + 60, .45, t, flap=.3); elephant(P, 850, CENTER + 60, .45, t + 1, flap=.3)
        for k in range(4):
            q = (t * .4 + k / 4) % 1
            P.arc(230, CENTER + 40, 120 + q * 520, -25, 25, lc((255, 220, 140), (40, 40, 60), q), 12 * (1 - q) + 3)
        P.text(540, CENTER - 430, "rumbles km away", 66, GLIM)

def spider(P, x, y, s, t, col=(60, 55, 75), glands=0.):
    lite = lc(col, CLOUD, .35)
    for side in (-1, 1):
        for k in range(4):
            a = math.radians(-60 + k * 38) ; wig = math.sin(t * 4 + k) * 6 * s
            kx, ky = x + side * math.cos(a) * 110 * s, y - 60 * s + math.sin(a) * 70 * s - 50 * s
            P.line([(x + side * 30 * s, y - 20 * s + k * 12 * s), (kx, ky + wig), (kx + side * 70 * s, ky + 120 * s + wig)], col, 12 * s)
    P.ell(x, y + 90 * s, 95 * s, 110 * s, col)
    for k in range(3): P.ell(x, y + 60 * s + k * 40 * s, 40 * s - k * 8 * s, 10 * s, lite)
    if glands:
        for dx, dy, r_ in ((-35, 70, 26), (30, 90, 30), (-10, 130, 22), (35, 140, 18)):
            P.circ(x + dx * s, y + dy * s, r_ * s * glands, (255, 220, 120), glow=dk(GLIM, 200 * glands))
    P.ell(x, y - 20 * s, 60 * s, 55 * s, lc(col, (90, 80, 110), .5))
    for dx in (-22, -8, 8, 22): P.circ(x + dx * s, y - 40 * s, 7 * s, (20, 20, 30)); P.circ(x + dx * s + 2 * s, y - 42 * s, 2.5 * s, (255, 255, 255))

def web(P, x, y, r, k, col=(220, 230, 255), w=4):
    for j in range(12):
        a = j / 12 * 2 * math.pi; P.line([(x, y), (x + math.cos(a) * r, y + math.sin(a) * r)], col, w)
    n = int(120 * k); pts = []
    for m in range(n):
        a = m / 12 * 2 * math.pi; rr = r * (1 - m / 130); pts.append((x + math.cos(a) * rr, y + math.sin(a) * rr))
    if len(pts) > 1: P.line(pts, col, w * .8)

def sc_spiders(i, P, t, u):
    if i == 0:
        k = eio(seg(u, 0, 3)); web(P, 540, CENTER - 80, 400, .3 + .7 * k)
        spider(P, 540, CENTER - 120, .9, t)
    elif i == 1:
        spider(P, 540, CENTER - 60, 1.9, t, glands=eout(seg(u, .4, 1.4)))
        P.text(540, CENTER + 470, "silk glands", 70, GLIM)
    elif i == 2:
        spider(P, 540, CENTER - 160, 1.6, t, glands=1)
        for k, dx in enumerate((-35, 30, -10)):
            for j in range(4):
                q = (u * .8 + j / 4 + k * .2) % 1
                P.circ(lerp(540 + dx * 1.6, 540 + (k - 1) * 20, q), lerp(CENTER - 160 + 110 * 1.6, CENTER - 160 + 190 * 1.6, q), 10, GLIM, glow=dk(GLIM, 220))
        for k in range(3): P.ell(540 + (k - 1) * 22, CENTER - 160 + 195 * 1.6, 12, 18, (200, 190, 210))
        P.text(540, CENTER + 470, "spinnerets", 70, GLIM)
    elif i == 3:
        spider(P, 540, CENTER - 420, .9, t, glands=1)
        top = CENTER - 420 + 190 * .9; bot = CENTER + 380
        P.line([(540, top), (540, top + (bot - top) * eout(seg(u, .2, 2)))], (230, 240, 255), 6, glow=dk((200, 220, 255), 120))
        random.seed(11)
        for j in range(16):
            y = top + 40 + j * 40; q = clamp((y - top) / (bot - top))
            a = lerp(random.random() * 3.14, 1.57, eio(q * 1.4))
            x = 540 + lerp(random.random() * 120 - 60, 0, eio(q * 1.4)) + 70
            P.line([(x - math.cos(a) * 18, y - math.sin(a) * 18), (x + math.cos(a) * 18, y + math.sin(a) * 18)], GLIM, 6)
        P.text(270, top + 80, "liquid", 50, CLOUD); P.text(270, bot - 40, "solid!", 60, GLIM)
    elif i == 4:
        k = lambda d: back(seg(u, d, d + .5))
        if k(.2) > 0: web(P, 230, CENTER - 150, 170 * k(.2), 1, w=3)
        if k(.9) > 0:
            P.circ(540, CENTER - 150, 110 * k(.9), (245, 245, 250), outline=(200, 200, 215), w=4)
            for j in range(6): P.arc(540, CENTER - 150, 30 + j * 14, j * 50, j * 50 + 120, (215, 215, 230), 3)
        if k(1.6) > 0:
            P.line([(850, CENTER - 450), (850, CENTER - 150 + math.sin(t * 2) * 30)], (230, 240, 255), 4)
            spider(P, 850, CENTER - 120 + math.sin(t * 2) * 30, .55 * k(1.6), t)
        P.text(230, CENTER + 90, "webs", 46, CLOUD); P.text(540, CENTER + 90, "egg sacs", 46, CLOUD); P.text(850, CENTER + 90, "safety line", 46, CLOUD)
        P.text(540, CENTER + 400, "up to 7 kinds", 72, GLIM)
    else:
        P.rrect(150, CENTER + 120, 500, CENTER + 200, 14, (170, 180, 195), outline=(110, 120, 140), w=5)
        P.text(325, CENTER + 260, "steel", 52, CLOUD)
        P.line([(600, CENTER + 160), (950, CENTER + 160)], (230, 240, 255), 6, glow=dk((200, 220, 255), 160))
        P.text(775, CENTER + 260, "silk", 52, CLOUD)
        P.text(540, CENTER - 20, ">", 140 * back(seg(u, .5, 1)), GLIM)
        web(P, 540, CENTER - 230, 130, 1, w=3)
        P.text(540, CENTER - 450, "stronger by weight!", 66, GLIM)

SCENES = {"cats": sc_cats, "bees": sc_bees, "beavers": sc_beavers, "flamingos": sc_flamingos, "turtles": sc_turtles,
          "octopuses": sc_octopuses, "whales": sc_whales, "migration": sc_migration, "zebras": sc_zebras, "fireflies": sc_fireflies,
          "chameleons": sc_chameleons, "elephants": sc_elephants, "spiders": sc_spiders}[TOPIC]
PAL = {"cats": ((40, 30, 70), (110, 70, 120)), "bees": ((60, 40, 20), (160, 110, 40)), "beavers": ((20, 50, 60), (60, 130, 110)),
       "flamingos": ((60, 25, 60), (200, 110, 120)), "turtles": ((10, 40, 70), (40, 120, 150)),
       "octopuses": ((10, 35, 70), (40, 110, 140)), "whales": ((10, 30, 70), (30, 80, 150)), "migration": ((40, 90, 160), (150, 190, 230)),
       "zebras": ((90, 150, 190), (230, 200, 130)), "fireflies": ((10, 20, 50), (20, 50, 60)),
       "chameleons": ((20, 60, 50), (120, 170, 90)), "elephants": ((150, 110, 70), (240, 190, 120)), "spiders": ((15, 15, 40), (50, 40, 80))}[TOPIC]
HI = {"cats": {"purr?", "voice", "box,", "twenty", "thirty", "pad", "deep", "kittens", "days", "calm"},
      "bees": {"honey?", "nectar", "stomach.", "enzymes", "sugars.", "fan", "wings", "thick", "sweet.", "wax", "winter.", "twelfth", "teaspoon"},
      "beavers": {"dams?", "deep", "safe", "wolves", "bears.", "branches,", "mud", "stones", "underwater", "door", "frogs,", "fish,", "birds", "dragonflies.", "ecosystem", "engineers!"},
      "flamingos": {"pink?", "gray,", "food,", "algae", "shrimp.", "carotenoids,", "carrots", "orange.", "pink.", "dinner!"},
      "turtles": {"home?", "oceans", "decades", "same", "magnetic", "signature,", "invisible", "address.", "map.", "gps,", "nature!"},
      "octopuses": {"color", "blink?", "chromatophores.", "pigment,", "muscles.", "brain", "open,", "ink.", "reflect", "light,", "sense", "light"},
      "whales": {"sing?", "males", "twenty", "minutes,", "attract", "females,", "rival", "far", "underwater,", "kilometers.", "same", "song,", "changes", "ocean,", "pop", "hits!"},
      "migration": {"migrate?", "born", "genes.", "sun,", "stars", "north", "star.", "magnetic", "field,", "eyes.", "rivers,", "coastlines,", "smells", "seventy", "thousand"},
      "zebras": {"stripes?", "decades.", "horseflies", "disease.", "landed", "ease.", "failed", "slow", "missed", "confuse", "striped", "coats", "fewer"},
      "fireflies": {"glow?", "bodies.", "luciferin,", "luciferase.", "oxygen", "light.", "cold", "heat.", "pattern", "partner.", "switch", "oxygen!"},
      "chameleons": {"fast?", "folded", "bone,", "bow.", "muscle", "elastic", "spring.", "shoots", "twice", "sticky,", "mucus", "sixty", "hundredth"},
      "elephants": {"ears?", "hot", "sweat", "blood", "vessels,", "flapping", "cools", "sounds,", "bigger", "threatened.", "rumbles", "kilometers"},
      "spiders": {"silk?", "glands,", "liquid", "protein.", "spinnerets,", "nozzles", "pulls,", "line", "solid", "thread.", "seven", "stronger", "steel!"}}[TOPIC]

def kinetic(d, t, line, y, size):
    words = line["text"].split(); n = len(words); a0 = line["start"]; span = line["dur"] * .85
    f = font(size * S); fk = font(int(size * S * 1.12))
    isk = lambda w: w.lower() in HI or w.strip(".,!?").lower() in HI
    rows, cur, curw = [], [], 0
    for i, w in enumerate(words):
        ww = d.textlength(w + " ", font=fk if isk(w) else f)
        if curw + ww > (W - 150) * S and cur: rows.append(cur); cur, curw = [], 0
        cur.append((i, w, ww)); curw += ww
    rows.append(cur)
    lh = size * 1.2 * S; y0 = y * S - (len(rows) - 1) * lh / 2
    fade = 1 - eio(seg(t, a0 + line["dur"] + .15, a0 + line["dur"] + .45))
    for ri, row in enumerate(rows):
        x = (W * S - sum(r[2] for r in row) + d.textlength(" ", font=f)) / 2
        for i, w, ww in row:
            k = back((t - (a0 + span * i / n)) / .22)
            if k > .01 and fade > 0:
                key = isk(w); fs = int(size * S * (0.6 + .4 * k) * (1.12 if key else 1))
                col = lc(NIGHT, GLIM if key else CLOUD, fade)
                d.text((x, y0 + ri * lh + (1 - k) * 40 * S + (size * S * (1.12 if key else 1) - fs) * .5), w, font=font(fs), fill=col, stroke_width=int(7 * S), stroke_fill=NIGHT)
            x += ww

# ---------- Stile ----------
GAIN = {"classic": .5, "night": .75, "sunny": .22, "paper": .2}.get(STYLE, .5)
EDGE = {"classic": (5, 8, 20), "night": (2, 4, 14), "sunny": (255, 236, 205), "paper": (70, 52, 36)}.get(STYLE, (5, 8, 20))
VIG = Image.new("L", (W, H), 0); vd = ImageDraw.Draw(VIG)
for i in range(40): vd.ellipse([-W * .35 + i * 6, -H * .2 + i * 8, W * 1.35 - i * 6, H * 1.2 - i * 8], fill=int(i * 6.3))
VIG = VIG.filter(ImageFilter.GaussianBlur(60)).point(lambda v: min(255, (200 if STYLE in ("sunny", "paper") else 160) + v)); DARK = Image.new("RGB", (W, H), EDGE)
random.seed(3); DUST = [(random.random() * W, random.random() * H, random.random() * 3 + 1.5, random.random() * 6.28) for _ in range(60)]
STARS = [(random.random() * W, random.random() * H * .8, random.random() * 2.5 + 1, random.random() * 6.28) for _ in range(150)]
BLOBS = [(random.random() * W, random.random() * H, 160 + random.random() * 220, random.random() * 6.28) for _ in range(9)]
if STYLE == "paper":
    _g = Image.effect_noise((W // 2, H // 2), 40).resize((W, H), Image.BILINEAR).filter(ImageFilter.GaussianBlur(1))
    GRAIN = Image.merge("RGB", [_g.point(lambda v: int(228 + v * 27 / 255))] * 3)
    FIBER = Image.new("L", (W, H), 255); fd = ImageDraw.Draw(FIBER)
    for _ in range(500):
        x, y = random.random() * W, random.random() * H; a = random.random() * 6.28; ln = 8 + random.random() * 30
        fd.line([(x, y), (x + math.cos(a) * ln, y + math.sin(a) * ln)], fill=232, width=1)
    GRAIN = ImageChops.multiply(GRAIN, Image.merge("RGB", [FIBER] * 3))

def background(d, Pb, t):
    top, bot = PAL
    if STYLE == "night":
        a, b = lc(NIGHT, (2, 4, 14), .4), lc(top, NIGHT, .55)
        for yy in range(0, H * S, 12): d.rectangle([0, yy, W * S, yy + 12], fill=lc(a, b, yy / (H * S)))
        for x, y, r, ph in STARS:
            tw = .5 + .5 * math.sin(t * 2.2 + ph)
            Pb.circ(x, y, r * (.7 + .5 * tw), lc(b, CLOUD, .35 + .6 * tw), glow=mul(GLIM, 70 * tw) if r > 3.1 else None)
        Pb.circ(960, 110, 50, (250, 240, 210), glow=mul((255, 230, 160), 60)); Pb.circ(978, 96, 44, a)
        return
    if STYLE == "sunny":
        a, b = lc(bot, (255, 246, 230), .55), (255, 214, 170)
        for yy in range(0, H * S, 12): d.rectangle([0, yy, W * S, yy + 12], fill=lc(a, b, yy / (H * S)))
        for x, y, r, ph in BLOBS:
            Pb.circ(x + math.sin(t * .3 + ph) * 40, y + math.cos(t * .25 + ph) * 50, r, lc(lc(a, b, y / H), (255, 255, 255), .3))
        return
    if STYLE == "paper":
        a, b = lc(top, (244, 232, 210), .9), lc(bot, (244, 232, 210), .78)
        for yy in range(0, H * S, 12): d.rectangle([0, yy, W * S, yy + 12], fill=lc(a, b, yy / (H * S)))
        for k in range(3):                                   # Papierstreifen im Hintergrund
            y0 = 380 + k * 520 + math.sin(t * .4 + k) * 12
            Pb.poly([(0, y0), (W, y0 - 60), (W, y0 + 40), (0, y0 + 110)], lc(a, b, .3 + k * .25))
        return
    for yy in range(0, H * S, 12): d.rectangle([0, yy, W * S, yy + 12], fill=lc(top, bot, yy / (H * S)))
    for x, y, r, ph in DUST:
        tw = .5 + .5 * math.sin(t * 1.5 + ph); Pb.circ(x, (y - t * 20 * r) % H, r, lc(top, CLOUD, .25 * tw))

def frame(t):
    base = Image.new("RGB", (W * S, H * S)); glow = Image.new("RGB", (W * S, H * S))
    d, g = ImageDraw.Draw(base), ImageDraw.Draw(glow)
    i = scene_of(t); u = t - T[i]
    cam0 = Cam(); Pb = Pen(d, g, cam0)
    background(d, Pb, t)
    if STYLE == "paper":
        lay = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0)); dl = ImageDraw.Draw(lay)
    else: lay, dl = None, d
    pop = back(seg(t, T[i] - .25, T[i] + .35)); z = (0.92 + .08 * pop) * (1 + .03 * math.sin(t * .6))
    P = Pen(dl, g, Cam(z, W / 2, H / 2 + 40))
    SCENES(i, P, t, u)
    talking = 0
    for l in L:
        if l["start"] <= t < l["start"] + l["dur"]: talking = .5 + .5 * math.sin(t * 22)
    last = i == len(L) - 1
    mood = "joy" if last else ("wow" if i in (2,) and u < 1.5 else "happy")
    gp = back(seg(t, .1, .6)); hop = abs(math.sin(t * 3)) * 22 if last else math.sin(t * 2.2) * 10
    Pg = Pen(dl, g, cam0)
    gx, gy, gs = (760, 1660, .8) if last else (900, 1700, .62)
    glim(Pg, gx, gy - hop, max(.02, gp) * gs, t, mood, talking, wave=1 if (last or t < 2) else 0, squash=max(0, 1 - gp) * .5)
    if lay is not None:                                       # Papierschnitt: weicher Schlagschatten
        al = lay.split()[3].resize((W // 4, H // 4), Image.BILINEAR).filter(ImageFilter.GaussianBlur(4)).point(lambda v: int(v * .5))
        sh = al.resize((W * S, H * S), Image.BILINEAR)
        base.paste((45, 30, 20), (int(10 * S), int(16 * S)), ImageChops.offset(sh, 0, 0).crop((0, 0, W * S - int(10 * S), H * S - int(16 * S))))
        base.paste(lay, (0, 0), lay)
    for k, l in enumerate(L):
        if l["start"] - .1 <= t < l["start"] + l["dur"] + .5: kinetic(d, t, l, 330 if k else 380, 86 if k == 0 else 64)
    end = eout(seg(t, DUR - 1.7, DUR - 1.3))
    if end > 0:
        f = font(54 * S); s_ = "Follow for more WHY?"; w = d.textlength(s_, font=f); yo = (1 - end) * 60 * S
        d.rounded_rectangle([(W * S - w) / 2 - 40 * S, 1490 * S + yo, (W * S + w) / 2 + 40 * S, 1590 * S + yo], 50 * S, fill=HOOK)
        d.text((W * S / 2, 1540 * S + yo), s_, font=f, fill=CLOUD, anchor="mm")
    small = glow.point(lambda v: int(v * GAIN)).resize((W // 4, H // 4), Image.BILINEAR).filter(ImageFilter.GaussianBlur(8))
    img = ImageChops.add(base, small.resize((W * S, H * S), Image.BILINEAR)).resize((W, H), Image.LANCZOS)
    if STYLE == "paper": img = ImageChops.multiply(img, GRAIN)
    fl = max([0] + [1 - abs(t - (s - .25)) / .18 for s in T[1:]])
    if fl > 0: img = Image.blend(img, Image.new("RGB", (W, H), (255, 255, 255)), eio(fl) * .55)
    return Image.composite(img, DARK, VIG)

off = int(sys.argv[4]) if len(sys.argv) > 4 else 0; step = int(sys.argv[5]) if len(sys.argv) > 5 else 1
for fi in range(off, int(DUR * FPS), step): frame(fi / FPS).save(f"{OUT}/f{fi:04d}.png")
