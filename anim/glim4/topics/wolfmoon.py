# Thema: Do wolves really howl at the moon?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6)
CENTER = 1050
WF, WF2, WB = (140, 145, 160), (105, 110, 125), (215, 215, 220)
PAL = ((15, 25, 60), (50, 70, 120))
HI = {"howl", "moon?", "myth!", "link", "active,", "pack", "lost", "home.", "territory", "away!", "noses", "farther!"}
WOW = (1,)
GROUND = CENTER + 300

def hills(P, t):
    P.ell(250, GROUND + 140, 600, 220, (30, 45, 70)); P.ell(850, GROUND + 160, 560, 240, (40, 55, 85))
    P.poly([(0, GROUND + 120), (W, GROUND + 110), (W, H), (0, H)], (40, 55, 85))

def moon(P, x=820, y=CENTER - 330, r=90): P.circ(x, y, r, (250, 245, 215), glow=(110, 110, 90))

def wolf(P, x, y, s, t, howl=0., f=1):
    for dx in (-80, -45, 55, 90): P.rrect(x + f * dx * s - 12 * s, y + 20 * s, x + f * dx * s + 12 * s, y + 150 * s, 6 * s, WF2)
    P.line([(x - f * 110 * s, y - 10 * s), (x - f * 190 * s, y + 60 * s + math.sin(t * 2) * 10 * s)], WF2, 28 * s)
    P.ell(x, y, 125 * s, 60 * s, WF); P.ell(x + f * 10 * s, y + 20 * s, 80 * s, 30 * s, WB)
    a = math.radians(-20 - 45 * howl)
    nx, ny = x + f * 110 * s, y - 40 * s
    hx, hy = nx + f * math.cos(a) * 80 * s, ny + math.sin(a) * 80 * s
    P.line([(nx, ny), (hx, hy)], WF, 60 * s)
    P.circ(hx, hy, 50 * s, WF)
    P.poly([(hx - f * 20 * s, hy - 35 * s), (hx - f * 5 * s, hy - 85 * s), (hx + f * 15 * s, hy - 35 * s)], WF2)
    mx, my = hx + f * math.cos(a) * 70 * s, hy + math.sin(a) * 70 * s
    P.line([(hx, hy), (mx, my)], WF, 36 * s); P.circ(mx, my, 10 * s, NIGHT)
    P.circ(hx + f * 12 * s, hy - 12 * s, 7 * s, NIGHT)
    if howl > .5:
        for j in range(3):
            q = (t * .8 + j / 3) % 1
            P.arc(mx, my, 40 + q * 160, -110 if f > 0 else 200, -20 if f > 0 else 290, lc(CLOUD, PAL[0], q), 8)

def SC(i, P, t, u):
    if i == 0:
        moon(P); hills(P, t); wolf(P, 420, GROUND - 60, 1.2, t, howl=1.)
        P.text(620, CENTER - 300, "?", 140 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        moon(P); hills(P, t); wolf(P, 420, GROUND - 60, 1.2, t, howl=1.)
        P.line([(520, CENTER - 160), (760, CENTER - 300)], CLOUD, 6); P.cross(640, CENTER - 230, 60, k=back(seg(u, .8, 1.3)))
        P.stamp(540, CENTER + 480, "MYTH", seg(u, .25, .7))
    elif i == 2:
        hills(P, t)
        for j in range(24): P.circ((j * 137) % W, (j * 211) % 700 + CENTER - 650, 3 + j % 3, (240, 240, 220))
        wolf(P, 420, GROUND - 60, 1.1, t * 2, howl=0.)
        P.badge(540, CENTER - 230, "night shift", 58, HOOK, CLOUD, back(seg(u, .6, 1.1)))
    elif i == 3:
        hills(P, t)
        wolf(P, 260, GROUND - 40, .8, t, howl=1.)
        wolf(P, 830, GROUND + 40, .7, t + 1, howl=1., f=-1)
        P.badge(540, CENTER - 230, "where are you?", 58, (70, 100, 170), CLOUD, back(seg(u, .5, 1.0)))
        P.heart(540, CENTER + 40, 50 * back(seg(u, 2.2, 2.7)), HOOK)
    elif i == 4:
        hills(P, t); wolf(P, 380, GROUND - 60, 1.1, t, howl=1.)
        P.line([(760, GROUND + 120), (760, CENTER - 120)], (140, 100, 70), 14)
        P.rrect(640, CENTER - 200, 900, CENTER - 60, 16, (220, 70, 70))
        P.text(770, CENTER - 130, "TAKEN", 54, CLOUD)
    else:
        moon(P, 220, CENTER - 300, 70); hills(P, t); wolf(P, 450, GROUND - 60, 1.2, t, howl=1.)
        P.stamp(780, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
