# Thema: How do squirrels find their buried nuts?
CENTER = 1050
FUR, BELLY, NUT, CAP = (150, 150, 155), (225, 220, 210), (175, 115, 60), (120, 80, 45)
SOIL = (120, 85, 55)
PAL = ((235, 180, 120), (200, 120, 70))
HI = {"nuts?", "thousands", "remember", "landmarks.", "sort", "same", "pantry.", "smell", "exact", "forget", "trees!"}
WOW = (1, 3, 5)

def acorn(P, x, y, s):
    P.ell(x, y + 10 * s, 26 * s, 32 * s, NUT); P.ell(x, y - 16 * s, 30 * s, 14 * s, CAP); P.line([(x, y - 28 * s), (x + 4 * s, y - 40 * s)], CAP, 5 * s)

def walnut(P, x, y, s):
    P.circ(x, y, 30 * s, (200, 165, 110), outline=(150, 120, 80), w=3 * s); P.line([(x, y - 30 * s), (x, y + 30 * s)], (150, 120, 80), 3 * s)

def squirrel(P, x, y, s, t, dig=0., sniff=0.):
    tw = math.sin(t * 2.5) * .08
    pts = [(x + (60 + 120 * math.sin(k / 10 * 3.0 + tw)) * s, y - (k * 28) * s) for k in range(11)]
    for k, (px, py) in enumerate(pts): P.circ(px + 30 * s, py, (48 + 12 * math.sin(k / 10 * 3.1)) * s, lc(FUR, (255, 255, 255), .1))
    P.ell(x, y - 30 * s, 75 * s, 100 * s, FUR); P.ell(x - 18 * s, y - 20 * s, 45 * s, 70 * s, BELLY)
    hx, hy = x - 40 * s, y - 150 * s + sniff * 6 * s * math.sin(t * 14)
    P.circ(hx, hy, 52 * s, FUR); P.ell(hx + 25 * s, hy - 52 * s, 14 * s, 24 * s, FUR)
    P.circ(hx - 14 * s, hy - 8 * s, 10 * s, NIGHT); P.circ(hx - 10 * s, hy - 12 * s, 3 * s, CLOUD)
    P.circ(hx - 50 * s, hy + 6 * s, 9 * s, (60, 40, 40))
    a = dig * math.sin(t * 12)
    P.line([(x - 40 * s, y - 50 * s), (x - 80 * s, y + (10 + 20 * a) * s)], FUR, 20 * s)
    P.ell(x + 20 * s, y + 60 * s, 60 * s, 25 * s, FUR)

def ground(P, y):
    P.rrect(-20, y, W + 20, H + 50, 0, SOIL); P.rrect(-20, y - 14, W + 20, y + 14, 10, (110, 150, 70))

def SC(i, P, t, u):
    if i == 0:
        ground(P, CENTER + 180); squirrel(P, 520, CENTER + 160, 1.4, t)
        acorn(P, 330, CENTER + 120, 1.6)
        P.text(820, CENTER - 300, "?", 150 * back(seg(u, .5, 1.0)), HOOK)
    elif i == 1:
        ground(P, CENTER + 60)
        random.seed(6)
        n = int(40 * eio(seg(u, .3, 3.5)))
        for k in range(n):
            x, y = 70 + random.random() * 940, CENTER + 120 + random.random() * 360
            acorn(P, x, y, .7)
        squirrel(P, 540, CENTER + 40, 1.0, t, dig=1)
        P.badge(540, CENTER - 300, "thousands of nuts", 60, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
    elif i == 2:
        ground(P, CENTER + 200)
        P.rrect(150, CENTER - 160, 200, CENTER + 200, 10, (110, 75, 50)); P.circ(175, CENTER - 200, 120, (90, 150, 70))
        P.ell(860, CENTER + 170, 110, 70, (150, 150, 160))
        q = eio(seg(u, .4, 2.0))
        P.line([(175, CENTER), (lerp(175, 540, q), lerp(CENTER, CENTER + 300, q))], GLIM, 8)
        P.line([(860, CENTER + 140), (lerp(860, 540, q), lerp(CENTER + 140, CENTER + 300, q))], GLIM, 8)
        if q > .95: P.text(540, CENTER + 310, "X", 90 * back(seg(u, 2.0, 2.4)), HOOK)
        squirrel(P, 540, CENTER + 180, .9, t)
        P.badge(540, CENTER - 300, "landmarks", 64, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
    elif i == 3:
        ground(P, CENTER - 100)
        for k in range(3):
            P.rrect(130 + k * 290, CENTER - 20, 370 + k * 290, CENTER + 280, 30, lc(SOIL, (0, 0, 0), .2))
            for j in range(4):
                q = back(seg(u, .3 + k * .4 + j * .08, .7 + k * .4 + j * .08))
                x, y = 190 + k * 290 + (j % 2) * 110, CENTER + 60 + (j // 2) * 120
                if q > .02:
                    if k == 0: acorn(P, x, y, 1.1 * q)
                    elif k == 1: walnut(P, x, y, 1.1 * q)
                    else: P.ell(x, y, 22 * q, 34 * q, (230, 200, 150), outline=(170, 140, 100), w=3)
        P.badge(540, CENTER - 300, "sorted like a pantry", 58, NIGHT, GLIM, back(seg(u, 1.6, 2.1)))
    elif i == 4:
        ground(P, CENTER + 160)
        squirrel(P, 540, CENTER + 140, 1.3, t, sniff=1)
        waves(P, 400, CENTER - 20, t, CLOUD, n=3, r0=30, dr=30, a0=120, a1=240)
        acorn(P, 380, CENTER + 330, 1.3)
        P.badge(540, CENTER - 300, "super sniffer", 62, HOPE, CLOUD, back(seg(u, .8, 1.3)))
    else:
        ground(P, CENTER + 260)
        g = eio(seg(u, .3, 4.0))
        P.line([(540, CENTER + 260), (540, CENTER + 260 - 400 * g)], (110, 75, 50), 10 + 40 * g)
        for k in range(5):
            a = -math.pi / 2 + (k - 2) * .55
            P.circ(540 + math.cos(a) * 160 * g, CENTER + 260 - 400 * g + math.sin(a) * 100 * g, 110 * g, (80, 150, 70))
        acorn(P, 540, CENTER + 300, 1.2)
        P.badge(540, CENTER + 360, "forgotten nut = new tree", 54, HOPE, CLOUD, back(seg(u, 1.0, 1.5)))
