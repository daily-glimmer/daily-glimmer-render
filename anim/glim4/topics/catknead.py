# Thema: Why do cats knead with their paws?
CENTER = 1050
FUR, FUR2, PINK = (170, 170, 185), (130, 130, 150), (245, 170, 180)
KIT = (240, 190, 120)
BLANK = (120, 170, 220)
PAL = ((250, 210, 200), (200, 180, 230))
HI = {"knead", "paws?", "kittens,", "milk.", "press", "flow.", "safe,", "cozy", "happy.", "scent", "glands,", "theirs!", "biscuits", "compliment."}
WOW = (1, 4)

def sitcat(P, x, y, s, t, knead=1., happy=False, col=FUR):
    c2 = lc(col, (0, 0, 0), .2)
    P.ell(x, y + 40 * s, 170 * s, 200 * s, col)                                     # Körper
    P.line([(x + 150 * s, y + 200 * s), (x + 230 * s, y + 120 * s), (x + 220 * s, y + 20 * s)], c2, 22 * s)
    for d, ph in ((-1, 0), (1, math.pi)):                                          # Pfoten abwechselnd
        lift = max(0, math.sin(t * 6 + ph)) * 40 * s * knead
        P.rrect(x + d * 70 * s - 32 * s, y + 120 * s - lift, x + d * 70 * s + 32 * s, y + 250 * s - lift, 30 * s, lc(col, CLOUD, .25), outline=c2, w=4 * s)
        for k in (-1, 0, 1): P.line([(x + d * 70 * s + k * 13 * s, y + 230 * s - lift), (x + d * 70 * s + k * 13 * s, y + 245 * s - lift)], c2, 4 * s)
    hx, hy = x, y - 170 * s
    for d in (-1, 1):
        P.poly([(hx + d * 120 * s, hy - 20 * s), (hx + d * 110 * s, hy - 140 * s), (hx + d * 40 * s, hy - 100 * s)], col)
        P.poly([(hx + d * 100 * s, hy - 40 * s), (hx + d * 98 * s, hy - 110 * s), (hx + d * 60 * s, hy - 90 * s)], PINK)
    P.ell(hx, hy, 130 * s, 110 * s, col)
    for d in (-1, 1):
        if happy: P.arc(hx + d * 50 * s, hy - 5 * s, 22 * s, 200, 340, NIGHT, 7 * s)
        else: P.ell(hx + d * 50 * s, hy - 5 * s, 18 * s, 26 * s, NIGHT); P.circ(hx + d * 50 * s + 6 * s, hy - 14 * s, 6 * s, CLOUD)
    P.poly([(hx - 14 * s, hy + 30 * s), (hx + 14 * s, hy + 30 * s), (hx, hy + 46 * s)], PINK)
    P.arc(hx - 14 * s, hy + 52 * s, 14 * s, 0, 150, NIGHT, 4 * s); P.arc(hx + 14 * s, hy + 52 * s, 14 * s, 30, 180, NIGHT, 4 * s)
    for d in (-1, 1):
        for k in (-1, 1): P.line([(hx + d * 50 * s, hy + 45 * s), (hx + d * 170 * s, hy + (40 + k * 20) * s)], CLOUD, 3 * s)

def mom(P, x, y, s, t):
    P.ell(x, y, 320 * s, 120 * s, FUR)
    P.circ(x - 300 * s, y - 70 * s, 100 * s, FUR)
    for d in (-1, 1): P.poly([(x - 300 * s + d * 80 * s, y - 120 * s), (x - 300 * s + d * 75 * s, y - 220 * s), (x - 300 * s + d * 20 * s, y - 160 * s)], FUR)
    for d in (-1, 1): P.arc(x - 300 * s + d * 40 * s, y - 80 * s, 18 * s, 200, 340, NIGHT, 6 * s)
    P.line([(x + 300 * s, y + 20 * s), (x + 400 * s, y - 60 * s + 15 * math.sin(t * 2) * s)], lc(FUR, (0, 0, 0), .2), 24 * s)

def kitten(P, x, y, s, t, ph=0.):
    P.ell(x, y, 60 * s, 45 * s, KIT); P.circ(x, y - 60 * s, 42 * s, KIT)
    for d in (-1, 1): P.poly([(x + d * 38 * s, y - 80 * s), (x + d * 34 * s, y - 125 * s), (x + d * 8 * s, y - 98 * s)], KIT)
    for d in (-1, 1): P.circ(x + d * 15 * s, y - 62 * s, 6 * s, NIGHT)
    lift = max(0, math.sin(t * 7 + ph)) * 18 * s
    P.circ(x - 20 * s, y - 100 * s - lift, 15 * s, KIT)

def biscuit(P, x, y, s):
    P.ell(x, y, 70 * s, 46 * s, (225, 170, 100), outline=(180, 120, 60), w=4 * s)
    for k in (-1, 0, 1): P.line([(x + k * 25 * s - 10 * s, y - 25 * s), (x + k * 25 * s + 10 * s, y + 20 * s)], (180, 120, 60), 5 * s)

def SC(i, P, t, u):
    if i == 0:
        P.rrect(80, CENTER + 260, 1000, CENTER + 420, 60, BLANK)
        sitcat(P, 540, CENTER + 20, 1.05, t)
        P.text(860, CENTER - 280, "?", 150 * back(seg(u, .5, 1.0)), HOOK)
    elif i == 1:
        mom(P, 600, CENTER + 120, 1.1, t)
        for j in range(3): kitten(P, 380 + j * 170, CENTER + 280, 1.0 * back(seg(u, .3 + j * .2, .8 + j * .2)), t, j)
        P.badge(540, CENTER - 280, "a kitten habit", 60, NIGHT, GLIM, back(seg(u, 1.2, 1.7)))
    elif i == 2:
        P.ell(540, CENTER + 60, 380, 230, FUR)
        for d, ph in ((-1, 0), (1, math.pi)):
            lift = max(0, math.sin(t * 6 + ph)) * 60
            P.circ(540 + d * 130, CENTER - 90 - lift, 70, KIT)
            for k in (-1, 0, 1): P.circ(540 + d * 130 + k * 35, CENTER - 35 - lift, 16, PINK)
        for j in range(4):
            q = (t * .8 + j / 4) % 1
            P.ell(400 + j * 90, CENTER + 120 + q * 120, 16, 22, CLOUD)
        P.badge(540, CENTER + 400, "helps the milk flow", 58, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
    elif i == 3:
        P.ell(540, CENTER + 280, 360, 110, (230, 120, 150))
        sitcat(P, 540, CENTER + 20, 1.0, t, knead=.6, happy=True)
        for j in range(3):
            q = (t * .6 + j / 3) % 1
            P.heart(300 + j * 240, CENTER - 160 - q * 120, 30 * (1 - q * .5), HOOK)
        P.badge(540, CENTER + 450, "safe + happy", 60, HOPE, CLOUD, back(seg(u, 1.0, 1.5)))
    elif i == 4:
        k = back(seg(u, .2, .8))
        P.ell(540, CENTER + 60, 230 * k, 200 * k, PINK)
        for j, (dx, dy) in enumerate(((-170, -210), (-60, -270), (60, -270), (170, -210))):
            P.ell(540 + dx * k, CENTER + 60 + dy * k, 62 * k, 72 * k, PINK)
        for j in range(5):
            q = (t * .5 + j / 5) % 1
            a = -2.6 + j * .35
            P.circ(540 + math.cos(a) * (260 + q * 160), CENTER + 60 + math.sin(a) * (260 + q * 160), 18 * (1 - q), lc(HOPE, CLOUD, q))
        P.badge(540, CENTER + 400, "scent glands", 60, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
    else:
        P.rrect(80, CENTER + 220, 1000, CENTER + 420, 60, BLANK)
        sitcat(P, 540, CENTER - 20, .95, t, happy=True)
        for j in range(3):
            k = back(seg(u, .6 + j * .3, 1.1 + j * .3))
            if k > .05: biscuit(P, 260 + j * 280, CENTER + 330, .9 * k)
        P.badge(540, CENTER - 330, "a big compliment!", 58, HOOK, CLOUD, back(seg(u, 1.6, 2.1)))
