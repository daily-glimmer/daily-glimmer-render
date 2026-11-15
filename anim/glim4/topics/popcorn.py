# Thema: Why does popcorn pop?
CENTER = 1050
KER, KER2, FOAM = (240, 175, 60), (200, 120, 35), (255, 250, 235)
PAL = ((255, 220, 180), (255, 190, 170))
HI = {"pop?", "water", "hard", "shell.", "180", "degrees", "steam.", "pushes", "bursts", "fluffy", "foam,", "inside", "out.", "steam", "escaping!"}
WOW = (3, 5)

def kernel(P, x, y, s, drop=False, steam=0., wob=0.):
    sx = 1 + wob * .08; sy = 1 - wob * .05
    P.poly([(x - 60 * s * sx, y + 20 * s), (x, y + 105 * s), (x + 60 * s * sx, y + 20 * s)], (250, 235, 200), outline=KER2, w=6 * s)
    P.ell(x, y - 20 * s, 85 * s * sx, 90 * s * sy, KER, outline=KER2, w=7 * s)
    P.ell(x - 35 * s, y - 55 * s, 16 * s, 26 * s, (255, 215, 130))
    if drop: P.ell(x, y - 20 * s, 22 * s * (1 + steam * .6), 30 * s * (1 + steam * .6), lc((90, 170, 240), CLOUD, steam), outline=(60, 130, 200), w=4 * s)

def popped(P, x, y, s, t=0., ph=0.):
    for a in range(6):
        ang = a * 1.047 + ph
        P.circ(x + math.cos(ang) * 55 * s, y + math.sin(ang) * 45 * s, 52 * s, FOAM, outline=(225, 210, 180), w=4 * s)
    P.circ(x, y, 55 * s, FOAM)
    P.poly([(x - 18 * s, y + 25 * s), (x + 18 * s, y + 25 * s), (x, y + 60 * s)], KER)

def pan(P, x, y, t, hot=0.):
    P.rrect(x - 330, y, x + 330, y + 90, 40, (70, 75, 95))
    P.line([(x + 330, y + 40), (x + 520, y + 20)], (60, 50, 45), 30)
    for k in range(4):
        q = (t * 1.5 + k / 4) % 1
        P.line([(x - 240 + k * 160, y + 150 + q * 20), (x - 240 + k * 160 + math.sin(t * 8 + k) * 10, y + 115)], lc((255, 120, 40), (255, 220, 120), q), 18 * (1 - q) + 4)

def SC(i, P, t, u):
    if i == 0:
        pan(P, 540, CENTER + 250, t)
        for j in range(5):
            jump = abs(math.sin(t * 3 + j)) * 160
            popped(P, 300 + j * 120, CENTER + 150 - jump, .55, t, j)
        P.text(840, CENTER - 280, "?", 150 * back(seg(u, .4, .9)), HOOK)
    elif i == 1:
        k = back(seg(u, .1, .6))
        kernel(P, 540, CENTER + 60, 3.0 * k, drop=u > 1.2)
        P.badge(540, CENTER + 440, "a drop of water", 58, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
    elif i == 2:
        pan(P, 540, CENTER + 280, t)
        st = seg(u, 1.0, 3.0)
        kernel(P, 540, CENTER + 60, 2.3, drop=True, steam=st)
        P.badge(540, CENTER - 280, "180 °C", 80, HOOK, CLOUD, back(seg(u, .8, 1.3)))
    elif i == 3:
        pr = seg(u, .2, 2.6)
        wob = math.sin(t * 40) * pr
        kernel(P, 540, CENTER + 60, 2.3 + pr * .25, drop=True, steam=1, wob=wob)
        for a in range(8):
            ang = a * .785
            r0 = 260 + pr * 30
            P.line([(540 + math.cos(ang) * r0, CENTER + 40 + math.sin(ang) * r0), (540 + math.cos(ang) * (r0 + 60 * pr), CENTER + 40 + math.sin(ang) * (r0 + 60 * pr))], HOOK, 12)
        if u > 2.6:
            P.text(540, CENTER - 280, "POP!", 160 * back(seg(u, 2.6, 2.9)), HOOK)
    elif i == 4:
        k = back(seg(u, .1, .7))
        popped(P, 540, CENTER + 60, 3.0 * k, t)
        P.badge(540, CENTER + 420, "inside out!", 60, HOPE, CLOUD, back(seg(u, 1.6, 2.1)))
    else:
        P.poly([(330, CENTER), (750, CENTER), (700, CENTER + 400), (380, CENTER + 400)], (235, 70, 70))
        for k in range(4): P.rrect(352 + k * 100, CENTER + 10, 392 + k * 100, CENTER + 390, 10, CLOUD)
        for j in range(9):
            popped(P, 360 + (j % 5) * 90, CENTER - 20 - (j // 5) * 70, .55, t, j)
        for k in range(3):
            q = (t * .7 + k / 3) % 1
            P.ell(330 + k * 210, CENTER - 140 - q * 160, 40 * (1 - q * .5), 30, lc(CLOUD, PAL[0], q))
