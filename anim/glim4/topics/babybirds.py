# Thema: If you touch a baby bird, will its mother reject it?  (Mythos-Format)
# Neue Figuren: songbird (Singvogel, open=Schnabel offen, flap=Flügelschlag), chick (Nestling nackt/flauschig, gape),
# nest, branch, hand (stilisierte Hand), smell (Duftwellen)
CENTER = 1050
BROWN, BELLY, BEAK, TWIG = (150, 95, 60), (245, 170, 110), (255, 180, 40), (120, 80, 50)
PAL = ((45, 60, 40), (140, 175, 120))
HI = {"touch", "reject", "myth.", "smells", "human.", "begging", "beak,", "feeding", "feathers", "nest.", "fledgling", "nearby.", "distance,", "job!"}
WOW = (1,)

def dk(c, k): return tuple(int(v * k / 255) for v in c)

def branch(P, y=CENTER + 120):
    P.line([(-20, y + 40), (W + 20, y - 30)], TWIG, 34)
    for x, d in ((200, -1), (820, 1)):
        P.line([(x, y + 20 - x * .07), (x + d * 90, y - 80 - x * .07)], TWIG, 16)
        P.ell(x + d * 100, y - 95 - x * .07, 40, 22, (110, 170, 90))

def nest(P, x, y, s=1.):
    P.ell(x, y, 190 * s, 80 * s, dk(TWIG, 200))
    for k in range(9):
        a = -.9 + k * .22
        P.line([(x - 190 * s, y - 10 * s + k * 8 * s), (x + 190 * s, y - 30 * s + k * 9 * s)], TWIG if k % 2 else dk(TWIG, 170), 8 * s)
    P.ell(x, y - 30 * s, 150 * s, 28 * s, dk(TWIG, 120))

def songbird(P, x, y, s, t, f=1, open_=0., flap=0., food=False):
    wing = math.sin(t * 18) * flap
    P.poly([(x + f * 70 * s, y), (x + f * 150 * s, y - 20 * s), (x + f * 150 * s, y + 25 * s)], dk(BROWN, 200))   # Schwanz
    P.ell(x, y, 90 * s, 70 * s, BROWN)
    P.ell(x - f * 15 * s, y + 20 * s, 60 * s, 45 * s, BELLY)
    P.poly([(x + f * 10 * s, y - 10 * s), (x + f * 80 * s, y - 10 * s - 60 * s * wing), (x + f * 70 * s, y + 30 * s)], dk(BROWN, 180))
    hx, hy = x - f * 70 * s, y - 55 * s
    P.circ(hx, hy, 45 * s, BROWN)
    P.circ(hx - f * 12 * s, hy - 8 * s, 9 * s, NIGHT); P.circ(hx - f * 9 * s, hy - 11 * s, 3 * s, (255, 255, 255))
    o = 14 * s * open_
    P.poly([(hx - f * 38 * s, hy - 4 * s), (hx - f * 85 * s, hy + 4 * s - o), (hx - f * 38 * s, hy + 12 * s)], BEAK)
    if food:
        P.line([(hx - f * 80 * s, hy + 6 * s), (hx - f * 110 * s, hy + 20 * s)], (200, 120, 160), 10 * s)

def chick(P, x, y, s, t, gape=0., fluffy=False, hop=0.):
    y -= abs(math.sin(t * 6)) * 40 * hop
    col = (190, 160, 140) if fluffy else (250, 190, 170)
    if fluffy:
        for k in range(10):
            a = k * .63; P.circ(x + math.cos(a) * 52 * s, y + math.sin(a) * 42 * s, 22 * s, col)
    P.ell(x, y, 60 * s, 50 * s, col)
    P.circ(x, y - 60 * s, 36 * s, col)
    P.circ(x - 14 * s, y - 68 * s, 6 * s, NIGHT); P.circ(x + 14 * s, y - 68 * s, 6 * s, NIGHT)
    g = 34 * s * gape
    P.poly([(x - 26 * s, y - 52 * s), (x, y - 52 * s - 30 * s - g), (x + 26 * s, y - 52 * s)], BEAK)
    P.poly([(x - 26 * s, y - 50 * s), (x, y - 40 * s + g * .6), (x + 26 * s, y - 50 * s)], BEAK)
    if gape > .3: P.poly([(x - 16 * s, y - 52 * s), (x, y - 72 * s - g * .7), (x + 16 * s, y - 52 * s)], HOOK)
    if fluffy:
        for dx in (-20, 20): P.line([(x + dx * s, y + 48 * s), (x + dx * s, y + 75 * s)], BEAK, 7 * s)

def hand(P, x, y, s=1.):
    skin = (240, 190, 150)
    P.rrect(x - 70 * s, y, x + 70 * s, y + 260 * s, 50 * s, skin)
    for k in range(4): P.rrect(x - 66 * s + k * 34 * s, y - 70 * s - (k % 3) * 12 * s, x - 38 * s + k * 34 * s, y + 30 * s, 14 * s, skin)
    P.rrect(x + 55 * s, y + 40 * s, x + 120 * s, y + 80 * s, 18 * s, skin)

def smell(P, x, y, t, col=(200, 160, 230)):
    for k in range(3):
        q = (t * .7 + k / 3) % 1
        pts = [(x + 30 * math.sin(j * .9 + k + t * 3) + k * 40 - 40, y - j * 22 - q * 120) for j in range(8)]
        P.line(pts, lc(col, (60, 60, 60), q * .6), 8)

def SC(i, P, t, u):
    if i == 0:
        branch(P); nest(P, 540, CENTER + 120)
        for k, dx in enumerate((-70, 40)): chick(P, 540 + dx, CENTER + 60, .9, t + k, gape=.5 + .5 * math.sin(t * 7 + k))
        k = eout(seg(u, .3, 1.6)); hand(P, lerp(1200, 820, k), lerp(CENTER - 400, CENTER - 150, k), .9)
        songbird(P, 200, CENTER - 230, .9, t, f=-1, flap=.6)
        P.text(220, CENTER - 420, "?", 130 * back(seg(u, 1.2, 1.7)), GLIM)
    elif i == 1:
        branch(P); nest(P, 540, CENTER + 120)
        for k, dx in enumerate((-70, 40)): chick(P, 540 + dx, CENTER + 60, .9, t + k, gape=.3)
        smell(P, 540, CENTER - 20, t)
        P.stamp(540, CENTER - 300, "MYTH", seg(u, .25, .7))
    elif i == 2:
        branch(P); nest(P, 560, CENTER + 120)
        g = .6 + .4 * math.sin(t * 9)
        for k, dx in enumerate((-80, 40)): chick(P, 560 + dx, CENTER + 50, .95, t + k, gape=g)
        k = eout(seg(u, .4, 1.4)); songbird(P, lerp(1100, 760, k), lerp(CENTER - 500, CENTER - 160, k), 1.0, t, f=1, open_=0, flap=1 - k, food=True)
        if u > 1.2:
            for j in range(3):
                q = (t * 1.5 + j / 3) % 1; P.arc(480, CENTER - 40, 60 + q * 120, 200, 340, lc(GLIM, (0, 0, 0), q), 7)
        P.badge(540, CENTER - 420 + 0, "cheep cheep!", 56, HOPE, CLOUD, back(seg(u, 1.0, 1.5)))
    elif i == 3:
        branch(P); nest(P, 620, CENTER + 120)
        chick(P, 560, CENTER + 60, .9, t, gape=.2)
        k = eio(seg(u, .5, 2.4))
        hand(P, lerp(300, 620, k) + 60, lerp(CENTER + 330, CENTER + 120, k) + 40, .8)
        chick(P, lerp(300, 680, k), lerp(CENTER + 330, CENTER + 70, k), .8, t + 1, gape=.4)
        P.badge(540, CENTER - 330, "no feathers?", 56, NIGHT, GLIM, back(seg(u, .3, .8)))
        P.check(820, CENTER - 140, 60, k=back(seg(u, 2.4, 2.9)))
    elif i == 4:
        P.poly([(0, CENTER + 200), (W, CENTER + 180), (W, H), (0, H)], (100, 150, 75))
        for gx in range(20, W, 60): P.line([(gx, CENTER + 200), (gx + 10, CENTER + 160)], (80, 130, 60), 6)
        chick(P, 600, CENTER + 120, 1.1, t, fluffy=True, hop=1)
        songbird(P, 220, CENTER - 160, .85, t, f=-1, food=True)
        P.line([(120, CENTER - 90), (360, CENTER - 100)], TWIG, 22)
        P.badge(540, CENTER - 330, "parents nearby", 56, HOPE, CLOUD, back(seg(u, 1.6, 2.1)))
    else:
        branch(P); nest(P, 560, CENTER + 120)
        for k, dx in enumerate((-80, 40)): chick(P, 560 + dx, CENTER + 50, .95, t + k, gape=.5 + .5 * math.sin(t * 6 + k))
        songbird(P, 820, CENTER - 140, .9, t, f=1, food=True)
        P.heart(300, CENTER - 120, 50 + 6 * math.sin(t * 5), (255, 120, 150))
        P.stamp(540, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
