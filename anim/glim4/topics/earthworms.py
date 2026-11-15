# Thema: Do earthworms really become two worms when cut in half?  (Mythos-Format)
CENTER = 1050
WORM, WORM2, BAND = (230, 140, 140), (200, 105, 115), (215, 95, 110)
SOIL, SOIL2 = (120, 85, 60), (95, 65, 45)
PAL = ((140, 200, 160), (170, 130, 95))
HI = {"two", "half?", "myth!", "brain", "five", "pairs", "hearts.", "front", "new", "tail.", "head,", "dies.", "flatworms", "whole", "body"}
WOW = (1, 5)

def soil(P, t):
    P.rrect(-40, CENTER + 200, W + 40, H, 0, SOIL)
    for k in range(18):
        x = (k * 137) % W; y = CENTER + 260 + (k * 71) % 260
        P.circ(x, y, 10 + k % 3 * 5, SOIL2)
    for x in (120, 300, 820, 980):
        P.line([(x, CENTER + 200), (x - 10, CENTER + 120)], (80, 150, 70), 10); P.ell(x - 20, CENTER + 110, 30, 14, (90, 170, 80))

def worm(P, x, y, s, t, n=16, a=0, b=None, face=True, gap=0., wig=1., faded=0.):
    """Wurm aus Segmenten; a..b = gezeichnete Segmente (für halbe Würmer), gap = Lücke am Schnitt."""
    b = n if b is None else b
    col, col2 = lc(WORM, (150, 140, 140), faded), lc(WORM2, (130, 120, 120), faded)
    for k in range(b - 1, a - 1, -1):
        px = x + (k - n / 2) * 36 * s + (gap if k >= n // 2 else -gap)
        py = y + math.sin(k * .55 - t * 4) * 22 * s * wig
        r = (26 - abs(k - 4) * .3) * s if k < 6 else 24 * s
        P.circ(px, py, r, BAND if k in (4, 5) else (col if k % 2 else col2))
    if face and a == 0:
        hx = x + (-n / 2) * 36 * s - gap; hy = y + math.sin(-t * 4) * 22 * s * wig
        P.circ(hx - 6 * s, hy - 8 * s, 6 * s, NIGHT); P.arc(hx - 6 * s, hy + 6 * s, 10 * s, 20, 160, NIGHT, 3 * s)

def scissors(P, x, y, s, close=0.):
    for d in (-1, 1):
        a = d * (.5 - .45 * close)
        P.line([(x, y), (x + math.sin(a) * 200 * s, y - math.cos(a) * 200 * s)], (200, 205, 215), 16 * s)
        P.circ(x - math.sin(a) * 70 * s, y + math.cos(a) * 70 * s, 34 * s, None, outline=HOOK, w=12 * s)

def SC(i, P, t, u):
    n = 16; x0 = 540 - 36 * 8
    if i == 0:
        soil(P, t); worm(P, 540, CENTER + 60, 1.4, t)
        P.text(870, CENTER - 260, "?", 150 * back(seg(u, .6, 1.1)), HOOK)
        P.text(540, CENTER - 160, "= 2 ?", 90 * back(seg(u, 1.6, 2.1)), GLIM)
    elif i == 1:
        soil(P, t); worm(P, 540, CENTER + 60, 1.4, t)
        P.stamp(540, CENTER - 200, "MYTH", seg(u, .25, .7))
    elif i == 2:
        soil(P, t); worm(P, 540, CENTER + 80, 1.4, t, wig=.4)
        hx = 540 - 8 * 36 * 1.4
        P.circ(hx + 20, CENTER + 60, 20 * back(seg(u, .3, .8)), GLIM, outline=NIGHT, w=4)
        for k in range(5):
            q = back(seg(u, 1.0 + k * .18, 1.4 + k * .18))
            P.heart(hx + 90 + k * 50, CENTER - 60, 22 * q, HOOK)
        P.badge(320, CENTER - 300, "brain", 56, NIGHT, GLIM, back(seg(u, .4, .9)))
        P.badge(680, CENTER - 300, "5 pairs of hearts", 52, HOOK, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 3:
        soil(P, t)
        gap = 40 * eio(seg(u, .2, .7))
        worm(P, 540, CENTER + 60, 1.3, t, a=0, b=11, gap=gap)
        g = eio(seg(u, .8, 2.6))
        worm(P, 540, CENTER + 60, 1.3, t, a=11, b=11 + int(5 * g), face=False, gap=gap - 10)
        P.badge(540, CENTER - 260, "new tail (sometimes)", 54, HOPE, CLOUD, back(seg(u, 1.6, 2.1)))
    elif i == 4:
        soil(P, t)
        k = eio(seg(u, .2, 1.6))
        worm(P, 540, CENTER + 60, 1.3, t, a=8, b=16, face=False, gap=60, wig=1 - k, faded=k * .7)
        P.circ(540 - 4 * 36 * 1.3, CENTER - 140, 95, (60, 60, 70), outline=CLOUD, w=6)
        P.text(540 - 4 * 36 * 1.3, CENTER - 140, "head?", 36, CLOUD)
        P.cross(540 - 4 * 36 * 1.3, CENTER - 140, 80, HOOK, back(seg(u, 1.2, 1.6)))
    else:
        P.rrect(140, CENTER - 160, 940, CENTER + 260, 40, (120, 190, 220), outline=CLOUD, w=6)    # Wasser-Schale
        for j in range(3):
            fx, fy = 300 + j * 240, CENTER + 50 + math.sin(t * 2 + j) * 20
            k = back(seg(u, .4 + j * .3, .9 + j * .3))
            P.ell(fx, fy, 90 * k, 34 * k, (90, 80, 70)); P.circ(fx - 60 * k, fy, 34 * k, (90, 80, 70))
            if k > .5:
                for d in (-1, 1): P.circ(fx - 60 + d * 12, fy - 8, 7, CLOUD)
        P.stamp(540, CENTER - 300, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
