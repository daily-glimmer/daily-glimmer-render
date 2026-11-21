# Thema: Will a mother bird reject a chick if you touch it?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6)
CENTER = 1050
BR, BR2, BELLYC, NEST = (120, 90, 70), (95, 70, 55), (240, 130, 70), (150, 110, 60)
SKINC = (240, 195, 160)
PAL = ((110, 170, 210), (200, 225, 180))
HI = {"reject", "touch", "myth!", "weak", "smell,", "scent.", "look", "sound.", "fledgling", "nearby.", "distance,", "predators", "back!"}
WOW = (1,)

def branch(P, y=CENTER + 120):
    P.line([(-20, y + 40), (1100, y - 30)], (110, 80, 50), 50)
    for x in (200, 760):
        P.ell(x, y - 80, 70, 30, (90, 160, 80)); P.ell(x + 60, y - 50, 60, 26, (80, 150, 70))

def nest(P, x, y, s):
    P.ell(x, y, 170 * s, 70 * s, NEST)
    for j in range(7): P.arc(x, y - 10 * s, (100 + j * 10) * s, 10 + j * 5, 170 - j * 5, (120, 85, 45), 6 * s)

def bird(P, x, y, s, t, chick=False, open_=0., flip=1):
    f = flip; b = math.sin(t * 3) * 4 * s
    body = (170, 160, 150) if chick else BR
    P.ell(x, y + b, 80 * s, 62 * s, body)
    P.ell(x + f * 15 * s, y + 15 * s + b, 50 * s, 40 * s, (230, 215, 200) if chick else BELLYC)
    if not chick: P.poly([(x - f * 60 * s, y - 10 * s + b), (x - f * 140 * s, y - 40 * s + b), (x - f * 120 * s, y + 10 * s + b)], BR2)
    hx, hy = x + f * 55 * s, y - 60 * s + b
    P.circ(hx, hy, 42 * s, body)
    if chick:
        for j in range(3): P.line([(hx - 10 * s + j * 10 * s, hy - 38 * s), (hx - 15 * s + j * 14 * s, hy - 62 * s)], body, 5 * s)
    op = 22 * s * open_
    P.poly([(hx + f * 30 * s, hy - 4 * s - op), (hx + f * 80 * s, hy + 4 * s), (hx + f * 30 * s, hy + 10 * s)], (250, 200, 60))
    P.poly([(hx + f * 30 * s, hy + 10 * s), (hx + f * 72 * s, hy + 8 * s + op), (hx + f * 28 * s, hy + 18 * s + op)], (240, 180, 40))
    P.circ(hx + f * 12 * s, hy - 10 * s, 8 * s, NIGHT); P.circ(hx + f * 14 * s, hy - 12 * s, 3 * s, CLOUD)

def hand(P, x, y, s):
    P.ell(x, y, 150 * s, 70 * s, SKINC)
    for j in range(4): P.ell(x - 100 * s + j * 60 * s, y - 70 * s, 26 * s, 50 * s, SKINC)
    P.ell(x + 150 * s, y - 20 * s, 60 * s, 26 * s, SKINC)

def SC(i, P, t, u):
    if i == 0:
        branch(P); nest(P, 540, CENTER + 80, 1.2)
        bird(P, 500, CENTER + 10, .8, t, chick=True, open_=abs(math.sin(t * 6)))
        hand(P, 620, CENTER + 400 - 60 * eio(seg(u, .4, 1.4)), 1.0)
        P.text(860, CENTER - 230, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        branch(P); nest(P, 540, CENTER + 80, 1.2)
        bird(P, 500, CENTER + 10, .8, t, chick=True, open_=abs(math.sin(t * 6)))
        bird(P, 260, CENTER - 160, 1.0, t)
        P.stamp(780, CENTER - 260, "MYTH", seg(u, .25, .7))
        P.badge(540, CENTER + 420, "can't smell you", 58, NIGHT, CLOUD, back(seg(u, 1.6, 2.1)))
    elif i == 2:
        branch(P); nest(P, 540, CENTER + 80, 1.2)
        bird(P, 470, CENTER + 10, .7, t, chick=True, open_=abs(math.sin(t * 7)))
        bird(P, 600, CENTER + 20, .7, t + 1, chick=True, open_=abs(math.sin(t * 7 + 1)), flip=-1)
        bird(P, 830, CENTER - 140, 1.0, t, flip=-1)
        P.badge(260, CENTER - 300, "looks", 52, NIGHT, CLOUD, back(seg(u, .6, 1.1)))
        P.badge(540, CENTER - 300, "sounds", 52, NIGHT, CLOUD, back(seg(u, 1.4, 1.9)))
        waves(P, 520, CENTER - 80, t, CLOUD, n=3, r0=50, dr=30, a0=-140, a1=-40)
    elif i == 3:
        P.poly([(0, CENTER + 250), (W, CENTER + 230), (W, H), (0, H)], (110, 170, 80))
        hop = abs(math.sin(t * 4)) * 40
        bird(P, 400, CENTER + 180 - hop, .9, t, chick=True)
        branch(P, CENTER - 300); bird(P, 760, CENTER - 400, .9, t, flip=-1)
        P.badge(540, CENTER + 450, "parents nearby", 58, HOPE, CLOUD, back(seg(u, 2.0, 2.5)))
    elif i == 4:
        branch(P); nest(P, 540, CENTER + 80, 1.2)
        bird(P, 520, CENTER + 10, .8, t, chick=True)
        k = back(seg(u, .5, 1.0))
        P.ell(880, CENTER + 300, 120 * k, 60 * k, (200, 110, 50)); P.circ(970, CENTER + 250, 45 * k, (200, 110, 50))
        if k > .3:
            for dx in (-25, 20): P.poly([(970 + dx - 18, CENTER + 220), (970 + dx, CENTER + 175), (970 + dx + 18, CENTER + 220)], (200, 110, 50))
            P.circ(990, CENTER + 245, 8, NIGHT); P.circ(1010, CENTER + 262, 7, NIGHT)
        P.badge(860, CENTER + 420, "predator", 44, NIGHT, CLOUD, back(seg(u, 1.0, 1.5)))
        P.badge(540, CENTER - 280, "keep your distance", 56, HOOK, CLOUD, back(seg(u, 1.5, 2.0)))
    else:
        branch(P); nest(P, 540, CENTER + 80, 1.2)
        bird(P, 500, CENTER + 10, .8, t, chick=True, open_=abs(math.sin(t * 6)))
        bird(P, 760, CENTER - 120, .9, t, flip=-1)
        P.heart(300, CENTER - 120, 50 * back(seg(u, .9, 1.4)), HOOK)
        P.stamp(560, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
