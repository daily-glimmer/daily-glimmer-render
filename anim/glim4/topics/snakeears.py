# Thema: Can snakes hear without ears?  (Mythos-Format, TRUE in Satz 2, FACT in Satz 6)
CENTER = 1050
SN, SN2, SNB = (90, 170, 90), (60, 130, 65), (220, 220, 140)
PAL = ((60, 80, 50), (170, 160, 100))
HI = {"hear", "ears?", "true!", "inner", "bone", "jaw", "vibrations.", "footsteps", "ground,", "low", "pitches,", "eighty", "jaw!"}
WOW = (1,)
GROUND = CENTER + 300

def sand(P, t):
    P.poly([(0, GROUND), (W, GROUND - 20), (W, H), (0, H)], (200, 175, 120))
    for j in range(5): P.ell(120 + j * 210, GROUND + 80 + (j % 2) * 60, 40, 14, (180, 155, 100))

def snake(P, x, y, s, t, head_up=0., jaw_glow=0., tongue=True):
    pts = [(x - 380 * s + j * 60 * s, y + math.sin(t * 2 + j * .8) * 30 * s) for j in range(8)]
    hx, hy = x + 100 * s, y - head_up * 160 * s
    pts += [(x + 60 * s, y - head_up * 60 * s), (hx - 30 * s, hy)]
    P.line(pts, SN2, 64 * s); P.line(pts, SN, 52 * s)
    for px, py in pts[1:-1:2]: P.circ(px, py - 6 * s, 9 * s, SN2)
    P.ell(hx + 20 * s, hy, 72 * s, 46 * s, SN)
    if jaw_glow > .02:
        P.line([(hx - 40 * s, hy + 30 * s), (hx + 80 * s, hy + 30 * s)], GLIM, 14 * s * jaw_glow)
        P.circ(hx - 20 * s, hy - 5 * s, 18 * s * jaw_glow, HOOK, glow=mul(HOOK, 150))
        P.line([(hx - 20 * s, hy - 5 * s), (hx - 40 * s, hy + 30 * s)], HOOK, 8 * s * jaw_glow)
    P.circ(hx + 40 * s, hy - 15 * s, 11 * s, NIGHT); P.circ(hx + 43 * s, hy - 18 * s, 4 * s, CLOUD)
    if tongue and math.sin(t * 4) > .3:
        P.line([(hx + 90 * s, hy + 10 * s), (hx + 140 * s, hy + 10 * s)], HOOK, 6 * s)
        P.line([(hx + 140 * s, hy + 10 * s), (hx + 160 * s, hy)], HOOK, 5 * s); P.line([(hx + 140 * s, hy + 10 * s), (hx + 160 * s, hy + 20 * s)], HOOK, 5 * s)

def boot(P, x, y, s): P.rrect(x - 60 * s, y - 120 * s, x + 30 * s, y, 20 * s, (110, 80, 60)); P.rrect(x - 60 * s, y - 30 * s, x + 90 * s, y, 15 * s, (90, 65, 50))

def SC(i, P, t, u):
    if i == 0:
        sand(P, t); snake(P, 560, GROUND - 40, 1.2, t, head_up=.6)
        P.text(820, CENTER - 240, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        sand(P, t); snake(P, 520, GROUND - 40, 1.3, t, head_up=.8, jaw_glow=back(seg(u, 1.0, 1.6)))
        P.stamp(780, CENTER - 280, "TRUE", seg(u, .25, .7), col=HOPE, rot=-6)
        P.badge(300, CENTER - 140, "no outer ears", 46, NIGHT, CLOUD, back(seg(u, .8, 1.3)))
    elif i == 2:
        P.rrect(120, CENTER - 300, 960, CENTER + 260, 80, (60, 90, 60))
        k = back(seg(u, .3, .8))
        P.ell(540, CENTER - 20, 330 * k, 210 * k, SN)
        P.line([(260, CENTER + 120), (820, CENTER + 120)], GLIM, 22 * k)
        P.circ(430, CENTER - 40, 40 * k, HOOK, glow=mul(HOOK, 160)); P.line([(430, CENTER - 40), (360, CENTER + 120)], (250, 240, 220), 14 * k)
        P.badge(430, CENTER - 160, "inner ear", 46, HOOK, CLOUD, back(seg(u, .8, 1.3)))
        P.badge(700, CENTER + 200, "jaw", 46, GLIM, NIGHT, back(seg(u, 1.5, 2.0)))
        waves(P, 540, CENTER + 120, t, CLOUD, n=3, r0=60, dr=40, a0=60, a1=120)
    elif i == 3:
        sand(P, t); snake(P, 420, GROUND - 30, 1.0, t, head_up=.2, jaw_glow=1.)
        st = int(u * 1.5) % 2
        boot(P, 830, GROUND - 10 - st * 70, 1.7)
        for j in range(3):
            q = (u * 1.2 + j / 3) % 1
            P.arc(820, GROUND + 10, 60 + q * 300, 180, 200, lc((140, 110, 70), (200, 175, 120), q), 8)
        P.badge(540, CENTER - 250, "feels footsteps", 56, NIGHT, CLOUD, back(seg(u, .6, 1.1)))
    elif i == 4:
        P.rrect(100, CENTER - 200, 980, CENTER + 200, 40, (40, 50, 40))
        pts = [(140 + j * 10, CENTER + math.sin((j * 10) / (30 + j * .9) * 6 + t * 3) * 120) for j in range(83)]
        P.line(pts, CLOUD, 6)
        P.rrect(140, CENTER - 190, 420, CENTER + 190, 20, None, outline=GLIM, w=8)
        P.badge(280, CENTER - 280, "80-160 Hz", 54, GLIM, NIGHT, back(seg(u, 1.6, 2.1)))
        P.badge(540, CENTER + 300, "low and deep", 54, NIGHT, CLOUD, back(seg(u, .6, 1.1)))
    else:
        sand(P, t); snake(P, 480, GROUND - 40, 1.2, t, head_up=.7, jaw_glow=1.)
        P.stamp(780, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
