# Thema: Do snowshoe hares really turn white in winter?  (Mythos-Format, TRUE in Satz 2, FACT in Satz 6)
CENTER = 1050
BROWN, BROWN2, WHITE, WHITE2 = (150, 110, 70), (120, 85, 55), (250, 250, 252), (215, 222, 235)
SNOW = (242, 247, 252)
PAL = ((70, 110, 160), (180, 205, 230))
HI = {"white", "winter?", "true!", "brand", "new", "shorter", "days", "ten", "weeks,", "brown.", "snowshoes,", "spot!"}
WOW = (1,)

def snow(P, t, y=CENTER + 300):
    P.ell(250, y + 80, 520, 160, (225, 235, 245)); P.ell(830, y + 100, 520, 180, SNOW)
    P.poly([(0, y + 100), (W, y + 90), (W, H), (0, H)], SNOW)

def pine(P, x, y, s, snowy=True):
    P.rrect(x - 14 * s, y, x + 14 * s, y + 80 * s, 6 * s, (100, 70, 45))
    for k in range(3):
        w_ = (140 - k * 35) * s; yy = y - k * 85 * s
        P.poly([(x - w_, yy + 20 * s), (x + w_, yy + 20 * s), (x, yy - 110 * s)], (40, 110, 80))
        if snowy: P.poly([(x - w_ * .5, yy - 30 * s), (x + w_ * .5, yy - 30 * s), (x, yy - 110 * s)], SNOW)

def hare(P, x, y, s, t, k=0., hop=0., patches=None, flip=1):
    """k = 0 braun ... 1 weiß; patches = Anteil weißer Flecken (Fellwechsel)."""
    f = flip; c = lc(BROWN, WHITE, k); c2 = lc(BROWN2, WHITE2, k)
    y = y - abs(math.sin(t * 5)) * 40 * s * hop
    P.ell(x - f * 40 * s, y + 85 * s, 120 * s, 32 * s, c2)                    # Hinterfuß (groß)
    P.ell(x, y, 150 * s, 105 * s, c)                                         # Körper
    P.circ(x - f * 145 * s, y - 20 * s, 34 * s, WHITE)                       # Schwänzchen
    if patches:
        random.seed(5)
        for j in range(int(14 * patches)):
            P.circ(x + (random.random() - .5) * 220 * s, y + (random.random() - .6) * 130 * s, 30 * s, WHITE)
    P.ell(x + f * 70 * s, y + 90 * s, 40 * s, 18 * s, c2)                    # Vorderpfote
    hx, hy = x + f * 120 * s, y - 90 * s
    for dx, a in ((-20, -.25), (15, .1)):                                    # Ohren
        P.ell(hx + f * dx * s + f * a * 60 * s, hy - 120 * s, 22 * s, 75 * s, c)
        P.ell(hx + f * dx * s + f * a * 60 * s, hy - 115 * s, 10 * s, 55 * s, (240, 180, 180) if k < .5 else (235, 220, 225))
    P.circ(hx, hy, 70 * s, c)
    P.ell(hx + f * 50 * s, hy + 15 * s, 30 * s, 25 * s, lc(c, (255, 255, 255), .3))
    P.circ(hx + f * 20 * s, hy - 12 * s, 11 * s, NIGHT); P.circ(hx + f * 24 * s, hy - 16 * s, 4 * s, (255, 255, 255))
    P.circ(hx + f * 72 * s, hy + 8 * s, 8 * s, (200, 110, 110))

def SC(i, P, t, u):
    if i == 0:
        snow(P, t); pine(P, 160, CENTER - 40, 1.0); pine(P, 930, CENTER, .8)
        hare(P, 520, CENTER + 280, 1.2, t, k=0., hop=1.)
        P.text(770, CENTER - 40, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        snow(P, t); pine(P, 930, CENTER - 20, .8)
        hare(P, 500, CENTER + 260, 1.35, t, k=0., patches=eio(seg(u, .5, 3.5)))
        P.stamp(780, CENTER - 230, "TRUE", seg(u, .25, .7), col=HOPE, rot=-6)
        P.badge(540, CENTER + 560, "new white coat", 58, NIGHT, GLIM, back(seg(u, 2.0, 2.5)))
    elif i == 2:
        k = eio(seg(u, .4, 3.0))
        P.circ(540, CENTER - 20, 330, (35, 55, 95))
        P.d.pieslice([*P.c.p(540 - 300, CENTER - 320), *P.c.p(540 + 300, CENTER + 280)], -90, -90 + 360 * lerp(.6, .35, k), fill=(255, 210, 90))
        P.circ(540, CENTER - 20, 60, (255, 210, 90) if k < .5 else (35, 55, 95))
        P.badge(540, CENTER + 400, "shorter days", 60, GLIM, NIGHT, back(seg(u, .6, 1.1)))
        P.badge(170, CENTER + 560, "snow", 46, NIGHT, CLOUD, back(seg(u, 1.6, 2.0))); P.cross(170, CENTER + 560, 60, k=back(seg(u, 2.0, 2.4)))
        P.badge(910, CENTER + 400, "cold", 46, NIGHT, CLOUD, back(seg(u, 1.8, 2.2))); P.cross(910, CENTER + 400, 60, k=back(seg(u, 2.2, 2.6)))
    elif i == 3:
        snow(P, t)
        k = eio(seg(u, .3, 3.0)) - eio(seg(u, 3.3, 5.0))
        hare(P, 520, CENTER + 230, 1.2, t, k=k)
        P.rrect(140, CENTER - 280, 940, CENTER - 210, 35, (60, 70, 90))
        P.rrect(150, CENTER - 270, 150 + 780 * max(.03, k), CENTER - 220, 25, WHITE)
        P.badge(540, CENTER - 140, "about 10 weeks", 56, NIGHT, CLOUD, back(seg(u, .5, 1.0)))
    elif i == 4:
        snow(P, t, CENTER + 100)
        for j in range(4):
            x = 200 + j * 210; P.ell(x, CENTER + 380 + (j % 2) * 40, 40, 85, (205, 215, 230)); P.ell(x + 60, CENTER + 360 + (j % 2) * 40, 20, 26, (205, 215, 230))
        hare(P, 560, CENTER + 100, 1.25, t, k=1.)
        P.ell(480, CENTER + 200, 140 * (1 + .1 * math.sin(t * 4)), 40, (255, 230, 120), outline=GLIM, w=6)
        P.badge(540, CENTER - 250, "built-in snowshoes", 58, NIGHT, GLIM, back(seg(u, .8, 1.3)))
    else:
        snow(P, t); pine(P, 150, CENTER - 20, 1.0); pine(P, 940, CENTER + 10, .9)
        hare(P, 560, CENTER + 330, 1.0, t, k=1.)
        P.stamp(560, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
