# Thema: Why is the ocean salty?
CENTER = 1050
SEA, SEA2, ROCK = (40, 120, 190), (25, 85, 150), (150, 135, 125)
PAL = ((140, 200, 240), (80, 150, 210))
HI = {"ocean", "salty?", "acidic,", "rocks", "Rivers", "salt", "sea.", "sun", "stays", "behind.", "millions", "three", "half", "percent.", "forty", "story"}
WOW = (3, 5)

def sea(P, y, t):
    pts = [(0, H)] + [(x, y + math.sin(x / 90 + t * 2) * 12) for x in range(0, W + 41, 40)] + [(W, H)]
    P.poly(pts, SEA)
    for k in range(3):
        P.line([(x, y + 60 + k * 70 + math.sin(x / 70 + t * 1.5 + k) * 8) for x in range(60, W - 40, 40)], SEA2, 6)

def crystal(P, x, y, r, col=CLOUD):
    P.rrect(x - r, y - r, x + r, y + r, r * .25, col, outline=(170, 190, 210), w=3)

def rain(P, t, x0, x1, y0, y1, n=14):
    for j in range(n):
        q = (t * 1.2 + j / n) % 1
        x = x0 + (j * 71) % (x1 - x0); y = lerp(y0, y1, q)
        P.line([(x, y), (x - 8, y + 34)], (220, 235, 255), 6)

def SC(i, P, t, u):
    if i == 0:
        sea(P, CENTER + 120, t)
        for j in range(8):
            q = (t * .3 + j / 8) % 1
            crystal(P, 150 + j * 110, CENTER + 200 + (j % 3) * 80 - q * 40, 16)
        P.circ(820, CENTER - 160, 80, GLIM, glow=GLIM)
        P.text(880, CENTER - 300, "?", 150 * back(seg(u, .4, .9)), HOOK)
    elif i == 1:
        P.ell(540, CENTER - 200, 280, 90, (200, 210, 225)); P.ell(380, CENTER - 230, 150, 80, (200, 210, 225))
        rain(P, t, 300, 800, CENTER - 150, CENTER + 120)
        P.poly([(160, CENTER + 330), (420, CENTER + 50), (620, CENTER + 180), (900, CENTER + 330)], ROCK, outline=lc(ROCK, (0, 0, 0), .3), w=6)
        for j in range(6):
            q = (t * .5 + j / 6) % 1
            crystal(P, 420 + j * 40 + q * 60, CENTER + 120 + q * 180, 10)
        P.badge(540, CENTER + 420, "rain wears rocks", 58, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
    elif i == 2:
        P.poly([(0, CENTER - 200), (W, CENTER - 200), (W, CENTER + 400), (0, CENTER + 400)], (150, 190, 110))
        P.line([(120, CENTER - 200), (300, CENTER - 20), (220, CENTER + 120), (560, CENTER + 240), (760, CENTER + 300), (1100, CENTER + 330)], (70, 150, 210), 70)
        sea(P, CENTER + 330, t)
        for j in range(8):
            q = (t * .25 + j / 8) % 1
            pts = [(120, CENTER - 200), (300, CENTER - 20), (220, CENTER + 120), (560, CENTER + 240), (760, CENTER + 300), (1100, CENTER + 330)]
            seg_i = min(4, int(q * 5)); f = q * 5 - seg_i
            (xa, ya), (xb, yb) = pts[seg_i], pts[seg_i + 1]
            crystal(P, lerp(xa, xb, f), lerp(ya, yb, f), 12)
        P.badge(540, CENTER + 460, "rivers carry it", 58, NIGHT, GLIM, back(seg(u, 1.2, 1.7)))
    elif i == 3:
        sea(P, CENTER + 160, t)
        P.circ(820, CENTER - 200, 90, GLIM, glow=GLIM)
        for j in range(6):
            q = (t * .5 + j / 6) % 1
            x = 200 + j * 120 + math.sin(t * 2 + j) * 20
            P.circ(x, lerp(CENTER + 140, CENTER - 200, q), 14 * (1 - q * .5), (220, 240, 255))
        for j in range(10):
            crystal(P, 120 + j * 90, CENTER + 260 + (j % 2) * 50, 15)
        P.badge(540, CENTER + 440, "salt stays", 64, HOOK, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 4:
        k = eout(seg(u, .3, 2.0))
        P.rrect(330, CENTER - 200, 750, CENTER + 280, 30, (200, 230, 250), outline=NIGHT, w=8)
        P.rrect(345, CENTER + 280 - 15 - 455 * .965, 735, CENTER + 265, 20, SEA)
        P.rrect(345, CENTER + 265 - 455 * .035 * k * 3, 735, CENTER + 265, 16, CLOUD)
        P.badge(540, CENTER + 420, "about 3.5% salt", 60, NIGHT, GLIM, back(seg(u, 1.6, 2.1)))
    else:
        k = eout(seg(u, .3, 2.2))
        P.rrect(-20, CENTER + 330, W + 20, H + 20, 0, (120, 170, 100))
        P.rrect(150, CENTER + 330 - 560 * k, 930, CENTER + 330, 10, CLOUD, outline=(170, 190, 210), w=5)
        P.rrect(760, CENTER + 330 - 520, 860, CENTER + 330, 6, (120, 130, 150))
        for r in range(12):
            for c in range(2): P.rrect(772 + c * 46, CENTER + 330 - 500 + r * 42, 800 + c * 46, CENTER + 330 - 480 + r * 42, 3, GLIM)
        P.badge(540, CENTER - 300, "~150 m of salt!", 58, NIGHT, GLIM, back(seg(u, 1.6, 2.1)))
