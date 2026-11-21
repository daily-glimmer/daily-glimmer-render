# Thema: Do penguins really have no knees?  (Mythos-Format, Stempel MYTH in Satz 2, FACT in Satz 6)
CENTER = 1050
ICE, ICE2, SEA = (235, 245, 252), (190, 215, 235), (40, 90, 150)
PB, PW, PO = (30, 34, 48), (250, 250, 245), (255, 150, 40)
BONE, XR = (250, 246, 230), (120, 190, 235)
PAL = ((20, 40, 80), (90, 150, 200))
HI = {"knees?", "myth!", "knees,", "inside", "feathers,", "knee", "crouch.", "ankle", "foot.", "twice", "energy", "squatting"}
WOW = (1,)

def floe(P, t, y=CENTER + 330):
    P.poly([(0, y + 60), (W, y + 40), (W, H), (0, H)], SEA)
    for k in range(3):
        P.line([(k * 400 - (t * 60) % 400, y + 120 + k * 40), (k * 400 + 160 - (t * 60) % 400, y + 120 + k * 40)], (90, 150, 210), 8)
    P.ell(540, y + 30, 640, 110, ICE2); P.ell(540, y + 10, 620, 95, ICE)

def leg_bones(P, x, y, s, f=1, col=BONE, hl=None):
    """Bein im Körper: Hüfte -> Oberschenkel -> Knie (gebeugt) -> Unterschenkel -> Knöchel -> Fuß."""
    hip = (x + f * 10 * s, y + 20 * s); knee = (x + f * 75 * s, y + 95 * s)
    ank = (x + f * 20 * s, y + 175 * s); toe = (x + f * 85 * s, y + 225 * s)
    w = 16 * s
    P.line([hip, knee], hl.get("thigh", col) if hl else col, w)
    P.line([knee, ank], hl.get("shin", col) if hl else col, w)
    P.line([ank, (ank[0] + f * 10 * s, y + 215 * s), toe], hl.get("ankle", col) if hl else col, w * .9)
    P.circ(*hip, 14 * s, col); P.circ(*knee, 15 * s, hl.get("knee", col) if hl else col); P.circ(*ank, 11 * s, hl.get("ankle", col) if hl else col)
    return hip, knee, ank, toe

def penguin(P, x, y, s, t, walk=True, xray=0., flip=1, squat=0., leg_hl=None):
    f = flip; ph = math.sin(t * 6) if walk else 0
    rot = ph * .08; x = x + ph * 8 * s
    def R(px, py):
        c, sn = math.cos(rot), math.sin(rot); return (x + px * c - py * sn, y + px * sn + py * c)
    yy = squat * 30 * s
    for side in (-1, 1):   # Füße
        fx, fy = R(side * 45 * s, 205 * s + yy)
        lift = max(0, side * ph) * 14 * s
        P.ell(fx + f * 18 * s, fy - lift, 42 * s, 16 * s, PO)
    bx, by = R(0, yy)
    P.ell(bx, by, 115 * s, 210 * s, PB)                         # Körper
    P.ell(bx + f * 12 * s, by + 30 * s, 82 * s, 170 * s, PW)     # Bauch
    for side in (-1, 1):                                         # Flossen
        a = side * (.35 + .25 * abs(ph))
        sx, sy = R(side * 100 * s, -40 * s + yy)
        P.poly([(sx, sy), (sx + side * 50 * s, sy + 150 * s), (sx + side * 10 * s, sy + 170 * s)], PB)
    hx, hy = R(f * 10 * s, -165 * s + yy)
    P.circ(hx, hy, 82 * s, PB)                                   # Kopf
    P.ell(hx + f * 28 * s, hy + 10 * s, 34 * s, 40 * s, PW)
    P.circ(hx + f * 32 * s, hy - 2 * s, 11 * s, NIGHT); P.circ(hx + f * 36 * s, hy - 6 * s, 4 * s, (255, 255, 255))
    P.poly([(hx + f * 60 * s, hy + 10 * s), (hx + f * 125 * s, hy + 26 * s), (hx + f * 60 * s, hy + 36 * s)], PO)
    if xray > .02:   # Röntgenfenster unten im Bauch
        wx, wy = R(f * 5 * s, 95 * s + yy)
        P.ell(wx, wy, 95 * s * xray, 125 * s * xray, XR, outline=(60, 130, 190), w=5)
        if xray > .6:
            k = (xray - .6) / .4
            leg_bones(P, wx - f * 40 * s, wy - 110 * s, .95 * s * k, f, hl=leg_hl)

def human_squat(P, x, y, s, col=CLOUD):
    P.circ(x, y - 210 * s, 40 * s, col)
    P.line([(x, y - 170 * s), (x - 20 * s, y - 40 * s)], col, 26 * s)
    P.line([(x - 20 * s, y - 40 * s), (x + 70 * s, y - 20 * s), (x + 40 * s, y + 80 * s)], col, 24 * s)
    P.line([(x, y - 140 * s), (x + 90 * s, y - 120 * s)], col, 20 * s)
    P.ell(x + 60 * s, y + 88 * s, 34 * s, 12 * s, col)

def SC(i, P, t, u):
    if i == 0:
        floe(P, t)
        penguin(P, 540 + math.sin(t * .8) * 60, CENTER + 50, 1.25, t)
        k = back(seg(u, .5, 1.0))
        P.text(760, CENTER + 120, "?", 170 * k, GLIM)
        P.text(320, CENTER + 220, "?", 120 * back(seg(u, .9, 1.4)), GLIM)
    elif i == 1:
        floe(P, t)
        penguin(P, 500, CENTER + 60, 1.3, t, walk=False, xray=eout(seg(u, .3, 1.4)))
        P.stamp(800, CENTER - 230, "MYTH", seg(u, .25, .7))
        P.badge(540, CENTER + 520, "knees hidden inside", 60, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
    elif i == 2:
        P.circ(540, CENTER + 40, 430, (24, 50, 90))
        P.ell(540, CENTER + 40, 300, 400, XR, outline=(60, 130, 190), w=8)
        _, knee, _, _ = leg_bones(P, 470, CENTER - 230, 2.4, hl={"thigh": GLIM, "knee": HOOK})
        kk = back(seg(u, .8, 1.3))
        P.badge(260, CENTER - 200, "thigh", 52, GLIM, NIGHT, back(seg(u, .4, .9)))
        P.badge(knee[0] + 150, knee[1], "knee", 56, HOOK, CLOUD, kk)
        P.badge(540, CENTER + 520, "deep crouch", 60, NIGHT, GLIM, back(seg(u, 2.2, 2.7)))
    elif i == 3:
        floe(P, t)
        penguin(P, 540, CENTER + 60, 1.35, t, walk=False, xray=1., leg_hl={"ankle": GLIM, "shin": (200, 230, 250), "thigh": (200, 230, 250), "knee": (200, 230, 250)})
        P.badge(240, CENTER + 260, "ankle", 54, GLIM, NIGHT, back(seg(u, .5, 1.0)))
        P.badge(840, CENTER + 360, "foot", 54, PO, NIGHT, back(seg(u, 1.4, 1.9)))
    elif i == 4:
        P.rrect(120, CENTER + 250, 960, CENTER + 330, 40, (70, 80, 100))                 # Laufband
        for j in range(8):
            xx = 140 + ((j * 110 - u * 160) % 800); P.line([(xx, CENTER + 262), (xx, CENTER + 318)], (110, 120, 140), 8)
        penguin(P, 380, CENTER + 30, .95, t * 1.5)
        k = eio(seg(u, .6, 3.0))
        P.rrect(700, CENTER - 260, 790, CENTER + 200, 24, (40, 50, 70))
        P.rrect(708, CENTER + 192 - 440 * k, 782, CENTER + 192, 20, HOOK)
        P.rrect(840, CENTER - 30, 930, CENTER + 200, 24, (40, 50, 70))
        P.rrect(848, CENTER + 192 - 220 * k, 922, CENTER + 192, 20, HOPE)
        P.text(745, CENTER + 228, "penguin", 30, CLOUD); P.text(885, CENTER + 228, "others", 30, CLOUD)
        P.text(745, CENTER - 320, "2x", 90 * back(seg(u, 2.6, 3.1)), GLIM)
        P.badge(540, CENTER + 470, "energy per step", 58, NIGHT, CLOUD, back(seg(u, 1.0, 1.5)))
    else:
        floe(P, t)
        penguin(P, 360, CENTER + 60, 1.1, t, walk=False, xray=1., squat=.5 + .5 * math.sin(t * 3))
        human_squat(P, 760, CENTER + 230, 1.0)
        P.stamp(560, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
