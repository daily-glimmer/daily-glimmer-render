# Thema: Do snakes really unhinge their jaws?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6)
# Quellen: Natural History Museum London "Snakes: senses, stretchy jaws and deadly venom" (kein Aushaken, sehr dehnbar),
# Live Science "How Do Snakes Swallow Large Animals?" (Unterkieferhälften vorn per elastischem Band verbunden,
# beweglicher Quadratknochen), JSTOR Daily "How Snakes Swallow".
exec(open(os.path.join(HERE, "topics", "snakeears.py")).read(), globals())   # snake(), sand(), SN, SN2
CENTER = 1050
PAL = ((200, 170, 110), (235, 215, 160))
HI = {"unhinge", "jaws?", "myth!", "stretchy.", "two", "halves,", "elastic", "band.", "extra", "joint", "walk", "jaws", "stretch!"}
WOW = (1,)
BONEC, LIG = (245, 240, 225), (240, 130, 150)

def egg(P, x, y, r): P.ell(x, y, r * .8, r, (250, 245, 235)); P.ell(x - r * .25, y - r * .35, r * .2, r * .15, (255, 255, 255))

def skull(P, x, y, s, spread=0., drop=0.):
    """Schlangenschädel von unten/vorn: zwei Unterkieferhälften, vorn per Band verbunden."""
    P.ell(x, y - 120 * s, 150 * s, 90 * s, BONEC)
    for d in (-1, 1):
        qx, qy = x + d * 140 * s, y - 120 * s
        jx, jy = qx + d * 20 * s, qy + (60 + 80 * drop) * s
        P.line([(qx, qy), (jx, jy)], (225, 215, 190), 22 * s)   # Quadratknochen
        tipx = x + d * (12 + 110 * spread) * s; tipy = y + 200 * s
        P.line([(jx, jy), (tipx, tipy)], BONEC, 26 * s)
        P.circ(jx, jy, 16 * s, (210, 200, 175))
    P.line([(x - (12 + 110 * spread) * s, y + 200 * s), (x + (12 + 110 * spread) * s, y + 200 * s)], LIG, 14 * s)

def SC(i, P, t, u):
    if i == 0:
        sand(P, t); snake(P, 520, CENTER + 260, 1.1, t, head_up=.4)
        egg(P, 860, CENTER + 230, 70)
        P.text(800, CENTER - 230, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        skull(P, 540, CENTER - 40, 1.3, spread=.2 + .2 * math.sin(t * 2))
        P.stamp(760, CENTER - 380, "MYTH", seg(u, .25, .7), rot=-6)
        P.badge(540, CENTER + 420, "no dislocating", 58, NIGHT, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 2:
        k = eio(seg(u, .6, 2.0)) * (1 - .3 * eio(seg(u, 3.0, 3.8)))
        skull(P, 540, CENTER - 40, 1.4, spread=k)
        P.badge(540, CENTER + 400, "two halves + elastic band", 52, LIG, NIGHT, back(seg(u, 1.2, 1.7)))
    elif i == 3:
        k = eio(seg(u, .4, 1.6))
        skull(P, 540, CENTER - 40, 1.4, spread=.6, drop=k)
        P.badge(540, CENTER + 400, "extra joint each side", 54, NIGHT, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 4:
        sand(P, t)
        q = eio(seg(u, .5, 4.5))
        snake(P, 520, CENTER + 260, 1.1, t, head_up=.2, tongue=False)
        P.ell(lerp(640, 360, q), CENTER + 260, lerp(70, 55, q), lerp(56, 75, q), lc((250, 245, 235), (130, 170, 90), q))
        P.badge(540, CENTER - 260, "left, right, left...", 56, NIGHT, CLOUD, back(seg(u, 1.0, 1.5)))
    else:
        sand(P, t); snake(P, 460, CENTER + 260, 1.0, t, head_up=.4)
        P.stamp(780, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
