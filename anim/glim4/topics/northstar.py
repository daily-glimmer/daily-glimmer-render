# Thema: Is the North Star the brightest star in the sky?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6)
# Quellen: EarthSky "Polaris is the present-day North Star" (etwa 48. hellster Stern; steht fast über dem Nordpol,
# Kastensterne des Großen Wagens zeigen hin), EarthSky/Farmer's Almanac: Sirius hellster Stern, ~8,6 Lichtjahre.
CENTER = 1050
STARC, POL, SIR = (255, 250, 230), (255, 230, 150), (200, 225, 255)
PAL = ((8, 12, 35), (30, 40, 80))
HI = {"north", "brightest", "myth!", "forty", "eighth", "sirius", "still", "north.", "pole,", "dipper", "steady", "shiniest!"}
WOW = (1,)

def star(P, x, y, r, col, t, tw=0.):
    k = 1 + tw * math.sin(t * 5 + x)
    P.circ(x, y, r * k, col, glow=mul(col, 140))
    P.line([(x - r * 2.2 * k, y), (x + r * 2.2 * k, y)], col, max(2, r * .25))
    P.line([(x, y - r * 2.2 * k), (x, y + r * 2.2 * k)], col, max(2, r * .25))

def field(P, t, n=40, seed=6):
    random.seed(seed)
    for _ in range(n): P.circ(40 + random.random() * 1000, CENTER - 450 + random.random() * 900, 2 + random.random() * 4, (200, 205, 230))

def hills(P): P.poly([(0, CENTER + 420), (300, CENTER + 360), (700, CENTER + 400), (W, CENTER + 340), (W, H), (0, H)], (10, 14, 28))

def dipper(P, x, y, s, a=0.):
    pts = [(0, 0), (60, -30), (120, -40), (185, -30), (200, 50), (290, 60), (300, -20)]
    ca, sa = math.cos(a), math.sin(a)
    q = [(x + (px * ca - py * sa) * s, y + (px * sa + py * ca) * s) for px, py in pts]
    P.line(q[:4] + [q[4], q[5], q[6], q[3]], (90, 100, 150), 4)
    for p in q: P.circ(*p, 9, STARC)
    return q

def SC(i, P, t, u):
    if i == 0:
        field(P, t); hills(P)
        star(P, 540, CENTER - 200, 26, POL, t)
        P.text(800, CENTER - 360, "?", 150 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        field(P, t); hills(P)
        star(P, 420, CENTER - 200, 20, POL, t); star(P, 760, CENTER + 60, 30 * back(seg(u, .8, 1.4)) + .1, SIR, t, .08)
        P.stamp(560, CENTER - 400, "MYTH", seg(u, .25, .7), rot=-6)
    elif i == 2:
        field(P, t, 25)
        n = int(lerp(1, 48, eio(seg(u, .3, 2.2))))
        P.text(540, CENTER - 150, f"#{n}", 180, POL)
        star(P, 540, CENTER + 180, 22, POL, t)
        P.badge(540, CENTER + 380, "Polaris rank", 56, (70, 85, 150), CLOUD, back(seg(u, .5, 1.0)))
    elif i == 3:
        field(P, t, 25)
        star(P, 540, CENTER - 60, 42, SIR, t, .1)
        P.badge(540, CENTER + 200, "Sirius: number 1", 60, GLIM, NIGHT, back(seg(u, .5, 1.0)))
        P.badge(540, CENTER + 340, "8.6 light-years away", 52, (70, 85, 150), CLOUD, back(seg(u, 1.6, 2.1)))
    elif i == 4:
        field(P, t, 30); hills(P)
        cx, cy = 540, CENTER - 230
        for r in (140, 240, 340):
            a0 = (t * 25) % 360
            P.arc(cx, cy, r, a0, a0 + 110, (70, 80, 130), 5)
        star(P, cx, cy, 22, POL, t)
        q = dipper(P, 330, CENTER + 120, 1.2, math.sin(t * .2) * .1)
        k = eout(seg(u, 1.4, 2.4))
        P.line([q[4], (lerp(q[4][0], cx, k), lerp(q[4][1], cy, k))], GLIM, 6)
        P.badge(540, CENTER + 400, "stays put in the north", 54, (70, 85, 150), CLOUD, back(seg(u, .6, 1.1)))
    else:
        field(P, t); hills(P)
        star(P, 420, CENTER - 120, 22, POL, t)
        P.stamp(780, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
