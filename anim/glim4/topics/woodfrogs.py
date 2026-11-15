# Thema: How do wood frogs survive being frozen?
CENTER = 1050
FROG, FROG2, MASKC, ICE = (165, 120, 75), (130, 90, 55), (70, 45, 30), (170, 220, 255)
PAL = ((15, 30, 70), (60, 110, 160))
HI = {"frozen?", "freeze", "solid,", "stops", "ice", "liver", "sugar.", "antifreeze", "burst,", "spring,", "thaws,", "hops", "minus", "eighteen"}
WOW = (1, 3, 5)

def wfrog(P, x, y, s, t, ice=0., beat=1., jump=0.):
    y -= jump * 160 * s
    col = lc(FROG, ICE, ice * .6); c2 = lc(FROG2, ICE, ice * .5)
    for dx in (-1, 1):
        P.ell(x + dx * 95 * s, y + 55 * s, 60 * s, 30 * s, c2)
        P.ell(x + dx * 150 * s, y + 80 * s, 38 * s, 12 * s, c2)
    P.ell(x, y, 140 * s, 90 * s, col, outline=lc(col, (0, 0, 0), .35), w=4 * s)
    P.ell(x - 70 * s, y - 20 * s, 34 * s, 22 * s, MASKC)       # dunkle "Maske" des Waldfroschs
    P.ell(x + 70 * s, y - 20 * s, 34 * s, 22 * s, MASKC)
    for dx in (-55, 55):
        P.circ(x + dx * s, y - 70 * s, 30 * s, col)
        if ice > .5: P.arc(x + dx * s, y - 70 * s, 14 * s, 200, 340, NIGHT, 5 * s)
        else: P.circ(x + dx * s, y - 70 * s, 16 * s, NIGHT); P.circ(x + dx * s + 5 * s, y - 75 * s, 5 * s, CLOUD)
    P.arc(x, y + 5 * s, 50 * s, 20, 160, lc(col, (0, 0, 0), .45), 5 * s)
    P.heart(x + 10 * s, y + 35 * s, 18 * s * beat, HOOK if ice < .5 else (120, 120, 150))
    if ice > .05:
        random.seed(9)
        for k in range(12):
            a = random.random() * 6.28
            ix, iy = x + math.cos(a) * 130 * s, y + math.sin(a) * 85 * s
            r = 16 * s * ice
            P.poly([(ix, iy - r), (ix + r * .6, iy), (ix, iy + r), (ix - r * .6, iy)], (230, 245, 255))

def flake(P, x, y, r, col=(230, 245, 255)):
    for k in range(3):
        a = k * math.pi / 3
        P.line([(x - math.cos(a) * r, y - math.sin(a) * r), (x + math.cos(a) * r, y + math.sin(a) * r)], col, 5)

def snowfall(P, t, n=24):
    random.seed(4)
    for k in range(n):
        q = (t * .08 + random.random()) % 1
        flake(P, 80 + random.random() * 920 + math.sin(t + k) * 25, lerp(CENTER - 520, CENTER + 520, q), 10 + random.random() * 8)

def SC(i, P, t, u):
    if i == 0:
        snowfall(P, t)
        P.ell(540, CENTER + 230, 420, 60, (220, 230, 245))
        wfrog(P, 540, CENTER + 90, 1.5, t, ice=eio(seg(u, .3, 1.6)))
        P.text(820, CENTER - 250, "?", 150 * back(seg(u, .6, 1.1)), GLIM)
    elif i == 1:
        snowfall(P, t, 14)
        ice = eio(seg(u, .2, 2.0)); beat = (1 + .25 * math.sin(t * 9)) * (1 - ice) + .9 * ice
        wfrog(P, 540, CENTER - 20, 1.6, t, ice=ice, beat=beat)
        # EKG-Linie wird flach
        pts = []
        for k in range(60):
            x = 150 + k * 13; ph = (k / 60 * 6 + t * 3) % 1
            amp = (1 - ice) * (60 if .45 < ph < .55 else 0)
            pts.append((x, CENTER + 330 - amp))
        P.line(pts, HOOK if ice < .8 else (150, 160, 180), 7)
        P.badge(540, CENTER + 450, "heart stops", 56, NIGHT, GLIM, back(seg(u, 2.4, 2.9)))
    elif i == 2:
        P.circ(540, CENTER - 40, 210, (40, 60, 100), outline=ICE, w=6)
        P.ell(500, CENTER - 60, 120, 80, (150, 70, 60))           # Leber
        P.text(500, CENTER - 60, "liver", 46, CLOUD)
        for k in range(14):
            q = ((t * .45) + k / 14) % 1; a = k * 2.4
            r = 60 + q * 330
            sx, sy = 500 + math.cos(a) * r, CENTER - 60 + math.sin(a) * r * .8
            if q > .02: P.rrect(sx - 14, sy - 14, sx + 14, sy + 14, 4, CLOUD, outline=(180, 180, 190), w=2)
        P.badge(540, CENTER + 330, "sugar flood", 60, GLIM, NIGHT, back(seg(u, .9, 1.4)))
    elif i == 3:
        for k, (cx, cy) in enumerate(((360, CENTER - 140), (720, CENTER - 140), (540, CENTER + 120))):
            q = back(seg(u, .2 + k * .25, .7 + k * .25))
            P.circ(cx, cy, 120 * q, (240, 170, 160), outline=(170, 80, 80), w=6)
            for j in range(5):
                a = j * 1.26 + t * .7
                P.rrect(cx + math.cos(a) * 60 * q - 10, cy + math.sin(a) * 60 * q - 10, cx + math.cos(a) * 60 * q + 10, cy + math.sin(a) * 60 * q + 10, 3, CLOUD)
        g = eio(seg(u, 1.4, 2.6))
        random.seed(2)
        for k in range(18):
            a = random.random() * 6.28; r = 270 + random.random() * 60
            x, y = 540 + math.cos(a) * r, CENTER - 40 + math.sin(a) * r * .9
            s = 22 * g
            if s > 1: P.poly([(x, y - s), (x + s * .6, y), (x, y + s), (x - s * .6, y)], ICE)
        P.badge(540, CENTER + 330, "natural antifreeze", 56, HOPE, CLOUD, back(seg(u, .6, 1.1)))
        P.badge(540, CENTER + 440, "ice stays outside cells", 50, NIGHT, ICE, back(seg(u, 2.4, 2.9)))
    elif i == 4:
        P.circ(860, CENTER - 380, 70, GLIM, glow=(255, 194, 51, 60))
        P.ell(540, CENTER + 230, 440, 60, (90, 160, 80))
        for k in range(5): P.line([(200 + k * 160, CENTER + 200), (215 + k * 160, CENTER + 140)], (60, 140, 60), 8)
        ice = 1 - eio(seg(u, .2, 1.6))
        jump = max(0., math.sin((u - 2.2) * 3.2)) if u > 2.2 else 0.
        beat = 1 + .25 * math.sin(t * 9) if ice < .3 else 1.
        wfrog(P, 540, CENTER + 90, 1.4, t, ice=ice, beat=beat, jump=jump)
        P.badge(540, CENTER + 400, "thawed & alive", 58, HOPE, CLOUD, back(seg(u, 1.8, 2.3)))
    else:
        snowfall(P, t, 16)
        P.rrect(150, CENTER - 300, 220, CENTER + 120, 35, CLOUD); P.circ(185, CENTER + 150, 62, (80, 150, 230))
        P.rrect(166, CENTER - 40 + 160 * (1 - eio(seg(u, .3, 2.0))) * 0, 204, CENTER + 150, 19, (80, 150, 230))
        wfrog(P, 560, CENTER + 40, 1.15, t, ice=.7)
        P.badge(560, CENTER - 300, "-18 °C", 84, NIGHT, ICE, back(seg(u, .6, 1.1)))
        P.badge(560, CENTER - 170, "(about 0 °F)", 48, NIGHT, CLOUD, back(seg(u, 1.2, 1.7)))
