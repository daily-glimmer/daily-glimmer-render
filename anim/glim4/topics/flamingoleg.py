# Thema: Why do flamingos stand on one leg?
CENTER = 1050
PINK, PINK2, BEAK = (250, 140, 160), (225, 100, 130), (40, 35, 45)
WATER = (110, 180, 210)
PAL = ((120, 190, 230), (250, 205, 180))
HI = {"leg?", "easier", "two!", "weight", "locks", "joints", "no", "muscle", "balanced", "nap", "barely", "sway,", "energy.", "warm.", "minute?"}
WOW = (1, 3)
GROUND = CENTER + 330

def lake(P, t):
    P.rrect(-40, GROUND - 10, W + 40, H, 0, WATER)
    for k in range(4):
        x = (k * 300 + t * 40) % (W + 200) - 100
        P.arc(x, GROUND + 40 + k * 30, 60, 200, 340, lc(WATER, CLOUD, .5), 6)

def flamingo(P, x, y, s, t, one=1., sleepy=0., sway=1., lean=0.):
    """Flamingo stehend; one = 1 -> ein Bein hochgezogen, sleepy -> Kopf im Gefieder."""
    sw = math.sin(t * 2.0) * 6 * s * sway
    bx, by = x + sw, y - 330 * s           # Körper
    # Standbein (gerade, mit "Knie" = Fußgelenk)
    P.line([(bx, by + 50 * s), (bx + 4 * s, by + 190 * s), (x, y)], PINK2, 12 * s)
    P.line([(x - 40 * s, y), (x + 40 * s, y)], PINK2, 10 * s)
    # zweites Bein: von unten (one=0) nach oben eingeklappt (one=1)
    kx, ky = lerp(bx + 40 * s, bx + 70 * s, one), lerp(by + 190 * s, by + 120 * s, one)
    fx, fy = lerp(x + 46 * s, bx - 10 * s, one), lerp(y, by + 80 * s, one)
    P.line([(bx + 20 * s, by + 50 * s), (kx, ky), (fx, fy)], PINK2, 12 * s)
    # Körper + Flügel
    P.ell(bx, by, 120 * s, 72 * s, PINK, outline=PINK2, w=4 * s)
    P.ell(bx + 30 * s, by - 8 * s, 80 * s, 44 * s, PINK2)
    P.poly([(bx + 100 * s, by - 20 * s), (bx + 170 * s, by + 10 * s), (bx + 100 * s, by + 30 * s)], PINK2)
    if sleepy > .5:
        hx, hy = bx - 50 * s, by - 50 * s
        P.circ(hx, hy, 40 * s, PINK); P.arc(hx - 5 * s, hy, 16 * s, 200, 340, NIGHT, 4 * s)
        for k in range(3):
            q = (t * .5 + k / 3) % 1
            P.text(hx - 40 * s - q * 60 * s, hy - 80 * s - q * 140 * s, "z", (30 + 20 * q) * s, CLOUD)
        return
    # Hals (S-Kurve) + Kopf
    nx = bx - 90 * s + lean * 30 * s
    pts = [(bx - 90 * s, by - 20 * s), (nx - 50 * s, by - 120 * s), (nx + 10 * s, by - 210 * s), (nx - 10 * s, by - 290 * s)]
    P.line(pts, PINK, 22 * s)
    hx, hy = pts[-1]
    P.circ(hx, hy, 36 * s, PINK)
    P.poly([(hx - 20 * s, hy - 10 * s), (hx - 80 * s, hy + 20 * s), (hx - 70 * s, hy + 45 * s), (hx - 18 * s, hy + 18 * s)], CLOUD)
    P.poly([(hx - 60 * s, hy + 24 * s), (hx - 80 * s, hy + 20 * s), (hx - 70 * s, hy + 45 * s)], BEAK)
    P.circ(hx + 6 * s, hy - 8 * s, 8 * s, NIGHT); P.circ(hx + 8 * s, hy - 10 * s, 3 * s, CLOUD)

def SC(i, P, t, u):
    if i == 0:
        lake(P, t); flamingo(P, 540, GROUND, 1.25, t, one=eio(seg(u, .3, 1.2)))
        P.text(830, CENTER - 230, "?", 150 * back(seg(u, .6, 1.1)), HOOK)
    elif i == 1:
        lake(P, t)
        flamingo(P, 320, GROUND, .9, t, one=0.)
        flamingo(P, 770, GROUND, .9, t + 1, one=1.)
        P.badge(320, CENTER - 300, "2 legs", 56, HOOK, CLOUD, back(seg(u, .4, .9)))
        P.badge(770, CENTER - 300, "1 leg = easier", 56, HOPE, CLOUD, back(seg(u, 1.2, 1.7)))
    elif i == 2:
        lake(P, t); flamingo(P, 540, GROUND, 1.25, t, sway=.2)
        k = back(seg(u, .5, 1.0))
        P.line([(560, CENTER - 140), (560, CENTER + 120)], HOOK, 10 * k)                         # Schwerpunkt-Linie
        P.poly([(530, CENTER + 90), (590, CENTER + 90), (560, CENTER + 140)], HOOK) if k > .5 else None
        q = back(seg(u, 1.8, 2.3))
        if q > .02:
            P.circ(545, GROUND - 155, 34 * q, GLIM, outline=NIGHT, w=5)
            P.rrect(530, GROUND - 175, 560, GROUND - 160, 6, NIGHT) if q > .6 else None
        P.badge(540, CENTER + 420, "weight locks the joint", 54, NIGHT, GLIM, back(seg(u, 2.2, 2.7)))
    elif i == 3:
        P.rrect(160, CENTER - 230, 920, CENTER + 330, 40, (240, 236, 226), outline=(180, 170, 160), w=6)   # Labor-Tafel
        flamingo(P, 540, CENTER + 270, .95, t, sway=0.)
        P.circ(820, CENTER - 140, 60, (200, 200, 210), outline=NIGHT, w=6)
        P.text(820, CENTER - 140, "0%", 40, CLOUD)
        P.badge(540, CENTER + 420, "no muscle power", 56, HOOK, CLOUD, back(seg(u, .6, 1.1)))
        P.check(300, CENTER - 140, 50, HOPE, back(seg(u, 2.0, 2.5)))
    elif i == 4:
        lake(P, t)
        P.circ(860, CENTER - 230, 70, (250, 245, 220), glow=(80, 80, 60))
        P.circ(890, CENTER - 250, 60, lc(PAL[0], NIGHT, .2))
        flamingo(P, 540, GROUND, 1.2, t, sleepy=1., sway=.15)
        P.badge(540, CENTER + 430, "almost no energy", 56, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
    else:
        lake(P, t); flamingo(P, 470, GROUND, 1.1, t, lean=math.sin(t * 2))
        g = .5 + .5 * math.sin(t * 4)
        for k in range(3):
            a = 3.6 + k * .5; P.arc(560, CENTER - 20, 180 + k * 30, 200 + k * 10, 250 + k * 10, lc(HOOK, GLIM, g), 10)
        P.badge(540, CENTER - 300, "keeps one leg warm", 56, HOOK, CLOUD, back(seg(u, .5, 1.0)))
