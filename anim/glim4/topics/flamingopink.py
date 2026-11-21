# Thema: Are flamingos born pink?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6) – Figur flamingo/lake aus flamingoleg.py
CENTER = 1050
exec(open(os.path.join(HERE, "topics", "flamingoleg.py")).read(), globals())
PAL = ((110, 180, 225), (250, 200, 185))
HI = {"pink?", "myth!", "gray", "white.", "carotenoids,", "algae", "shrimp", "years", "fade", "eats!"}
WOW = (1,)
_P0 = (PINK, PINK2)

def fl(P, x, y, s, t, k=1., **kw):
    """Flamingo mit Farbe k (0 = weiß/blass, 1 = kräftig pink)."""
    global PINK, PINK2
    PINK, PINK2 = lc((240, 236, 232), _P0[0], k), lc((205, 200, 198), _P0[1], k)
    flamingo(P, x, y, s, t, **kw); PINK, PINK2 = _P0

def chick(P, x, y, s, t, col=(170, 170, 175)):
    b = math.sin(t * 6) * 4 * s
    P.line([(x - 15 * s, y - 40 * s), (x - 15 * s, y)], (60, 60, 70), 8 * s); P.line([(x + 15 * s, y - 40 * s), (x + 15 * s, y)], (60, 60, 70), 8 * s)
    P.circ(x, y - 90 * s + b, 65 * s, col)
    P.circ(x + 45 * s, y - 170 * s + b, 42 * s, col)
    P.poly([(x + 80 * s, y - 175 * s + b), (x + 120 * s, y - 160 * s + b), (x + 82 * s, y - 150 * s + b)], (40, 40, 45))
    P.circ(x + 55 * s, y - 180 * s + b, 7 * s, NIGHT)

def shrimp(P, x, y, s, col=(255, 120, 110)):
    for j in range(5): P.circ(x + j * 18 * s, y - math.sin(j * .7) * 20 * s, (16 - j * 2) * s, col)
    P.line([(x - 10 * s, y), (x - 40 * s, y - 30 * s)], col, 3 * s)

def SC(i, P, t, u):
    if i == 0:
        lake(P, t); fl(P, 380, GROUND + 20, 1.0, t, one=0.)
        chick(P, 760, GROUND + 20, 1.0, t, col=(250, 150, 170))
        P.text(760, CENTER - 160, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        lake(P, t); chick(P, 520, GROUND + 30, 1.6, t)
        P.stamp(780, CENTER - 230, "MYTH", seg(u, .25, .7))
        P.badge(540, CENTER + 520, "born gray!", 62, NIGHT, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 2:
        lake(P, t)
        for j in range(6):
            q = (u * .25 + j / 6) % 1
            shrimp(P, 160 + j * 150, GROUND + 120 + math.sin(t * 2 + j) * 20, 1.2)
        for j in range(8):
            P.circ(120 + j * 120, GROUND + 260 + (j % 2) * 30, 14, (110, 190, 90))
        fl(P, 540, GROUND + 20, 1.1, t, k=eio(seg(u, 1., 5.)), one=0., lean=1.)
        P.badge(540, CENTER + 560, "carotenoids", 60, HOOK, CLOUD, back(seg(u, .6, 1.1)))
    elif i == 3:
        lake(P, t)
        for j, (k, lab) in enumerate(((.0, "0"), (.4, "1"), (.75, "2"), (1., "3"))):
            x = 170 + j * 245
            if j == 0: chick(P, x, GROUND + 20, .8, t)
            else: fl(P, x, GROUND + 20, .55, t, k=k * back(seg(u, .3 + j * .5, .8 + j * .5)), one=0.)
            P.badge(x, GROUND + 130, lab, 44, NIGHT, CLOUD, back(seg(u, .2 + j * .5, .6 + j * .5)))
        P.badge(540, GROUND + 260, "years", 54, NIGHT, GLIM, back(seg(u, 2.2, 2.7)))
    elif i == 4:
        lake(P, t); fl(P, 540, GROUND + 20, 1.2, t, k=1 - eio(seg(u, .5, 3.5)), one=1.)
        shrimp(P, 810, CENTER - 200, 1.3); P.cross(850, CENTER - 210, 70, k=back(seg(u, .3, .8)))
    else:
        lake(P, t); fl(P, 380, GROUND + 20, 1.0, t, one=1.)
        for j in range(3): shrimp(P, 720 + j * 70, CENTER + 120 - j * 50, 1.1)
        P.stamp(620, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
