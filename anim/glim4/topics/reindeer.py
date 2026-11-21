# Thema: Do reindeer eyes really change color in winter?  (Mythos-Format, TRUE in Satz 2, FACT in Satz 6)
CENTER = 1050
FUR, FUR2, MUZ, ANT = (140, 100, 70), (110, 75, 50), (225, 205, 180), (225, 200, 160)
SNOW = (240, 246, 252)
GOLD_E, BLUE_E = (240, 180, 50), (40, 110, 230)
PAL = ((15, 25, 60), (60, 90, 140))
HI = {"winter?", "true!", "gold", "blue", "mirror", "tapetum,", "wide", "months", "pressure", "fibers", "dark!", "winter", "eyes?"}
WOW = (1,)

def snowfield(P, t, y=CENTER + 380):
    P.ell(300, y + 120, 600, 200, (220, 232, 245)); P.ell(820, y + 160, 560, 220, SNOW)
    P.poly([(0, y + 140), (W, y + 120), (W, H), (0, H)], SNOW)
    for k in range(40):
        sx = (k * 137) % W; sy = (k * 211 + t * 70 * (1 + k % 3)) % (H * .8)
        P.circ(sx + math.sin(t + k) * 10, sy, 4 + k % 3, (255, 255, 255))

def antler(P, x, y, s, f):
    P.line([(x, y), (x + f * 60 * s, y - 120 * s), (x + f * 40 * s, y - 230 * s), (x + f * 90 * s, y - 320 * s)], ANT, 18 * s)
    P.line([(x + f * 60 * s, y - 120 * s), (x + f * 150 * s, y - 170 * s)], ANT, 15 * s)
    P.line([(x + f * 45 * s, y - 220 * s), (x + f * 130 * s, y - 250 * s)], ANT, 14 * s)
    P.line([(x + f * 25 * s, y - 60 * s), (x - f * 20 * s, y - 120 * s)], ANT, 13 * s)

def eye(P, x, y, r, col, glow=False, pupil=.45):
    P.ell(x, y, r, r * .85, (30, 20, 15))
    P.circ(x, y, r * .78, col, glow=mul(col, 200) if glow else None)
    P.circ(x, y, r * .78 * pupil, NIGHT); P.circ(x + r * .25, y - r * .25, r * .16, (255, 255, 255))

def head(P, x, y, s, t, ecol=GOLD_E, glow=False, pupil=.45):
    for f in (-1, 1): antler(P, x + f * 70 * s, y - 150 * s, s, f)
    for f in (-1, 1): P.poly([(x + f * 110 * s, y - 120 * s), (x + f * 230 * s, y - 170 * s), (x + f * 150 * s, y - 70 * s)], FUR2)
    P.ell(x, y, 150 * s, 185 * s, FUR)
    P.ell(x, y + 120 * s, 105 * s, 95 * s, MUZ)
    P.ell(x, y + 105 * s, 40 * s, 26 * s, (60, 40, 35))
    for f in (-1, 1): eye(P, x + f * 72 * s, y - 40 * s, 38 * s, ecol, glow, pupil)
    P.arc(x, y + 150 * s, 30 * s, 20, 160, (90, 60, 50), 6 * s)

def SC(i, P, t, u):
    if i == 0:
        snowfield(P, t)
        P.circ(850, CENTER - 300, 60, (250, 245, 220), glow=(120, 120, 90))
        head(P, 520, CENTER + 120, 1.25, t)
        k = back(seg(u, .6, 1.1))
        P.text(860, CENTER + 60, "?", 160 * k, GLIM)
    elif i == 1:
        snowfield(P, t)
        k = eout(seg(u, .3, 1.2))
        P.circ(290, CENTER - 110, 210, (255, 225, 120)); P.circ(790, CENTER - 110, 210, (30, 50, 110))
        eye(P, 290, CENTER - 110, 150, GOLD_E)
        eye(P, 790, CENTER - 110, 150 * max(.05, k), BLUE_E, pupil=.6)
        P.badge(290, CENTER + 200, "summer", 56, GLIM, NIGHT, back(seg(u, .5, 1.0)))
        P.badge(790, CENTER + 200, "winter", 56, BLUE_E, CLOUD, back(seg(u, 1.6, 2.1)))
        P.stamp(540, CENTER + 420, "TRUE", seg(u, .25, .7), col=HOPE, rot=-6)
    elif i == 2:
        P.circ(540, CENTER + 20, 340, (245, 240, 235), outline=(180, 160, 150), w=10)       # Augapfel
        P.arc(540, CENTER + 20, 320, 40, 140, (200, 80, 80), 18)                            # Netzhaut
        P.arc(540, CENTER + 20, 300, 45, 135, GOLD_E, 22)                                   # Tapetum
        P.ell(540, CENTER - 260, 110, 40, (150, 200, 240))                                  # Linse
        k = seg(u, .8, 2.4); k2 = seg(u, 2.4, 4.0)
        for dx in (-60, 0, 60):
            ya = CENTER - 520; yb = CENTER + 300
            if k > 0: P.line([(540 + dx, ya), (540 + dx * .6, lerp(ya, yb, k))], (255, 240, 150), 10, glow=(120, 110, 50))
            if k2 > 0: P.line([(540 + dx * .6, yb), (540 + dx * 1.4, lerp(yb, CENTER - 300, k2))], (255, 210, 90), 8)
        P.badge(540, CENTER + 470, "tapetum = mirror", 58, NIGHT, GLIM, back(seg(u, 1.2, 1.7)))
    elif i == 3:
        snowfield(P, t)
        P.circ(820, CENTER - 300, 55, (250, 245, 220), glow=(120, 120, 90))
        head(P, 470, CENTER + 120, 1.15, t, ecol=lc(GOLD_E, BLUE_E, seg(u, 1., 5.)), pupil=lerp(.45, .85, eout(seg(u, .5, 2.))))
        P.badge(540, CENTER + 520, "months of darkness", 56, NIGHT, CLOUD, back(seg(u, .4, .9)))
        k = eio(seg(u, 3.0, 5.0))      # Druckanzeige
        P.circ(870, CENTER + 120, 95, (240, 240, 245), outline=(120, 130, 150), w=8)
        a = math.radians(210 - 240 * k); P.line([(870, CENTER + 120), (870 + math.cos(a) * 70, CENTER + 120 - math.sin(a) * 70)], HOOK, 10)
        P.badge(870, CENTER + 260, "pressure", 44, HOOK, CLOUD, back(seg(u, 3.0, 3.5)))
    elif i == 4:
        k = eio(seg(u, .5, 3.0)); col = lc(GOLD_E, BLUE_E, k); gap = lerp(110, 62, k)
        P.rrect(140, CENTER - 300, 940, CENTER + 260, 60, (30, 40, 70))
        for r_ in range(6):
            for c in range(7):
                x = 540 + (c - 3) * gap; y = CENTER - 20 + (r_ - 2.5) * gap
                P.circ(x, y, 24, col)
        if k > .9:
            for j in range(4): P.circ(260 + j * 30, CENTER - 230 + j * 140, 10, (200, 230, 255))
        P.badge(540, CENTER + 400, "squeezed = blue", 58, NIGHT, CLOUD, back(seg(u, 2.6, 3.1)))
    else:
        snowfield(P, t)
        head(P, 440, CENTER + 200, 1.05, t, ecol=BLUE_E, pupil=.85)
        P.stamp(830, CENTER - 40, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
