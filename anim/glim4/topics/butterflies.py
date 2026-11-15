# Thema: Do butterflies really taste with their feet?  (Mythos-Format TRUE/FACT)
CENTER = 1050
PAL = ((150, 205, 240), (170, 220, 140))
HI = {"taste", "feet?", "True!", "sensors.", "drums", "leaf", "right", "caterpillars", "eggs", "nectar", "tongue!", "second"}
WOW = (1, 5)
WING1, WING2 = (255, 140, 40), (255, 200, 70)
GROUND = CENTER + 420

def leafplant(P, x, y, s, t, tap=0.):
    P.line([(x, y + 300 * s), (x, y)], (60, 140, 60), 14 * s)
    for k, (dx, dy, a) in enumerate(((-1, 0, .4), (1, 60, -.4), (-1, 140, .3))):
        sx = x + dx * 10 * s; sy = y + dy * s
        P.ell(sx + dx * 120 * s, sy - tap * 6 * (k == 0), 130 * s, 50 * s, (80, 170, 80), outline=(50, 120, 50), w=5 * s)
        P.line([(sx, sy), (sx + dx * 230 * s, sy)], (50, 120, 50), 4 * s)

def flower(P, x, y, r, col=(255, 120, 170)):
    P.line([(x, y), (x, GROUND + 100)], (60, 140, 60), 12)
    for j in range(6): a = j / 6 * 6.28; P.circ(x + math.cos(a) * r, y + math.sin(a) * r, r * .7, col)
    P.circ(x, y, r * .6, GLIM)

def butterfly(P, x, y, s, t, flap=1., legs=False, tongue=0., wing=(WING1, WING2)):
    a = .35 + .65 * abs(math.cos(t * 7 * flap)) if flap else 1
    for f in (-1, 1):
        P.poly([(x, y - 10 * s), (x + f * 200 * s * a, y - 170 * s), (x + f * 230 * s * a, y - 20 * s), (x, y + 10 * s)], wing[0], outline=NIGHT, w=6 * s)
        P.poly([(x, y + 5 * s), (x + f * 150 * s * a, y + 40 * s), (x + f * 110 * s * a, y + 150 * s), (x, y + 30 * s)], wing[1], outline=NIGHT, w=6 * s)
        P.circ(x + f * 140 * s * a, y - 90 * s, 28 * s * a, CLOUD)
        P.line([(x, y - 90 * s), (x + f * 60 * s, y - 170 * s)], NIGHT, 5 * s); P.circ(x + f * 60 * s, y - 170 * s, 10 * s, NIGHT)
    P.ell(x, y, 22 * s, 95 * s, NIGHT)
    if legs:
        for f in (-1, 1):
            for k in range(3): P.line([(x, y + (k * 25 - 10) * s), (x + f * 50 * s, y + (k * 25 + 60) * s)], NIGHT, 6 * s)
    if tongue > 0:
        P.arc(x, y - 105 * s + 40 * s * (1 - tongue), 30 * s, 90, 90 + 300 * (1 - tongue), NIGHT, 5 * s)
        if tongue > .6: P.line([(x, y - 90 * s), (x, y - 90 * s + 140 * s * tongue)], NIGHT, 5 * s)

def caterpillar(P, x, y, s, t):
    for j in range(6):
        P.circ(x + j * 45 * s, y - abs(math.sin(t * 4 + j * .7)) * 14 * s, 30 * s, (120, 200, 80) if j % 2 else (90, 170, 60))
    P.circ(x + 270 * s, y - 10 * s, 36 * s, (120, 200, 80)); P.circ(x + 282 * s, y - 20 * s, 7 * s, NIGHT)

def SC(i, P, t, u):
    P.poly([(0, GROUND), (W, GROUND - 40), (W, H), (0, H)], (120, 190, 90))
    if i == 0:
        butterfly(P, 540 + math.sin(t) * 80, CENTER - 60 + math.sin(t * 2) * 30, 1.3, t)
        P.text(840, CENTER - 300, "?", 140 * back(seg(u, .4, .9)), GLIM)
    elif i == 1:
        butterfly(P, 540, CENTER - 80, 1.3, t, flap=.3, legs=True)
        for f in (-1, 1):
            P.circ(540 + f * 65, CENTER + 70, 38 * back(seg(u, 1.0, 1.4)), None, outline=GLIM, w=8)
        P.badge(540, CENTER + 220, "taste sensors", 56, NIGHT, GLIM, back(seg(u, 1.3, 1.8)))
        P.stamp(540, CENTER - 330, "TRUE", seg(u, .25, .7), HOPE)
    elif i == 2:
        tap = abs(math.sin(u * 10)) if u > 1.2 else 0
        leafplant(P, 540, CENTER, 1.2, t, tap)
        butterfly(P, 400, CENTER - 160 - tap * 10, .9, t, flap=.2, legs=True)
        for k in range(3):
            q = (u * 1.5 + k / 3) % 1
            if u > 1.2: P.arc(400, CENTER - 20, 30 + q * 90, 200, 340, lc(GLIM, (80, 170, 80), q), 6)
    elif i == 3:
        leafplant(P, 380, CENTER - 40, 1.1, t)
        caterpillar(P, 560, CENTER + 260, 1.1, t)
        P.check(800, CENTER - 160, 70, k=back(seg(u, 1.4, 1.9)))
        P.badge(620, CENTER - 320, "right plant?", 56, NIGHT, GLIM, back(seg(u, .4, .9)))
    elif i == 4:
        flower(P, 700, CENTER - 20, 70)
        butterfly(P, 700 - 40 * (1 - eio(seg(u, 2.2, 3.2))), CENTER - 240, .8, t, flap=.4, tongue=seg(u, 2.8, 4.0))
        for j in range(5): P.circ(230 + j * 40, CENTER + 260, 16 * back(seg(u, .5 + j * .2, .8 + j * .2)), (250, 245, 210), outline=(200, 190, 140), w=3)
        P.badge(300, CENTER + 120, "eggs", 52, HOPE, CLOUD, back(seg(u, 1.2, 1.6)))
    else:
        butterfly(P, 540, CENTER - 30, 1.1, t, flap=.6, legs=True)
        P.stamp(540, CENTER + 300, "FACT", seg(u, .25, .7), HOPE)
