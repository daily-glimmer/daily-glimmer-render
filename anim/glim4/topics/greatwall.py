# Thema: Can you see the Great Wall of China from space?  (Mythos-Format)
CENTER = 1050
PAL = ((8, 14, 40), (20, 30, 70))
HI = {"Great", "Wall", "space?", "naked", "eye!", "road.", "colors", "blends", "Yang", "Liwei,", "zoom", "lights", "Moon,", "structure"}
WOW = (1, 3)
EARTH, LAND, SEA = (40, 110, 190), (90, 170, 100), (40, 110, 190)

def planet(P, x, y, r, t):
    P.circ(x, y, r, SEA)
    for k, (dx, dy, rx, ry) in enumerate(((-.3, -.2, .35, .22), (.25, .1, .3, .35), (-.1, .45, .25, .15))):
        P.ell(x + dx * r + math.sin(t * .1) * 4, y + dy * r, rx * r, ry * r, LAND)
    P.arc(x, y, r + 8, 0, 360, (140, 200, 255), 6)

def station(P, x, y, s, t):
    P.rrect(x - 30 * s, y - 14 * s, x + 30 * s, y + 14 * s, 6 * s, (220, 220, 230))
    for d in (-1, 1): P.rrect(x + d * 40 * s - 30 * s, y - 40 * s, x + d * 40 * s + 30 * s, y + 40 * s, 4 * s, (60, 90, 170))
    P.line([(x - 70 * s, y), (x + 70 * s, y)], (200, 200, 210), 4 * s)

def hills(P, y, col=(150, 140, 100)):
    P.poly([(0, y), (200, y - 120), (420, y - 30), (650, y - 160), (880, y - 40), (W, y - 110), (W, H), (0, H)], col)

def wall(P, y0, k=1., col=(170, 155, 115)):
    pts = [(x, y0 - 90 * math.sin(x / 160) - 30 * math.cos(x / 70)) for x in range(-20, int(W * k) + 20, 20)]
    P.line(pts, col, 22)
    for x, y in pts[::3]: P.rrect(x - 8, y - 22, x + 8, y - 8, 3, col)

def SC(i, P, t, u):
    if i == 0:
        planet(P, 540, CENTER + 120, 300, t); station(P, 540 + math.cos(t * .5) * 380, CENTER + 120 + math.sin(t * .5) * 200 - 260, 1.2, t)
        P.text(820, CENTER - 300, "?", 140 * back(seg(u, .4, .9)), GLIM)
    elif i == 1:
        P.rrect(-20, CENTER - 200, W + 20, CENTER + 500, 0, (140, 130, 95)); hills(P, CENTER + 60)
        wall(P, CENTER + 200)
        P.rrect(380, CENTER + 330, 700, CENTER + 400, 10, (60, 60, 70))
        for x in range(400, 690, 60): P.rrect(x, CENTER + 360, x + 30, CENTER + 370, 2, CLOUD)
        P.badge(540, CENTER + 460, "about as wide as a road", 50, NIGHT, GLIM, back(seg(u, 1.2, 1.7)))
        P.stamp(540, CENTER - 320, "MYTH", seg(u, .25, .7))
    elif i == 2:
        P.rrect(-20, CENTER - 300, W + 20, CENTER + 500, 0, (150, 140, 100)); hills(P, CENTER, (140, 132, 96))
        a = 1 - .75 * eio(seg(u, .8, 3.0))
        wall(P, CENTER + 150, col=lc((140, 132, 96), (200, 60, 50), a))
        P.badge(540, CENTER - 360, "same colors as the land", 52, NIGHT, GLIM, back(seg(u, .4, .9)))
    elif i == 3:
        planet(P, 540, CENTER + 650, 600, t)
        x, y = 540, CENTER - 120
        P.circ(x, y, 150, (230, 230, 235)); P.circ(x, y, 112, (30, 50, 90)); P.ell(x - 40, y - 40, 30, 18, (120, 160, 220))
        P.badge(540, CENTER + 120, "Yang Liwei, 2003", 56, NIGHT, GLIM, back(seg(u, .4, .9)))
        P.cross(780, CENTER - 200, 50, k=back(seg(u, 2.2, 2.7)))
    elif i == 4:
        planet(P, 540, CENTER + 650, 600, t)
        for k in range(14):
            random.seed(k); px, py = 260 + random.random() * 560, CENTER + 120 + random.random() * 200
            P.circ(px, py, 6 + (k % 3) * 3, GLIM, glow=(120, 90, 20))
        P.rrect(330, CENTER - 360, 750, CENTER - 80, 30, (40, 40, 50), outline=CLOUD, w=6)
        P.circ(540, CENTER - 220, 90, (20, 20, 30), outline=(120, 120, 140), w=14)
        P.circ(540, CENTER - 220, 40 + 10 * math.sin(t * 3), (60, 80, 140))
        P.badge(540, CENTER - 20, "zoom lens: yes!", 54, HOPE, CLOUD, back(seg(u, .8, 1.3)))
    else:
        P.circ(300, CENTER + 250, 260, (190, 190, 195)); 
        for dx, dy, r in ((-60, -40, 40), (70, 60, 30), (10, 120, 22)): P.circ(300 + dx, CENTER + 250 + dy, r, (160, 160, 168))
        planet(P, 820, CENTER - 160, 90, t)
        P.stamp(540, CENTER - 320, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
