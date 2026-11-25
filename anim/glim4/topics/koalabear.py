# Thema: Is a koala really a bear?  (Mythos-Format, MYTH/FACT)
exec(open(os.path.join(HERE, "topics", "koalas.py")).read(), globals())
exec(open(os.path.join(HERE, "topics", "kangaroos.py")).read(), globals())
CENTER = 1050
FUR, FUR2, NOSE = (165, 170, 180), (110, 115, 130), (55, 55, 70)
_roo = roo
def roo(P, *a, **k):
    global FUR, FUR2
    sv = FUR, FUR2; FUR, FUR2 = (205, 120, 75), (160, 85, 50)
    _roo(P, *a, **k); FUR, FUR2 = sv
PAL = ((220, 238, 215), (175, 212, 190))
HI = {"bear?", "bears.", "marsupials,", "kangaroos.", "teddy", "jelly", "bean,", "pouch.", "joey,", "six", "months", "wombat!"}
WOW = (1, 5)
TEDDY, TEDDY2 = (190, 130, 80), (140, 90, 55)
WOMB, WOMB2 = (150, 115, 85), (105, 80, 60)
PINK = (245, 170, 175)

def ground(P):
    P.poly([(0, CENTER + 360), (W, CENTER + 330), (W, H), (0, H)], (150, 190, 120))
    for gx in (90, 260, 470, 690, 900, 1010):
        for d in (-1, 0, 1): P.line([(gx, CENTER + 400), (gx + d * 18, CENTER + 365)], (110, 160, 95), 6)

def teddy(P, x, y, s, t):
    for d in (-1, 1):
        P.circ(x + d * 80 * s, y - 95 * s, 38 * s, TEDDY, outline=TEDDY2, w=5 * s)
        P.circ(x + d * 80 * s, y - 95 * s, 20 * s, (230, 190, 150))
        P.ell(x + d * 120 * s, y + 90 * s, 40 * s, 60 * s, TEDDY, outline=TEDDY2, w=5 * s)
        P.ell(x + d * 70 * s, y + 210 * s, 50 * s, 40 * s, TEDDY, outline=TEDDY2, w=5 * s)
    P.ell(x, y + 110 * s, 100 * s, 120 * s, TEDDY, outline=TEDDY2, w=5 * s)
    P.ell(x, y + 120 * s, 55 * s, 70 * s, (230, 190, 150))
    P.circ(x, y - 30 * s, 95 * s, TEDDY, outline=TEDDY2, w=5 * s)
    P.ell(x, y, 40 * s, 30 * s, (230, 190, 150)); P.ell(x, y - 10 * s, 14 * s, 10 * s, NIGHT)
    for d in (-1, 1): P.circ(x + d * 38 * s, y - 50 * s, 10 * s, NIGHT)

def wombat(P, x, y, s, t, face=1):
    b = math.sin(t * 3) * 4 * s
    for d in (-1, 1):
        P.rrect(x + d * 70 * s - 22 * s, y + 40 * s, x + d * 70 * s + 22 * s, y + 110 * s, 12 * s, WOMB2)
    P.ell(x, y + b, 150 * s, 95 * s, WOMB, outline=WOMB2, w=5 * s)
    hx = x + face * 135 * s
    for d in (-1, 1): P.circ(hx + d * 30 * s, y - 85 * s + b, 18 * s, WOMB, outline=WOMB2, w=4 * s)
    P.ell(hx, y - 35 * s + b, 70 * s, 60 * s, WOMB, outline=WOMB2, w=5 * s)
    P.ell(hx + face * 38 * s, y - 25 * s + b, 26 * s, 22 * s, NOSE)
    P.circ(hx - face * 5 * s, y - 50 * s + b, 8 * s, NIGHT); P.circ(hx + face * 25 * s, y - 50 * s + b, 8 * s, NIGHT)

def mother(P, t):
    koala(P, 540, CENTER - 20, 1.5, t, sleep=0)
    P.ell(540, CENTER + 230, 95, 55, (205, 205, 212), outline=FUR2, w=5)
    P.arc(540, CENTER + 230, 95, 200, 340, FUR2, 8)

def bean(P, x, y, s, a=0.):
    P.ell(x, y, 26 * s, 16 * s, PINK, outline=(200, 120, 130), w=3 * s)
    P.circ(x + 18 * s, y - 4 * s, 4 * s, NIGHT)

def SC(i, P, t, u):
    if i == 0:
        tree(P); koala(P, 500, CENTER + 60, 1.0, t, sleep=0)
        P.badge(820, CENTER - 300, "bear?", 70, NIGHT, GLIM, back(seg(u, .5, 1.0)))
    elif i == 1:
        ground(P)
        koala(P, 300, CENTER + 165, .75, t, sleep=0)
        roo(P, 790, CENTER + 300, .8, t)
        P.badge(540, CENTER + 470, "marsupials", 64, HOPE, CLOUD, back(seg(u, 2.0, 2.5)))
        P.stamp(540, CENTER - 300, "MYTH", seg(u, .25, .7))
    elif i == 2:
        ground(P)
        teddy(P, 300, CENTER + 60, .95, t)
        koala(P, 780, CENTER + 60, .8, t, sleep=0)
        k = back(seg(u, .4, .9))
        P.badge(540, CENTER - 260, "looks like a teddy", 56, NIGHT, GLIM, k)
        P.badge(540, CENTER + 460, "\"koala bear\"", 58, HOOK, CLOUD, back(seg(u, 2.6, 3.1)))
    elif i == 3:
        mother(P, t)
        q = eio(seg(u, 1.6, 4.6))
        bx, by = lerp(400, 540, q), lerp(CENTER + 60, CENTER + 215, q)
        if q < .97: bean(P, bx, by, 1.3 * back(seg(u, .4, .9)))
        P.badge(870, CENTER - 230, "jelly bean size", 50, NIGHT, GLIM, back(seg(u, .9, 1.4)))
        P.badge(540, CENTER + 480, "about 2 cm", 54, HOPE, CLOUD, back(seg(u, 2.0, 2.5)))
    elif i == 4:
        mother(P, t)
        g = eout(seg(u, .5, 3.5)); pk = eout(seg(u, 2.6, 3.6))
        hy = CENTER + 225 - 70 * pk
        if pk > .02:
            for d in (-1, 1): P.circ(540 + d * 34, hy - 26, 18, FUR, outline=FUR2, w=3)
            P.ell(540, hy, 40, 34, FUR, outline=FUR2, w=3)
            P.ell(540, hy + 6, 10, 13, NOSE)
            for d in (-1, 1): P.circ(540 + d * 16, hy - 8, 5, NIGHT)
            P.ell(540, CENTER + 245, 95, 38, (205, 205, 212))
        P.rrect(240, CENTER + 420, 840, CENTER + 480, 20, CLOUD, outline=NIGHT, w=5)
        P.rrect(250, CENTER + 430, 250 + 580 * g, CENTER + 470, 14, HOPE)
        P.badge(540, CENTER + 560, "~6 months", 54, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
    else:
        ground(P)
        koala(P, 300, CENTER + 170, .7, t, sleep=0)
        wombat(P, 760, CENTER + 230, .9, t, face=-1)
        P.heart(540, CENTER + 20 + 10 * math.sin(t * 4), 50 * back(seg(u, .8, 1.3)), HOOK)
        P.badge(790, CENTER + 90, "wombat", 56, HOPE, CLOUD, back(seg(u, 1.4, 1.9)))
        P.stamp(540, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
