# Thema: Do bulls really hate the color red?  (Mythos-Format, Stempel in Satz 1)
CENTER = 1050
BULL, BULL2, HORN = (95, 65, 50), (70, 45, 35), (245, 235, 210)
PAL = ((60, 20, 30), (170, 70, 60))
HI = {"red?", "red", "two", "cones,", "gray", "moving", "any", "color,", "still.", "movement,", "blue", "myth"}
WOW = (1,)

def arena(P, t):
    P.poly([(0, CENTER + 250), (W, CENTER + 250), (W, H), (0, H)], (220, 180, 120))
    P.rrect(-20, CENTER + 150, W + 20, CENTER + 260, 10, (180, 50, 50))
    for x in range(40, W, 160): P.rrect(x, CENTER + 170, x + 90, CENTER + 240, 8, (240, 220, 180))

def bull(P, x, y, s, t, charge=0., flip=1, tint=None):
    f = flip; body = tint or BULL; dark = tint and lc(tint, (0, 0, 0), .3) or BULL2
    ph = t * (12 if charge else 2)
    for k, dx in enumerate((-110, -60, 70, 120)):
        sw = math.sin(ph + k * 1.7) * (30 if charge else 4) * s
        P.line([(x + f * dx * s, y + 40 * s), (x + f * dx * s + sw, y + 200 * s)], dark, 32 * s)
        P.ell(x + f * dx * s + sw, y + 205 * s, 20 * s, 12 * s, NIGHT)
    P.line([(x - f * 170 * s, y - 20 * s), (x - f * 210 * s, y + 80 * s + math.sin(t * 4) * 15 * s)], dark, 10 * s)
    P.ell(x, y, 185 * s, 100 * s, body)
    P.ell(x + f * 90 * s, y - 40 * s, 110 * s, 90 * s, body)                     # Schulter
    hx, hy = x + f * (210 + charge * 20) * s, y + (charge * 50) * s
    P.ell(hx, hy, 72 * s, 80 * s, body)
    P.ell(hx + f * 25 * s, hy + 50 * s, 48 * s, 36 * s, (200, 150, 140))
    for nx in (5, 45): P.circ(hx + f * nx * s, hy + 55 * s, 8 * s, NIGHT)
    for side in (-1, 1):
        P.line([(hx + side * 40 * s, hy - 50 * s), (hx + side * 95 * s, hy - 80 * s), (hx + side * 110 * s, hy - 130 * s)], HORN, 18 * s)
    P.circ(hx - 25 * s, hy - 15 * s, 10 * s, NIGHT); P.circ(hx + 30 * s, hy - 15 * s, 10 * s, NIGHT)
    if charge:
        for j in range(3):
            q = (t * 2 + j / 3) % 1; P.circ(x - f * (200 + q * 200) * s, y + 190 * s - q * 60 * s, (20 + q * 30) * s, lc((230, 210, 170), (180, 150, 110), q))

def cape(P, x, y, s, t, col, wave_amt=1.):
    pts = []
    for j in range(9):
        a = j / 8; pts.append((x + a * 260 * s, y + math.sin(t * 7 + a * 4) * 35 * s * wave_amt * a))
    bottom = [(px + math.sin(t * 7 + k) * 20 * s * wave_amt, py + 230 * s) for k, (px, py) in enumerate(reversed(pts))]
    P.poly(pts + bottom, col)
    P.line([(x - 10 * s, y), (x + 270 * s, y + math.sin(t * 7 + 4) * 35 * s * wave_amt)], (120, 80, 50), 10 * s)

def person(P, x, y, s, col):
    P.circ(x, y - 170 * s, 42 * s, (240, 200, 170))
    P.rrect(x - 55 * s, y - 120 * s, x + 55 * s, y + 60 * s, 30 * s, col)
    for dx in (-25, 25): P.line([(x + dx * s, y + 50 * s), (x + dx * s, y + 180 * s)], NIGHT, 26 * s)

def SC(i, P, t, u):
    if i == 0:
        arena(P, t); bull(P, 380, CENTER + 50, 1.0, t)
        cape(P, 640, CENTER - 150, 1.1, t, (220, 30, 40))
        P.text(540, CENTER - 330, "?!", 140 * back(seg(u, .3, .8)), GLIM)
    elif i == 1:
        arena(P, t); bull(P, 420, CENTER + 50, 1.05, t)
        cape(P, 640, CENTER - 160, 1.0, t, (220, 30, 40), .4)
        P.stamp(540, CENTER - 330, "MYTH", seg(u, .25, .7))
    elif i == 2:
        k = eio(seg(u, 1.0, 2.6))
        for j, (lab, col, x) in enumerate((("you", (220, 30, 40), 290), ("bull", lc((220, 30, 40), (120, 110, 90), 1.0), 790))):
            P.circ(x, CENTER - 20, 210, (250, 250, 250), outline=(200, 200, 210), w=10)
            c = (220, 30, 40) if j == 0 else lc((220, 30, 40), (125, 112, 92), k)
            P.circ(x, CENTER - 20, 120, c); P.circ(x, CENTER - 20, 50, NIGHT); P.circ(x + 25, CENTER - 45, 16, (255, 255, 255))
            P.badge(x, CENTER + 260, lab, 60, NIGHT, CLOUD, back(seg(u, .2 + j * .3, .7 + j * .3)))
        for j, c in enumerate(((60, 120, 255), (255, 210, 60))):
            P.circ(700 + j * 180, CENTER + 430, 50 * back(seg(u, 2.0 + j * .3, 2.5 + j * .3)), c)
        P.text(540, CENTER + 560, "2 color cones", 58, GLIM)
    elif i == 3:
        arena(P, t)
        cols = [(40, 110, 230), (250, 200, 40), (60, 180, 90)]
        c = cols[int(u / 1.6) % 3]
        cape(P, 640, CENTER - 230, .9, t, c)
        bull(P, lerp(150, 430, (math.sin(u * 4) + 1) / 2), CENTER + 40, .85, t, charge=1.)
        person(P, 150, CENTER - 20, .8, (220, 30, 40))
        P.badge(150, CENTER - 230, "ignored", 44, NIGHT, CLOUD, back(seg(u, 3.5, 4.0)))
    elif i == 4:
        arena(P, t)
        bull(P, 360, CENTER + 50, .95, t)
        cape(P, 600, CENTER - 160, 1.0, t, (240, 240, 240), 1.6)
        for j in range(3):
            q = (t * 1.5 + j / 3) % 1; P.arc(720, CENTER - 40, 120 + q * 260, -60, 60, lc(GLIM, (0, 0, 0), q), 10 * (1 - q) + 3)
        P.badge(540, CENTER + 470, "MOVEMENT", 72, HOOK, CLOUD, back(seg(u, .3, .8)))
    else:
        arena(P, t); bull(P, 380, CENTER + 50, 1.0, t, charge=.6)
        cape(P, 620, CENTER - 170, 1.0, t, (40, 110, 230))
        P.stamp(540, CENTER - 330, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
