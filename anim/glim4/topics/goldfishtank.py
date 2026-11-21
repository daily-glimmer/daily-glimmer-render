# Thema: Does a goldfish only grow to the size of its tank?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6) – Figuren aus goldfish.py
CENTER = 1050
exec(open(os.path.join(HERE, "topics", "goldfish.py")).read(), globals())
PAL = ((10, 50, 90), (40, 140, 170))
HI = {"size", "tank?", "myth!", "magically", "waste", "dirty", "stunts", "stress", "crowding", "thirty", "centimeters.", "bowl", "myth?"}
WOW = (1,)

def bowl(P, x, y, r, murky=0.):
    P.circ(x, y, r, (150, 215, 240), outline=(230, 245, 255), w=10)
    P.d.chord([*P.c.p(x - r + 10, y - r + 10), *P.c.p(x + r - 10, y + r - 10)], -20, 200, fill=lc((70, 170, 220), (110, 120, 70), murky))
    P.rrect(x - r * .55, y - r * 1.02, x + r * .55, y - r * .9, 10, (230, 245, 255))

def SC(i, P, t, u):
    if i == 0:
        bowl(P, 540, CENTER + 80, 330)
        goldfish(P, 540 + math.sin(t) * 80, CENTER + 120, .9, t, flip=1 if math.cos(t) > 0 else -1)
        P.text(840, CENTER - 290, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        tank(P, t, 150, CENTER - 240, 930, CENTER + 300)
        goldfish(P, 380, CENTER + 20, .7, t); goldfish(P, 700, CENTER + 80, 1.2, t, flip=-1)
        P.stamp(780, CENTER - 270, "MYTH", seg(u, .25, .7))
        P.badge(540, CENTER + 420, "tank size alone? no", 56, NIGHT, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 2:
        m = eio(seg(u, .3, 3.0))
        bowl(P, 540, CENTER + 60, 330, murky=m)
        for j in range(int(12 * m)):
            P.circ(330 + (j * 53) % 420, CENTER + 300 - (j * 37) % 120, 10, (100, 80, 50))
        goldfish(P, 540, CENTER + 120, .75, t, happy=m < .5)
        P.badge(540, CENTER + 480, "dirty water", 58, HOOK, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 3:
        bowl(P, 540, CENTER + 60, 330, murky=.6)
        for j in range(5): goldfish(P, 380 + (j % 3) * 150, CENTER + (j // 3) * 150 - 20, .5, t + j, flip=1 if j % 2 else -1, happy=False)
        P.badge(540, CENTER + 480, "stress + crowding", 56, NIGHT, CLOUD, back(seg(u, .6, 1.1)))
    elif i == 4:
        tank(P, t, 60, CENTER - 280, 1020, CENTER + 380)
        k = eout(seg(u, .3, 3.0))
        goldfish(P, 520 + math.sin(t * .6) * 60, CENTER + 40, .7 + .9 * k, t)
        P.line([(160, CENTER + 300), (lerp(160, 900, k), CENTER + 300)], GLIM, 10)
        P.badge(540, CENTER - 360, "up to ~30 cm", 60, NIGHT, GLIM, back(seg(u, 2.2, 2.7)))
    else:
        tank(P, t, 150, CENTER - 200, 930, CENTER + 340)
        goldfish(P, 540, CENTER + 60, 1.3, t)
        P.stamp(780, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
