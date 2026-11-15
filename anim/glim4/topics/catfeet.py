# Thema: How do cats land on their feet?
CENTER = 1050
FUR, FUR2, PINK = (240, 150, 70), (200, 110, 50), (250, 170, 170)
PAL = ((160, 200, 240), (250, 220, 190))
HI = {"feet?", "righting", "reflex,", "kittens", "weeks", "inner", "ear", "up,", "twists", "front", "back", "flexible", "spine", "collarbone", "spread", "safe!"}
WOW = (1, 3, 4)

def kitty(P, x, y, s, t, front=0., back_=0., legs=0.):
    """Katze von der Seite; front/back = Drehung (0 = Rücken unten, 1 = Füße unten)."""
    def leg(px, py, flip):
        d = 1 if flip < .5 else -1
        ln = 70 + 30 * legs
        P.line([(px, py), (px + (20 * legs * (1 if px > x else -1)) * s, py + d * ln * s)], FUR2, 22 * s)
        P.circ(px + (20 * legs * (1 if px > x else -1)) * s, py + d * ln * s, 14 * s, PINK if flip < .5 else FUR2)
    fb = 1 - front; bb = 1 - back_
    # Hinterteil
    P.ell(x + 70 * s, y, 85 * s, 58 * s, FUR); leg(x + 100 * s, y + (40 if back_ > .5 else -40) * s, bb); leg(x + 60 * s, y + (40 if back_ > .5 else -40) * s, bb)
    P.line([(x + 150 * s, y), (x + 230 * s, y - 60 * s * math.sin(t * 3)), (x + 260 * s, y - 120 * s)], FUR2, 18 * s)
    # Vorderteil
    P.ell(x - 50 * s, y, 85 * s, 60 * s, FUR); leg(x - 80 * s, y + (40 if front > .5 else -40) * s, fb); leg(x - 40 * s, y + (40 if front > .5 else -40) * s, fb)
    hy = y + (-50 if front > .5 else 50) * s
    P.circ(x - 140 * s, hy, 55 * s, FUR)
    ey = -1 if front > .5 else 1
    P.poly([(x - 180 * s, hy + ey * 30 * s), (x - 165 * s, hy + ey * 80 * s), (x - 140 * s, hy + ey * 40 * s)], FUR)
    P.poly([(x - 130 * s, hy + ey * 35 * s), (x - 105 * s, hy + ey * 75 * s), (x - 100 * s, hy + ey * 25 * s)], FUR)
    for dx in (-158, -122): P.ell(x + dx * s, hy - ey * 5 * s, 8 * s, 12 * s, NIGHT)
    P.circ(x - 140 * s, hy - ey * 22 * s, 6 * s, PINK)
    for k in (-1, 0, 1): P.line([(x - 160 * s, hy - ey * 22 * s), (x - 215 * s, hy - ey * (22 + k * 12) * s)], CLOUD, 2 * s)

def kitten(P, x, y, s, t):
    P.ell(x, y, 70 * s, 50 * s, FUR); P.circ(x - 70 * s, y - 30 * s, 50 * s, FUR)
    P.poly([(x - 110 * s, y - 60 * s), (x - 100 * s, y - 110 * s), (x - 75 * s, y - 75 * s)], FUR)
    P.poly([(x - 60 * s, y - 75 * s), (x - 35 * s, y - 110 * s), (x - 30 * s, y - 60 * s)], FUR)
    for dx in (-88, -52): P.circ(x + dx * s, y - 35 * s, 9 * s, NIGHT)
    P.line([(x + 60 * s, y), (x + 110 * s, y - 50 * s * math.sin(t * 3))], FUR2, 14 * s)

def SC(i, P, t, u):
    if i == 0:
        q = eio(seg(u, .2, 1.8))
        kitty(P, 540, lerp(CENTER - 250, CENTER + 120, q), 1.3, t, front=q, back_=q, legs=q)
        P.rrect(100, CENTER + 270, 980, CENTER + 300, 12, (150, 120, 90))
        P.text(860, CENTER - 300, "?", 150 * back(seg(u, .6, 1.1)), HOOK)
    elif i == 1:
        kitten(P, 540, CENTER + 60, 1.8, t)
        P.badge(540, CENTER - 280, "righting reflex", 62, NIGHT, GLIM, back(seg(u, .5, 1.0)))
        P.badge(540, CENTER + 330, "from ~3-4 weeks", 54, HOPE, CLOUD, back(seg(u, 2.0, 2.5)))
    elif i == 2:
        P.circ(540, CENTER - 20, 230, (250, 210, 190), outline=FUR2, w=10)
        P.arc(540, CENTER - 20, 120, 200, 520, (120, 150, 220), 24)
        q = (t * .7) % 1
        P.circ(540 + math.cos(q * 6.28) * 120, CENTER - 20 + math.sin(q * 6.28) * 120, 22, HOOK)
        P.text(540, CENTER - 20, "UP?", 70, CLOUD)
        P.badge(540, CENTER + 330, "inner ear = balance", 56, NIGHT, GLIM, back(seg(u, .8, 1.3)))
    elif i == 3:
        f = eio(seg(u, .3, 1.4)); b = eio(seg(u, 1.6, 2.8))
        kitty(P, 540, CENTER - 20, 1.6, t, front=f, back_=b)
        P.badge(300, CENTER + 330, "1. front", 56, HOOK, CLOUD, back(seg(u, .5, 1.0)))
        P.badge(780, CENTER + 330, "2. back", 56, HOPE, CLOUD, back(seg(u, 1.8, 2.3)))
    elif i == 4:
        g = math.sin(t * 2.2) * .5
        pts = [(220 + k * 70, CENTER + 40 + math.sin(k * .6 + t * 2) * 60 * (1 + g)) for k in range(10)]
        for (x, y) in pts: P.rrect(x - 28, y - 22, x + 28, y + 22, 10, CLOUD, outline=FUR2, w=4)
        P.cross(540, CENTER - 210, 50, HOOK, back(seg(u, 1.6, 2.0)))
        P.badge(540, CENTER + 280, "flexible spine", 60, NIGHT, GLIM, back(seg(u, .5, 1.0)))
        P.badge(540, CENTER + 400, "no fixed collarbone", 52, HOOK, CLOUD, back(seg(u, 1.8, 2.3)))
    else:
        kitty(P, 540, CENTER + 60, 1.3, t, front=1, back_=1, legs=eio(seg(u, .3, 1.0)))
        P.rrect(100, CENTER + 230, 980, CENTER + 260, 12, (150, 120, 90))
        P.rrect(360, CENTER - 320, 720, CENTER - 140, 14, (170, 210, 240), outline=CLOUD, w=8)
        P.line([(540, CENTER - 320), (540, CENTER - 140)], CLOUD, 8)
        P.check(540, CENTER - 230, 50, HOPE, back(seg(u, 3.0, 3.5)))
