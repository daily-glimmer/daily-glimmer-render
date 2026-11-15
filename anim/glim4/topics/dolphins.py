# Thema: How do dolphins sleep without drowning?
CENTER = 1050
DOL, DOL2, BELLY = (120, 150, 185), (85, 110, 145), (220, 230, 240)
PAL = ((10, 60, 110), (40, 140, 190))
HI = {"sleep", "drowning?", "breathe,", "never", "one", "half", "brain", "awake", "danger.", "eye", "open,", "swap", "sides"}
WOW = (2, 5)
SURF = CENTER - 120

def sea(P, t, y=SURF):
    P.poly([(0, 0), (W, 0), (W, y + 10), (0, y + 10)], (120, 190, 235))
    P.circ(930, y - 170, 80, (255, 225, 120))
    P.poly([(0, y)] + [(x, y + math.sin(x / 70 + t * 2) * 10) for x in range(0, 1081, 40)] + [(W, H), (0, H)], (20, 80, 140))
    P.poly([(0, y)] + [(x, y + math.sin(x / 70 + t * 2) * 10) for x in range(0, 1081, 40)] + [(W, y + 18), (0, y + 18)], (90, 170, 220))
    for k in range(6):
        q = (t * .3 + k / 6) % 1; P.circ(120 + k * 170, lerp(CENTER + 500, y + 20, q), 7 + k % 3 * 4, (120, 190, 230))

def dolphin(P, x, y, s, t, eyes=(1, 1), swim=True, flip=1, ang=0.):
    f = flip; tw = math.sin(t * (5 if swim else 1.2)) * (24 if swim else 8) * s
    ca, sa = math.cos(ang), math.sin(ang)
    def q(px, py): return (x + f * (px * ca - py * sa), y + (px * sa + py * ca))
    P.poly([q(160 * s, -10 * s), q(250 * s, -60 * s + tw), q(230 * s, 0 + tw * .4), q(250 * s, 60 * s + tw)], DOL2)
    P.poly([q(-10 * s, -60 * s), q(50 * s, -140 * s), q(80 * s, -55 * s)], DOL2)
    P.poly([q(x_ * s, y_ * s) for x_, y_ in [(-200, 10), (-175, -40), (-80, -75), (60, -70), (180, -20), (190, 10), (100, 50), (-60, 60), (-170, 35)]], DOL)
    P.poly([q(x_ * s, y_ * s) for x_, y_ in [(-190, 20), (-80, 50), (60, 45), (120, 25), (-60, 25)]], BELLY)
    P.poly([q(-200 * s, 10 * s), q(-260 * s, 18 * s), q(-255 * s, 32 * s), q(-185 * s, 30 * s)], DOL)
    P.poly([q(-30 * s, 40 * s), q(20 * s, 105 * s), q(40 * s, 40 * s)], DOL2)
    ex, ey = q(-140 * s, -15 * s)
    if eyes[0]: P.circ(ex, ey, 10 * s, NIGHT); P.circ(ex - f * 3 * s, ey - 4 * s, 3.5 * s, CLOUD)
    else: P.arc(ex, ey - 4 * s, 11 * s, 20, 160, NIGHT, 4 * s)
    bx, by = q(-120 * s, -60 * s); P.circ(bx, by, 6 * s, DOL2)
    mx, my = q(-205 * s, 22 * s); P.arc(mx + f * 25 * s, my - 22 * s, 30 * s, 60, 120, NIGHT, 4 * s)

def brain(P, x, y, r, left, right, t):
    for side, on in ((-1, left), (1, right)):
        col = GLIM if on else (90, 110, 170)
        P.ell(x + side * r * .52, y, r * .5, r * .75, col, outline=lc(col, (0, 0, 0), .3), w=8)
        for k in range(3): P.arc(x + side * r * .52, y - r * .35 + k * r * .35, r * .25, 200, 340, lc(col, (0, 0, 0), .3), 6)
        if not on:
            for j in range(2):
                qq = (t * .6 + j / 2) % 1
                P.text(x + side * r * .52 + 40 + qq * 60, y - r - qq * 120, "z", 60 * (1 - qq * .4), lc(CLOUD, NIGHT, qq), kind="head")

def SC(i, P, t, u):
    sea(P, t)
    if i == 0:
        dolphin(P, 540, CENTER + 180 + math.sin(t * 1.5) * 20, 1.4, t)
        P.text(200, CENTER - 230, "?", 150 * back(seg(u, .4, .9)), GLIM)
    elif i == 1:
        k = eio(seg(u, .2, 2.4))
        dolphin(P, 540, lerp(CENTER + 300, SURF + 30, k), 1.2, t, ang=-.5 * (1 - abs(k - .5) * 2))
        if k > .9:
            for j in range(4):
                qq = (t * 1.3 + j / 4) % 1
                P.circ(430 + math.sin(j * 2) * 20, SURF - 40 - qq * 220, 18 * (1 - qq) + 4, (210, 235, 255))
        P.badge(540, CENTER + 450, "needs air", 60, HOOK, CLOUD, back(seg(u, 2.0, 2.5)))
    elif i == 2:
        brain(P, 540, CENTER + 120, 260 * back(seg(u, .2, .7)), False, True, t)
        P.badge(540, CENTER + 450, "half asleep", 60, NIGHT, GLIM, back(seg(u, 1.2, 1.7)))
    elif i == 3:
        dolphin(P, 540 + math.sin(t * .8) * 60, CENTER + 180, 1.2, t, eyes=(1, 1))
        for k in range(3):
            qq = (t * 1.2 + k / 3) % 1
            P.arc(330, CENTER + 165, 40 + qq * 160, 140, 220, lc(GLIM, (25, 95, 150), qq), 9 * (1 - qq) + 2)
        P.badge(540, CENTER + 450, "on watch", 60, HOPE, CLOUD, back(seg(u, 1.2, 1.7)))
    elif i == 4:
        sw = u > 2.4
        dolphin(P, 540, CENTER + 60, 1.25, t, eyes=(0, 1) if not sw else (1, 0), swim=False, flip=1 if not sw else -1)
        brain(P, 540, CENTER + 430, 100, sw, not sw, t)
        P.badge(540, CENTER - 280, "swap sides", 58, NIGHT, GLIM, back(seg(u, 2.4, 2.9)))
    else:
        dolphin(P, 540, CENTER + 230, 1.15, t, eyes=(0, 1), swim=False)
        brain(P, 540, CENTER - 130, 150, False, True, t)
