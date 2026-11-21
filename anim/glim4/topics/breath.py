# Thema: Why can you see your breath when it's cold?  (Wissensformat, Stempel NOT AIR in Satz 2, FACT in Satz 6)
CENTER = 1050
PAL = ((60, 90, 150), (170, 200, 235))
HI = {"breath", "cold?", "cloud", "water!", "warm", "invisible", "vapor.", "dew", "point.", "droplets,", "mini", "clouds?"}
WOW = (1, 4)
SKINC, HAT, SCARF = (240, 200, 165), (220, 70, 80), (60, 150, 200)
SNOW = (242, 247, 252)

def snowy(P, t, y=CENTER + 330):
    P.rrect(-20, y, W + 20, H + 50, 0, SNOW)
    for j in range(25): P.circ((j * 131 + t * 25) % W, (j * 197 + t * 70) % 1000 + CENTER - 650, 5 + j % 3, (255, 255, 255))

def face(P, x, y, s, t, blow=0.):
    P.rrect(x - 150 * s, y + 120 * s, x + 150 * s, y + 420 * s, 80 * s, (90, 110, 160))
    P.circ(x, y, 140 * s, SKINC)
    P.d.chord([*P.c.p(x - 150 * s, y - 170 * s), *P.c.p(x + 150 * s, y + 80 * s)], 180, 360, fill=HAT)
    P.rrect(x - 155 * s, y - 60 * s, x + 155 * s, y - 20 * s, 20 * s, CLOUD); P.circ(x, y - 175 * s, 30 * s, CLOUD)
    P.rrect(x - 130 * s, y + 110 * s, x + 130 * s, y + 160 * s, 25 * s, SCARF)
    for ex in (-50, 50): P.circ(x + ex * s, y + 10 * s, 13 * s, NIGHT)
    for ex in (-80, 80): P.ell(x + ex * s, y + 50 * s, 20 * s, 12 * s, (250, 150, 140))
    P.ell(x + 60 * s, y + 75 * s, (14 + 10 * blow) * s, (12 + 14 * blow) * s, (150, 60, 60))

def puff(P, x, y, k, t, col=(245, 248, 255)):
    for j in range(7):
        q = clamp(k * 1.3 - j * .08)
        if q <= 0: continue
        P.circ(x + j * 55 * q + math.sin(t + j) * 8, y - j * 18 * q, (25 + j * 9) * q, col)

def SC(i, P, t, u):
    if i == 0:
        snowy(P, t); face(P, 360, CENTER + 20, 1.2, t, blow=1.)
        puff(P, 470, CENTER + 100, (u * .6) % 1, t)
        P.text(840, CENTER - 230, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        snowy(P, t); face(P, 300, CENTER + 20, 1.1, t, blow=1.)
        puff(P, 400, CENTER + 100, eout(seg(u, .2, 1.5)), t)
        k = back(seg(u, 1.6, 2.1))
        for j in range(6): P.ell(700 + (j % 3) * 70, CENTER + 60 + (j // 3) * 70, 14 * k, 20 * k, (120, 190, 255))
        P.stamp(700, CENTER - 270, "NOT AIR", seg(u, .25, .7), col=HOOK, rot=-6)
    elif i == 2:
        P.rrect(140, CENTER - 300, 940, CENTER + 300, 80, (250, 200, 160))
        for j in range(18):
            a = j * 2.4 + t * 1.5; r = 80 + (j * 37) % 200
            P.circ(540 + math.cos(a) * r * 1.4, CENTER + math.sin(a) * r, 16, (255, 240, 220))
        P.badge(540, CENTER - 380, "warm + water vapor", 54, HOOK, CLOUD, back(seg(u, .5, 1.0)))
        P.badge(540, CENTER + 400, "invisible gas", 52, NIGHT, CLOUD, back(seg(u, 2.0, 2.5)))
    elif i == 3:
        k = eio(seg(u, .3, 3.0))
        P.rrect(140, CENTER - 300, 940, CENTER + 300, 80, lc((250, 200, 160), (170, 210, 250), k))
        for j in range(18):
            a = j * 2.4 + t * 1.5 * (1 - k * .8); r = 80 + (j * 37) % 200
            P.circ(540 + math.cos(a) * r * 1.4, CENTER + math.sin(a) * r, 16, lc((255, 240, 220), (230, 240, 255), k))
        P.rrect(60, CENTER - 250, 100, CENTER + 250, 20, CLOUD)
        P.rrect(68, CENTER + 242 - 400 * (1 - k * .8), 92, CENTER + 242, 12, lc(HOOK, (80, 140, 255), k))
        P.badge(540, CENTER + 400, "dew point", 58, NIGHT, GLIM, back(seg(u, 2.6, 3.1)))
    elif i == 4:
        snowy(P, t)
        k = eio(seg(u, .3, 2.5))
        for j in range(40):
            a = j * 2.4; r = 40 + (j * 29) % 260
            x = 540 + math.cos(a) * r * 1.3 * (1 - k * .3); y = CENTER - 120 + math.sin(a) * r * .7
            P.circ(x, y, 10 + 14 * k, (240, 245, 255))
        P.badge(540, CENTER + 220, "tiny droplets = cloud", 54, NIGHT, CLOUD, back(seg(u, 1.5, 2.0)))
    else:
        snowy(P, t); face(P, 330, CENTER + 20, 1.1, t, blow=1.)
        puff(P, 430, CENTER + 100, (u * .5) % 1, t)
        P.circ(780, CENTER - 60, 70, (245, 248, 255)); P.circ(850, CENTER - 80, 80, (245, 248, 255)); P.circ(920, CENTER - 50, 60, (245, 248, 255))
        P.stamp(660, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
