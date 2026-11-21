# Thema: Do crocodiles really cry while they eat?  (Mythos-Format, TRUE in Satz 2, FACT in Satz 6)
CENTER = 1050
CR, CR2, BELLYC = (90, 140, 70), (60, 105, 50), (200, 210, 150)
TEAR = (120, 200, 255)
PAL = ((40, 90, 80), (130, 170, 110))
HI = {"cry", "eat?", "true!", "teared", "five", "seven", "frothed", "bubbled", "hissing", "huffing", "sinuses", "eating!", "real?"}
WOW = (1, 3)
GROUND = CENTER + 300

def bank(P, t):
    P.poly([(0, GROUND), (W, GROUND - 20), (W, H), (0, H)], (150, 130, 90))
    P.poly([(0, GROUND + 260), (W, GROUND + 240), (W, H), (0, H)], (60, 120, 130))

def croc(P, x, y, s, t, chew=0., tears=0., froth=0., f=1):
    P.poly([(x - f * 120 * s, y - 30 * s), (x - f * 420 * s, y + 10 * s + math.sin(t * 2) * 10 * s), (x - f * 120 * s, y + 40 * s)], CR2)   # Schwanz
    for dx in (-60, 90):
        P.ell(x + f * dx * s, y + 50 * s, 30 * s, 40 * s, CR2)
    P.ell(x, y, 180 * s, 60 * s, CR)
    for j in range(6): P.poly([(x + f * (-130 + j * 45) * s, y - 50 * s), (x + f * (-110 + j * 45) * s, y - 80 * s), (x + f * (-90 + j * 45) * s, y - 50 * s)], CR2)
    op = (.2 + .8 * abs(math.sin(t * 5))) * chew
    hx, hy = x + f * 170 * s, y - 20 * s
    P.poly([(hx, hy - 30 * s), (hx + f * 260 * s, hy - 5 * s - op * 60 * s), (hx + f * 260 * s, hy + 15 * s - op * 50 * s), (hx, hy + 20 * s)], CR)       # Oberkiefer
    P.poly([(hx, hy + 20 * s), (hx + f * 250 * s, hy + 25 * s + op * 40 * s), (hx + f * 240 * s, hy + 50 * s + op * 40 * s), (hx, hy + 50 * s)], BELLYC)  # Unterkiefer
    for j in range(5): P.poly([(hx + f * (40 + j * 45) * s, hy + 15 * s - op * j * 10 * s), (hx + f * (50 + j * 45) * s, hy + 32 * s - op * j * 10 * s), (hx + f * (60 + j * 45) * s, hy + 15 * s - op * j * 10 * s)], CLOUD)
    ex, ey = hx + f * 30 * s, hy - 45 * s
    P.circ(ex, ey, 30 * s, CR); P.circ(ex, ey, 18 * s, (230, 200, 60)); P.ell(ex, ey, 5 * s, 15 * s, NIGHT)
    if tears > .02:
        for j in range(3):
            q = (t * .8 + j / 3) % 1
            P.ell(ex + f * 10 * s, ey + 20 * s + q * 120 * s, 9 * s * tears, 14 * s * tears, TEAR)
    if froth > .02:
        for j in range(6): P.circ(ex + math.cos(j + t * 3) * 30 * s, ey + math.sin(j + t * 3) * 20 * s, (8 + j % 3 * 4) * s * froth, (235, 245, 255))
    return hx, hy

def food(P, x, y, s): P.ell(x, y, 50 * s, 30 * s, (220, 120, 100)); P.circ(x + 40 * s, y - 10 * s, 18 * s, (240, 230, 220))

def SC(i, P, t, u):
    if i == 0:
        bank(P, t); croc(P, 450, GROUND - 80, 1.35, t)
        P.text(820, CENTER - 200, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
        P.ell(820, CENTER - 40, 20, 30, TEAR)
    elif i == 1:
        bank(P, t); hx, hy = croc(P, 400, GROUND - 80, 1.35, t, chew=1., tears=eout(seg(u, .6, 1.4)))
        food(P, hx + 290, hy + 35, 1.3)
        P.stamp(780, CENTER - 270, "TRUE", seg(u, .25, .7), col=HOPE, rot=-6)
    elif i == 2:
        for j in range(7):
            x = 160 + j * 127; cried = j < 5; k = back(seg(u, .3 + j * .2, .7 + j * .2))
            P.circ(x, CENTER, 52 * k, CR); P.circ(x, CENTER - 10, 20 * k, (230, 200, 60))
            if cried and k > .5: P.ell(x + 10, CENTER + 70, 14, 22, TEAR)
        P.badge(540, CENTER + 260, "5 out of 7", 70, NIGHT, GLIM, back(seg(u, 2.0, 2.5)))
    elif i == 3:
        bank(P, t); croc(P, 420, GROUND - 80, 1.45, t, chew=.6, tears=1., froth=back(seg(u, .3, .9)))
        P.badge(540, CENTER - 260, "froth & bubbles", 58, NIGHT, CLOUD, back(seg(u, .8, 1.3)))
    elif i == 4:
        bank(P, t); hx, hy = croc(P, 400, GROUND - 80, 1.35, t, chew=1., tears=1.)
        for j in range(4):
            q = (u * .8 + j / 4) % 1
            P.arc(hx + 330 + q * 90, hy, 30 + q * 60, 300, 60, (230, 240, 255), 6)
        P.badge(540, CENTER - 240, "hiss + huff", 58, HOOK, CLOUD, back(seg(u, .6, 1.1)))
        P.badge(540, CENTER + 560, "air pushes tears out", 50, NIGHT, CLOUD, back(seg(u, 2.5, 3.0)))
    else:
        bank(P, t); hx, hy = croc(P, 400, GROUND - 80, 1.35, t, chew=1., tears=.8)
        food(P, hx + 290, hy + 35, 1.3)
        P.stamp(720, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
