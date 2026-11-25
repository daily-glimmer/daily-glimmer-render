# Thema: Why do sea otters hold hands?
CENTER = 1050
FUR, FUR2, FACE = (125, 88, 62), (85, 58, 42), (215, 190, 160)
KELP, KELP2 = (95, 140, 60), (60, 100, 45)
PAL = ((150, 205, 235), (200, 230, 245))
HI = {"otters", "hands?", "backs", "ocean.", "wind", "currents", "away", "paws", "kelp,", "rafts.", "dozens", "pups", "thickest", "million", "hairs"}
WOW = (3, 5)
SURF = CENTER + 120

def dk(c, k): return tuple(int(v * k) for v in c)

def sea(P, t, y=SURF, sun=True):
    P.poly([(0, 0), (W, 0), (W, y + 10), (0, y + 10)], (170, 215, 240))
    if sun: P.circ(900, CENTER - 180, 70, (255, 225, 120))
    wv = [(x, y + math.sin(x / 80 + t * 1.6) * 9) for x in range(0, 1081, 40)]
    P.poly([(0, y)] + wv + [(W, H), (0, H)], (30, 95, 150))
    P.poly([(0, y)] + wv + [(W, y + 16), (0, y + 16)], (100, 175, 220))

def kelp(P, x, y0, t, h=260, s=1.):
    pts = [(x + math.sin(t * 1.3 + k * .6) * 16 * s * k / 8, y0 - k * h / 8) for k in range(9)]
    P.line(pts, KELP2, 14 * s)
    for k in range(2, 9, 2):
        px, py = pts[k]
        P.ell(px + 22 * s, py, 26 * s, 11 * s, KELP)

def otter(P, x, y, s, t, f=1, sleep=0., bob=0., paw=0., pup=False):
    """Seeotter auf dem Rücken treibend; f = Blickrichtung (Kopf links bei f=1), paw = Arm ausgestreckt (0..1)."""
    y = y + math.sin(t * 1.4 + bob) * 8 * s
    def X(dx): return x + f * dx * s
    P.ell(X(150), y + 5 * s, 90 * s, 26 * s, FUR2)                       # Schwanz
    P.ell(X(10), y, 165 * s, 62 * s, FUR, outline=FUR2, w=5 * s)         # Körper
    P.ell(X(0), y - 22 * s, 120 * s, 30 * s, lc(FUR, FACE, .35))           # Bauch
    for d in (0, 34):                                                     # Hinterpfoten
        P.ell(X(165 + d), y - 50 * s, 18 * s, 36 * s, FUR2)
    if pup:
        P.ell(X(10), y - 62 * s, 62 * s, 30 * s, (190, 160, 130), outline=FUR2, w=4 * s)
        P.circ(X(-48), y - 70 * s, 26 * s, (225, 205, 180), outline=FUR2, w=3 * s)
        P.arc(X(-52), y - 74 * s, 7 * s, 20, 160, NIGHT, 3 * s)
    hx, hy = X(-170), y - 18 * s                                          # Kopf
    for d in (-1, 1): P.circ(hx + d * 40 * s, hy - 52 * s, 14 * s, FUR2)
    P.circ(hx, hy, 62 * s, FUR, outline=FUR2, w=5 * s)
    P.ell(hx - f * 6 * s, hy + 6 * s, 48 * s, 42 * s, FACE)
    P.ell(hx - f * 12 * s, hy + 10 * s, 15 * s, 10 * s, NIGHT)
    for d in (-1, 1):
        ex = hx - f * 12 * s + d * 26 * s
        if sleep > .5: P.arc(ex, hy - 14 * s, 10 * s, 20, 160, NIGHT, 4 * s)
        else: P.circ(ex, hy - 14 * s, 8 * s, NIGHT); P.circ(ex + 2 * s, hy - 17 * s, 3 * s, CLOUD)
    P.arc(hx - f * 12 * s, hy + 20 * s, 12 * s, 30, 150, NIGHT, 3 * s)
    for d in (-1, 1):                                                     # Schnurrhaare
        P.line([(hx - f * 12 * s + d * 18 * s, hy + 14 * s), (hx - f * 12 * s + d * 50 * s, hy + 8 * s)], CLOUD, 2 * s)
    # Vorderpfote: auf der Brust (paw=0) oder zur Seite ausgestreckt (paw=1)
    sx, sy = X(-90), y - 40 * s
    ex_, ey_ = lerp(X(-60), X(-260), paw), lerp(y - 80 * s, y - 70 * s, paw)
    P.line([(sx, sy), (ex_, ey_)], FUR2, 22 * s)
    P.circ(ex_, ey_, 15 * s, FUR2)
    if sleep > .5:
        for k in range(3):
            q = (t * .5 + k / 3) % 1
            P.text(hx - f * (40 * s + q * 60), hy - 90 * s - q * 140, "z", (34 + 18 * k) * s * (1 - q * .3), NIGHT)

def SC(i, P, t, u):
    sea(P, t, sun=i != 5)
    if i == 0:
        otter(P, 290, SURF, .85, t, f=-1, sleep=1, paw=1)
        otter(P, 790, SURF + 4, .85, t, f=1, sleep=1, bob=.3, paw=1)
        P.heart(545, SURF - 210 - 10 * math.sin(t * 3), 50 * back(seg(u, .3, .8)), HOOK)
        P.text(540, CENTER - 300, "?", 150 * back(seg(u, .5, 1.0)), HOOK)
    elif i == 1:
        otter(P, 560, SURF, 1.25, t, sleep=eio(seg(u, 1.0, 1.4)))
        P.badge(540, SURF + 320, "nap on their backs", 58, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
    elif i == 2:
        k = eio(seg(u, .4, 3.6))
        otter(P, 380 - 170 * k, SURF, .85, t, sleep=1)
        otter(P, 720 + 170 * k, SURF + 10, .85, t, f=-1, sleep=1, bob=1.5)
        for j in range(3):
            q = (t * .8 + j / 3) % 1
            yy = CENTER - 180 + j * 70
            P.line([(160 + q * 120, yy), (300 + q * 120, yy)], lc(CLOUD, (170, 215, 240), q), 8)
            P.line([(920 - q * 120, yy), (780 - q * 120, yy)], lc(CLOUD, (170, 215, 240), q), 8)
        P.badge(540, SURF + 320, "drifting apart", 58, HOOK, CLOUD, back(seg(u, 1.6, 2.1)))
    elif i == 3:
        p = eio(seg(u, .3, 1.3))
        otter(P, 290, SURF, .85, t, f=-1, sleep=1, paw=p)
        otter(P, 790, SURF + 4, .85, t, f=1, sleep=1, bob=.3, paw=p)
        for kx in (130, 950):
            kelp(P, kx, SURF + 200, t, 380 * eout(seg(u, 1.6, 2.6)) + 1, 1.2)
        if p > .95: P.heart(545, SURF - 170 - 8 * math.sin(t * 3), 40 * back(seg(u, 1.3, 1.7)), HOOK)
        P.badge(540, SURF + 320, "raft", 64, HOPE, CLOUD, back(seg(u, 3.0, 3.5)))
    elif i == 4:
        spots = [(200, SURF - 40, .45), (520, SURF - 50, .45), (850, SURF - 35, .45),
                 (330, SURF + 70, .5), (720, SURF + 75, .5)]
        for n, (ox, oy, sc) in enumerate(sorted(spots, key=lambda q: q[1])):
            otter(P, ox, oy, sc * back(seg(u, .2 + n * .15, .6 + n * .15)), t, f=1 if n % 2 else -1, sleep=0, bob=n)
        otter(P, 540, SURF + 210, .9, t, sleep=0, pup=u > 2.6, bob=2)
        if u > 2.6: P.heart(540, SURF + 70 - 10 * math.sin(t * 3), 34 * back(seg(u, 2.6, 3.0)), HOOK)
        P.badge(540, CENTER - 300, "dozens together", 56, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
    else:
        otter(P, 540, SURF + 40, 1.3, t, sleep=0, paw=0)
        k = eout(seg(u, .4, 1.6))
        for j in range(26):                                           # Fell-Lupe
            a = j / 26 * 2 * math.pi
            P.line([(820 + 70 * math.cos(a) * .3, CENTER - 110 + 70 * math.sin(a) * .3),
                    (820 + 70 * math.cos(a) * k, CENTER - 110 + 70 * math.sin(a) * k)], FUR2, 4)
        P.arc(820, CENTER - 110, 90, 0, 360, NIGHT, 10)
        P.line([(760, CENTER - 45), (700, CENTER + 30)], NIGHT, 16)
        P.badge(380, CENTER - 110, "1,000,000 hairs", 50, NIGHT, GLIM, back(seg(u, 2.0, 2.5)))
