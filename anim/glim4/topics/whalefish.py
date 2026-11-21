# Thema: Is a whale a fish?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6)
CENTER = 1050
PAL = ((10, 50, 110), (40, 130, 180))
HI = {"fish?", "myth!", "mammals,", "lungs,", "blowhole.", "milk,", "warm-blooded,", "up-and-down", "side", "mammal", "fish?"}
WOW = (1,)
WH, WH2, WB = (70, 100, 150), (50, 75, 120), (200, 215, 230)
SURF = CENTER - 300

def sea(P, t):
    P.rrect(-20, SURF, W + 20, H + 40, 0, (30, 90, 150))
    for k in range(6):
        x = (k * 210 + t * 40) % (W + 200) - 100; P.arc(x, SURF, 50, 200, 340, (120, 190, 230), 8)

def whale(P, x, y, s, t, tail_up=None, spout=0.):
    tw = math.sin(t * 2.5) * 30 * s if tail_up is None else tail_up * 40 * s
    P.line([(x - 220 * s, y), (x - 300 * s, y - 10 * s + tw * .6)], WH, 50 * s)
    P.poly([(x - 290 * s, y - 10 * s + tw), (x - 390 * s, y - 40 * s + tw), (x - 410 * s, y - 15 * s + tw), (x - 390 * s, y + 10 * s + tw), (x - 290 * s, y + 5 * s + tw)], WH2)
    P.ell(x, y, 260 * s, 100 * s, WH)
    P.ell(x + 40 * s, y + 45 * s, 200 * s, 45 * s, WB)
    for j in range(5): P.line([(x - 40 * s + j * 40 * s, y + 30 * s), (x - 30 * s + j * 40 * s, y + 80 * s)], lc(WB, WH, .4), 5 * s)
    P.circ(x + 170 * s, y - 20 * s, 12 * s, NIGHT); P.arc(x + 200 * s, y + 20 * s, 40 * s, 30, 150, NIGHT, 5 * s)
    P.poly([(x + 30 * s, y + 50 * s), (x - 20 * s, y + 140 * s), (x - 40 * s, y + 50 * s)], WH2)
    if spout > 0:
        for j in range(6):
            a = -math.pi / 2 + (j - 2.5) * .25; r = 140 * s * spout
            P.line([(x + 80 * s, y - 95 * s), (x + 80 * s + math.cos(a) * r, y - 95 * s + math.sin(a) * r)], (220, 240, 255), 10 * s)

def fish(P, x, y, s, t, col=(255, 150, 60)):
    w_ = math.sin(t * 8) * 30 * s
    P.poly([(x - 60 * s, y), (x - 120 * s + w_ * .2, y - 50 * s + w_), (x - 120 * s + w_ * .2, y + 50 * s + w_)], col)
    P.ell(x, y, 80 * s, 45 * s, col); P.circ(x + 45 * s, y - 10 * s, 9 * s, NIGHT)

def SC(i, P, t, u):
    if i == 0:
        sea(P, t); whale(P, 540, CENTER + 120, 1.2, t)
        P.text(820, CENTER - 160, "?", 150 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        sea(P, t); whale(P, 540, CENTER + 120, 1.2, t)
        P.stamp(780, CENTER - 160, "MYTH", seg(u, .25, .7))
        P.badge(540, CENTER + 480, "mammal", 66, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
    elif i == 2:
        sea(P, t)
        k = eio(seg(u, .3, 1.8))
        whale(P, 540, lerp(CENTER + 200, SURF + 60, k), 1.1, t, spout=back(seg(u, 1.8, 2.3)))
        P.badge(540, CENTER + 480, "breathes air", 60, NIGHT, CLOUD, back(seg(u, 2.0, 2.5)))
    elif i == 3:
        sea(P, t); whale(P, 480, CENTER + 60, 1.1, t)
        whale(P, 640, CENTER + 260, .45, t + 1)
        P.heart(760, CENTER - 140, 50 * back(seg(u, .8, 1.3)), HOOK)
        P.badge(540, CENTER + 480, "milk + warm blood", 56, NIGHT, CLOUD, back(seg(u, 1.6, 2.1)))
    elif i == 4:
        sea(P, t)
        whale(P, 480, CENTER - 20, .9, t, tail_up=math.sin(t * 3))
        P.line([(130, CENTER - 100), (130, CENTER + 60)], GLIM, 10); P.badge(130, CENTER - 170, "up-down", 42, GLIM, NIGHT, 1.)
        fish(P, 560, CENTER + 330, 1.2, t)
        P.line([(330, CENTER + 330), (430, CENTER + 330)], HOOK, 10); P.badge(380, CENTER + 420, "side-side", 42, HOOK, CLOUD, 1.)
    else:
        sea(P, t); whale(P, 480, CENTER + 120, 1.1, t, spout=.8)
        P.stamp(780, CENTER - 230, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
