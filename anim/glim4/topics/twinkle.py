# Thema: Why do stars twinkle?
CENTER = 1050
PAL = ((8, 12, 40), (30, 40, 90))
HI = {"twinkle?", "air", "bumpy", "warm", "cold", "bend", "points,", "wobble", "disks", "steadily.", "space,", "all!", "planet?"}
WOW = (1, 5)

def star(P, x, y, r, col=CLOUD, glow=None, rot=0.):
    pts = []
    for k in range(8):
        rr = r if k % 2 == 0 else r * .28; a = k / 8 * 6.28 + rot
        pts.append((x + math.cos(a) * rr, y + math.sin(a) * rr))
    P.poly(pts, col); P.circ(x, y, r * .3, col, glow=glow)

def air(P, y0, y1, t, k=1.):
    for j in range(7):
        y = lerp(y0, y1, j / 6)
        pts = [(x, y + math.sin(x / 120 + t * (1.5 + j * .3) + j) * 25 * k) for x in range(0, W + 60, 60)]
        P.line(pts, lc((255, 150, 120), (120, 180, 255), j % 2), 8)

def house(P, t):
    P.poly([(0, CENTER + 560), (W, CENTER + 520), (W, H), (0, H)], (20, 30, 50))
    P.rrect(120, CENTER + 400, 320, CENTER + 560, 6, (50, 60, 90)); P.poly([(100, CENTER + 400), (220, CENTER + 300), (340, CENTER + 400)], (70, 60, 90))
    P.rrect(190, CENTER + 440, 250, CENTER + 500, 4, GLIM)

def SC(i, P, t, u):
    if i == 0:
        house(P, t)
        for k, (x, y) in enumerate(((300, CENTER - 200), (720, CENTER - 80), (520, CENTER + 120), (850, CENTER + 250))):
            tw = .6 + .4 * math.sin(t * (9 + k * 3) + k)
            star(P, x, y, 60 * tw, glow=(255, 240, 200), rot=t * .3)
        P.text(860, CENTER - 300, "?", 140 * back(seg(u, .4, .9)), GLIM)
    elif i == 1:
        star(P, 540, CENTER - 260, 70, glow=(255, 240, 200))
        q = seg(u, .3, 2.0)
        P.line([(540, CENTER - 200), (540, lerp(CENTER - 200, CENTER + 120, q))], GLIM, 10)
        if u > 2.0:
            pts = [(540 + math.sin(j * .9 + t * 6) * 30 * seg(u, 2.0, 3.0), CENTER + 120 + j * 30) for j in range(10)]
            P.line(pts, GLIM, 10)
        air(P, CENTER + 120, CENTER + 400, t, seg(u, 1.5, 2.5))
        house(P, t)
    elif i == 2:
        air(P, CENTER - 140, CENTER + 260, t, 1.4)
        for b in range(3):
            pts = [(300 + b * 240 + math.sin(j * .7 + t * 5 + b) * 50, CENTER - 300 + j * 70) for j in range(10)]
            P.line(pts, GLIM, 8)
        P.badge(540, CENTER + 400, "warm + cold air", 58, (50, 70, 140), GLIM, back(seg(u, .6, 1.1)))
    elif i == 3:
        tw = .5 + .5 * math.sin(t * 14)
        star(P, 540 + math.sin(t * 9) * 12, CENTER - 20, 110 * (.5 + .5 * tw), glow=(255, 240, 200))
        P.circ(540, CENTER - 20, 12, CLOUD)
        P.badge(540, CENTER + 330, "a tiny point", 58, (50, 70, 140), GLIM, back(seg(u, .6, 1.1)))
    elif i == 4:
        star(P, 300, CENTER - 20, 70 * (.5 + .5 * math.sin(t * 13)), glow=(255, 240, 200))
        P.circ(760, CENTER - 20, 110, (230, 150, 90)); P.ell(760, CENTER - 50, 105, 22, (200, 120, 70)); P.ell(760, CENTER + 20, 100, 18, (245, 190, 140))
        P.badge(300, CENTER + 250, "star", 56, (50, 70, 140), GLIM, back(seg(u, .4, .9)))
        P.badge(760, CENTER + 250, "planet", 56, HOPE, CLOUD, back(seg(u, 1.4, 1.9)))
    else:
        earth_r = 900
        P.circ(540, CENTER + 1150, earth_r, (40, 110, 190)); P.arc(540, CENTER + 1150, earth_r + 40, 200, 340, (120, 180, 255), 30)
        P.rrect(640, CENTER - 60, 760, CENTER + 10, 10, (200, 205, 215)); P.rrect(560, CENTER - 40, 640, CENTER - 10, 4, (60, 100, 180)); P.rrect(760, CENTER - 40, 840, CENTER - 10, 4, (60, 100, 180))
        for k, (x, y) in enumerate(((200, CENTER - 200), (420, CENTER - 280), (880, CENTER - 180), (300, CENTER + 60))):
            star(P, x, y, 40, glow=(255, 240, 200))
