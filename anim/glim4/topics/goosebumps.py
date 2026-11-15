# Thema: Why do we get goosebumps?
CENTER = 1050
SKIN, SKIN2, HAIR, MUS = (240, 195, 160), (215, 160, 125), (90, 60, 40), (220, 90, 90)
PAL = ((200, 225, 250), (255, 225, 200))
HI = {"goosebumps?", "hair", "tiny", "muscle", "cold", "excited,", "upright.", "fluffs", "warm", "bigger.", "fur,", "bumps!", "mice,", "grow!"}
WOW = (2, 4, 5)

def skin_cut(P, y0, t, up=0., n=4, bump=0.):
    P.rrect(60, y0, 1020, y0 + 520, 30, SKIN2)
    pts = [(60, y0)]
    for k in range(n):
        x = 60 + (k + .5) * 960 / n
        pts += [(x - 80, y0), (x, y0 - 40 * bump), (x + 80, y0)]
    pts += [(1020, y0), (1020, y0 + 60), (60, y0 + 60)]
    P.poly(pts, SKIN)
    for k in range(n):
        x = 60 + (k + .5) * 960 / n
        P.ell(x, y0 + 220, 38, 120, (200, 140, 110), outline=(170, 110, 90), w=4)
        ang = lerp(-.95, -.05, up)
        L = 300
        hx, hy = x + math.sin(ang + .0) * 0, y0 + 220
        ex, ey = x + math.sin(ang) * -L * 0 + math.cos(ang + math.pi / 2) * 0, 0
        tipx, tipy = x + math.cos(-math.pi / 2 + ang + 1.0 - up * 1.0) * L, y0 + 160 + math.sin(-math.pi / 2 + ang + 1.0 - up * 1.0) * L
        P.line([(x, y0 + 300), (x, y0 + 120), (tipx, tipy)], HAIR, 9)
        mx = x + 140
        P.line([(x + 20, y0 + 230), (mx, y0 + 90 + 20 * (1 - up))], MUS, 18 + 8 * up)

def SC(i, P, t, u):
    if i == 0:
        P.rrect(160, CENTER - 300, 920, CENTER + 360, 120, SKIN, outline=SKIN2, w=6)
        random.seed(2)
        b = eio(seg(u, .4, 1.4))
        for k in range(40):
            x, y = 220 + random.random() * 640, CENTER - 240 + random.random() * 540
            P.circ(x, y, 12 * b, SKIN2); P.line([(x, y), (x + 8, y - 30 * b)], HAIR, 3)
        P.text(860, CENTER - 330, "?", 150 * back(seg(u, .5, 1.0)), HOOK)
    elif i == 1:
        skin_cut(P, CENTER - 150, t, up=0)
        P.badge(540, CENTER + 460, "1 hair = 1 tiny muscle", 54, NIGHT, GLIM, back(seg(u, .8, 1.3)))
    elif i == 2:
        up = eio(seg(u, 1.0, 2.2))
        skin_cut(P, CENTER - 100, t, up=up, bump=up)
        for k in range(3):
            q = (t * 1.5 + k / 3) % 1
            P.line([(120 + q * 300, CENTER - 360), (150 + q * 300, CENTER - 330)], (80, 150, 230), 6)
        P.badge(540, CENTER + 470, "muscle pulls -> hair stands up", 48, MUS, CLOUD, back(seg(u, 1.8, 2.3)))
    elif i == 3:
        f = 1 + .3 * eio(seg(u, .4, 1.6))
        cx, cy = 540, CENTER + 20
        for k in range(36):
            a = k * 6.28 / 36
            P.line([(cx + math.cos(a) * 150 * f, cy + math.sin(a) * 110 * f), (cx + math.cos(a) * 200 * f, cy + math.sin(a) * 150 * f)], (120, 120, 130), 14)
        P.ell(cx, cy, 190 * f, 140 * f, (160, 160, 170))
        P.circ(cx - 170 * f, cy - 60, 70, (160, 160, 170))
        P.poly([(cx - 220 * f, cy - 120), (cx - 200 * f, cy - 180), (cx - 170 * f, cy - 120)], (160, 160, 170))
        P.poly([(cx - 150 * f, cy - 120), (cx - 120 * f, cy - 180), (cx - 110 * f, cy - 110)], (160, 160, 170))
        P.circ(cx - 195 * f, cy - 70, 10, NIGHT)
        P.badge(540, CENTER + 330, "trap warm air", 56, HOPE, CLOUD, back(seg(u, 1.2, 1.7)))
        P.badge(540, CENTER + 440, "look bigger", 52, NIGHT, GLIM, back(seg(u, 2.4, 2.9)))
    elif i == 4:
        P.rrect(160, CENTER - 260, 920, CENTER + 320, 120, SKIN, outline=SKIN2, w=6)
        random.seed(2)
        b = .6 + .4 * math.sin(t * 3)
        for k in range(40):
            x, y = 220 + random.random() * 640, CENTER - 200 + random.random() * 480
            P.circ(x, y, 14 * b, SKIN2); P.line([(x, y), (x + 4, y - 22)], HAIR, 3)
        P.badge(540, CENTER + 430, "little bumps!", 60, HOOK, CLOUD, back(seg(u, .8, 1.3)))
    else:
        cx, cy = 540, CENTER + 80
        P.ell(cx, cy, 160, 100, (200, 200, 205)); P.circ(cx - 150, cy - 40, 62, (200, 200, 205))
        P.circ(cx - 170, cy - 100, 30, (240, 180, 190)); P.circ(cx - 120, cy - 100, 30, (240, 180, 190))
        P.circ(cx - 180, cy - 50, 8, NIGHT); P.circ(cx - 210, cy - 30, 9, (240, 150, 160))
        P.line([(cx + 150, cy), (cx + 260, cy - 60)], (240, 180, 190), 8)
        g = eio(seg(u, .8, 2.6))
        for k in range(10):
            x = cx - 60 + k * 18
            P.line([(x, cy - 90), (x + 6, cy - 90 - 60 * g)], (150, 150, 160), 5)
        P.badge(540, CENTER - 150, "nerves help hair grow", 56, NIGHT, GLIM, back(seg(u, 1.6, 2.1)))
