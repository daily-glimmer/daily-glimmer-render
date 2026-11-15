# Thema: Why do leaves change color in fall?
CENTER = 1050
GREEN, YEL, ORA, RED, BARK = (70, 160, 70), (250, 200, 50), (240, 130, 40), (210, 50, 50), (110, 75, 50)
PAL = ((60, 90, 120), (190, 140, 90))
HI = {"fall?", "chlorophyll,", "shorter", "cooler,", "yellow", "orange", "along,", "reds", "fresh", "sugars", "brighter!"}
WOW = (3, 4)

def mleaf(P, x, y, s, col, rot=0.):
    """Ahornblatt-ähnliches Blatt (5 Spitzen) mit Stiel."""
    pts = []
    for k in range(10):
        a = rot - math.pi / 2 + k * math.pi / 5
        r = (70 if k % 2 == 0 else 32) * s
        if k in (4, 6): r *= .8
        pts.append((x + math.cos(a) * r, y + math.sin(a) * r))
    P.poly(pts, col, outline=lc(col, (0, 0, 0), .3), w=3 * s)
    for k in range(0, 10, 2): P.circ(pts[k][0] * .82 + x * .18, pts[k][1] * .82 + y * .18, 17 * s, col)
    a = rot + math.pi / 2
    P.line([(x, y), (x + math.cos(a) * 70 * s, y + math.sin(a) * 70 * s)], lc(col, (0, 0, 0), .4), 5 * s)
    for k in (0, 2, 8):
        b = rot - math.pi / 2 + k * math.pi / 5
        P.line([(x, y), (x + math.cos(b) * 50 * s, y + math.sin(b) * 50 * s)], lc(col, (255, 255, 255), .3), 3 * s)

def tree(P, x, y, s, cols, t, fall=0.):
    P.rrect(x - 34 * s, y - 40 * s, x + 34 * s, y + 330 * s, 20 * s, BARK)
    P.line([(x, y + 60 * s), (x - 150 * s, y - 40 * s)], BARK, 26 * s); P.line([(x, y + 90 * s), (x + 150 * s, y - 10 * s)], BARK, 26 * s)
    random.seed(11)
    for k in range(34):
        a = random.random() * 6.28; r = random.random() ** .6 * 230 * s
        lx, ly = x + math.cos(a) * r * 1.15, y - 80 * s + math.sin(a) * r * .8
        c = cols[k % len(cols)]
        P.circ(lx, ly, (52 + random.random() * 22) * s, c)

def sun(P, x, y, r, t):
    for k in range(10):
        a = t * .4 + k * .628
        P.line([(x + math.cos(a) * r * 1.25, y + math.sin(a) * r * 1.25), (x + math.cos(a) * r * 1.6, y + math.sin(a) * r * 1.6)], GLIM, 12)
    P.circ(x, y, r, GLIM)

def SC(i, P, t, u):
    if i == 0:
        cols = [lc(GREEN, c, eio(seg(u, .3, 1.6))) for c in (GREEN, YEL, ORA, RED)]
        tree(P, 540, CENTER - 40, 1.25, cols, t)
        P.text(840, CENTER + 330, "?", 150 * back(seg(u, .6, 1.1)), GLIM)
    elif i == 1:
        sun(P, 210, CENTER - 390, 70, t)
        mleaf(P, 560, CENTER + 10, 3.0 * back(seg(u, .1, .6)), GREEN, math.sin(t) * .05)
        for k in range(4):                       # Lichtstrahlen in das Blatt
            q = (t * .8 + k / 4) % 1
            P.circ(lerp(260, 520, q), lerp(CENTER - 330, CENTER - 20, q), 12, GLIM)
        P.badge(540, CENTER + 330, "chlorophyll", 62, HOPE, CLOUD, back(seg(u, .8, 1.3)))
        P.badge(540, CENTER + 450, "sunlight -> food", 52, NIGHT, GLIM, back(seg(u, 1.8, 2.3)))
    elif i == 2:
        g = eio(seg(u, 1.4, 4.0))
        mleaf(P, 540, CENTER - 20, 3.0, lc(GREEN, YEL, g), math.sin(t) * .05)
        # Tageslicht-Balken schrumpft, Thermometer sinkt
        P.rrect(160, CENTER + 330, 920, CENTER + 400, 30, (40, 50, 70))
        P.rrect(166, CENTER + 336, 166 + 740 * (1 - .55 * eio(seg(u, .3, 2.5))), CENTER + 394, 26, GLIM)
        P.text(540, CENTER + 460, "daylight", 48, CLOUD)
        P.rrect(905, CENTER - 300, 955, CENTER - 60, 25, CLOUD); P.circ(930, CENTER - 40, 42, (80, 150, 230))
        P.rrect(917, CENTER - 60 - 200 * (1 - .7 * eio(seg(u, .3, 2.5))), 943, CENTER - 40, 13, (80, 150, 230))
    elif i == 3:
        g = eio(seg(u, .2, 1.6))
        for k, (dx, col) in enumerate(((-260, YEL), (0, ORA), (260, YEL))):
            q = back(seg(u, .3 + k * .3, .8 + k * .3))
            mleaf(P, 540 + dx, CENTER - 40 + (k % 2) * 60, 1.6 * max(q, .01), lc(GREEN, col, g), (k - 1) * .3)
        P.badge(540, CENTER + 300, "hidden all summer", 58, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
        P.badge(540, CENTER + 420, "carotenoids", 54, ORA, CLOUD, back(seg(u, 2.4, 2.9)))
    elif i == 4:
        r = eio(seg(u, 1.0, 3.5))
        mleaf(P, 540, CENTER - 40, 2.8, lc(ORA, RED, r), math.sin(t) * .06)
        for k in range(6):                     # Zuckerwürfel werden rot
            a = k * 1.05 + t * .5
            x, y = 540 + math.cos(a) * 300, CENTER - 40 + math.sin(a) * 230
            q = back(seg(u, .3 + k * .12, .7 + k * .12))
            P.rrect(x - 26 * q, y - 26 * q, x + 26 * q, y + 26 * q, 8, lc(CLOUD, RED, r), outline=lc((200, 200, 200), (140, 30, 30), r), w=3)
        P.badge(540, CENTER + 330, "sugar -> red", 58, RED, CLOUD, back(seg(u, 1.6, 2.1)))
        P.badge(540, CENTER + 450, "made new in fall", 52, NIGHT, GLIM, back(seg(u, 2.6, 3.1)))
    else:
        sun(P, 230, CENTER - 300, 60, t)
        P.circ(850, CENTER - 300, 50, CLOUD); P.circ(875, CENTER - 318, 44, lc(PAL[0], (0, 0, 0), .1))
        random.seed(3)
        for k in range(14):
            q = ((t * .12) + random.random()) % 1
            x = 120 + random.random() * 840 + math.sin(t * 1.5 + k) * 40
            mleaf(P, x, lerp(CENTER - 220, CENTER + 420, q), .8 + random.random() * .5, (RED, ORA, YEL)[k % 3], t * .8 + k)
        P.badge(540, CENTER - 160, "sunny days + cool nights", 52, NIGHT, GLIM, back(seg(u, .8, 1.3)))
