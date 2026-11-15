# Thema: Is a starfish really a fish?  (Mythos-Format)
CENTER = 1050
STAR_C, STAR_D = (255, 130, 80), (220, 90, 60)
PAL = ((15, 90, 130), (30, 140, 150))
HI = {"fish?", "gills,", "fins", "backbone.", "echinoderms,", "urchins", "seawater", "tube", "feet.", "eye", "regrow", "star!"}
WOW = (1, 4)
FLOOR = CENTER + 300

def sea(P, t):
    P.poly([(0, FLOOR), (W, FLOOR - 30), (W, H), (0, H)], (225, 200, 150))
    for x in (130, 950):
        for k in range(3): P.line([(x + k * 25, FLOOR), (x + k * 25 + math.sin(t * 1.5 + k) * 25, FLOOR - 180 - k * 40)], (60, 160, 110), 14)
    for k in range(5):
        q = (t * .3 + k / 5) % 1; P.circ(200 + k * 170, lerp(FLOOR, CENTER - 600, q), 7 + k % 3 * 4, (170, 220, 240))

def seastar(P, x, y, r, t, rot=0., col=STAR_C, missing=-1, regrow=1., eyes=False):
    pts = []
    for k in range(10):
        a = rot + k * math.pi / 5 - math.pi / 2
        rr = r if k % 2 == 0 else r * .42
        if k == missing * 2: rr = r * (.42 + .58 * regrow)
        pts.append((x + math.cos(a) * rr, y + math.sin(a) * rr))
    P.poly(pts, col)
    for k in range(5):
        a = rot + k * 2 * math.pi / 5 - math.pi / 2
        for j in range(1, 4): P.circ(x + math.cos(a) * r * j * .2, y + math.sin(a) * r * j * .2, r * .045, lc(col, (255, 255, 255), .35))
        if eyes: P.circ(x + math.cos(a) * r * .93, y + math.sin(a) * r * .93, r * .06, HOOK, glow=(120, 40, 20))
    P.circ(x - r * .12, y - r * .08, r * .06, NIGHT); P.circ(x + r * .12, y - r * .08, r * .06, NIGHT)
    P.arc(x, y + r * .04, r * .12, 20, 160, NIGHT, max(3, r * .025))

def fish(P, x, y, s, t):
    P.poly([(x + 90 * s, y), (x + 150 * s, y - 50 * s + math.sin(t * 8) * 10), (x + 150 * s, y + 50 * s)], (90, 170, 230))
    P.ell(x, y, 100 * s, 55 * s, (120, 190, 240)); P.circ(x - 55 * s, y - 10 * s, 9 * s, NIGHT)

def urchin(P, x, y, r, t):
    for k in range(18):
        a = k / 18 * 6.28 + math.sin(t + k) * .05; P.line([(x, y), (x + math.cos(a) * r * 1.6, y + math.sin(a) * r * 1.6)], (90, 50, 120), 6)
    P.circ(x, y, r, (120, 70, 150))

def SC(i, P, t, u):
    if i == 0:
        sea(P, t); seastar(P, 540, FLOOR - 120, 190, t, rot=math.sin(t * .8) * .1)
        fish(P, lerp(1200, -200, (u / 5) % 1), CENTER - 300, .9, t)
        P.text(820, CENTER - 160, "?", 140 * back(seg(u, .4, .9)), GLIM)
    elif i == 1:
        sea(P, t); seastar(P, 540, FLOOR - 120, 180, t)
        for j, lab in enumerate(("gills", "fins", "backbone")):
            k = back(seg(u, .6 + j * .45, 1.0 + j * .45)); y = CENTER - 220 + j * 110
            P.badge(460, y, lab, 50, NIGHT, CLOUD, k); P.cross(700, y, 34, k=k)
        P.stamp(540, CENTER - 430, "MYTH", seg(u, .25, .7))
    elif i == 2:
        sea(P, t); seastar(P, 540, FLOOR - 160, 150, t)
        urchin(P, 230, FLOOR - 80, 70, t)
        P.ell(860, FLOOR - 60, 110, 40, (235, 220, 190)); 
        for k in range(5):
            a = k / 5 * 6.28 - 1.57; P.ell(860 + math.cos(a) * 45, FLOOR - 60 + math.sin(a) * 15, 14, 6, (200, 180, 150))
        P.badge(540, CENTER - 330, "echinoderms", 62, NIGHT, GLIM, back(seg(u, .4, .9)))
        P.text(230, FLOOR + 60, "urchin", 42, CLOUD); P.text(860, FLOOR + 60, "sand dollar", 42, CLOUD)
    elif i == 3:
        sea(P, t)
        P.rrect(140, CENTER - 300, 940, CENTER + 120, 50, (20, 50, 80), outline=GLIM, w=8)
        P.line([(170, CENTER - 120), (910, CENTER - 120)], (120, 200, 240), 30)
        for k in range(8):
            q = (t * .5 + k / 8) % 1; P.circ(lerp(180, 900, q), CENTER - 120, 10, (220, 245, 255))
        for k in range(10):
            x = 200 + k * 75; ext = 40 + 30 * (.5 + .5 * math.sin(t * 4 + k * .8))
            P.line([(x, CENTER - 110), (x, CENTER - 110 + ext + 40)], (255, 170, 130), 18); P.circ(x, CENTER - 50 + ext, 14, (255, 200, 170))
        P.badge(540, CENTER + 240, "seawater + tube feet", 56, NIGHT, GLIM, back(seg(u, .6, 1.1)))
    elif i == 4:
        sea(P, t); rg = eout(seg(u, 2.0, 4.5))
        seastar(P, 540, FLOOR - 160, 200, t, eyes=True, missing=1, regrow=rg)
        P.badge(540, CENTER - 360, "an eye on every arm", 56, NIGHT, GLIM, back(seg(u, .3, .8)))
        P.badge(540, FLOOR + 120, "arms grow back", 56, HOPE, CLOUD, back(seg(u, 2.0, 2.5)))
    else:
        sea(P, t); seastar(P, 520, FLOOR - 140, 170, t, rot=math.sin(t * 2) * .12)
        P.badge(520, CENTER - 230, "sea star", 66, HOPE, CLOUD, back(seg(u, 1.0, 1.5)))
        P.stamp(540, CENTER - 430, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
