# Thema: Did giraffes get long necks by stretching? (Mythos-Format, MYTH/FACT)
# nutzt die Giraffen-Figuren aus giraffes.py und ergänzt eine Giraffe mit variabler Halslänge
exec(open(os.path.join(HERE, "topics", "giraffes.py")).read(), globals())
CENTER = 1050
PAL = ((170, 215, 245), (245, 215, 150))
HI = {"giraffes", "long", "necks", "stretching", "myth:", "passed", "longer", "food", "young.", "millions",
      "six", "feet,", "seven", "bones,", "necking,", "win.", "ten", "inches"}
WOW = (1, 3)
GROUND = CENTER + 360
LEAF, LEAF2, BARK = (70, 150, 70), (110, 185, 90), (110, 75, 45)

def savanna(P, t, g=GROUND):
    P.poly([(0, g), (W, g - 20), (W, H), (0, H)], (215, 190, 110))
    for j in range(7): P.line([(80 + j * 150, g + 40 + (j % 2) * 30), (95 + j * 150, g + 10 + (j % 2) * 30)], (160, 140, 70), 6)

def tree(P, x, top, t, g=GROUND, w=1.):
    """Akazie mit Krone bei Höhe top"""
    P.line([(x, g), (x - 10, top + 60)], BARK, 34 * w)
    P.line([(x - 10, top + 120), (x - 110 * w, top + 30)], BARK, 16 * w); P.line([(x - 10, top + 120), (x + 100 * w, top + 30)], BARK, 16 * w)
    for dx, dy, r in ((-150, 10, 120), (0, -20, 150), (150, 10, 120)):
        P.ell(x + dx * w, top + dy, r * w, 55 * w, LEAF)
    for j in range(9):
        a = j * .7 + t * .6
        P.circ(x + (j - 4) * 34 * w, top + 22 + math.sin(a) * 6, 14 * w, LEAF2)

def giraffe_n(P, x, y, s, t, neck=1., sleepy=False, sway=1., face=1):
    """stehende Giraffe mit Halslänge neck (1 = normal); face=-1 spiegelt"""
    sw = math.sin(t * 1.1) * 8 * s * sway
    f = face
    bx, by = x, y - 330 * s
    for dx in (-110, -70, 75, 115):
        P.line([(bx + f * dx * s, by + 30 * s), (bx + f * dx * s, y)], COAT, 22 * s); P.rrect(bx + f * dx * s - 13 * s, y - 16 * s, bx + f * dx * s + 13 * s, y, 4 * s, (90, 55, 30))
    P.line([(bx - f * 150 * s, by - 10 * s), (bx - f * 185 * s, by + 120 * s + sw)], COAT, 8 * s)
    P.ell(bx, by, 160 * s, 78 * s, COAT)
    spots(P, [(bx + f * d[0] * s, by + d[1] * s) for d in ((-90, -20), (-20, -35), (55, -10), (-55, 30), (20, 35), (105, 25))], 22 * s)
    hx, hy = bx + f * (110 + 105 * neck) * s + sw, by - (20 + 360 * neck) * s + abs(sw) * .5
    P.line([(bx + f * 110 * s, by - 20 * s), (hx - f * 10 * s, hy + 40 * s)], COAT, 52 * s)
    P.line([(bx + f * 95 * s, by - 50 * s), (hx - f * 40 * s, hy + 20 * s)], MANE, 10 * s)
    nsp = max(2, int(4 * neck + .5))
    for k in range(nsp):
        q = .15 + k * .7 / max(1, nsp - 1); spots(P, [(lerp(bx + f * 115 * s, hx - f * 10 * s, q), lerp(by - 20 * s, hy + 40 * s, q))], 14 * s)
    head(P, hx, hy, s, sleepy)
    return hx, hy

def arrow(P, x0, y0, x1, y1, col, w=14):
    P.line([(x0, y0), (x1, y1)], col, w)
    a = math.atan2(y1 - y0, x1 - x0)
    P.poly([(x1 + math.cos(a) * 30, y1 + math.sin(a) * 30), (x1 + math.cos(a + 2.3) * 30, y1 + math.sin(a + 2.3) * 30), (x1 + math.cos(a - 2.3) * 30, y1 + math.sin(a - 2.3) * 30)], col)

def bone(P, x, y, L, h, col=(250, 245, 230), out=(150, 130, 100)):
    """Halswirbel als länglicher Knochen"""
    for ex in (-1, 1):
        P.circ(x + ex * L / 2, y - h * .35, h * .45, col, outline=out, w=5); P.circ(x + ex * L / 2, y + h * .35, h * .45, col, outline=out, w=5)
    P.rrect(x - L / 2, y - h * .4, x + L / 2, y + h * .4, h * .3, col)
    P.line([(x - L / 2 + h * .3, y - h * .4), (x + L / 2 - h * .3, y - h * .4)], out, 5)
    P.line([(x - L / 2 + h * .3, y + h * .4), (x + L / 2 - h * .3, y + h * .4)], out, 5)

def SC(i, P, t, u):
    if i == 0:
        savanna(P, t); tree(P, 720, CENTER - 330, t)
        st = .9 + .25 * eio(seg(u, .6, 2.4)) + .03 * math.sin(t * 3)
        hx, hy = giraffe_n(P, 360, GROUND + 10, .95, t, neck=st, sway=.2)
        P.text(900, CENTER - 80, "?", 170 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        savanna(P, t)
        hx, hy = giraffe_n(P, 330, GROUND + 10, .8, t, neck=1.15)
        arrow(P, hx + 60, hy + 160, hx + 60, hy - 30, HOPE, 12)
        k = eout(seg(u, .9, 1.6))
        if k > .02: giraffe_n(P, 790, GROUND + 10, .5 * k, t, neck=.8)
        arrow(P, 520, GROUND - 150, 640, GROUND - 150, CLOUD, 10)
        P.cross(580, GROUND - 150, 55, k=back(seg(u, 1.6, 2.1)))
        P.badge(540, GROUND + 150, "stretching isn't inherited", 52, NIGHT, GLIM, back(seg(u, 2.0, 2.5)))
        P.stamp(810, CENTER - 400, "MYTH", seg(u, .25, .7))
    elif i == 2:
        savanna(P, t); tree(P, 540, CENTER - 360, t, w=1.3)
        for x, n, s in ((200, .75, .62), (540, 1.15, .68), (880, .9, .62)):
            hx, hy = giraffe_n(P, x, GROUND + 10, s, t, neck=n, sway=.4)
        k = back(seg(u, 1.4, 1.9))
        if k > .02: P.heart(600, CENTER - 470, 40 * k, HOOK)
        k2 = eout(seg(u, 3.0, 3.8))
        if k2 > .02:
            giraffe_n(P, 400, GROUND + 10, .3 * k2, t, neck=1.1); giraffe_n(P, 690, GROUND + 10, .3 * k2, t, neck=1.1)
        P.badge(540, GROUND + 150, "more food = more babies", 54, HOPE, CLOUD, back(seg(u, .8, 1.3)))
    elif i == 3:
        savanna(P, t)
        n = .7 + .6 * eio(seg(u, .4, 3.0))
        hx, hy = giraffe_n(P, 330, GROUND + 10, .85, t, neck=n, sway=.2)
        bx, by = 330 + 110 * .85, GROUND + 10 - 330 * .85 - 20 * .85
        for j in range(7):
            q = (j + .5) / 7; kk = back(seg(u, 3.0 + j * .18, 3.3 + j * .18))
            if kk > .02: P.circ(lerp(bx, hx - 10, q), lerp(by, hy + 40, q), 15 * kk, CLOUD, outline=NIGHT, w=4)
        P.badge(770, CENTER - 160, "millions of years", 50, NIGHT, CLOUD, back(seg(u, .2, .7)))
        P.line([(hx + 70, hy), (hx + 70, GROUND - 330 * .85)], CLOUD, 6)
        P.badge(770, CENTER + 20, "about 6 ft", 56, HOPE, CLOUD, back(seg(u, 2.6, 3.1)))
        P.badge(770, CENTER + 200, "7 neck bones", 56, HOOK, CLOUD, back(seg(u, 3.4, 3.9)))
    elif i == 4:
        savanna(P, t)
        sw = math.sin(u * 3.2)
        giraffe_n(P, 260, GROUND + 10, .72, t, neck=1.0 + .05 * sw, sway=2.5)
        giraffe_n(P, 820, GROUND + 10, .72, t + 1.5, neck=1.0 - .05 * sw, sway=2.5, face=-1)
        if abs(sw) > .85:
            P.poly([(540 + 70 * math.cos(a * math.pi / 5) * (1 if a % 2 else .45), CENTER - 120 + 70 * math.sin(a * math.pi / 5) * (1 if a % 2 else .45)) for a in range(10)], GLIM)
        P.badge(540, GROUND + 150, "NECKING", 70, HOOK, CLOUD, back(seg(u, .9, 1.4)))
    else:
        savanna(P, t)
        giraffe_n(P, 250, GROUND + 10, .62, t, neck=1.1)
        k = eout(seg(u, .3, 1.0))
        bone(P, 700, CENTER - 40, 300 * k + 1, 90 * k + 1)
        P.line([(550, CENTER + 60), (850, CENTER + 60)], CLOUD, 6)
        for j in range(11): P.line([(550 + j * 30, CENTER + 60), (550 + j * 30, CENTER + 60 - (22 if j % 5 == 0 else 12))], CLOUD, 4)
        P.badge(700, CENTER + 150, "up to 10 inches", 54, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
        P.stamp(700, CENTER - 300, "FACT", seg(u, .2, .6), col=HOPE, rot=8)
