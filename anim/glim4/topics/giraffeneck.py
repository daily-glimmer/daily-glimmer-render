# Thema: Does a giraffe have more neck bones than you?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6) – Giraffe aus giraffes.py
CENTER = 1050
exec(open(os.path.join(HERE, "topics", "giraffes.py")).read(), globals())
PAL = ((235, 170, 90), (250, 215, 150))
HI = {"more", "neck", "bones", "myth!", "seven", "mice", "whales.", "twenty", "five", "centimeters", "two", "meters", "super-sized!"}
WOW = (1,)
BONE = (250, 244, 228)

def savanna(P, t):
    P.poly([(0, GROUND), (W, GROUND - 20), (W, H), (0, H)], (200, 160, 80))
    for x, s in ((120, 1.), (960, .8)):
        P.line([(x, GROUND), (x + 10, GROUND - 240 * s)], (110, 80, 50), 22 * s)
        P.ell(x + 10, GROUND - 260 * s, 140 * s, 40 * s, (90, 140, 70))

def spine(P, x0, y0, x1, y1, n, w, col=BONE, k=1., hl=None):
    for j in range(n):
        q0, q1 = j / n, (j + .68) / n
        if j / n > k: break
        a = (lerp(x0, x1, q0), lerp(y0, y1, q0)); b = (lerp(x0, x1, q1), lerp(y0, y1, q1))
        P.line([a, b], hl if hl and j == n - 1 else col, w)
        P.circ(*a, w * .62, col); P.circ(*b, w * .62, col)

def human(P, x, y, s):
    c = (240, 200, 160)
    P.circ(x, y - 260 * s, 55 * s, c); P.rrect(x - 26 * s, y - 210 * s, x + 26 * s, y - 160 * s, 10 * s, c)
    P.rrect(x - 75 * s, y - 165 * s, x + 75 * s, y + 20 * s, 34 * s, (90, 130, 200))
    P.circ(x - 20 * s, y - 268 * s, 6 * s, NIGHT); P.circ(x + 20 * s, y - 268 * s, 6 * s, NIGHT)

def SC(i, P, t, u):
    if i == 0:
        savanna(P, t); giraffe(P, 430, GROUND + 20, 1.0, t, sleepy=False)
        human(P, 860, GROUND + 20, .9)
        P.text(860, CENTER - 160, "?", 150 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        k = seg(u, .4, 2.2)
        spine(P, 140, CENTER + 260, 520, CENTER - 230, 7, 34, k=k)
        spine(P, 760, CENTER + 260, 760, CENTER + 20, 7, 14, k=k)
        P.badge(330, CENTER + 380, "giraffe: 7", 54, NIGHT, GLIM, back(seg(u, 1.8, 2.3)))
        P.badge(760, CENTER + 380, "you: 7", 54, NIGHT, GLIM, back(seg(u, 2.2, 2.7)))
        P.stamp(800, CENTER - 250, "MYTH", seg(u, .25, .7))
    elif i == 2:
        savanna(P, t)
        for j, (lab, s) in enumerate((("mouse", .5), ("dog", .75), ("whale", 1.0))):
            x = 200 + j * 340; k = back(seg(u, .3 + j * .5, .8 + j * .5))
            P.badge(x, CENTER - 60, lab, 50, NIGHT, CLOUD, k)
            if k > .1: spine(P, x - 90 * s, CENTER + 120, x + 90 * s, CENTER + 120, 7, 12 + 10 * s)
        P.badge(540, CENTER + 330, "all have 7", 58, HOPE, CLOUD, back(seg(u, 1.8, 2.3)))
    elif i == 3:
        P.rrect(120, CENTER - 160, 960, CENTER + 160, 40, (60, 50, 40))
        k = eio(seg(u, .4, 2.6))
        P.line([(200, CENTER), (lerp(200, 880, k), CENTER)], BONE, 70)
        P.circ(200, CENTER, 50, BONE); P.circ(lerp(200, 880, k), CENTER, 50, BONE)
        P.line([(200, CENTER + 110), (880, CENTER + 110)], GLIM, 6)
        P.text(540, CENTER - 300, f"{int(25 * k)} cm", 110, GLIM)
        P.badge(540, CENTER + 330, "per bone!", 56, NIGHT, CLOUD, back(seg(u, 2.4, 2.9)))
    elif i == 4:
        savanna(P, t); giraffe(P, 380, GROUND + 20, 1.05, t, sleepy=False)
        k = eio(seg(u, .5, 2.5))
        P.line([(780, GROUND - 330), (780, lerp(GROUND - 330, CENTER - 450, k))], GLIM, 10)
        P.line([(740, CENTER - 450), (820, CENTER - 450)], GLIM, 8)
        P.badge(780, CENTER - 120, "~2 m", 60, NIGHT, GLIM, back(seg(u, 2.0, 2.5)))
    else:
        savanna(P, t); giraffe(P, 360, GROUND + 20, .95, t, sleepy=False)
        human(P, 820, GROUND + 20, .85)
        P.stamp(800, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
