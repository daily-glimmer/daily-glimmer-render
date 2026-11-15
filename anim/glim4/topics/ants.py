# Thema: Can ants really lift fifty times their own weight?  (Mythos-Format, Stempel TRUE / FACT)
CENTER = 1050
ANT, ANT2 = (90, 50, 40), (60, 30, 25)
LEAF = (110, 190, 90)
PAL = ((180, 220, 160), (240, 210, 150))
HI = {"fifty", "weight?", "Yes,", "more!", "muscles", "strong", "tiny", "neck", "five", "thousand", "times", "jaws.", "car", "two!"}
WOW = (1, 3)
GROUND = CENTER + 300

def ground(P):
    P.poly([(0, GROUND), (W, GROUND - 20), (W, H), (0, H)], (190, 150, 100))
    for k in range(12): P.circ((k * 97) % W, GROUND + 40 + (k * 53) % 200, 8 + k % 3 * 4, (165, 125, 85))

def ant(P, x, y, s, t, walk=1., load=None, neck=0.):
    """Ameise seitlich, Kopf links; load = ('leaf'|'crumb', Größe)."""
    for k, dx in enumerate((-30, 10, 50)):
        ph = t * 10 * walk + k * 2.1
        for side in (-1, 1):
            a = math.sin(ph + (0 if side > 0 else math.pi)) * 18 * s
            P.line([(x + dx * s, y), (x + dx * s + a - 20 * s, y + 40 * s), (x + dx * s + a - 30 * s, y + 80 * s)], ANT2, 7 * s)
    P.ell(x + 120 * s, y - 10 * s, 75 * s, 50 * s, ANT)        # Hinterleib
    P.ell(x + 20 * s, y - 5 * s, 55 * s, 30 * s, ANT)          # Brust
    nk = lc(ANT, GLIM, neck)
    P.line([(x - 30 * s, y - 10 * s), (x - 65 * s, y - 25 * s)], nk, 18 * s * (1 + neck * .4))
    hx, hy = x - 95 * s, y - 35 * s
    P.circ(hx, hy, 40 * s, ANT)
    P.circ(hx - 10 * s, hy - 10 * s, 9 * s, CLOUD); P.circ(hx - 12 * s, hy - 10 * s, 5 * s, NIGHT)
    for d in (-1, 1): P.line([(hx, hy - 30 * s), (hx - 30 * s + d * 15 * s, hy - 90 * s), (hx - 60 * s + d * 15 * s, hy - 100 * s)], ANT2, 5 * s)
    P.line([(hx - 30 * s, hy + 20 * s), (hx - 55 * s, hy + 35 * s)], ANT2, 8 * s)
    if load:
        kind, z = load
        lx, ly = hx - 40 * s, hy - 90 * s * z
        if kind == "leaf":
            P.ell(lx, ly, 150 * s * z, 80 * s * z, LEAF); P.line([(lx - 140 * s * z, ly), (lx + 140 * s * z, ly)], lc(LEAF, (0, 0, 0), .3), 5 * s)
        else:
            P.rrect(lx - 100 * s * z, ly - 70 * s * z, lx + 100 * s * z, ly + 70 * s * z, 30 * s * z, (230, 200, 140), outline=(190, 150, 90), w=5 * s)

def car(P, x, y, s, col):
    P.rrect(x - 170 * s, y - 50 * s, x + 170 * s, y + 30 * s, 26 * s, col)
    P.rrect(x - 100 * s, y - 110 * s, x + 80 * s, y - 40 * s, 24 * s, col)
    P.rrect(x - 85 * s, y - 98 * s, x - 15 * s, y - 52 * s, 10 * s, (200, 230, 250)); P.rrect(x, y - 98 * s, x + 65 * s, y - 52 * s, 10 * s, (200, 230, 250))
    for d in (-1, 1): P.circ(x + d * 100 * s, y + 30 * s, 34 * s, NIGHT); P.circ(x + d * 100 * s, y + 30 * s, 14 * s, (200, 200, 210))

def SC(i, P, t, u):
    if i == 0:
        ground(P)
        x = lerp(760, 520, (u * .12) % 1)
        ant(P, x, GROUND - 80, 1.5, t, load=("leaf", 1.4))
        P.text(840, CENTER - 280, "50x?", 120 * back(seg(u, .5, 1.0)), HOOK)
    elif i == 1:
        ground(P); ant(P, 560, GROUND - 80, 1.5, t, walk=.3, load=("crumb", 1.2))
        P.stamp(540, CENTER - 270, "TRUE", seg(u, .25, .7), col=HOPE)
    elif i == 2:
        for j, (lab, mus, wt, xx) in enumerate((("ant", 300, 60, 330), ("elephant", 300, 520, 750))):
            k = eio(seg(u, .4 + j * .4, 1.4 + j * .4))
            P.rrect(xx - 110, CENTER + 280 - mus * k, xx - 20, CENTER + 280, 16, HOPE)
            P.rrect(xx + 20, CENTER + 280 - wt * k, xx + 110, CENTER + 280, 16, HOOK)
            P.text(xx, CENTER + 340, lab, 46, CLOUD)
        P.badge(380, CENTER - 300, "muscle", 50, HOPE, CLOUD, back(seg(u, .3, .8)))
        P.badge(700, CENTER - 300, "weight", 50, HOOK, CLOUD, back(seg(u, .6, 1.1)))
    elif i == 3:
        P.rrect(150, CENTER - 200, 930, CENTER + 300, 40, (240, 236, 226), outline=(180, 170, 160), w=6)
        ant(P, 560, CENTER + 140, 1.6, t, walk=0, neck=.5 + .5 * math.sin(t * 5))
        n = int(5000 * eout(seg(u, .6, 3.0)))
        P.badge(540, CENTER + 420, f"{n:,}x body weight", 58, NIGHT, GLIM, 1. if u > .6 else back(seg(u, .4, .6)))
        P.line([(420, CENTER - 140), (420, CENTER - 20)], HOOK, 14); P.poly([(395, CENTER - 30), (445, CENTER - 30), (420, CENTER + 10)], HOOK)
    elif i == 4:
        ground(P)
        x = lerp(780, 500, (u * .1) % 1)
        ant(P, x, GROUND - 80, 1.5, t, load=("crumb", 1.3), neck=.8)
        P.badge(540, CENTER - 300, "strong neck joint", 58, NIGHT, GLIM, back(seg(u, .6, 1.1)))
    else:
        ground(P)
        lift = eio(seg(u, .3, 1.5)) * 60
        P.circ(540, GROUND - 240, 60, (240, 200, 170))                  # Kopf
        for d in (-1, 1): P.circ(540 + d * 22, GROUND - 250, 8, NIGHT)
        P.arc(540, GROUND - 230, 22, 20, 160, NIGHT, 5)
        P.rrect(480, GROUND - 180, 600, GROUND - 40, 40, HOOK)          # Körper
        for d in (-1, 1): P.line([(540 + d * 50, GROUND - 160), (540 + d * 90, GROUND - 330 - lift)], (240, 200, 170), 26)
        for d in (-1, 1): P.line([(540 + d * 30, GROUND - 50), (540 + d * 50, GROUND)], NIGHT, 26)
        car(P, 540, GROUND - 420 - lift, .95, (100, 160, 230))
        car(P, 540, GROUND - 560 - lift, .85, HOPE)
        P.stamp(840, CENTER + 60, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
