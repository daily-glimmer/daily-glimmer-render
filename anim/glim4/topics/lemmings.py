# Thema: Do lemmings really jump off cliffs on purpose? (Mythos M32, MYTH/FACT)
CENTER = 1050
PAL = ((200, 225, 240), (150, 190, 220))
HI = {"cliffs", "purpose?", "myth", "boom,", "new", "homes.", "swim,", "drown", "1958", "staged", "space", "food!"}
WOW = (1, 4)
FURL, FURD, BELLY = (205, 150, 90), (90, 60, 40), (240, 215, 175)
SNOW, ROCK, ROCKD, WATER, GRASS = (245, 248, 252), (130, 125, 135), (95, 90, 105), (70, 140, 210), (110, 180, 90)

def lemming(P, x, y, s, t, f=1, hop=0., swim=False, eat=False, ph=0.):
    b = abs(math.sin(t * 9 + ph)) * hop * 18 * s
    y = y - b
    if not swim:
        for dx in (-30, 30): P.ell(x + dx * s, y + 52 * s, 14 * s, 9 * s, FURD)
    P.ell(x, y, 78 * s, 56 * s, FURL, outline=FURD, w=5 * s)
    P.ell(x - 10 * f * s, y - 22 * s, 46 * s, 22 * s, FURD)
    hx = x + 58 * f * s; hy = y - 10 * s + (math.sin(t * 6 + ph) * 4 * s if eat else 0)
    P.circ(hx, hy, 40 * s, FURL, outline=FURD, w=5 * s)
    P.ell(hx - 4 * f * s, hy - 26 * s, 14 * s, 12 * s, FURD)
    P.ell(hx + 8 * f * s, hy + 14 * s, 22 * s, 16 * s, BELLY)
    P.circ(hx + 14 * f * s, hy - 6 * s, 7 * s, NIGHT); P.circ(hx + 16 * f * s, hy - 9 * s, 2.5 * s, CLOUD)
    P.circ(hx + 36 * f * s, hy + 6 * s, 6 * s, (230, 120, 130))
    if eat: P.line([(hx + 34 * f * s, hy + 18 * s), (hx + 60 * f * s, hy + 34 * s)], GRASS, 6 * s)

def cliff(P, x0, y0, w, h):
    P.poly([(x0, y0), (x0 + w, y0), (x0 + w + 40, y0 + h * .4), (x0 + w - 10, y0 + h), (x0, y0 + h)], ROCK, outline=ROCKD, w=6)
    P.rrect(x0, y0 - 20, x0 + w + 10, y0 + 18, 14, SNOW)

def water(P, y, t, x0=0, x1=1080, col=WATER):
    P.rrect(x0, y, x1, y + 500, 0, col)
    for k in range(7):
        xx = x0 + ((k * 170 + t * 60) % (x1 - x0))
        P.arc(xx, y + 40 + (k % 2) * 60, 30, 200, 340, (200, 230, 250), 6)

def tundra(P, y):
    P.rrect(0, y, 1080, y + 600, 0, SNOW)
    for k in range(9): P.ell(60 + k * 125, y + 10, 50, 16, (200, 225, 200))

def SC(i, P, t, u):
    if i == 0:
        water(P, CENTER + 260, t)
        cliff(P, 0, CENTER - 60, 560, 340)
        for k in range(3): lemming(P, 120 + k * 150, CENTER - 125, .9, t, hop=.6, ph=k)
        P.text(820, CENTER - 160, "?", 190 * back(seg(u, .5, 1.0)), HOOK)
    elif i == 1:
        tundra(P, CENTER + 200)
        lemming(P, 480, CENTER + 130, 1.8, t, hop=.3)
        P.stamp(540, CENTER - 230, "MYTH", seg(u, .25, .7))
    elif i == 2:
        tundra(P, CENTER + 260)
        n = int(2 + 12 * eio(seg(u, .3, 4.5)))
        for k in range(n):
            lemming(P, 120 + (k * 197) % 860, CENTER + 150 + (k * 53 % 4) * 40, .75, t, f=1 if k % 2 else -1, hop=.4, ph=k)
        P.badge(540, CENTER - 280, "every 3-4 years", 60, NIGHT, GLIM, back(seg(u, 1.2, 1.7)))
        P.text(870, CENTER + 520, "new homes!", 52 * back(seg(u, 3.8, 4.3)), HOPE)
    elif i == 3:
        P.rrect(0, CENTER - 40, 1080, CENTER + 120, 0, (200, 225, 200))
        water(P, CENTER + 100, t)
        for k in range(3):
            xx = 160 + ((u * 70 + k * 280) % 760)
            lemming(P, xx, CENTER + 200 + k * 70, .8, t, swim=True, ph=k)
        P.badge(540, CENTER - 260, "good swimmers", 58, HOPE, CLOUD, back(seg(u, .9, 1.4)))
    elif i == 4:
        P.rrect(150, CENTER - 230, 930, CENTER + 330, 30, (40, 40, 50))
        for k in range(8):
            P.rrect(170 + k * 97, CENTER - 215, 215 + k * 97, CENTER - 185, 6, (220, 220, 220))
            P.rrect(170 + k * 97, CENTER + 285, 215 + k * 97, CENTER + 315, 6, (220, 220, 220))
        P.rrect(195, CENTER - 160, 885, CENTER + 260, 10, (190, 180, 160))
        cliff(P, 195, CENTER - 20, 380, 280)
        P.text(720, CENTER + 60, "1958", 110, (90, 80, 70))
        P.stamp(540, CENTER + 470, "STAGED", seg(u, 2.6, 3.1), rot=6)
    else:
        tundra(P, CENTER + 220)
        for k in range(5): P.line([(150 + k * 30, CENTER + 220), (140 + k * 34, CENTER + 150 - k % 2 * 30)], GRASS, 10)
        lemming(P, 380, CENTER + 150, 1.5, t, eat=True)
        P.heart(720, CENTER + 40, 50 * back(seg(u, 1.0, 1.5)), HOOK)
        P.stamp(540, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
