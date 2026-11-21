# Thema: Is one dog year really seven human years?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6) – Hund aus dogs.py
CENTER = 1050
exec(open(os.path.join(HERE, "topics", "dogs.py")).read(), globals())
PAL = ((60, 110, 160), (150, 200, 220))
HI = {"seven", "years?", "myth!", "faster", "slower", "DNA", "thirty-year-old", "four-year-old", "fifty", "two,", "fast!", "years?"}
WOW = (1, 3)

def cake(P, x, y, s, n, k=1.):
    P.rrect(x - 110 * s, y - 70 * s, x + 110 * s, y + 60 * s, 20 * s, (250, 200, 210))
    P.rrect(x - 110 * s, y - 80 * s, x + 110 * s, y - 50 * s, 15 * s, CLOUD)
    for j in range(n):
        cx = x - 60 * s + j * 120 * s / max(1, n - 1) if n > 1 else x
        P.rrect(cx - 8 * s, y - 150 * s, cx + 8 * s, y - 80 * s, 4 * s, (120, 180, 250))
        P.ell(cx, y - 170 * s, 9 * s * k, 16 * s * k, GLIM)

def person(P, x, y, s, age):
    hair = (90, 70, 50) if age < 45 else (190, 190, 195)
    P.circ(x, y - 230 * s, 55 * s, (240, 200, 165)); P.d.chord([*P.c.p(x - 58 * s, y - 290 * s), *P.c.p(x + 58 * s, y - 200 * s)], 180, 360, fill=hair)
    P.rrect(x - 70 * s, y - 170 * s, x + 70 * s, y + 40 * s, 34 * s, (90, 130, 200))
    P.circ(x - 20 * s, y - 230 * s, 6 * s, NIGHT); P.circ(x + 20 * s, y - 230 * s, 6 * s, NIGHT)

def SC(i, P, t, u):
    if i == 0:
        grass(P); dog(P, 380, CENTER + 120, 1.0, t)
        P.badge(780, CENTER - 100, "1 = 7 ?", 80, NIGHT, GLIM, back(seg(u, .5, 1.0)))
    elif i == 1:
        P.rrect(100, CENTER - 300, 980, CENTER + 250, 40, (240, 240, 245))
        k = eio(seg(u, .3, 2.5))
        pts = [(160 + q * 760, CENTER + 200 - (math.log(1 + q * 15) / math.log(16)) * 450 * 1.0) for q in [j / 40 * k for j in range(41)]]
        P.line([(160, CENTER + 200), (920, CENTER - 250)], (180, 180, 190), 8)
        P.line(pts, HOOK, 14)
        P.stamp(540, CENTER + 420, "MYTH", seg(u, .25, .7))
    elif i == 2:
        P.rrect(140, CENTER - 280, 940, CENTER + 280, 60, (40, 60, 100))
        for j in range(10):
            y = CENTER - 240 + j * 52
            P.line([(380 + math.sin(j * .7 + t) * 60, y), (700 - math.sin(j * .7 + t) * 60, y)], (120, 200, 255), 10)
            if j % 3 == 1: P.circ(380 + math.sin(j * .7 + t) * 60, y, 16 * back(seg(u, .5 + j * .1, 1.0 + j * .1)), GLIM)
        P.badge(540, CENTER + 360, "DNA tags", 58, GLIM, NIGHT, back(seg(u, 1.4, 1.9)))
    elif i == 3:
        grass(P); dog(P, 300, CENTER + 120, .8, t)
        person(P, 760, CENTER + 190, 1.0, 30)
        P.badge(300, CENTER - 200, "1 year", 56, NIGHT, CLOUD, back(seg(u, .3, .8)))
        P.badge(760, CENTER - 200, "~30 years", 56, HOOK, CLOUD, back(seg(u, 1.2, 1.7)))
    elif i == 4:
        grass(P); dog(P, 300, CENTER + 120, .9, t)
        person(P, 760, CENTER + 190, 1.0, 52)
        P.badge(300, CENTER - 200, "4 years", 56, NIGHT, CLOUD, back(seg(u, .3, .8)))
        P.badge(760, CENTER - 200, "~52 years", 56, HOOK, CLOUD, back(seg(u, 1.2, 1.7)))
    else:
        grass(P); dog(P, 340, CENTER + 120, .9, t)
        cake(P, 780, CENTER + 120, 1.0, 1)
        P.stamp(700, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
