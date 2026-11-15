# Thema: What are cat whiskers really for?
CENTER = 1050
FUR, FUR2, PINK = (235, 150, 80), (190, 105, 50), (245, 170, 180)
PAL = ((255, 225, 190), (250, 190, 170))
HI = {"whiskers", "nerves.", "tiniest", "touch,", "air", "wide", "body,", "gap", "mood,", "curious,", "scared.", "legs!"}
WOW = (3, 5)

def cathead(P, x, y, s, t, wh=0., col=FUR, glowwh=False, happy=False):
    """Katzenkopf frontal; wh = Schnurrhaar-Winkel (+ nach vorn, - nach hinten)."""
    c2 = col if col == FUR2 else FUR2
    for d in (-1, 1):
        P.poly([(x + d * 150 * s, y - 40 * s), (x + d * 140 * s, y - 200 * s), (x + d * 50 * s, y - 140 * s)], col, outline=c2, w=5 * s)
        P.poly([(x + d * 125 * s, y - 70 * s), (x + d * 122 * s, y - 165 * s), (x + d * 75 * s, y - 135 * s)], PINK)
    P.ell(x, y, 170 * s, 140 * s, col, outline=c2, w=6 * s)
    for k in (-1, 0, 1): P.line([(x + k * 30 * s, y - 135 * s), (x + k * 30 * s, y - 95 * s)], c2, 10 * s)
    for d in (-1, 1):
        if happy: P.arc(x + d * 62 * s, y - 15 * s, 26 * s, 200, 340, NIGHT, 8 * s)
        else:
            P.ell(x + d * 62 * s, y - 15 * s, 30 * s, 36 * s, (170, 210, 90)); P.ell(x + d * 62 * s, y - 15 * s, 9 * s, 30 * s, NIGHT)
            P.circ(x + d * 62 * s + 10 * s, y - 28 * s, 7 * s, CLOUD)
    P.ell(x, y + 50 * s, 70 * s, 45 * s, lc(col, CLOUD, .55))
    P.poly([(x - 18 * s, y + 25 * s), (x + 18 * s, y + 25 * s), (x, y + 45 * s)], PINK)
    P.arc(x - 16 * s, y + 55 * s, 16 * s, 0, 150, NIGHT, 5 * s); P.arc(x + 16 * s, y + 55 * s, 16 * s, 30, 180, NIGHT, 5 * s)
    for d in (-1, 1):
        for k in (-1, 0, 1):
            ang = math.radians(k * 12 + wh * 25 + math.sin(t * 3 + k) * 2)
            x0, y0 = x + d * 50 * s, y + 40 * s + k * 14 * s
            x1, y1 = x0 + d * 240 * s * math.cos(ang), y0 - 240 * s * math.sin(ang) * 1
            P.line([(x0, y0), (x1, y1)], GLIM if glowwh else CLOUD, (7 if glowwh else 5) * s, glow=(GLIM if glowwh else None))
            P.circ(x0, y0, 6 * s, c2)

def sidecat(P, x, y, s, t, walk=0.):
    """Katze seitlich (nach rechts)."""
    for k, dx in enumerate((-110, -60, 70, 120)):
        o = math.sin(t * 7 + k * 3.1) * 20 * s * walk
        P.rrect(x + dx * s - 20 * s + o, y + 30 * s, x + dx * s + 20 * s + o, y + 150 * s, 18 * s, FUR2 if k % 2 else FUR)
    P.ell(x, y + 20 * s, 170 * s, 80 * s, FUR, outline=FUR2, w=5 * s)
    P.line([(x - 160 * s, y), (x - 240 * s, y - 80 * s + math.sin(t * 2) * 15 * s), (x - 220 * s, y - 160 * s)], FUR2, 22 * s)
    hx, hy = x + 170 * s, y - 50 * s
    for d in (-1, 1): P.poly([(hx + d * 50 * s, hy - 40 * s), (hx + d * 45 * s, hy - 110 * s), (hx + d * 5 * s, hy - 70 * s)], FUR, outline=FUR2, w=4 * s)
    P.ell(hx, hy, 80 * s, 68 * s, FUR, outline=FUR2, w=5 * s)
    P.ell(hx + 30 * s, hy - 10 * s, 12 * s, 16 * s, NIGHT)
    P.circ(hx + 70 * s, hy + 15 * s, 10 * s, PINK)
    for k in (-1, 0, 1): P.line([(hx + 60 * s, hy + 25 * s), (hx + 190 * s, hy + 25 * s + k * 30 * s)], CLOUD, 4 * s)

def SC(i, P, t, u):
    P.rrect(-20, CENTER + 330, W + 20, H + 20, 0, lc(PAL[1], NIGHT, .15))
    if i == 0:
        cathead(P, 540, CENTER + 60, 1.25, t, math.sin(t * 2) * .3)
        P.text(880, CENTER - 290, "?", 150 * back(seg(u, .4, .9)), HOOK)
    elif i == 1:
        k = eout(seg(u, .2, 1.2))
        P.rrect(140, CENTER - 200, 940, CENTER + 300, 40, (250, 205, 190), outline=(210, 150, 140), w=6)
        P.rrect(140, CENTER - 200, 940, CENTER - 120, 30, FUR)
        P.line([(540, CENTER - 420), (540, CENTER + 120)], CLOUD, 16)
        P.ell(540, CENTER + 150, 50, 80, (255, 235, 220), outline=(210, 150, 140), w=5)
        for j in range(8):
            a = j / 8 * 6.283 + t * .5
            x1, y1 = 540 + math.cos(a) * 230 * k, CENTER + 150 + math.sin(a) * 120 * k
            P.line([(540, CENTER + 150), (x1, y1)], HOOK, 7, glow=HOOK)
            P.circ(x1, y1, 12 * k, HOOK, glow=HOOK)
        P.badge(540, CENTER + 410, "lots of nerves", 60, NIGHT, GLIM, back(seg(u, 1.3, 1.8)))
    elif i == 2:
        cathead(P, 540, CENTER + 120, 1.1, t, 0, glowwh=True)
        for j in range(6):
            q = (t * .7 + j / 6) % 1
            y = CENTER - 120 + j * 50
            P.line([(lerp(60, 1020, q) - 80, y), (lerp(60, 1020, q), y)], (255, 255, 255), 6)
        P.badge(540, CENTER + 410, "feels the air", 60, HOPE, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 3:
        gap = 380 + 60 * math.sin(u * 1.2)
        P.rrect(560, CENTER - 260, 1100, CENTER - 20 - gap / 2 + 100, 0, (150, 110, 90))
        P.rrect(560, CENTER + 120 + gap / 2 - 100, 1100, CENTER + 330, 0, (150, 110, 90))
        sidecat(P, 320, CENTER + 120, .95, t)
        hx = 320 + 170 * .95
        P.line([(hx + 120, CENTER - 60), (hx + 120, CENTER + 120)], GLIM, 6)
        P.badge(540, CENTER + 420, "whiskers = body width", 52, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
    elif i == 4:
        fwd = u < 2.6
        cathead(P, 300, CENTER + 80, .8, t, .8 if True else 0)
        cathead(P, 780, CENTER + 80, .8, t, -1.2)
        P.badge(300, CENTER + 330, "curious", 50, HOPE, CLOUD, back(seg(u, .6, 1.1)))
        P.badge(780, CENTER + 330, "scared", 50, HOOK, CLOUD, back(seg(u, 2.2, 2.7)))
    else:
        sidecat(P, 460, CENTER + 60, 1.1, t)
        for x in (460 + 70 * 1.1, 460 + 120 * 1.1):
            for k in (-1, 0, 1): P.line([(x + 18, CENTER + 60 + 90), (x + 70, CENTER + 60 + 60 + k * 25)], GLIM, 5)
        P.arc(460 + 105 * 1.1, CENTER + 145, 90, 0, 360, HOOK, 8 * seg(u, .8, 1.2))
        P.badge(540, CENTER - 330, "leg whiskers!", 60, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
