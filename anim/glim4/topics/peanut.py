# Thema: Is a peanut really a nut?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6)
CENTER = 1050
PAL = ((200, 150, 100), (240, 210, 160))
HI = {"nut?", "myth!", "legume,", "peas", "beans.", "hazelnuts", "trees", "pods,", "underground!", "soil,", "bean!"}
WOW = (1, 3)
SHELL, SHELL2, SEED = (225, 185, 130), (190, 145, 95), (200, 120, 80)
SOIL_Y = CENTER + 150

def peanut(P, x, y, s, open_=0.):
    P.ell(x, y - 55 * s, 55 * s, 70 * s, SHELL); P.ell(x, y + 55 * s, 55 * s, 70 * s, SHELL)
    P.ell(x, y, 42 * s, 30 * s, SHELL)
    for j in range(5): P.line([(x - 35 * s, y - 100 * s + j * 50 * s), (x + 35 * s, y - 90 * s + j * 50 * s)], SHELL2, 4 * s)
    if open_ > 0:
        P.ell(x + 120 * s * open_, y - 50 * s, 38 * s, 50 * s, SEED); P.ell(x + 120 * s * open_, y + 50 * s, 38 * s, 50 * s, SEED)

def peapod(P, x, y, s):
    P.ell(x, y, 160 * s, 50 * s, (110, 180, 80))
    for j in range(4): P.circ(x - 90 * s + j * 60 * s, y, 26 * s, (150, 210, 100))

def hazel(P, x, y, s):
    P.ell(x, y, 70 * s, 65 * s, (170, 110, 60)); P.ell(x, y - 55 * s, 60 * s, 25 * s, (130, 160, 80))

def plant(P, x, s, t, pegs=0.):
    P.poly([(0, SOIL_Y), (W, SOIL_Y - 10), (W, H), (0, H)], (130, 90, 60))
    P.line([(x, SOIL_Y), (x, SOIL_Y - 260 * s)], (80, 150, 70), 14 * s)
    for f in (-1, 1):
        for j in range(3): P.ell(x + f * 70 * s, SOIL_Y - (100 + j * 70) * s, 50 * s, 24 * s, (90, 170, 80))
    P.circ(x + 40 * s, SOIL_Y - 220 * s, 20 * s, (250, 200, 60))
    if pegs > 0:
        for f in (-1, 1):
            P.line([(x + f * 40 * s, SOIL_Y - 120 * s), (x + f * 130 * s, SOIL_Y - 20 * s), (x + f * 150 * s, SOIL_Y + 160 * s * pegs)], (200, 170, 120), 7 * s)
            if pegs > .6: peanut(P, x + f * 150 * s, SOIL_Y + 220 * s * pegs, .6 * s)

def SC(i, P, t, u):
    if i == 0:
        peanut(P, 420, CENTER + 60, 1.8); hazel(P, 760, CENTER + 100, 1.3)
        P.text(600, CENTER - 300, "?", 150 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        peanut(P, 320, CENTER + 80, 1.6); peapod(P, 760, CENTER + 120, 1.0)
        P.text(560, CENTER + 100, "=", 100 * back(seg(u, 1.0, 1.5)), GLIM)
        P.stamp(540, CENTER - 300, "MYTH", seg(u, .25, .7))
        P.badge(540, CENTER + 460, "legume", 64, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
    elif i == 2:
        P.line([(300, CENTER + 300), (300, CENTER - 160)], (120, 85, 55), 40)
        P.circ(300, CENTER - 240, 200, (90, 160, 80)); hazel(P, 300, CENTER - 100, .8)
        hazel(P, 760, CENTER + 60, 1.6)
        P.badge(760, CENTER + 300, "real nut", 58, NIGHT, CLOUD, back(seg(u, .8, 1.3)))
    elif i == 3:
        plant(P, 540, 1.3, t, pegs=1.)
        P.badge(540, CENTER + 520, "pods underground!", 58, HOOK, CLOUD, back(seg(u, .8, 1.3)))
    elif i == 4:
        plant(P, 540, 1.3, t, pegs=eio(seg(u, .5, 4.0)))
    else:
        peanut(P, 380, CENTER + 60, 1.6, open_=1.)
        P.stamp(760, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
