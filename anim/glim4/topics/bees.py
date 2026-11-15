# Thema: Do all bees die after they sting?  (Mythos-Format)
CENTER = 1050
YEL, BUM = (255, 196, 40), (250, 200, 60)
PAL = ((70, 140, 200), (140, 190, 90))
HI = {"die", "sting?", "honeybee", "workers", "barbs,", "stuck", "smooth", "again", "male", "can't", "survive", "nectar."}
WOW = (1, 3)
GROUND = CENTER + 380

def meadow(P, t):
    P.poly([(0, GROUND), (W, GROUND - 30), (W, H), (0, H)], (110, 170, 80))
    for k, x in enumerate((120, 330, 760, 960)):
        P.line([(x, GROUND), (x, GROUND - 140 - k % 2 * 50)], (60, 140, 60), 10)
        cy = GROUND - 140 - k % 2 * 50
        for j in range(6): a = j / 6 * 6.28; P.circ(x + math.cos(a) * 26, cy + math.sin(a) * 26, 18, (255, 150, 190) if k % 2 else (250, 245, 250))
        P.circ(x, cy, 16, YEL)

def bee(P, x, y, s, t, fuzzy=False, sting=True, col=YEL, flip=1):
    f = flip; a = math.sin(t * 40) * 10 * s
    P.ell(x + f * 10 * s, y - 55 * s - a, 40 * s, 26 * s, (225, 240, 255), outline=(150, 180, 210), w=3 * s)
    P.ell(x + f * 50 * s, y - 50 * s + a, 34 * s, 22 * s, (225, 240, 255), outline=(150, 180, 210), w=3 * s)
    if sting: P.poly([(x + f * 75 * s, y - 8 * s), (x + f * 115 * s, y), (x + f * 75 * s, y + 8 * s)], NIGHT)
    P.ell(x, y, (88 if fuzzy else 80) * s, (58 if fuzzy else 48) * s, col)
    for k in (-20, 15, 48): P.line([(x + f * k * s, y - 44 * s), (x + f * k * s, y + 44 * s)], NIGHT, 14 * s)
    P.circ(x - f * 82 * s, y - 4 * s, 34 * s, NIGHT)
    P.circ(x - f * 92 * s, y - 12 * s, 9 * s, CLOUD); P.circ(x - f * 94 * s, y - 13 * s, 4 * s, NIGHT)
    for k in (-1, 1): P.line([(x - f * 90 * s, y - 30 * s), (x - f * (110 + 10 * k) * s, y - 70 * s)], NIGHT, 5 * s)

def stinger(P, x, y, L, barbs=True, k=1.):
    P.line([(x, y), (x + L, y)], (60, 50, 50), 22); P.poly([(x + L, y - 11), (x + L + 60, y), (x + L, y + 11)], (60, 50, 50))
    if barbs:
        for j in range(6):
            bx = x + L - j * 50; P.line([(bx, y - 10), (bx - 30, y - 34 * k)], (60, 50, 50), 7); P.line([(bx, y + 10), (bx - 30, y + 34 * k)], (60, 50, 50), 7)

def SC(i, P, t, u):
    if i == 0:
        meadow(P, t); bee(P, 540 + math.sin(t * 1.2) * 120, CENTER - 60 + math.sin(t * 2.5) * 30, 1.6, t)
        P.text(800, CENTER - 300, "?", 140 * back(seg(u, .4, .9)), GLIM)
    elif i == 1:
        meadow(P, t); bee(P, 540, CENTER - 40, 1.5, t)
        P.badge(540, CENTER + 170, "honeybee workers only", 54, NIGHT, GLIM, back(seg(u, .8, 1.3)))
        P.stamp(540, CENTER - 360, "MYTH", seg(u, .25, .7))
    elif i == 2:
        P.circ(540, CENTER - 40, 300, (250, 238, 210), outline=GLIM, w=10)
        P.rrect(600, CENTER - 300, 780, CENTER + 220, 20, (240, 180, 160))
        stinger(P, 290, CENTER - 40, lerp(220, 360, eout(seg(u, .5, 1.3))))
        P.badge(540, CENTER - 420, "barbs = hooks", 60, HOOK, CLOUD, back(seg(u, .4, .9)))
    elif i == 3:
        meadow(P, t); x = 540 + math.sin(u * 2.5) * 200
        bee(P, x, CENTER - 60, 1.7, t, fuzzy=True, col=BUM)
        P.circ(820, CENTER + 220, 130, (250, 238, 210), outline=GLIM, w=8)
        stinger(P, 715, CENTER + 220, 150, barbs=False)
        P.badge(540, CENTER - 330, "smooth stinger", 56, HOPE, CLOUD, back(seg(u, .6, 1.1)))
        for j in range(3): P.check(220 + j * 90, CENTER + 220, 34, k=back(seg(u, 1.5 + j * .4, 1.9 + j * .4)))
    elif i == 4:
        meadow(P, t); bee(P, 540, CENTER - 40, 1.5, t, sting=False, col=(230, 170, 60))
        P.badge(540, CENTER - 330, "male bee (drone)", 56, NIGHT, GLIM, back(seg(u, .3, .8)))
        P.cross(780, CENTER - 40, 50, k=back(seg(u, 1.0, 1.5)))
    else:
        meadow(P, t)
        q = eio(seg(u, .3, 2.5)); bee(P, lerp(900, 360, q), lerp(CENTER - 200, GROUND - 230, q), 1.1, t)
        bee(P, 700 + math.sin(t * 2) * 100, CENTER - 60, 1.0, t, fuzzy=True, col=BUM, flip=-1)
        P.stamp(540, CENTER - 320, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
