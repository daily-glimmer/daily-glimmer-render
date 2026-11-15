# Thema: Why do koalas sleep so much?
CENTER = 1050
FUR, FUR2, NOSE = (165, 170, 180), (110, 115, 130), (55, 55, 70)
BARK, LEAF = (150, 110, 80), (95, 160, 110)
PAL = ((225, 240, 220), (190, 220, 200))
HI = {"koalas", "sleep", "twenty", "hours", "eucalyptus", "toxins.", "energy", "gut", "liver", "resting", "cool", "chill"}
WOW = (1, 3)

def tree(P, x=540):
    P.rrect(x - 70, CENTER - 300, x + 70, H + 40, 30, BARK, outline=lc(BARK, (0, 0, 0), .3), w=6)
    P.line([(x + 40, CENTER - 40), (x + 300, CENTER - 260)], BARK, 50)
    for lx, ly in ((x + 300, CENTER - 280), (x + 240, CENTER - 230), (x + 350, CENTER - 220)):
        leaf(P, lx, ly, 1.0, 0)

def leaf(P, x, y, s, a):
    P.ell(x, y, 26 * s, 60 * s, LEAF, outline=lc(LEAF, (0, 0, 0), .3), w=3 * s)

def koala(P, x, y, s, t, sleep=1., z=0.):
    c2 = FUR2
    P.ell(x, y + 90 * s, 120 * s, 140 * s, FUR, outline=c2, w=5 * s)
    P.ell(x, y + 120 * s, 70 * s, 90 * s, (225, 225, 230))
    for d in (-1, 1):
        P.circ(x + d * 115 * s, y - 70 * s, 62 * s, FUR, outline=c2, w=5 * s)
        P.circ(x + d * 115 * s, y - 70 * s, 36 * s, (235, 225, 230))
    P.ell(x, y - 20 * s, 120 * s, 100 * s, FUR, outline=c2, w=5 * s)
    P.ell(x, y + 5 * s, 34 * s, 46 * s, NOSE)
    for d in (-1, 1):
        if sleep > .5: P.arc(x + d * 55 * s, y - 40 * s, 18 * s, 20, 160, NIGHT, 6 * s)
        else:
            P.circ(x + d * 55 * s, y - 40 * s, 13 * s, NIGHT); P.circ(x + d * 55 * s + 4 * s, y - 45 * s, 4 * s, CLOUD)
    if sleep > .5:
        for k in range(3):
            q = (t * .5 + k / 3) % 1
            P.text(x + 140 * s + q * 80, y - 140 * s - q * 160, "z", (40 + 30 * k) * s * (1 - q * .3), HOPE)

def SC(i, P, t, u):
    if i == 0:
        tree(P)
        koala(P, 500, CENTER + 60, 1.0, t, sleep=1)
        P.text(860, CENTER - 330, "?", 150 * back(seg(u, .4, .9)), HOOK)
    elif i == 1:
        tree(P)
        koala(P, 500, CENTER + 60, 1.0, t, sleep=1)
        P.circ(820, CENTER - 200, 110, CLOUD, outline=NIGHT, w=8)
        a = math.radians(-90 + 300 * eout(seg(u, .4, 2.6)))
        P.line([(820, CENTER - 200), (820 + 80 * math.cos(a), CENTER - 200 + 80 * math.sin(a))], HOOK, 10)
        P.badge(540, CENTER + 430, "up to 20 h a day", 62, NIGHT, GLIM, back(seg(u, 1.2, 1.7)))
    elif i == 2:
        for k in range(5):
            leaf(P, 200 + k * 170, CENTER - 60 + 30 * math.sin(t * 2 + k), 1.6 * back(seg(u, .2 + k * .15, .6 + k * .15)), 0)
        P.badge(300, CENTER + 160, "low energy", 50, HOOK, CLOUD, back(seg(u, 1.0, 1.4)))
        P.badge(780, CENTER + 160, "toxins", 50, HOOK, CLOUD, back(seg(u, 1.6, 2.0)))
        koala(P, 540, CENTER + 330, .7, t, sleep=0)
    elif i == 3:
        k = eio(seg(u, .3, 2.6))
        P.rrect(150, CENTER - 220, 930, CENTER + 220, 40, CLOUD, outline=FUR2, w=6)
        pts = [(220 + 640 * q / 40, CENTER + 120 * math.sin(q / 40 * 4 * math.pi)) for q in range(41)]
        P.line(pts, (230, 150, 150), 30)
        n = int(k * 40)
        if n > 0: leaf(P, pts[n][0], pts[n][1], .6, 0)
        P.badge(540, CENTER - 300, "long gut", 56, NIGHT, GLIM, back(seg(u, .5, 1.0)))
        P.badge(540, CENTER + 320, "busy liver", 56, HOPE, CLOUD, back(seg(u, 1.6, 2.1)))
    elif i == 4:
        tree(P)
        koala(P, 500, CENTER + 60, 1.0, t, sleep=1)
        P.rrect(760, CENTER + 300, 960, CENTER + 400, 16, CLOUD, outline=NIGHT, w=6)
        lv = .2 + .8 * eout(seg(u, .6, 2.6))
        P.rrect(772, CENTER + 312, 772 + 168 * lv, CENTER + 388, 10, HOPE)
        P.badge(540, CENTER + 480, "energy saver", 56, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
    else:
        tree(P)
        koala(P, 480, CENTER + 120, .9, t, sleep=1)
        for k in range(3):
            P.text(820 + 40 * math.sin(t * 2 + k), CENTER - 60 + k * 110, "*", 70, (120, 190, 240))
        P.badge(540, CENTER - 420, "cool tree hug", 58, NIGHT, GLIM, back(seg(u, .8, 1.3)))
