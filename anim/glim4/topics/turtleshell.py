# Thema: Can a turtle crawl out of its shell?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6)
# Quellen: National Geographic "How the turtle got its shell" (Rippen + Wirbel bilden den Rückenpanzer),
# NY State Parks Blog (Panzer = Skelett), Science ABC / Live Science (Rippen, Wirbelsäule, ~50 Knochen; Panzer mit Nerven).
CENTER = 1050
SHELL, SHELL2, SKINT, BONEC = (110, 140, 70), (85, 110, 55), (150, 185, 110), (245, 240, 225)
PAL = ((120, 190, 200), (210, 230, 190))
HI = {"crawl", "shell?", "myth!", "skeleton.", "ribs", "backbone", "fuse", "fifty", "bones.", "nerves", "feel", "home"}
WOW = (1,)
GROUND = CENTER + 300

def ground(P):
    P.poly([(0, GROUND), (W, GROUND - 25), (W, H), (0, H)], (190, 170, 110))
    for x in (120, 880): P.ell(x, GROUND - 10, 90, 30, (110, 160, 80))

def turtle(P, x, y, s, t, xray=0., walk=True, tuck=0.):
    """Schildkröte, Bauch bei y."""
    ph = t * 4 if walk else 0
    for k, dx in enumerate((-110, -40, 50, 120)):
        P.ell(x + dx * s + math.sin(ph + k * 1.7) * 10 * s, y + 10 * s, 32 * s, 40 * s * (1 - .7 * tuck), SKINT)
    hx = x + lerp(215, 150, tuck) * s
    P.ell(hx, y - 50 * s, 60 * s, 46 * s, SKINT); P.circ(hx + 25 * s, y - 62 * s, 9 * s, NIGHT)
    P.d.chord([*P.c.p(x - 200 * s, y - 210 * s), *P.c.p(x + 200 * s, y + 70 * s)], 180, 360, fill=lc(SHELL, (60, 70, 90), xray))
    P.rrect(x - 205 * s, y - 80 * s, x + 205 * s, y - 50 * s, 14 * s, lc(SHELL2, (50, 60, 80), xray))
    if xray < .5:
        for dx, dy in ((-90, -110), (0, -150), (90, -110)): P.circ(x + dx * s, y + dy * s, 42 * s, SHELL2)
    else:
        P.line([(x - 190 * s, y - 120 * s), (x - 100 * s, y - 175 * s), (x, y - 190 * s), (x + 100 * s, y - 175 * s), (x + 190 * s, y - 120 * s)], BONEC, 16 * s)
        for j in range(8):
            a = math.pi * (.12 + .76 * j / 7); bx, by = x - math.cos(a) * 170 * s, y - 70 * s - math.sin(a) * 120 * s
            P.line([(x - math.cos(a) * 40 * s, y - 70 * s - math.sin(a) * 110 * s), (bx, by)], BONEC, 12 * s)

def SC(i, P, t, u):
    if i == 0:
        ground(P); turtle(P, lerp(380, 480, u / 4), GROUND - 50, 1.3, t)
        P.text(820, CENTER - 260, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        ground(P); turtle(P, 480, GROUND - 50, 1.3, t, walk=False)
        P.stamp(560, CENTER - 300, "MYTH", seg(u, .25, .7), rot=-6)
        P.badge(540, CENTER + 470, "shell = skeleton", 60, NIGHT, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 2:
        turtle(P, 480, CENTER + 220, 1.6, t, xray=eio(seg(u, .4, 1.4)), walk=False)
        P.badge(380, CENTER - 330, "ribs", 56, GLIM, NIGHT, back(seg(u, 1.4, 1.9)))
        P.badge(720, CENTER - 330, "backbone", 56, GLIM, NIGHT, back(seg(u, 2.0, 2.5)))
    elif i == 3:
        turtle(P, 480, CENTER + 220, 1.4, t, xray=1., walk=False)
        n = int(lerp(0, 50, eio(seg(u, .5, 2.5))))
        P.text(540, CENTER - 300, f"~{n} bones", 110, CLOUD)
        P.cross(480, CENTER + 60, 230, k=back(seg(u, 2.8, 3.3)))
    elif i == 4:
        ground(P); turtle(P, 420, GROUND - 50, 1.3, t, walk=False, tuck=.3)
        k = eout(seg(u, .4, 1.2))
        P.ell(lerp(900, 520, k), CENTER - 210, 34, 70, (240, 195, 160))
        if k > .95:
            for r in (60, 100, 140): P.arc(500, CENTER - 160, r, 200, 340, GLIM, 8)
        P.badge(540, CENTER + 470, "it can feel a touch", 58, NIGHT, CLOUD, back(seg(u, 1.6, 2.1)))
    else:
        ground(P); turtle(P, 380, GROUND - 50, 1.1, t)
        P.stamp(780, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
