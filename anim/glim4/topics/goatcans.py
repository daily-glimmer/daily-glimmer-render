# Thema: Do goats really eat tin cans?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6)
CENTER = 1050
GF, GF2, HORN = (240, 235, 225), (200, 195, 185), (170, 150, 120)
PAL = ((110, 160, 210), (190, 220, 160))
HI = {"tin", "cans?", "myth!", "metal.", "curious", "lips", "toddlers.", "label", "glue", "leaves,", "twigs", "shrubs.", "disappears!"}
WOW = (1,)
GROUND = CENTER + 300

def farm(P, t):
    P.poly([(0, GROUND), (W, GROUND - 20), (W, H), (0, H)], (110, 170, 80))
    for x in range(40, W, 160): P.rrect(x - 10, GROUND - 160, x + 10, GROUND + 10, 4, (170, 120, 70))
    P.line([(0, GROUND - 120), (W, GROUND - 130)], (170, 120, 70), 14); P.line([(0, GROUND - 60), (W, GROUND - 70)], (170, 120, 70), 14)

def goat(P, x, y, s, t, chew=0., f=1):
    for dx in (-90, -55, 60, 95): P.rrect(x + dx * s - 13 * s, y + 30 * s, x + dx * s + 13 * s, y + 170 * s, 6 * s, GF2)
    P.ell(x, y, 140 * s, 75 * s, GF)
    P.poly([(x - f * 130 * s, y - 30 * s), (x - f * 175 * s, y - 70 * s), (x - f * 150 * s, y - 10 * s)], GF)
    hx, hy = x + f * 150 * s, y - 90 * s
    P.line([(x + f * 90 * s, y - 20 * s), (hx, hy)], GF, 60 * s)
    P.line([(hx - f * 10 * s, hy - 40 * s), (hx - f * 50 * s, hy - 100 * s), (hx - f * 80 * s, hy - 90 * s)], HORN, 14 * s)
    P.ell(hx - f * 30 * s, hy - 10 * s, 40 * s, 16 * s, GF2)
    P.ell(hx + f * 30 * s, hy + 10 * s, 52 * s, 38 * s, GF)
    m = abs(math.sin(t * 8)) * chew
    P.ell(hx + f * 70 * s, hy + 30 * s + m * 6 * s, 22 * s, (10 + m * 6) * s, GF2)
    P.poly([(hx + f * 40 * s, hy + 45 * s), (hx + f * 55 * s, hy + 90 * s), (hx + f * 25 * s, hy + 50 * s)], GF2)   # Bart
    P.ell(hx + f * 20 * s, hy - 5 * s, 10 * s, 7 * s, NIGHT); P.line([(hx + f * 12 * s, hy - 5 * s), (hx + f * 28 * s, hy - 5 * s)], (200, 170, 60), 3 * s)

def can(P, x, y, s, label=1.):
    P.rrect(x - 55 * s, y - 80 * s, x + 55 * s, y + 80 * s, 12 * s, (190, 195, 205))
    P.ell(x, y - 80 * s, 55 * s, 14 * s, (215, 220, 228))
    if label > .02: P.rrect(x - 55 * s, y - 45 * s, x - 55 * s + 110 * s * label, y + 45 * s, 4 * s, (230, 90, 80))

def SC(i, P, t, u):
    if i == 0:
        farm(P, t); goat(P, 400, CENTER + 90, 1.35, t); can(P, 820, GROUND - 60, 1.2)
        P.text(820, CENTER - 160, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        farm(P, t); goat(P, 380, CENTER + 90, 1.35, t, chew=1.); can(P, 760, GROUND - 60, 1.2)
        P.stamp(560, CENTER - 280, "MYTH", seg(u, .25, .7))
        P.badge(760, GROUND + 120, "no metal", 52, NIGHT, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 2:
        farm(P, t); goat(P, 380, CENTER + 90, 1.35, t, chew=.5)
        for j, (x, y) in enumerate(((760, CENTER - 60), (860, CENTER + 60), (720, CENTER + 140))):
            k = back(seg(u, .5 + j * .5, 1.0 + j * .5)); P.circ(x, y, 30 * k, (120, 180, 250))
        P.badge(540, CENTER - 280, "curious lips", 58, NIGHT, GLIM, back(seg(u, .8, 1.3)))
    elif i == 3:
        farm(P, t); goat(P, 360, CENTER + 90, 1.35, t, chew=1.)
        can(P, 760, GROUND - 60, 1.2, label=1 - eio(seg(u, .5, 3.0)))
        for j in range(4):
            q = (u * .8 + j / 4) % 1
            P.rrect(700 - q * 150, CENTER + 40 - q * 60 - j * 20, 730 - q * 150, CENTER + 70 - q * 60 - j * 20, 4, (230, 90, 80))
        P.badge(540, CENTER - 280, "label + glue", 58, HOOK, CLOUD, back(seg(u, 1.0, 1.5)))
    elif i == 4:
        farm(P, t); goat(P, 400, CENTER + 90, 1.35, t, chew=1.)
        for j in range(6):
            P.ell(780 + (j % 3) * 60, CENTER - 40 + (j // 3) * 70, 50, 26, (70, 150, 70))
        P.line([(840, CENTER + 260), (840, CENTER - 40)], (120, 85, 50), 16)
        P.badge(540, CENTER - 280, "leaves & twigs", 58, NIGHT, CLOUD, back(seg(u, .6, 1.1)))
    else:
        farm(P, t); goat(P, 380, CENTER + 90, 1.3, t); can(P, 790, GROUND - 60, 1.2, label=0.)
        P.stamp(700, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
