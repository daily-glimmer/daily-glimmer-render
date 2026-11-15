# Thema: Why do skunks smell so bad?
CENTER = 1050
BK, WH = (40, 40, 50), (245, 245, 240)
STINK = (170, 200, 80)
PAL = ((220, 235, 205), (190, 215, 190))
HI = {"skunks", "smell", "bad?", "glands", "tail.", "sulfur", "thiols,", "tiny", "warn", "hiss,", "stamp", "three", "meters", "ten", "days,"}
WOW = (2, 4)

def skunk(P, x, y, s, t, tail=0., hand=False, stamp=0., flip=1):
    """Stinktier seitlich nach rechts; tail 0..1 = Schwanz hoch."""
    f = flip
    for k, dx in enumerate((-90, -50, 70, 105)):
        lift = (abs(math.sin(t * 10)) * 25 * s * stamp) if k >= 2 else 0
        P.rrect(x + f * dx * s - 16 * s, y + 30 * s - lift, x + f * dx * s + 16 * s, y + 110 * s - lift, 14 * s, BK)
    a = math.radians(lerp(160, 95, tail))
    bx, by = x - f * 130 * s, y - 10 * s
    tx, ty = bx + f * math.cos(a) * 170 * s, by - math.sin(a) * 170 * s
    P.line([(bx, by), (tx, ty)], BK, 70 * s)
    P.ell(tx, ty, 70 * s, 90 * s, BK); P.ell(tx, ty, 30 * s, 60 * s, WH)
    P.ell(x, y, 160 * s, 80 * s, BK)
    P.ell(x, y - 55 * s, 140 * s, 22 * s, WH)
    hx, hy = x + f * 160 * s, y - 20 * s
    P.ell(hx, hy, 70 * s, 55 * s, BK)
    P.poly([(hx + f * 50 * s, hy - 20 * s), (hx + f * 120 * s, hy + 15 * s), (hx + f * 50 * s, hy + 35 * s)], BK)
    P.line([(hx - f * 30 * s, hy - 50 * s), (hx + f * 70 * s, hy + 5 * s)], WH, 14 * s)
    P.circ(hx + f * 120 * s, hy + 15 * s, 10 * s, (60, 50, 60))
    P.circ(hx + f * 25 * s, hy - 10 * s, 9 * s, CLOUD); P.circ(hx + f * 27 * s, hy - 10 * s, 5 * s, NIGHT)
    for d in (-1, 1): P.circ(hx - f * 20 * s + d * 18 * s, hy - 52 * s, 16 * s, BK)

def cloudpuff(P, x, y, r, k, t):
    for j in range(6):
        a = j / 6 * 6.283 + t * .4
        P.circ(x + math.cos(a) * r * .55 * k, y + math.sin(a) * r * .4 * k, r * .45 * k, STINK)
    P.circ(x, y, r * .5 * k, lc(STINK, CLOUD, .3))

def SC(i, P, t, u):
    P.rrect(-20, CENTER + 330, W + 20, H + 20, 0, (120, 170, 100))
    if i == 0:
        skunk(P, 500, CENTER + 200, 1.15, t, tail=.3)
        for j in range(3): cloudpuff(P, 220 + j * 60, CENTER - 40 - j * 90, 80, back(seg(u, .3 + j * .2, .8 + j * .2)), t)
        P.text(880, CENTER - 290, "?", 150 * back(seg(u, .4, .9)), HOOK)
    elif i == 1:
        skunk(P, 600, CENTER + 200, 1.15, t, tail=1.)
        bx = 600 - 130 * 1.15
        for d in (-1, 1): P.circ(bx + d * 30, CENTER + 230, 26 * back(seg(u, .6, 1.0)), STINK, outline=(110, 140, 40), w=5)
        P.arc(bx, CENTER + 230, 90, 0, 360, GLIM, 8 * seg(u, .9, 1.3))
        P.badge(540, CENTER + 420, "2 scent glands", 60, NIGHT, GLIM, back(seg(u, 1.2, 1.7)))
    elif i == 2:
        k = eout(seg(u, .2, 1.4))
        for j, (x, y) in enumerate(((330, CENTER - 60), (750, CENTER - 20), (540, CENTER + 180))):
            P.circ(x, y, 90 * k, (250, 220, 70), outline=(190, 150, 30), w=6)
            P.text(x, y, "S", 80 * k, NIGHT)
            P.line([(x, y), (540, CENTER + 40)], STINK, 10 * k)
        P.badge(540, CENTER + 420, "thiols", 64, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
    elif i == 3:
        skunk(P, 520, CENTER + 200, 1.1, t, tail=eout(seg(u, 2.2, 3.0)), stamp=1. if 1.2 < u < 2.4 else 0)
        P.badge(300, CENTER - 160, "hiss!", 50, HOOK, CLOUD, back(seg(u, .5, .9)))
        P.badge(540, CENTER - 60, "stamp!", 50, HOOK, CLOUD, back(seg(u, 1.2, 1.6)))
        P.badge(800, CENTER - 160, "tail up!", 50, HOOK, CLOUD, back(seg(u, 2.2, 2.6)))
        P.badge(540, CENTER + 420, "warning first", 60, NIGHT, GLIM, back(seg(u, .3, .8)))
    elif i == 4:
        skunk(P, 760, CENTER + 200, .9, t, tail=1., flip=-1)
        k = eout(seg(u, .3, 1.3))
        for j in range(8):
            q = j / 8
            P.circ(lerp(860, 160, q * k), CENTER + 40 - math.sin(q * math.pi) * 120 * k, 26 + 10 * q, STINK)
        P.line([(160, CENTER + 300), (860, CENTER + 300)], NIGHT, 6 * seg(u, 1.2, 1.4))
        P.badge(510, CENTER + 420, "up to 3 m", 64, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
    else:
        skunk(P, 400, CENTER + 220, .9, t, tail=.4)
        P.rrect(840, CENTER - 60, 980, CENTER + 260, 30, CLOUD, outline=NIGHT, w=6)
        lvl = clamp((u % 4) / 4)
        P.rrect(855, CENTER + 245 - 290 * lvl, 965, CENTER + 245, 22, STINK)
        P.badge(540, CENTER - 330, "refill: ~10 days", 56, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
