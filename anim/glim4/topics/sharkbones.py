# Thema: Do sharks have bones?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6) – Hai aus sharks.py
CENTER = 1050
exec(open(os.path.join(HERE, "topics", "sharks.py")).read(), globals())
PAL = ((10, 50, 100), (30, 120, 160))
HI = {"bones?", "myth!", "cartilage,", "bone.", "bendy", "nose", "ears.", "half", "dense", "light", "oily", "liver", "teeth!"}
WOW = (1,)
CART = (180, 225, 235)

def xray_shark(P, x, y, s, t, k=1.):
    shark(P, x, y, s, t)
    if k > .02:
        P.ell(x, y, 170 * s * k, 45 * s * k, (20, 40, 70))
        P.line([(x - 150 * s * k, y), (x + 160 * s * k, y)], CART, 12 * s)
        for j in range(9): P.line([(x - 120 * s * k + j * 32 * s * k, y - 30 * s * k), (x - 120 * s * k + j * 32 * s * k, y + 30 * s * k)], CART, 6 * s)

def face(P, x, y, s, hl=0.):
    c = (240, 200, 165)
    P.circ(x, y, 150 * s, c); P.circ(x - 150 * s, y, 40 * s, c); P.circ(x + 150 * s, y, 40 * s, c)
    P.poly([(x, y - 30 * s), (x - 30 * s, y + 50 * s), (x + 30 * s, y + 50 * s)], lc(c, (0, 0, 0), .1))
    if hl > 0:
        P.circ(x, y + 40 * s, 26 * s * hl, CART, glow=mul(CART, 120)); P.circ(x - 150 * s, y, 26 * s * hl, CART, glow=mul(CART, 120)); P.circ(x + 150 * s, y, 26 * s * hl, CART, glow=mul(CART, 120))
    for ex in (-50, 50): P.circ(x + ex * s, y - 30 * s, 12 * s, NIGHT)

def SC(i, P, t, u):
    if i == 0:
        bubbles(P, t); seafloor(P); shark(P, 540 + math.sin(t * .7) * 60, CENTER - 20, 1.3, t)
        P.text(820, CENTER - 280, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        bubbles(P, t); seafloor(P); xray_shark(P, 540, CENTER - 20, 1.4, t, eout(seg(u, .4, 1.4)))
        P.stamp(780, CENTER - 290, "MYTH", seg(u, .25, .7))
        P.badge(540, CENTER + 230, "cartilage", 62, NIGHT, CLOUD, back(seg(u, 1.6, 2.1)))
    elif i == 2:
        face(P, 540, CENTER, 1.4, hl=back(seg(u, .5, 1.0)))
        P.badge(540, CENTER + 330, "same bendy stuff", 58, NIGHT, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 3:
        P.line([(160, CENTER + 120), (920, CENTER + 120)], CLOUD, 10); P.poly([(520, CENTER + 120), (560, CENTER + 120), (540, CENTER + 220)], CLOUD)
        k = eio(seg(u, .5, 2.0)); tilt = 60 * k
        P.rrect(200, CENTER + 120 - tilt - 120, 380, CENTER + 120 - tilt, 20, CART)
        P.rrect(700, CENTER + 120 + tilt - 120, 880, CENTER + 120 + tilt, 20, (245, 240, 225))
        P.badge(290, CENTER - 260, "cartilage", 46, NIGHT, CLOUD, 1.); P.badge(790, CENTER - 140, "bone", 46, NIGHT, CLOUD, 1.)
        P.badge(540, CENTER + 400, "half as dense", 60, HOOK, CLOUD, back(seg(u, 2.0, 2.5)))
    elif i == 4:
        bubbles(P, t); seafloor(P)
        x = 540 + math.sin(t * 1.2) * 120
        shark(P, x, CENTER - 20 + math.sin(t * 2.4) * 40, 1.3, t)
        P.ell(x + 10, CENTER + 10, 70, 22, (255, 210, 90))
        P.badge(540, CENTER + 260, "oily liver floats", 56, NIGHT, GLIM, back(seg(u, .6, 1.1)))
    else:
        bubbles(P, t); seafloor(P); shark(P, 520, CENTER, 1.3, t)
        for j in range(5): P.poly([(330 + j * 25, CENTER + 220), (342 + j * 25, CENTER + 190), (354 + j * 25, CENTER + 220)], CLOUD)
        P.stamp(780, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
