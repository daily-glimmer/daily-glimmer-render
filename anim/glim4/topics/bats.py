# Thema: Are bats really blind?  (Mythos-Format, Stempel in Satz 1)
CENTER = 1050
BAT, BAT2, WING = (90, 70, 95), (60, 45, 70), (120, 95, 125)
PAL = ((15, 20, 55), (60, 50, 110))
HI = {"blind?", "every", "see.", "big", "eyes", "ultraviolet", "echolocation.", "clicks", "echoes.", "switch", "compliment!", "sonar?"}
WOW = (1, 2)

def moon(P, x, y, r): P.circ(x, y, r, (250, 240, 200), glow=mul((255, 240, 180), 45))

def bat(P, x, y, s, t, flap=True, big_eyes=False, fruit=False):
    a = math.sin(t * (14 if flap else 2)) * (1 if flap else .2)
    for side in (-1, 1):
        tip = (x + side * 230 * s, y - 40 * s - a * 90 * s)
        pts = [(x + side * 40 * s, y - 20 * s), (x + side * 120 * s, y - 70 * s - a * 50 * s), tip,
               (x + side * 190 * s, y + 30 * s - a * 40 * s), (x + side * 140 * s, y + 10 * s - a * 20 * s),
               (x + side * 95 * s, y + 50 * s - a * 15 * s), (x + side * 40 * s, y + 40 * s)]
        P.poly(pts, WING, outline=BAT2, w=4)
        P.line([(x + side * 40 * s, y - 20 * s), (x + side * 120 * s, y - 70 * s - a * 50 * s), tip], BAT2, 6 * s)
    P.ell(x, y + 10 * s, 52 * s, 70 * s, BAT)
    P.circ(x, y - 60 * s, 48 * s, BAT)
    for side in (-1, 1):
        P.poly([(x + side * 18 * s, y - 95 * s), (x + side * 48 * s, y - 160 * s), (x + side * 50 * s, y - 85 * s)], BAT)
        P.poly([(x + side * 24 * s, y - 98 * s), (x + side * 44 * s, y - 140 * s), (x + side * 45 * s, y - 92 * s)], (220, 150, 160))
    er = (19 if big_eyes else 11) * s
    for side in (-1, 1):
        P.circ(x + side * 20 * s, y - 65 * s, er, (255, 255, 255) if big_eyes else NIGHT)
        if big_eyes: P.circ(x + side * 20 * s, y - 63 * s, er * .6, NIGHT); P.circ(x + side * 16 * s, y - 70 * s, er * .25, (255, 255, 255))
    P.poly([(x - 9 * s, y - 40 * s), (x + 9 * s, y - 40 * s), (x, y - 28 * s)], (230, 140, 150))
    if fruit: P.circ(x, y + 70 * s, 34 * s, (255, 150, 40)); P.line([(x, y + 36 * s), (x + 8 * s, y + 20 * s)], (70, 140, 60), 6 * s)

def moth(P, x, y, s, t):
    a = math.sin(t * 20) * .5
    for side in (-1, 1): P.ell(x + side * 22 * s, y - a * 6 * s, 26 * s, 18 * s, (230, 220, 190))
    P.ell(x, y, 8 * s, 22 * s, (150, 130, 100))

def SC(i, P, t, u):
    if i == 0:
        moon(P, 780, CENTER - 300, 120)
        bat(P, 520 + math.sin(t * 1.3) * 160, CENTER + 60 + math.sin(t * 2.6) * 60, 1.4, t)
        k = back(seg(u, .4, .9))
        if k > .02:
            P.rrect(420, CENTER + 380, 660, CENTER + 440, 30, NIGHT)
            P.text(540, CENTER + 410, "blind?", 62 * k, GLIM)
    elif i == 1:
        moon(P, 180, CENTER - 420, 70)
        bat(P, 540, CENTER + 60, 1.6, t, flap=False, big_eyes=True)
        P.stamp(540, CENTER - 330, "MYTH", seg(u, .25, .7))
        P.badge(540, CENTER + 470, "all ~1,400 species can see", 50, HOPE, CLOUD, back(seg(u, 1.2, 1.7)))
    elif i == 2:
        P.line([(0, CENTER - 190), (1080, CENTER - 230)], (110, 75, 45), 26)
        for j in range(6): P.ell(90 + j * 190, CENTER - 230 + (j % 2) * 30, 80, 34, (60, 150, 80))
        bat(P, 540, CENTER + 60, 1.3, t, flap=False, big_eyes=True, fruit=True)
        k = eout(seg(u, 2.0, 3.2))
        for j in range(7):
            a = j / 7 * 2 * math.pi + t * .6
            P.circ(540 + math.cos(a) * 330, CENTER - 40 + math.sin(a) * 260, 18 * k, (190, 120, 255), glow=mul((170, 90, 255), 230 * k))
        P.badge(540, CENTER + 470, "sees UV light", 60, (130, 70, 200), CLOUD, back(seg(u, 2.2, 2.7)))
    elif i == 3:
        moon(P, 200, CENTER - 360, 70)
        bx, by = 300, CENTER + 40
        bat(P, bx, by, 1.0, t)
        mx, my = 820 + math.sin(t * 3) * 40, CENTER - 60 + math.cos(t * 2) * 50
        moth(P, mx, my, 1.4, t)
        for j in range(4):
            q = (t * 1.1 + j / 4) % 1
            P.arc(bx + 40, by - 60, 60 + q * 520, -25, 25, lc((120, 220, 255), (20, 30, 70), q), 12 * (1 - q) + 3)
            P.arc(mx, my, 40 + ((q + .5) % 1) * 300, 155, 205, lc((255, 220, 120), (20, 30, 70), (q + .5) % 1), 8)
        P.badge(540, CENTER + 470, "click... echo!", 60, NIGHT, (150, 220, 255), back(seg(u, .5, 1.0)))
    elif i == 4:
        side = int(u / 1.6) % 2
        bat(P, 540, CENTER + 20, 1.2, t, flap=False, big_eyes=bool(side))
        for x, lab, on in ((260, "EYES", side == 1), (820, "ECHOES", side == 0)):
            P.rrect(x - 150, CENTER - 360, x + 150, CENTER - 250, 50, HOPE if on else (60, 60, 90))
            P.text(x, CENTER - 305, lab, 56, CLOUD)
        if side == 0:
            for j in range(3):
                q = (t + j / 3) % 1; P.arc(540, CENTER - 30, 120 + q * 300, -40, 40, lc((120, 220, 255), (20, 30, 70), q), 10)
    else:
        moon(P, 180, CENTER - 420, 70)
        bat(P, 470, CENTER + 60, 1.25, t, big_eyes=True)
        P.stamp(540, CENTER - 330, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
        P.badge(540, CENTER + 480, "night vision or sonar?", 54, HOOK, CLOUD, back(seg(u, 1.0, 1.5)))
