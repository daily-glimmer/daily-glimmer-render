# Thema: Why do we get hiccups? (G59, Alltagsfrage)
CENTER = 1050
PAL = ((255, 220, 200), (250, 190, 170))
HI = {"hiccups?", "diaphragm,", "breathing", "irritated,", "fast", "soda,", "twitches.", "gulp.", "vocal", "cords", "hic", "babies", "born!", "trick?"}
WOW = (2, 5)
SKIN, SKIND, LUNG, LUNGD, DIA = (255, 205, 170), (210, 150, 120), (250, 150, 160), (200, 90, 110), (220, 70, 80)

def torso(P, x, y, s, t, jerk=0., air=0.):
    P.rrect(x - 260 * s, y - 330 * s, x + 260 * s, y + 330 * s, 150 * s, SKIN, outline=SKIND, w=8 * s)
    P.circ(x, y - 420 * s, 120 * s, SKIN, outline=SKIND, w=8 * s)
    P.rrect(x - 40 * s, y - 330 * s, x + 40 * s, y - 180 * s, 20 * s, (230, 170, 150))
    infl = 1 + .12 * air
    for d in (-1, 1): P.ell(x + d * 110 * s, y - 60 * s, 95 * s * infl, 150 * s * infl, LUNG, outline=LUNGD, w=6 * s)
    dy = 40 * s * jerk
    pts = [(x - 240 * s + k * 24 * s, y + 140 * s + dy - math.sin(k / 20 * math.pi) * (90 * s - dy)) for k in range(21)]
    P.line(pts, DIA, 26 * s)
    for d in (-1, 1): P.circ(x + d * 40 * s, y - 440 * s, 12 * s, NIGHT)
    P.arc(x, y - 410 * s, 40 * s, 20, 160, NIGHT, 8 * s)

def arrows_down(P, x, y, t, k, col=(90, 170, 235)):
    for j in range(3):
        q = (t * 1.5 + j / 3) % 1
        yy = y + q * 160
        P.line([(x, yy - 40), (x, yy + 20)], col, 14 * k)
        P.poly([(x - 22 * k, yy + 15), (x + 22 * k, yy + 15), (x, yy + 45 * k)], col)

def cords(P, x, y, s, shut):
    P.ell(x, y, 160 * s, 210 * s, (240, 150, 150), outline=(190, 90, 100), w=8 * s)
    g = 70 * s * (1 - shut)
    for d in (-1, 1):
        P.poly([(x, y - 170 * s), (x + d * (g + 10 * s), y), (x, y + 170 * s), (x + d * 130 * s, y)], (250, 235, 225), outline=(200, 160, 150), w=5 * s)
    if g > 2: P.poly([(x, y - 170 * s), (x + g, y), (x, y + 170 * s), (x - g, y)], (90, 40, 50))

def SC(i, P, t, u):
    if i == 0:
        hic = (u % 1.2) < .15
        torso(P, 540, CENTER + 150, 1.0, t, jerk=1 if hic else 0)
        if hic or u < .6: P.text(820, CENTER - 280, "HIC!", 110 * back(seg(u % 1.2, 0, .15)), HOOK)
    elif i == 1:
        torso(P, 540, CENTER + 150, 1.0, t)
        P.badge(540, CENTER + 400, "diaphragm", 62, DIA, CLOUD, back(seg(u, 1.6, 2.1)))
        P.line([(540, CENTER + 350), (540, CENTER + 260)], DIA, 10 * seg(u, 1.6, 2.0))
    elif i == 2:
        torso(P, 380, CENTER + 180, .8, t, jerk=abs(math.sin(u * 14)) * seg(u, 3.5, 4.0))
        for k in range(3): P.circ(820 + k * 30, CENTER + 120 - k * 90, (20 + k * 8) * back(seg(u, 2.6 + k * .2, 3.0 + k * .2)), (200, 235, 255), outline=(90, 170, 235), w=4)
        P.rrect(760, CENTER + 160, 900, CENTER + 400, 20, (90, 170, 235))
        P.badge(540, CENTER - 270, "too fast? fizzy?", 56, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
    elif i == 3:
        jk = (u % 1.0) < .2
        torso(P, 540, CENTER + 150, 1.0, t, jerk=1 if jk else 0, air=1 if jk else .2)
        arrows_down(P, 540, CENTER - 300, t, 1.0)
        P.text(860, CENTER - 230, "GULP!", 80 * back(seg(u, .8, 1.2)), (90, 170, 235))
    elif i == 4:
        sh = eio(seg(u, 1.0, 1.4)) if (u % 1.6) < 1.3 else 1
        cords(P, 540, CENTER + 120, 1.3, sh)
        P.badge(540, CENTER + 470, "vocal cords", 58, NIGHT, GLIM, back(seg(u, .4, .9)))
        if sh > .9: P.text(540, CENTER - 230, "HIC!", 130 * back(seg(u, 1.3, 1.6)), HOOK)
    else:
        P.ell(540, CENTER + 120, 260, 300, (255, 215, 220), outline=(230, 150, 170), w=10)
        P.circ(470, CENTER + 50, 90, SKIN, outline=SKIND, w=6)
        P.ell(580, CENTER + 170, 130, 100, SKIN, outline=SKIND, w=6)
        P.arc(450, CENTER + 40, 20, 200, 340, NIGHT, 6); P.arc(500, CENTER + 40, 20, 200, 340, NIGHT, 6)
        if (u % 1.3) < .3: P.text(720, CENTER - 120, "hic", 70, HOOK)
        P.heart(800, CENTER + 330, 44 * back(seg(u, 2.5, 3.0)), HOOK)
