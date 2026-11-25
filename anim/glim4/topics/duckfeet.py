# Thema: Do ducks get frozen feet when they stand on ice?  (Mythos-Format, Winter)
exec(open(os.path.join(HERE, "topics", "ducks.py")).read(), globals())
CENTER = 1050
PAL = ((70, 130, 180), (150, 200, 235))
HI = {"frozen", "ice?", "myth.", "trick.", "warm", "cold", "jumps", "freezing,", "bone", "tendon,", "Fact:", "feet"}
WOW = (1, 3, 5)
ICE = CENTER + 300
RED = (220, 60, 60); BLUE = (60, 120, 220); ORANGE = (245, 150, 40)

def icepond(P, t):
    P.poly([(0, ICE - 20), (W, ICE - 20), (W, H), (0, H)], (205, 230, 245), outline=(150, 190, 220), w=6)
    for k in range(5):
        x = 80 + k * 230
        P.line([(x, ICE + 40 + k % 2 * 60), (x + 120, ICE + 70 + k % 2 * 60)], (240, 250, 255), 6)
    for x in (70, 1010):
        for j in range(3): P.line([(x + j * 16, ICE - 20), (x + j * 16 + math.sin(t + j) * 6, ICE - 130 - j * 20)], (150, 130, 90), 8)

def snow(P, t, n=26):
    for k in range(n):
        x = (k * 97 + math.sin(t * .8 + k) * 30) % W
        y = (k * 173 + t * 70) % (ICE - 100 - (CENTER - 260)) + CENTER - 260
        P.circ(x, y, 7 + k % 3 * 2, (235, 245, 255), outline=(150, 185, 215), w=2)

def webfoot(P, x, y, s, col=ORANGE):
    P.poly([(x - 10 * s, y - 6 * s), (x - 60 * s, y + 22 * s), (x + 60 * s, y + 22 * s), (x + 10 * s, y - 6 * s)], col, outline=lc(col, (0, 0, 0), .3), w=3)
    for dx in (-45, 0, 45): P.line([(x, y), (x + dx * s, y + 20 * s)], lc(col, (0, 0, 0), .3), 3)

def sduck(P, x, y, s, t, quack=0., flip=False, female=False):
    # stehende Ente: Beine + Schwimmfüße, darüber Körper aus ducks.py
    for dx in (-30, 30):
        P.line([(x + dx * s, y - 40 * s), (x + dx * s, y + 40 * s)], ORANGE, 12 * s)
        webfoot(P, x + dx * s, y + 46 * s, s)
    duck(P, x, y - 100 * s, s, t, female=female, quack=quack, flip=flip)

def vessel(P, x, y0, y1, col, t, down=True, w=60):
    P.rrect(x - w / 2, y0, x + w / 2, y1, w / 2, lc(col, CLOUD, .35), outline=col, w=6)
    n = 6; L = y1 - y0
    for k in range(n):
        q = ((k / n) + (t * .35 if down else -t * .35)) % 1
        yy = y0 + 30 + q * (L - 60)
        if down: P.poly([(x - 18, yy - 12), (x + 18, yy - 12), (x, yy + 14)], col)
        else: P.poly([(x - 18, yy + 12), (x + 18, yy + 12), (x, yy - 14)], col)

def legdiag(P, t, u, heat=0.):
    y0, y1 = CENTER - 170, CENTER + 330
    P.rrect(300, y0 - 40, 780, y1 + 40, 60, (250, 220, 170), outline=(200, 150, 90), w=6)
    vessel(P, 440, y0, y1, RED, t, True); vessel(P, 640, y0, y1, BLUE, t, False)
    if heat > 0:
        for k in range(4):
            yy = y0 + 70 + k * 115; q = (t * .9 + k * .25) % 1
            xx = lerp(480, 600, q); a = heat * (1 - abs(q - .5) * 1.6)
            P.line([(xx - 22, yy), (xx + 22, yy)], lc(CLOUD, GLIM, a), 10)
            P.poly([(xx + 22, yy - 14), (xx + 42, yy), (xx + 22, yy + 14)], lc(CLOUD, GLIM, a))

def therm(P, x, y, level, col, k=1.):
    if k <= 0: return
    P.rrect(x - 22, y - 160, x + 22, y + 40, 22, CLOUD, outline=NIGHT, w=5)
    P.circ(x, y + 50, 36, col, outline=NIGHT, w=5)
    P.rrect(x - 11, y + 30 - 170 * level * k, x + 11, y + 40, 11, col)

def SC(i, P, t, u):
    q = .5 + .5 * math.sin(t * 7)
    if i == 0:
        icepond(P, t); snow(P, t)
        sduck(P, 470, ICE - 70, 1.25, t, quack=q * seg(u, .2, .5))
        P.text(840, CENTER - 120, "?", 170 * back(seg(u, .5, 1.0)), GLIM)
        P.text(840, ICE + 140, "-5 °C", 70 * back(seg(u, .9, 1.4)), BLUE)
    elif i == 1:
        icepond(P, t); snow(P, t)
        sduck(P, 470, ICE - 70, 1.2, t)
        P.badge(560, CENTER - 110, "frozen feet?", 60, BLUE, CLOUD, back(seg(u, .6, 1.1)))
        P.cross(850, CENTER - 110, 36, k=back(seg(u, 1.0, 1.4)))
        P.stamp(540, CENTER - 330, "MYTH", seg(u, .25, .7))
    elif i == 2:
        legdiag(P, t, u)
        P.badge(440, CENTER + 450, "warm", 54, RED, CLOUD, back(seg(u, .6, 1.1)))
        P.badge(640, CENTER + 450, "cold", 54, BLUE, CLOUD, back(seg(u, 2.4, 2.9)))
        P.text(440, CENTER - 230, "down", 44 * back(seg(u, .9, 1.3)), RED)
        P.text(640, CENTER - 230, "up", 44 * back(seg(u, 2.6, 3.0)), BLUE)
    elif i == 3:
        legdiag(P, t, u, heat=seg(u, .3, .9))
        therm(P, 160, CENTER - 20, .85, RED, eout(seg(u, 2.2, 2.8)))
        therm(P, 920, CENTER + 180, .2, BLUE, eout(seg(u, 2.0, 2.6)))
        P.badge(160, CENTER + 160, "body", 46, RED, CLOUD, back(seg(u, 2.6, 3.0)))
        P.badge(920, CENTER + 360, "feet ~1 °C", 46, BLUE, CLOUD, back(seg(u, 2.2, 2.7)))
        P.badge(540, CENTER + 460, "heat swaps over", 54, NIGHT, GLIM, back(seg(u, .9, 1.4)))
    elif i == 4:
        icepond(P, t)
        s = 3.0; x, y = 540, CENTER + 80
        P.poly([(x - 10 * s, y - 120), (x - 60 * s, y + 22 * s), (x + 60 * s, y + 22 * s), (x + 10 * s, y - 120)], lc(ORANGE, CLOUD, .4), outline=ORANGE, w=6)
        k = eout(seg(u, .4, 1.4))
        for dx in (-50, 0, 50):
            P.line([(x, y - 140), (x + dx * s * k, y + 15 * s)], CLOUD, 14)
            P.line([(x, y - 140), (x + dx * s * k, y + 15 * s)], (170, 160, 150), 4)
        P.line([(x, CENTER - 230), (x, y - 140)], CLOUD, 26); P.line([(x, CENTER - 230), (x, y - 140)], (190, 180, 170), 8)
        P.badge(800, CENTER - 140, "bone", 52, NIGHT, CLOUD, back(seg(u, .5, 1.0)))
        P.badge(820, CENTER + 10, "tendon", 52, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
        P.badge(270, CENTER - 60, "little muscle", 48, HOOK, CLOUD, back(seg(u, 2.6, 3.1)))
    else:
        icepond(P, t); snow(P, t, 18)
        sduck(P, 330, ICE - 60, 1.0, t, quack=q, female=True)
        sduck(P, 720, ICE - 50, .9, t, flip=True)
        for k in range(3): P.heart(530 + k * 40, CENTER - 40 - k * 50 - (t * 30) % 40, 18, HOOK)
        P.stamp(540, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
