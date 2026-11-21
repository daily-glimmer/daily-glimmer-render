# Thema: Are zebras white with black stripes?  (Mythos-Format, NOT QUITE in Satz 2, FACT in Satz 6)
CENTER = 1050
ZW, ZB, SKIN = (248, 246, 240), (30, 30, 35), (45, 40, 45)
PAL = ((220, 150, 80), (240, 200, 120))
HI = {"white", "stripes?", "not", "quite!", "black", "melanin,", "switched", "off,", "flies", "stripes!"}
WOW = (1,)
GROUND = CENTER + 330

def savanna(P, t):
    P.poly([(0, GROUND - 20), (W, GROUND - 40), (W, H), (0, H)], (200, 170, 90))
    for x in (120, 960):
        P.line([(x, GROUND - 20), (x, GROUND - 250)], (110, 80, 50), 22)
        P.ell(x, GROUND - 270, 150, 45, (90, 140, 70))

def zebra(P, x, y, s, t, skin=0., walk=False):
    """Zebra (Hufe bei y); skin = 0..1 Fell wird zur schwarzen Haut."""
    bx, by = x, y - 300 * s; ph = t * 6 if walk else 0
    body = lc(ZW, SKIN, skin); st = lc(ZB, SKIN, skin)
    for k, dx in enumerate((-110, -75, 80, 115)):
        sw = math.sin(ph + k * 1.6) * 14 * s if walk else 0
        P.line([(bx + dx * s, by + 30 * s), (bx + dx * s + sw, y)], body, 24 * s)
        P.rrect(bx + dx * s + sw - 14 * s, y - 18 * s, bx + dx * s + sw + 14 * s, y, 4 * s, ZB)
        for j in range(3): P.line([(bx + dx * s - 12 * s + sw * j / 3, by + 80 * s + j * 60 * s), (bx + dx * s + 12 * s + sw * j / 3, by + 90 * s + j * 60 * s)], st, 9 * s)
    P.line([(bx - 160 * s, by - 10 * s), (bx - 190 * s, by + 110 * s + math.sin(t * 2) * 10 * s)], st, 9 * s)
    P.ell(bx, by, 170 * s, 85 * s, body)
    for j in range(7):
        xx = bx + (j - 3) * 42 * s
        P.line([(xx - 10 * s, by - 80 * s), (xx + 12 * s, by), (xx - 6 * s, by + 78 * s)], st, 14 * s)
    hx, hy = bx + 230 * s, by - 250 * s
    P.line([(bx + 120 * s, by - 20 * s), (hx - 20 * s, hy + 30 * s)], body, 62 * s)
    for j in range(4):
        q = .2 + j * .2; P.line([(lerp(bx + 100 * s, hx - 50 * s, q), lerp(by - 50 * s, hy, q)), (lerp(bx + 150 * s, hx + 5 * s, q), lerp(by + 10 * s, hy + 60 * s, q))], st, 12 * s)
    P.line([(bx + 95 * s, by - 60 * s), (hx - 45 * s, hy - 5 * s)], ZB, 14 * s)       # Mähne
    P.ell(hx + 20 * s, hy + 20 * s, 75 * s, 45 * s, body)
    P.ell(hx + 80 * s, hy + 35 * s, 32 * s, 30 * s, ZB)
    P.ell(hx - 25 * s, hy - 40 * s, 14 * s, 32 * s, body)
    P.circ(hx + 15 * s, hy + 5 * s, 8 * s, NIGHT)

def hair(P, x, y0, y1, col, on, t):
    P.line([(x, y0), (x + math.sin(t * 2 + x) * 6, y1)], col, 18)
    P.ell(x, y0 + 40, 30, 22, (240, 200, 190))
    P.circ(x - 40, y0 + 60, 18, GLIM if on else (120, 120, 130), glow=mul(GLIM, 150) if on else None)

def SC(i, P, t, u):
    if i == 0:
        savanna(P, t); zebra(P, 470, GROUND + 20, 1.15, t, walk=True)
        P.text(260, CENTER - 230, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        savanna(P, t); zebra(P, 470, GROUND + 20, 1.15, t, skin=eio(seg(u, .6, 2.2)))
        P.stamp(540, CENTER + 430, "NOT QUITE", seg(u, .25, .7), col=HOOK, rot=-6)
        P.badge(540, CENTER + 580, "black skin", 62, NIGHT, CLOUD, back(seg(u, 1.8, 2.3)))
    elif i == 2:
        P.rrect(80, CENTER + 60, 1000, CENTER + 420, 40, (235, 190, 175))
        P.rrect(80, CENTER + 60, 1000, CENTER + 120, 30, SKIN)
        for j in range(6): hair(P, 200 + j * 135, CENTER + 60, CENTER - 280 * eout(seg(u, .3 + j * .1, 1.5 + j * .1)) + 60, ZB, True, t)
        P.badge(540, CENTER + 520, "melanin = dark", 58, NIGHT, GLIM, back(seg(u, 1.2, 1.7)))
    elif i == 3:
        P.rrect(80, CENTER + 60, 1000, CENTER + 420, 40, (235, 190, 175))
        P.rrect(80, CENTER + 60, 1000, CENTER + 120, 30, SKIN)
        for j in range(6):
            on = j < 2 or j > 3
            hair(P, 200 + j * 135, CENTER + 60, CENTER - 220, ZB if on else ZW, on, t)
        P.badge(540, CENTER + 270, "switched off", 56, HOOK, CLOUD, back(seg(u, 1.0, 1.5)))
    elif i == 4:
        savanna(P, t); zebra(P, 470, GROUND + 20, 1.1, t)
        for j in range(5):
            q = (u * .7 + j / 5) % 1; a = j * 1.3
            fx = 470 + math.cos(a) * (180 + 300 * abs(math.sin(q * math.pi))); fy = CENTER - 120 + math.sin(a) * 160 - q * 120
            P.circ(fx, fy, 12, NIGHT); P.ell(fx - 10, fy - 12, 10, 6, (200, 220, 240)); P.ell(fx + 10, fy - 12, 10, 6, (200, 220, 240))
        P.badge(540, CENTER + 520, "flies stay away", 58, NIGHT, CLOUD, back(seg(u, 1.0, 1.5)))
    else:
        savanna(P, t); zebra(P, 330, GROUND + 20, .9, t)
        P.stamp(800, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
