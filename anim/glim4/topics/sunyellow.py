# Thema: Is the Sun really yellow?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6)
# Quellen: NASA (Sonne strahlt alle Farben, erscheint aus dem All weiß), NOAA/NASA zur Rayleigh-Streuung
# (Atmosphäre streut Blau, Sonne wirkt gelb/orange, besonders tief am Horizont).
CENTER = 1050
YEL, WHT, ORG = (255, 210, 60), (255, 253, 245), (255, 140, 50)
RAINBOW = [(235, 70, 70), (250, 150, 50), (250, 220, 60), (90, 200, 100), (70, 140, 230), (130, 90, 210)]
PAL = ((90, 160, 230), (170, 210, 245))
HI = {"yellow?", "myth!", "white,", "every", "color", "white.", "astronauts", "black", "blue", "yellow,", "orange", "white", "disguise!"}
WOW = (1,)

def sunball(P, x, y, r, col, t, rays=True):
    if rays:
        for k in range(14):
            a = k * math.pi / 7 + t * .25
            P.line([(x + math.cos(a) * (r + 18), y + math.sin(a) * (r + 18)), (x + math.cos(a) * (r + 60), y + math.sin(a) * (r + 60))], col, 14)
    P.circ(x, y, r, col, glow=(150, 140, 90), outline=(235, 200, 110), w=5)

def hills(P, col=(110, 180, 100)):
    c2 = tuple(int(v * .85) for v in col)
    P.ell(250, CENTER + 420, 520, 160, col); P.ell(850, CENTER + 450, 520, 180, c2)
    P.poly([(0, CENTER + 450), (W, CENTER + 450), (W, H), (0, H)], c2)

def station(P, x, y, s):
    P.rrect(x - 60 * s, y - 18 * s, x + 60 * s, y + 18 * s, 8 * s, (200, 205, 215))
    for dx in (-150, 95):
        P.rrect(x + dx * s, y - 50 * s, x + (dx + 55) * s, y + 50 * s, 4 * s, (60, 90, 170))
    P.line([(x - 95 * s, y), (x + 95 * s, y)], (200, 205, 215), 6 * s)

def SC(i, P, t, u):
    if i == 0:
        hills(P); sunball(P, 540, CENTER - 120, 150, YEL, t)
        P.text(800, CENTER - 300, "?", 160 * back(seg(u, .5, 1.0)), (40, 60, 110))
    elif i == 1:
        hills(P); sunball(P, 540, CENTER - 120, 150, lc(YEL, WHT, eio(seg(u, .5, 1.8))), t)
        P.stamp(560, CENTER + 330, "MYTH", seg(u, .25, .7), rot=-6)
        P.badge(540, CENTER + 520, "really white", 60, NIGHT, CLOUD, back(seg(u, 1.6, 2.1)))
    elif i == 2:
        k = eout(seg(u, .3, 1.6))
        for j, c in enumerate(RAINBOW):
            y0 = CENTER - 250 + j * 70
            P.line([(80, y0), (lerp(80, 560, k), lerp(y0, CENTER - 75, k))], c, 30)
        if k > .9:
            P.line([(560, CENTER - 75), (lerp(560, 1000, seg(u, 1.6, 2.4)), CENTER - 75)], WHT, 60 * eout(seg(u, 1.6, 2.2)), glow=(120, 120, 110))
        P.badge(540, CENTER + 280, "all colors mix to white", 54, NIGHT, CLOUD, back(seg(u, 2.0, 2.5)))
    elif i == 3:
        P.rrect(40, CENTER - 360, 1040, CENTER + 360, 50, (8, 10, 20))
        random.seed(3)
        for _ in range(40): P.circ(80 + random.random() * 920, CENTER - 320 + random.random() * 640, 3, (200, 200, 220))
        sunball(P, 380, CENTER - 60, 120, WHT, t)
        station(P, 760 + math.sin(t * .5) * 30, CENTER + 160, 1.0)
        P.badge(540, CENTER + 450, "seen from space", 58, NIGHT, CLOUD, back(seg(u, .8, 1.3)))
    elif i == 4:
        P.rrect(0, CENTER - 520, W, CENTER + 460, 0, lc((80, 150, 230), (250, 160, 90), eio(seg(u, 1.5, 4.0))))
        sunball(P, 540, lerp(CENTER - 120, CENTER + 230, eio(seg(u, 1.0, 3.5))), 130, lc(YEL, ORG, eio(seg(u, 1.0, 3.5))), t)
        random.seed(8)
        for j in range(18):
            q = (u * .4 + random.random()) % 1
            P.circ(100 + random.random() * 880, CENTER - 420 + q * 700, 9, (70, 120, 230))
        hills(P, (90, 140, 90))
        P.badge(540, CENTER - 380, "air scatters blue", 58, NIGHT, CLOUD, back(seg(u, .4, .9)))
    else:
        hills(P); sunball(P, 420, CENTER - 60, 140, WHT, t)
        P.stamp(800, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
