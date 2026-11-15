# Thema: Why do onions make us cry?
CENTER = 1050
SKIN, FLESH, RING = (200, 120, 70), (245, 230, 210), (220, 200, 175)
GAS = (190, 230, 120)
PAL = ((40, 30, 60), (110, 80, 110))
HI = {"cry?", "two", "chemicals", "trap.", "cuts", "mix,", "enzyme", "gas.", "eyes,", "tears.", "defense", "chill", "sharp"}
WOW = (2, 3)

def onion(P, x, y, s, half=False):
    if half:
        P.ell(x, y, 150 * s, 130 * s, SKIN)
        for k in range(5): P.ell(x, y + 8 * k * s, (138 - k * 26) * s, (118 - k * 23) * s, FLESH if k % 2 == 0 else RING)
        return
    P.ell(x, y, 150 * s, 135 * s, SKIN, outline=lc(SKIN, (0, 0, 0), .3), w=4 * s)
    P.poly([(x - 30 * s, y - 120 * s), (x + 30 * s, y - 120 * s), (x, y - 200 * s)], SKIN)
    for dx in (-70, 0, 70): P.arc(x + dx * s * .3, y, 120 * s, 250 + dx * .2, 290 + dx * .2, lc(SKIN, (0, 0, 0), .25), 4 * s)
    for k in range(5): P.line([(x - 20 * s + k * 10 * s, y + 132 * s), (x - 30 * s + k * 15 * s, y + 160 * s)], (150, 120, 90), 3 * s)

def knife(P, x, y, s, a=0.):
    P.poly([(x, y), (x + 320 * s, y - 10 * s), (x + 320 * s, y + 50 * s), (x + 20 * s, y + 50 * s)], (210, 215, 225), outline=(130, 135, 150), w=3 * s)
    P.rrect(x + 320 * s, y - 4 * s, x + 470 * s, y + 46 * s, 18 * s, (90, 60, 40))

def eye(P, x, y, s, tear=0., t=0.):
    P.ell(x, y, 120 * s, 70 * s, CLOUD, outline=NIGHT, w=6 * s)
    P.circ(x, y, 42 * s, (90, 140, 200)); P.circ(x, y, 20 * s, NIGHT); P.circ(x + 10 * s, y - 10 * s, 7 * s, CLOUD)
    if tear > 0:
        for k in range(3):
            q = (t * .9 + k / 3) % 1
            ty = y + 70 * s + q * 260 * s * tear
            P.circ(x + 90 * s, ty, 20 * s * tear, (120, 190, 255)); P.poly([(x + 72 * s, ty - 4 * s), (x + 108 * s, ty - 4 * s), (x + 90 * s, ty - 40 * s)], (120, 190, 255))

def cloud(P, x, y, r, a=1.):
    for dx, dy, k in ((-1, 0, 1), (0, -.5, 1.2), (1, 0, 1), (0, .3, 1.1)): P.circ(x + dx * r * .8, y + dy * r * .6, r * k * a, GAS)

def SC(i, P, t, u):
    if i == 0:
        onion(P, 540, CENTER + 20, 1.6)
        P.text(820, CENTER - 250, "?", 150 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        P.circ(540, CENTER - 20, 280, (250, 240, 225), outline=RING, w=10)
        for k, (dx, col, lab) in enumerate(((-130, (120, 170, 240), "A"), (130, (240, 140, 120), "B"))):
            q = back(seg(u, .3 + k * .4, .8 + k * .4))
            P.circ(540 + dx, CENTER - 20 + math.sin(t * 2 + k) * 10, 80 * q, col)
            P.text(540 + dx, CENTER - 20, lab, 70 * q, CLOUD)
        P.line([(540, CENTER - 240), (540, CENTER + 200)], (190, 170, 150), 10)
        P.badge(540, CENTER + 360, "kept apart", 60, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
    elif i == 2:
        cut = eio(seg(u, .2, 1.0))
        onion(P, 540, CENTER + 120, 1.2, half=cut > .5)
        knife(P, lerp(380, 300, cut), lerp(CENTER - 260, CENTER + 60, cut), .9)
        if cut > .5:
            g = eio(seg(u, 1.2, 3.0))
            for k in range(3): cloud(P, 380 + k * 160, CENTER - 120 - k * 50 * g, 60 * g, 1)
            P.badge(540, CENTER + 360, "irritating gas", 60, HOOK, CLOUD, back(seg(u, 1.8, 2.3)))
    elif i == 3:
        g = eio(seg(u, .2, 1.4))
        cloud(P, 540, lerp(CENTER + 300, CENTER + 120, g), 70)
        eye(P, 400, CENTER - 160, 1.1, tear=eio(seg(u, 1.2, 2.0)), t=t)
        eye(P, 690, CENTER - 160, 1.1, tear=eio(seg(u, 1.3, 2.1)), t=t + .3)
        P.badge(540, CENTER + 400, "tears wash it out", 56, NIGHT, GLIM, back(seg(u, 1.8, 2.3)))
    elif i == 4:
        onion(P, 540, CENTER + 60, 1.4)
        P.arc(540, CENTER + 60, 290, 200, 340, HOPE, 16)
        P.badge(540, CENTER - 300, "self-defense!", 64, HOPE, CLOUD, back(seg(u, .5, 1.0)))
    else:
        P.rrect(250, CENTER - 140, 830, CENTER + 220, 40, (170, 210, 240), outline=(120, 160, 200), w=6)   # Kühlschrank-Fach
        for k in range(6):
            a = k * 1.05 + t
            flx, fly = 300 + k * 95, CENTER - 100 + 30 * math.sin(a)
            P.line([(flx - 14, fly), (flx + 14, fly)], CLOUD, 4); P.line([(flx, fly - 14), (flx, fly + 14)], CLOUD, 4)
        onion(P, 540, CENTER + 80, .8)
        P.badge(540, CENTER - 260, "cold + sharp = fewer tears", 50, NIGHT, GLIM, back(seg(u, .8, 1.3)))
