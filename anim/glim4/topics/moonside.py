# Thema: Is there a dark side of the Moon?  (Mythos-Format)
CENTER = 1050
PAL = ((6, 10, 32), (18, 24, 60))
HI = {"dark", "Moon?", "far", "sunlight", "once", "same", "hidden,", "new", "sunshine!", "1959,", "probe."}
WOW = (1, 4)
MOON, CRATER = (205, 205, 210), (170, 170, 178)

def sun(P, x, y, r, t):
    for k in range(12):
        a = k / 12 * 6.28 + t * .2; P.line([(x + math.cos(a) * (r + 15), y + math.sin(a) * (r + 15)), (x + math.cos(a) * (r + 55), y + math.sin(a) * (r + 55))], GLIM, 10)
    P.circ(x, y, r, GLIM)

def earth(P, x, y, r, t):
    P.circ(x, y, r, (40, 110, 190)); P.ell(x - r * .25, y - r * .2, r * .35, r * .25, (90, 170, 100)); P.ell(x + r * .3, y + r * .2, r * .25, r * .3, (90, 170, 100))

def moon(P, x, y, r, lit_dir=None, face=True, mark=False):
    P.circ(x, y, r, MOON)
    for dx, dy, rr in ((-.3, -.3, .18), (.35, .1, .14), (-.05, .4, .12), (.2, -.45, .08)): P.circ(x + dx * r, y + dy * r, rr * r, CRATER)
    if lit_dir is not None:   # Schattenhälfte
        a = lit_dir + math.pi
        pts = [(x + math.cos(a + (k / 20 - .5) * math.pi) * r, y + math.sin(a + (k / 20 - .5) * math.pi) * r) for k in range(21)]
        P.poly(pts, (40, 44, 60))
    if face:
        P.circ(x - r * .2, y - r * .05, r * .06, NIGHT); P.circ(x + r * .2, y - r * .05, r * .06, NIGHT); P.arc(x, y + r * .1, r * .14, 20, 160, NIGHT, max(3, r * .03))
    if mark: P.circ(x + r * .7, y, r * .12, HOOK)

def SC(i, P, t, u):
    if i == 0:
        moon(P, 540, CENTER - 40, 250, lit_dir=0.)
        P.text(820, CENTER - 360, "?", 140 * back(seg(u, .4, .9)), GLIM)
    elif i == 1:
        sun(P, 160, CENTER - 40, 80, t)
        a = t * .6; moon(P, 620, CENTER - 40, 220, face=True)
        P.badge(620, CENTER + 260, "sunlight on both sides", 52, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
        P.stamp(540, CENTER - 360, "MYTH", seg(u, .25, .7))
    elif i == 2:
        earth(P, 540, CENTER - 20, 110, t)
        a = u * .9
        mx, my = 540 + math.cos(a) * 330, CENTER - 20 + math.sin(a) * 330
        P.arc(540, CENTER - 20, 330, 0, 360, (80, 90, 130), 4)
        moon(P, mx, my, 70, face=False)
        fx, fy = mx - math.cos(a) * 50, my - math.sin(a) * 50; P.circ(fx, fy, 14, HOPE)   # Seite zur Erde
        P.badge(540, CENTER + 400, "1 spin = 1 orbit", 56, NIGHT, GLIM, back(seg(u, .6, 1.1)))
    elif i == 3:
        earth(P, 200, CENTER, 90, t)
        moon(P, 700, CENTER, 170, face=True)
        P.line([(300, CENTER), (520, CENTER)], (120, 200, 255), 8)
        P.badge(820, CENTER - 260, "far side", 54, NIGHT, GLIM, back(seg(u, .5, 1.0)))
        P.badge(540, CENTER + 280, "hidden, not dark", 58, HOPE, CLOUD, back(seg(u, 2.0, 2.5)))
    elif i == 4:
        sun(P, 940, CENTER - 40, 70, t)
        earth(P, 140, CENTER - 40, 80, t)
        moon(P, 540, CENTER - 40, 170, lit_dir=0., face=False)
        P.badge(300, CENTER + 220, "our side: dark", 48, NIGHT, CLOUD, back(seg(u, .6, 1.1)))
        P.badge(760, CENTER + 220, "far side: sunny!", 48, HOOK, CLOUD, back(seg(u, 1.6, 2.1)))
    else:
        moon(P, 460, CENTER + 60, 200, face=True)
        x = lerp(1100, 780, eout(seg(u, .3, 2.0))); y = CENTER - 160
        P.rrect(x - 40, y - 30, x + 40, y + 30, 8, (200, 200, 210)); P.line([(x - 90, y), (x + 90, y)], (150, 150, 160), 6)
        for d in (-1, 1): P.rrect(x + d * 70 - 15, y - 45, x + d * 70 + 15, y + 45, 4, (60, 90, 170))
        P.badge(780, y + 110, "1959", 56, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
        P.stamp(540, CENTER - 320, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
