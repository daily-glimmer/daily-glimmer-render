# Thema: Do sunflowers really follow the sun?  (Mythos-Format: „nur junge“)
CENTER = 1050
PETAL, DISK, STEM = (255, 205, 40), (120, 75, 30), (70, 150, 70)
PAL = ((40, 80, 140), (240, 170, 100))
HI = {"follow", "sun?", "young!", "east", "west", "night", "clock.", "grown-up", "good,", "five", "bee", "visits!"}
WOW = (1, 5)

def field(P, y=CENTER + 330): P.poly([(0, y), (W, y - 20), (W, H), (0, H)], (110, 160, 70))

def sunflower(P, x, y, s, t, face=0., young=False):
    """face: -1 = Osten (links), +1 = Westen (rechts)."""
    h = (260 if young else 420) * s
    hx = x + face * 60 * s; hy = y - h
    P.line([(x, y), (x + face * 25 * s, y - h * .5), (hx, hy)], STEM, 18 * s)
    P.ell(x + 40 * s, y - h * .35, 55 * s, 20 * s, STEM); P.ell(x - 40 * s, y - h * .55, 55 * s, 20 * s, STEM)
    r = (60 if young else 95) * s; sq = .55 + .45 * (1 - abs(face))
    for k in range(14):
        a = k / 14 * 2 * math.pi; P.ell(hx + math.cos(a) * r * 1.15 * sq, hy + math.sin(a) * r * 1.15, r * .45 * sq, r * .45, PETAL)
    P.ell(hx, hy, r * .75 * sq, r * .75, DISK)
    P.ell(hx + face * r * .5, hy, r * .25 * sq, r * .25, lc(DISK, (0, 0, 0), .3))

def sky_sun(P, k, y0=CENTER - 420):
    x = lerp(120, 960, k); y = y0 + (abs(k - .5) * 2) ** 2 * 160
    P.circ(x, y, 55, (255, 220, 90), glow=mul(GLIM, 140))

def bee(P, x, y, s, t):
    P.ell(x, y, 26 * s, 18 * s, (255, 200, 40)); P.line([(x - 6 * s, y - 16 * s), (x - 6 * s, y + 16 * s)], NIGHT, 6 * s)
    a = math.sin(t * 40) * 6 * s; P.ell(x, y - 20 * s - a, 14 * s, 10 * s, (220, 240, 255))

def SC(i, P, t, u):
    if i == 0:
        k = (u / 2.5) % 1; sky_sun(P, k); field(P)
        for j, x in enumerate((240, 540, 840)): sunflower(P, x, CENTER + 360, 1.0, t, face=lerp(-1, 1, k))
        P.text(540, CENTER - 200, "?", 120 * back(seg(u, .4, .9)), CLOUD)
    elif i == 1:
        field(P)
        sunflower(P, 330, CENTER + 360, 1.0, t, face=math.sin(t * 2), young=True)
        sunflower(P, 750, CENTER + 360, 1.1, t, face=-1)
        P.badge(330, CENTER - 40, "young", 54, HOPE, CLOUD, back(seg(u, .3, .8)))
        P.badge(750, CENTER - 200, "grown-up", 54, NIGHT, CLOUD, back(seg(u, .6, 1.1)))
        P.stamp(540, CENTER - 400, "HALF TRUE", seg(u, .25, .7), col=HOOK, rot=-6)
    elif i == 2:
        k = eio(seg(u, .2, 3.6)); sky_sun(P, k); field(P)
        for x in (280, 540, 800): sunflower(P, x, CENTER + 360, 1.0, t, face=lerp(-1, 1, k), young=True)
        P.text(110, CENTER + 470, "E", 70, GLIM); P.text(970, CENTER + 470, "W", 70, GLIM)
    elif i == 3:
        k = eio(seg(u, .2, 3.4)); field(P)
        P.arc(820, CENTER - 420, 50, 100, 280, (250, 245, 210), 26)     # Mondsichel
        for x in (280, 540, 800): sunflower(P, x, CENTER + 360, 1.0, t, face=lerp(1, -1, k), young=True)
        P.circ(540, CENTER - 160, 90, (250, 250, 250), outline=(60, 60, 80), w=8)
        a = t * 2; P.line([(540, CENTER - 160), (540 + math.cos(a) * 65, CENTER - 160 + math.sin(a) * 65)], NIGHT, 8)
        P.badge(540, CENTER - 20, "inner clock", 54, NIGHT, GLIM, back(seg(u, .6, 1.1)))
    elif i == 4:
        k = (u / 3) % 1; sky_sun(P, k); field(P)
        for x in (240, 540, 840): sunflower(P, x, CENTER + 360, 1.0, t, face=-1)
        P.text(110, CENTER + 470, "E", 70, GLIM)
    else:
        field(P)
        sky_sun(P, .05)
        sunflower(P, 330, CENTER + 360, 1.0, t, face=-1); sunflower(P, 780, CENTER + 360, 1.0, t, face=1)
        for j in range(5):
            if seg(u, .5 + j * .3, .8 + j * .3) > 0: bee(P, 230 + math.sin(t * 3 + j) * 60, CENTER - 140 + j * 40, 1.4, t + j)
        if seg(u, 2.0, 2.3) > 0: bee(P, 880 + math.sin(t * 3) * 60, CENTER - 60, 1.4, t)
        P.badge(330, CENTER + 470, "5x bees", 60, HOPE, CLOUD, back(seg(u, 1.8, 2.3)))
