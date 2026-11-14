# Thema: Do dogs really see in black and white?  (Mythos-Format)
CENTER = 1050
FUR, FUR2 = (210, 160, 100), (170, 115, 65)
PAL = ((40, 50, 90), (110, 150, 200))
HI = {"black", "white?", "color,", "three", "two.", "blues", "yellows", "red", "green", "blue", "yellow", "favorite"}
WOW = (1,)

def dog(P, x, y, s, t, wag=True, tilt=0.):
    tw = math.sin(t * (14 if wag else 2)) * 30 * s
    P.line([(x + 140 * s, y - 10 * s), (x + 200 * s, y - 90 * s + tw)], FUR2, 24 * s)
    for dx in (-90, -50, 70, 110): P.line([(x + dx * s, y + 40 * s), (x + dx * s, y + 170 * s)], FUR, 30 * s)
    P.ell(x, y, 160 * s, 80 * s, FUR)
    hx, hy = x - 170 * s, y - 90 * s + tilt * 10 * s
    P.circ(hx, hy, 80 * s, FUR)
    P.ell(hx - 70 * s, hy + 25 * s, 50 * s, 35 * s, (235, 200, 150))
    P.circ(hx - 110 * s, hy + 12 * s, 16 * s, NIGHT)
    P.ell(hx + 40 * s, hy + 10 * s, 30 * s, 75 * s, FUR2)     # Schlappohr
    P.circ(hx - 25 * s, hy - 20 * s, 13 * s, NIGHT); P.circ(hx - 21 * s, hy - 24 * s, 4 * s, (255, 255, 255))
    P.arc(hx - 75 * s, hy + 45 * s, 20 * s, 20, 160, NIGHT, 5 * s)

def eye(P, x, y, r, cones, k=1.):
    P.circ(x, y, r, (250, 250, 250), outline=(190, 190, 200), w=8); P.circ(x, y, r * .55, (90, 140, 200)); P.circ(x, y, r * .25, NIGHT)
    for j, c in enumerate(cones):
        kk = back(seg(k, j * .25, j * .25 + .3))
        P.circ(x - (len(cones) - 1) * 50 + j * 100, y + r + 90, 38 * kk, c)

def ball(P, x, y, r, col): P.circ(x, y, r, col); P.arc(x, y, r * .7, 200, 300, lc(col, (255, 255, 255), .5), r * .12)

def grass(P, y=CENTER + 220, col=(80, 170, 80)): P.poly([(0, y), (W, y - 30), (W, H), (0, H)], col)

def SC(i, P, t, u):
    if i == 0:
        grass(P); dog(P, 600, CENTER + 60, 1.1, t)
        k = eio(seg(u, .3, 1.5))
        P.rrect(140, CENTER - 420, 940, CENTER - 160, 30, lc((255, 255, 255), (120, 120, 120), 0))
        for j, c in enumerate([(220, 50, 50), (60, 120, 255), (255, 200, 40), (60, 170, 80)]):
            g = int(sum(c) / 3); P.rrect(190 + j * 190, CENTER - 380, 330 + j * 190, CENTER - 200, 20, lc(c, (g, g, g), k))
    elif i == 1:
        grass(P); dog(P, 600, CENTER + 60, 1.1, t)
        P.stamp(540, CENTER - 330, "MYTH", seg(u, .25, .7))
    elif i == 2:
        eye(P, 290, CENTER - 120, 150, [(220, 50, 50), (60, 170, 80), (60, 120, 255)], seg(u, .2, 1.6))
        eye(P, 790, CENTER - 120, 150, [(255, 200, 40), (60, 120, 255)], seg(u, 1.5, 2.9))
        P.text(290, CENTER + 280, "you", 60, CLOUD); P.text(790, CENTER + 280, "dog", 60, GLIM)
    elif i == 3:
        k = eio(seg(u, 1.0, 2.5))
        cols = [(220, 50, 50), (255, 140, 30), (255, 220, 50), (60, 170, 80), (60, 120, 255), (140, 70, 200)]
        dogv = [(120, 110, 80), (170, 150, 70), (220, 200, 90), (160, 150, 110), (70, 110, 220), (80, 100, 200)]
        for j, (c, d) in enumerate(zip(cols, dogv)):
            P.rrect(140 + j * 135, CENTER - 200, 260 + j * 135, CENTER + 200, 20, lc(c, d, k))
        P.badge(540, CENTER + 330, "dog view", 60, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
    elif i == 4:
        side = 1 if u > 2.6 else 0
        grass(P, col=(80, 170, 80) if not side else (150, 145, 100))
        ball(P, 380, CENTER + 300, 55, (220, 50, 50) if not side else (130, 120, 90))
        ball(P, 720, CENTER + 300, 55, (60, 120, 255) if not side else (70, 110, 220))
        dog(P, 560, CENTER + 20, .8, t, tilt=1)
        P.badge(540, CENTER - 330, "you see" if not side else "your dog sees", 60, NIGHT, GLIM, 1)
    else:
        grass(P); dog(P, 480, CENTER + 60, 1.0, t)
        ball(P, 820, CENTER + 200, 70, (255, 210, 40)); ball(P, 700, CENTER + 250, 45, (60, 120, 255))
        P.stamp(540, CENTER - 330, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
