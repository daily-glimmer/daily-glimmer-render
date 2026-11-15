# Thema: How long do giraffes sleep?
CENTER = 1050
COAT, SPOT, MANE = (240, 185, 95), (170, 95, 45), (150, 85, 40)
PAL = ((20, 30, 75), (60, 70, 130))
HI = {"sleep?", "tiny", "naps.", "standing", "lions.", "four", "half", "hours", "deep", "lies", "down", "minutes"}
WOW = (3, 4)
GROUND = CENTER + 330

def land(P, t):
    P.poly([(0, GROUND), (W, GROUND - 20), (W, H), (0, H)], (60, 75, 50))
    for x, s in ((120, 1.), (960, .8)):          # Akazien
        P.line([(x, GROUND), (x + 10, GROUND - 240 * s)], (70, 50, 35), 22 * s)
        P.ell(x + 10, GROUND - 260 * s, 140 * s, 40 * s, (50, 95, 55))

def moon(P, t, x=900, y=CENTER - 400):
    P.circ(x, y, 70, (250, 240, 200)); P.circ(x + 30, y - 18, 62, PAL[0])

def zz(P, x, y, t, n=3):
    for k in range(n):
        q = (t * .45 + k / n) % 1
        P.text(x + q * 90 + k * 10, y - q * 220, "z", 40 + 40 * q, lc(CLOUD, PAL[0], max(0, q - .6) * 2.5))

def spots(P, pts, r):
    for (px, py) in pts: P.ell(px, py, r, r * .8, SPOT)

def head(P, hx, hy, s, sleepy, ang=0.):
    for dx in (-14, 14): P.line([(hx + dx * s, hy - 20 * s), (hx + dx * 1.3 * s, hy - 62 * s)], MANE, 9 * s); P.circ(hx + dx * 1.3 * s, hy - 64 * s, 9 * s, (90, 55, 30))
    P.ell(hx - 34 * s, hy - 14 * s, 20 * s, 10 * s, COAT); P.ell(hx + 34 * s, hy - 14 * s, 20 * s, 10 * s, COAT)
    P.ell(hx, hy, 34 * s, 40 * s, COAT); P.ell(hx, hy + 34 * s, 28 * s, 22 * s, (225, 160, 90))
    for ex in (-15, 15):
        if sleepy: P.arc(hx + ex * s, hy - 4 * s, 8 * s, 20, 160, NIGHT, 4 * s)
        else: P.circ(hx + ex * s, hy - 4 * s, 6 * s, NIGHT)
    P.circ(hx - 9 * s, hy + 38 * s, 4 * s, (110, 60, 30)); P.circ(hx + 9 * s, hy + 38 * s, 4 * s, (110, 60, 30))

def giraffe(P, x, y, s, t, sleepy=True, sway=1.):
    """stehende Giraffe, Hufe bei y"""
    sw = math.sin(t * 1.1) * 8 * s * sway
    bx, by = x, y - 330 * s
    for dx in (-110, -70, 75, 115):
        P.line([(bx + dx * s, by + 30 * s), (bx + dx * s, y)], COAT, 22 * s); P.rrect(bx + dx * s - 13 * s, y - 16 * s, bx + dx * s + 13 * s, y, 4 * s, (90, 55, 30))
    P.line([(bx - 150 * s, by - 10 * s), (bx - 185 * s, by + 120 * s + sw)], COAT, 8 * s)
    P.ell(bx, by, 160 * s, 78 * s, COAT)
    spots(P, [(bx - 90 * s, by - 20 * s), (bx - 20 * s, by - 35 * s), (bx + 55 * s, by - 10 * s), (bx - 55 * s, by + 30 * s), (bx + 20 * s, by + 35 * s), (bx + 105 * s, by + 25 * s)], 22 * s)
    hx, hy = bx + 215 * s + sw, by - 380 * s + abs(sw) * .5
    P.line([(bx + 110 * s, by - 20 * s), (hx - 10 * s, hy + 40 * s)], COAT, 52 * s)
    P.line([(bx + 95 * s, by - 50 * s), (hx - 40 * s, hy + 20 * s)], MANE, 10 * s)
    for k in range(4):
        q = .18 + k * .2; spots(P, [(lerp(bx + 115 * s, hx - 10 * s, q), lerp(by - 20 * s, hy + 40 * s, q))], 14 * s)
    head(P, hx, hy, s, sleepy)

def giraffe_lying(P, x, y, s, t, k=1.):
    """liegende Giraffe; k: Hals 0 = aufrecht, 1 = Kopf ruht auf dem Körper"""
    br = 1 + .03 * math.sin(t * 1.6)
    bx, by = x, y - 80 * s
    for dx in (-90, 60): P.ell(bx + dx * s, y - 16 * s, 70 * s, 18 * s, COAT)
    P.ell(bx, by, 170 * s, 75 * s * br, COAT)
    spots(P, [(bx - 100 * s, by - 20 * s), (bx - 30 * s, by - 35 * s), (bx + 45 * s, by - 20 * s), (bx - 60 * s, by + 25 * s), (bx + 30 * s, by + 30 * s), (bx + 110 * s, by + 10 * s)], 22 * s)
    P.line([(bx - 165 * s, by), (bx - 200 * s, by + 50 * s)], COAT, 8 * s)
    # Hals als Kurve: Basis vorne, Kopf je nach k oben vorn bzw. hinten auf dem Rücken
    base = (bx + 130 * s, by - 30 * s)
    hx = lerp(bx + 230 * s, bx - 90 * s, eio(k)); hy = lerp(by - 400 * s, by - 105 * s, eio(k))
    cx, cy = lerp(bx + 220 * s, bx + 120 * s, k), lerp(by - 220 * s, by - 330 * s, k)
    pts = [(lerp(lerp(base[0], cx, q), lerp(cx, hx, q), q), lerp(lerp(base[1], cy, q), lerp(cy, hy, q), q)) for q in [j / 12 for j in range(13)]]
    P.line(pts, COAT, 48 * s)
    for q in (.3, .55, .78): spots(P, [pts[int(q * 12)]], 13 * s)
    head(P, hx, hy, s, k > .5)

def clock(P, x, y, r, frac, col=GLIM):
    P.circ(x, y, r, (30, 40, 80), outline=CLOUD, w=10)
    n = 28; a1 = -90 + 360 * frac
    if frac > .01:
        P.poly([(x, y)] + [(x + math.cos(math.radians(lerp(-90, a1, j / n))) * r * .9, y + math.sin(math.radians(lerp(-90, a1, j / n))) * r * .9) for j in range(n + 1)], col)
    for h in range(12):
        a = math.radians(h * 30); P.circ(x + math.cos(a) * r * .8, y + math.sin(a) * r * .8, 6, CLOUD)

def lion(P, x, y, s, t):
    P.ell(x, y - 70 * s, 110 * s, 55 * s, (190, 140, 70))
    for dx in (-70, 70): P.line([(x + dx * s, y - 40 * s), (x + dx * s, y)], (190, 140, 70), 22 * s)
    P.circ(x + 100 * s, y - 110 * s, 62 * s, (140, 85, 40)); P.circ(x + 108 * s, y - 108 * s, 40 * s, (205, 155, 80))
    for ex in (-12, 14): P.circ(x + 108 * s + ex * s, y - 114 * s, 5 * s, NIGHT)

def SC(i, P, t, u):
    if i == 0:
        moon(P, t); land(P, t); giraffe(P, 430, GROUND + 10, 1.05, t)
        zz(P, 680, CENTER - 300, t)
        P.text(820, CENTER - 80, "?", 150 * back(seg(u, .4, .9)), GLIM)
    elif i == 1:
        moon(P, t); land(P, t)
        clock(P, 540, CENTER - 120, 230, .06 * eout(seg(u, .5, 1.8)))
        P.badge(540, CENTER + 220, "tiny naps", 64, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
    elif i == 2:
        moon(P, t); land(P, t); giraffe(P, 560, GROUND + 10, 1.0, t)
        zz(P, 820, CENTER - 330, t, 2)
        lion(P, lerp(-200, 120, eout(seg(u, 1.2, 2.6))), GROUND + 20, .7, t)
        P.badge(380, CENTER - 280, "dozing standing up", 56, NIGHT, GLIM, back(seg(u, .3, .8)))
    elif i == 3:
        moon(P, t); land(P, t)
        x0, x1, y = 120, 960, CENTER - 120
        P.rrect(x0, y - 50, x1, y + 50, 30, (30, 40, 80), outline=CLOUD, w=6)
        random.seed(3); naps = sorted(random.sample(range(24), 9)); tot = 0
        for j, h in enumerate(naps):
            k = eout(seg(u, .8 + j * .22, 1.2 + j * .22)); w = (x1 - x0) / 24 * .5 * k
            xm = x0 + (h + .5) * (x1 - x0) / 24
            if w > 1: P.rrect(xm - w / 2 - 8, y - 34, xm + w / 2 + 8, y + 34, 14, GLIM)
        for h in (0, 6, 12, 18, 24): P.text(x0 + h * (x1 - x0) / 24, y + 90, f"{h}h", 36, CLOUD)
        P.badge(540, CENTER - 330, "about 4.5 hours a day", 60, NIGHT, GLIM, back(seg(u, .3, .8)))
        P.badge(540, CENTER + 120, "in zoo studies", 50, HOPE, CLOUD, back(seg(u, 2.4, 2.9)))
    elif i == 4:
        moon(P, t); land(P, t); giraffe_lying(P, 500, GROUND + 10, 1.25, t, seg(u, 1.5, 3.8))
        P.badge(540, CENTER - 320, "deep sleep", 64, NIGHT, GLIM, back(seg(u, .3, .8)))
        if u > 3.8: zz(P, 380, GROUND - 230, t, 3)
    else:
        moon(P, t); land(P, t); giraffe_lying(P, 470, GROUND + 10, 1.15, t, 1.)
        zz(P, 360, GROUND - 210, t, 3)
        P.badge(540, CENTER - 430, "just a few minutes", 60, NIGHT, GLIM, back(seg(u, .5, 1.0)))
