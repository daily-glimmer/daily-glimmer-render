# Thema: How do owls fly so silently?
CENTER = 1050
OWL, OWL2, BELLY = (160, 118, 80), (118, 82, 55), (230, 205, 165)
PIG = (150, 160, 180)
PAL = ((20, 30, 60), (60, 80, 130))
HI = {"silently?", "whooshing", "barely", "comb-like", "teeth", "soft", "velvety,", "soak", "glide", "slowly,", "few", "quieter", "fans!"}
WOW = (2, 5)

def wing(P, x, y, s, side, ang, col=OWL, comb=False, tip=OWL2):
    """Flügel von (x,y) nach außen; ang = Schlagwinkel in Grad (+ = hoch)."""
    a = math.radians(-ang) ; L = 330 * s
    ex, ey = x + side * math.cos(a) * L, y + math.sin(a) * L
    mx, my = x + side * math.cos(a) * L * .5, y + math.sin(a) * L * .5
    pts = [(x, y - 30 * s), (mx, my - 45 * s), (ex, ey), (mx + side * 40 * s, my + 70 * s), (x, y + 60 * s)]
    P.poly(pts, col)
    for k in range(5):                                         # Schwungfedern
        q = .35 + k * .14
        fx, fy = x + side * math.cos(a) * L * q, y + math.sin(a) * L * q
        P.line([(fx, fy + 10 * s), (fx + side * 25 * s, fy + 75 * s - k * 6 * s)], tip, 9 * s)
    if comb:
        for k in range(9):
            q = .15 + k * .09
            fx, fy = lerp(x, mx, q * 2) if q < .5 else lerp(mx, ex, (q - .5) * 2), 0
            fy = lerp(y - 30 * s, my - 45 * s, q * 2) if q < .5 else lerp(my - 45 * s, ey, (q - .5) * 2)
            P.line([(fx, fy), (fx - side * 10 * s, fy - 28 * s)], GLIM, 6 * s)

def flyowl(P, x, y, s, t, speed=1.6, amp=28):
    ang = math.sin(t * speed * 2) * amp
    for side in (-1, 1): wing(P, x, y, s, side, ang)
    P.ell(x, y + 30 * s, 85 * s, 120 * s, OWL)
    P.ell(x, y + 50 * s, 55 * s, 85 * s, BELLY)
    hx, hy = x, y - 95 * s
    P.circ(hx, hy, 80 * s, OWL)
    for side in (-1, 1): P.poly([(hx + side * 45 * s, hy - 55 * s), (hx + side * 72 * s, hy - 105 * s), (hx + side * 72 * s, hy - 45 * s)], OWL2)
    for side in (-1, 1):
        P.ell(hx + side * 32 * s, hy - 5 * s, 30 * s, 30 * s, (250, 240, 220))
        P.ell(hx + side * 32 * s, hy - 5 * s, 20 * s, 20 * s, (255, 190, 40)); P.circ(hx + side * 32 * s, hy - 5 * s, 10 * s, NIGHT)
        P.circ(hx + side * 36 * s, hy - 10 * s, 4 * s, CLOUD)
    P.poly([(hx - 9 * s, hy + 22 * s), (hx + 9 * s, hy + 22 * s), (hx, hy + 46 * s)], (240, 180, 60))

def pigeon(P, x, y, s, t):
    ang = math.sin(t * 14) * 45
    for side in (-1, 1): wing(P, x, y, s * .7, side, ang, PIG, tip=lc(PIG, (0, 0, 0), .3))
    P.ell(x, y + 10 * s, 70 * s, 95 * s, PIG); P.circ(x, y - 85 * s, 50 * s, lc(PIG, (0, 0, 0), .15))
    P.circ(x - 18 * s, y - 92 * s, 8 * s, NIGHT); P.circ(x + 18 * s, y - 92 * s, 8 * s, NIGHT)
    P.poly([(x - 9 * s, y - 72 * s), (x + 9 * s, y - 72 * s), (x, y - 52 * s)], (240, 170, 60))

def moon(P, x, y, r):
    P.circ(x, y, r, (240, 236, 210)); P.circ(x - r * .3, y - r * .2, r * .18, (220, 215, 190)); P.circ(x + r * .35, y + r * .3, r * .12, (220, 215, 190))

def SC(i, P, t, u):
    if i == 0:
        moon(P, 780, CENTER - 180, 150)
        flyowl(P, 470 + math.sin(t * .7) * 30, CENTER + 120, 1.1, t)
        P.text(860, CENTER + 300, "?", 150 * back(seg(u, .4, .9)), GLIM)
    elif i == 1:
        pigeon(P, 300, CENTER + 60, 1.0, t)
        for k in range(3):
            q = (t * 1.5 + k / 3) % 1
            P.arc(300, CENTER + 60, 220 + q * 200, 200, 340, lc(HOOK, NIGHT, q), 10 * (1 - q) + 3)
        P.badge(300, CENTER + 330, "WHOOSH", 56, HOOK, CLOUD, back(seg(u, .5, 1.0)))
        flyowl(P, 780, CENTER + 40, .8, t)
        P.badge(780, CENTER + 330, "shhh...", 56, HOPE, CLOUD, back(seg(u, 2.2, 2.7)))
    elif i == 2:
        k = eout(seg(u, 0, .6))
        wing(P, 120, CENTER + 120, 2.2 * k, 1, 12, comb=True)
        for j in range(6):                                     # Luftstrom: glatt -> kleine Wirbel
            q = (t * .9 + j / 6) % 1; yy = CENTER - 160 + j * 30
            xx = lerp(1000, 80, q)
            if xx > 650: P.line([(xx, yy), (xx + 90, yy)], (150, 210, 255), 7)
            else: P.arc(xx, yy + 40, 14 + (650 - xx) * .03, 0, 300, (150, 210, 255), 5)
        P.badge(540, CENTER + 420, "comb-like edge", 60, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
    elif i == 3:
        k = back(seg(u, .1, .6))
        P.line([(540, CENTER + 330), (540, CENTER - 230 * k)], (230, 220, 200), 10)
        for j in range(14):
            yy = CENTER + 300 - j * 38 * k; w = (70 + 90 * math.sin(j / 13 * math.pi)) * k
            for d in (-1, 1): P.line([(540, yy), (540 + d * w, yy - 40 * k)], lc((245, 235, 215), OWL, .25), 16)
        for j in range(3):                                     # Schallwellen werden geschluckt
            q = (t * .8 + j / 3) % 1
            P.arc(960 - q * 300, CENTER, 90 + q * 40, 130, 230, lc(GLIM, NIGHT, q * 1.1), 14 * (1 - q) + 3)
        P.badge(540, CENTER + 420, "soft = quiet", 60, HOPE, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 4:
        moon(P, 850, CENTER - 200, 110)
        x = lerp(-150, 1230, (u / 4.2) % 1)
        flyowl(P, x, CENTER + 80 + math.sin(u * 1.5) * 30, 1.0, t, speed=.6, amp=14)
        P.badge(540, CENTER + 400, "big wings, few flaps", 56, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
    else:
        cx, cy = 480, CENTER + 120
        P.rrect(cx - 20, cy, cx + 20, cy + 300, 12, (90, 100, 130))
        P.ell(cx, cy + 300, 160, 40, (90, 100, 130))
        rot = t * 2.5
        for b in range(3):
            a = rot + b * 2.094
            bx, by = cx + math.cos(a) * 150, cy + math.sin(a) * 150
            P.ell(bx, by, 95, 50, OWL)
            P.circ(cx + math.cos(a) * 225, cy + math.sin(a) * 225, 10, CLOUD)
        P.circ(cx, cy, 45, OWL2, outline=CLOUD, w=6)
        P.badge(540, CENTER - 300, "quieter fans!", 60, HOPE, CLOUD, back(seg(u, 1.0, 1.5)))
