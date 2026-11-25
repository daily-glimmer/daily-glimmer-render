# Thema: Do cows really have best friends?  (Mythos-Format, Stempel TRUE / FACT) – erstes Video im Gouache-Stil (26.11.2026)
# Quelle: K. McLennan, University of Northampton – Kühe mit bevorzugter Partnerin, 30 Min im Pferch mit Partnerin vs. fremder Kuh, Herzfrequenz niedriger mit Partnerin.
exec(open(os.path.join(HERE, "topics", "cows.py")).read(), globals())   # cow(), meadow(), Farben
PAL = ((150, 205, 240), (200, 228, 160))
HI = {"best", "friends?", "True!", "favorite", "buddy", "together.", "30", "minutes", "stranger.", "slower", "calmer.", "relaxed!", "friend?"}
WOW = (1, 4)
BROWN = (196, 150, 110)

class Flip:
    """Pen-Hülle, die alles um die senkrechte Achse cx spiegelt (für eine nach rechts schauende Kuh)."""
    def __init__(s, P, cx): s.P, s.cx = P, cx
    def fx(s, x): return 2 * s.cx - x
    def ell(s, x, y, rx, ry, fill, glow=None, outline=None, w=0): s.P.ell(s.fx(x), y, rx, ry, fill, glow, outline, w)
    def circ(s, x, y, r, fill, glow=None, outline=None, w=0): s.P.circ(s.fx(x), y, r, fill, glow, outline, w)
    def poly(s, pts, fill, outline=None, w=0): s.P.poly([(s.fx(x), y) for x, y in pts], fill, outline, w)
    def line(s, pts, col, w, glow=None): s.P.line([(s.fx(x), y) for x, y in pts], col, w, glow)
    def rrect(s, x0, y0, x1, y1, r, fill, outline=None, w=0): s.P.rrect(s.fx(x1), y0, s.fx(x0), y1, r, fill, outline, w)
    def arc(s, x, y, r, a0, a1, col, w): s.P.arc(s.fx(x), y, r, 180 - a1, 180 - a0, col, w)

def cow_r(P, x, y, s, t, **kw):     # Kuh, die nach rechts schaut
    cow(Flip(P, x), x, y, s, t, **kw)

def heart_pop(P, x, y, r, k, col=HOOK):
    if k > 0: P.heart(x, y - 30 * k, r * back(k), col)

def fence(P, x0, x1, y0, y1):
    for x in range(int(x0), int(x1) + 1, 70): P.rrect(x - 9, y0, x + 9, y1, 6, BROWN, outline=lc(BROWN, NIGHT, .5), w=3)
    for yy in (y0 + 40, y0 + (y1 - y0) * .6): P.rrect(x0 - 20, yy, x1 + 20, yy + 18, 6, BROWN, outline=lc(BROWN, NIGHT, .5), w=3)

def pulse(P, x0, y, w, t, fast, col):
    pts = []; per = 70 if fast else 150
    for k in range(0, int(w), 6):
        ph = ((k + t * (260 if fast else 110)) % per) / per
        v = -70 if .42 < ph < .48 else (40 if .48 <= ph < .54 else 0)
        pts.append((x0 + k, y + v))
    if len(pts) > 1: P.line(pts, col, 7)

def SC(i, P, t, u):
    meadow(P)
    if i == 0:      # zwei Kühe, Fragezeichen
        cow_r(P, 290, CENTER + 330, .85, t); cow(P, 800, CENTER + 330, .85, t)
        P.text(540, CENTER + 20, "?", 150 * back(seg(u, .3, .8)), GLIM)
    elif i == 1:    # TRUE: Kühe kuscheln, Herzen
        k = eio(seg(u, 0, 1.0))
        cow_r(P, 250 + 80 * k, CENTER + 330, .85, t, happy=True); cow(P, 840 - 80 * k, CENTER + 330, .85, t, happy=True)
        for j in range(3): heart_pop(P, 470 + j * 70, CENTER + 60 - j * 50, 40, seg(u, 1.0 + j * .3, 1.6 + j * .3))
        P.stamp(540, CENTER - 230, "TRUE", seg(u, .25, .7), col=HOPE)
    elif i == 2:    # Herde, zwei Freundinnen markiert
        for j, (x, y, s) in enumerate(((190, CENTER + 200, .42), (890, CENTER + 190, .42), (560, CENTER + 150, .34), (300, CENTER + 520, .46), (820, CENTER + 520, .46))):
            (cow_r if j % 2 else cow)(P, x, y, s, t + j)
        k = seg(u, .8, 1.6)
        cow_r(P, 420, CENTER + 360, .56, t, happy=True); cow(P, 700, CENTER + 360, .56, t, happy=True)
        if k > 0: P.ell(560, CENTER + 380, 360 * back(k), 170 * back(k), None, outline=GLIM, w=10)
        P.badge(560, CENTER - 60, "best buddies", 54, HOPE, k=seg(u, 1.6, 2.1))
    elif i == 3:    # 30 Minuten im Pferch: Freundin vs. Fremde
        for side, (x0, mate) in enumerate(((60, "buddy"), (570, "stranger"))):
            fence(P, x0, x0 + 450, CENTER + 150, CENTER + 430)
            cow_r(P, x0 + 120, CENTER + 320, .42, t, happy=side == 0)
            if side == 0: cow(P, x0 + 330, CENTER + 320, .42, t, happy=True)
            else: cow(P, x0 + 330, CENTER + 320, .42, t)
            P.badge(x0 + 225, CENTER + 540, mate, 44, HOPE if side == 0 else HOOK, k=seg(u, 1.0 + side * .5, 1.5 + side * .5))
        k = seg(u, .2, .7)
        if k > 0:
            P.circ(540, CENTER - 60, 95 * back(k), CLOUD, outline=NIGHT, w=8)
            a = math.radians(-90 + 360 * seg(u, .7, 5.0) * .5)
            P.line([(540, CENTER - 60), (540 + 70 * math.cos(a), CENTER - 60 + 70 * math.sin(a))], HOOK, 8)
            P.badge(540, CENTER + 80, "30 min", 50, NIGHT, k=k)
    elif i == 4:    # Herzschlag: ruhig mit Freundin, schnell mit Fremder
        for row, (fast, col, lab) in enumerate(((False, HOPE, "with buddy"), (True, HOOK, "with stranger"))):
            y = CENTER + 20 + row * 330
            P.rrect(90, y - 120, 990, y + 110, 30, CLOUD, outline=lc(col, NIGHT, .3), w=6)
            pulse(P, 130, y, 820 * seg(u, .3 + row * .4, 1.6 + row * .4), t, fast, col)
            P.heart(170, y - 70, 26 * (1 + .15 * math.sin(t * (14 if fast else 6))), col)
            P.badge(760, y - 70, lab, 40, col, k=seg(u, .6 + row * .4, 1.0 + row * .4))
        P.badge(540, CENTER + 500, "calmer", 60, HOPE, k=seg(u, 2.2, 2.7))
    else:           # FACT: Freundinnen zusammen
        cow_r(P, 330, CENTER + 330, .85, t, happy=True); cow(P, 760, CENTER + 330, .85, t, happy=True)
        for j in range(4): heart_pop(P, 380 + j * 110, CENTER + 40 - (j % 2) * 60, 36, seg(u, .4 + j * .25, 1.0 + j * .25), (255, 120, 140))
        P.stamp(540, CENTER - 200, "FACT", seg(u, .25, .7), col=HOPE)
