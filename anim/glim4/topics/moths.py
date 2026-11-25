# Thema: Do moths really love flames?  (Mythos-Format, Stempel in Satz 1 + 5)
# Fakten: Fabian, Lin et al., Nature Communications 2024 (Imperial College London / FIU):
# Insekten richten den Rücken zum hellsten Licht aus (dorsal light response) -> an Lampen kreisen, stallen, kippen.
CENTER = 1050
PAL = ((14, 18, 48), (52, 44, 100))
HI = {"love", "flames", "Nope!", "trapped", "sky", "backs", "up.", "tilt,", "circle,", "upside", "down.", "2024.", "porch"}
WOW = (1, 4)
WING, WING2, BODY = (225, 205, 160), (170, 145, 105), (140, 115, 85)

def _rot(pts, x, y, a):
    c, s_ = math.cos(a), math.sin(a)
    return [(x + px * c - py * s_, y + px * s_ + py * c) for px, py in pts]

def smoth(P, x, y, s, t, ang=0., flap=True):
    """Seitenansicht: Rücken (Flügelseite) zeigt bei ang=0 nach oben; ang in Rad (im Uhrzeigersinn)."""
    f = (math.sin(t * 22) if flap else 0) * .5 + .5
    body = [(math.cos(k / 16 * 6.283) * 62 * s, math.sin(k / 16 * 6.283) * 20 * s) for k in range(16)]
    wtip = (-10 * s, -(70 + 50 * f) * s)
    wing = [(-35 * s, -10 * s), wtip, (45 * s, -(40 + 40 * f) * s), (30 * s, -10 * s)]
    P.poly(_rot(wing, x, y, ang), WING, outline=WING2, w=4)
    P.poly(_rot(body, x, y, ang), BODY, outline=dk2(BODY, .7), w=3)
    for d in (1, -1):
        ant = [(55 * s, -6 * s), (85 * s, (-30 + d * 6) * s), (100 * s, (-34 + d * 10) * s)]
        P.line(_rot(ant, x, y, ang), dk2(BODY, .7), 4 * s)
    ex, ey = _rot([(46 * s, -2 * s)], x, y, ang)[0]
    P.circ(ex, ey, 7 * s, NIGHT)
    P.circ(ex + 2 * s, ey - 2 * s, 2.5 * s, (255, 255, 255))

def dk2(c, k): return tuple(int(v * k) for v in c)

def lamp(P, x, y, t, k=1.):
    P.line([(x, y + 40), (x, y + 620)], (70, 75, 95), 22)
    P.rrect(x - 70, y - 40, x + 70, y + 40, 20, (90, 95, 120))
    fl = .9 + .1 * math.sin(t * 9)
    P.circ(x, y + 70, 56, (255, 236, 160), glow=mul((255, 200, 90), 220 * k * fl))

def sky(P, k=1.):
    for j in range(8):
        P.ell(540, CENTER - 330, 900 - j * 70, 80 - j * 7, lc((40, 50, 110), (150, 170, 255), j / 7 * k))

def arrow(P, x0, y0, x1, y1, col, w=12):
    P.line([(x0, y0), (x1, y1)], col, w)
    a = math.atan2(y1 - y0, x1 - x0)
    P.poly([(x1 + math.cos(a) * 26, y1 + math.sin(a) * 26), (x1 + math.cos(a + 2.4) * 30, y1 + math.sin(a + 2.4) * 30),
            (x1 + math.cos(a - 2.4) * 30, y1 + math.sin(a - 2.4) * 30)], col)

def SC(i, P, t, u):
    if i == 0:
        lamp(P, 540, CENTER - 160, t)
        for j in range(3):
            a = t * (1.8 + j * .4) + j * 2.1
            r = 150 + j * 60
            smoth(P, 540 + math.cos(a) * r, CENTER - 90 + math.sin(a) * r * .55, 1.2 - j * .2, t + j, ang=math.cos(a) * .8)
        k = back(seg(u, .5, 1.0))
        if k > .02: P.badge(540, CENTER + 470, "love the light?", 58, HOOK, CLOUD, k)
    elif i == 1:
        lamp(P, 540, CENTER - 100, t)
        a = t * 2.4
        smoth(P, 540 + math.cos(a) * 200, CENTER - 30 + math.sin(a) * 120, 1.4, t, ang=a + math.pi / 2)
        P.stamp(540, CENTER - 330, "MYTH", seg(u, .25, .7))
        P.badge(540, CENTER + 470, "trapped, not attracted", 54, (50, 70, 140), CLOUD, back(seg(u, 1.6, 2.1)))
    elif i == 2:
        sky(P, eout(seg(u, 0, 1.2)))
        P.poly([(0, CENTER + 300), (200, CENTER + 230), (420, CENTER + 280), (700, CENTER + 220), (1080, CENTER + 290), (1080, CENTER + 700), (0, CENTER + 700)], (20, 40, 35))
        for j in range(5): P.ell(120 + j * 210, CENTER + 260 - (j % 2) * 30, 90, 60, (25, 60, 45))
        smoth(P, 280 + (u * 90) % 600, CENTER - 20 + math.sin(t * 3) * 25, 1.5, t)
        P.badge(540, CENTER + 470, "brightest = the sky", 58, HOPE, CLOUD, back(seg(u, 1.5, 2.0)))
    elif i == 3:
        sky(P)
        smoth(P, 540, CENTER + 60, 1.7, t, ang=math.sin(t * 1.5) * .12)
        k = eout(seg(u, .8, 1.6))
        if k > .02: arrow(P, 540, CENTER - 40, 540, CENTER - 40 - 160 * k, GLIM, 14)
        P.text(700, CENTER - 200, "BACK", 64 * back(seg(u, 1.2, 1.7)), GLIM)
        P.badge(540, CENTER + 470, "back toward the light = up", 50, (50, 70, 140), CLOUD, back(seg(u, 2.6, 3.1)))
    elif i == 4:
        lx, ly = 540, CENTER - 40
        lamp(P, lx, ly - 70, t)
        a = t * 3.0
        mx, my = lx + math.cos(a) * 230, ly + math.sin(a) * 230
        ph = int(u / 1.4) % 3
        if ph == 0: ang = a - math.pi / 2 + math.pi   # Rücken zur Lampe -> kreisen
        elif ph == 1: ang = a - math.pi / 2 + math.pi + math.sin(t * 6) * .6
        else: ang = math.pi + math.sin(t * 2) * .3     # auf dem Kopf
        smoth(P, mx, my, 1.4, t, ang=ang)
        for lab, x, on in (("tilt", 220, ph == 1), ("circle", 540, ph == 0), ("flip", 860, ph == 2)):
            P.rrect(x - 130, CENTER + 420, x + 130, CENTER + 520, 46, HOOK if on else (60, 60, 95))
            P.text(x, CENTER + 470, lab, 52, CLOUD)
    else:
        lamp(P, 760, CENTER - 60, t, .7)
        a = t * 2.2
        smoth(P, 760 + math.cos(a) * 170, CENTER + 20 + math.sin(a) * 110, 1.2, t, ang=a + math.pi / 2)
        # Kamera
        cx, cy = 300, CENTER + 60
        P.rrect(cx - 130, cy - 80, cx + 130, cy + 80, 24, (60, 65, 90), outline=(120, 125, 160), w=4)
        P.rrect(cx - 60, cy - 110, cx + 10, cy - 80, 8, (60, 65, 90))
        P.circ(cx, cy, 52, (30, 35, 55), outline=(150, 160, 200), w=6)
        P.circ(cx, cy, 24, (90, 140, 220))
        P.circ(cx + 90, cy - 50, 12, HOOK if int(t * 4) % 2 else (90, 40, 40))
        P.stamp(540, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
        P.badge(540, CENTER + 480, "seen one circling?", 56, HOOK, CLOUD, back(seg(u, 1.0, 1.5)))
