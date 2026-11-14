# Thema: Do chameleons change color to blend in?  (Mythos-Format)
CENTER = 1050
PAL = ((20, 50, 40), (90, 160, 110))
HI = {"blend", "in?", "myth.", "talk:", "stay", "away,", "thermostat:", "darker", "lighter", "crystals", "mood", "ring!"}
WOW = (1, 4)

def branch(P, y=CENTER + 180):
    P.line([(0, y + 40), (1080, y - 20)], (110, 75, 45), 34)
    for k in range(4): P.ell(130 + k * 270, y - 10 - (k % 2) * 30, 80, 30, (60, 140, 80))

def cham(P, x, y, s, t, col, eye_rot=0., stripes=None):
    dark = lc(col, (0, 0, 0), .3)
    for k in range(10):                                  # Ringelschwanz
        a = k * .55 + 1.2; r = (110 - k * 9) * s
        P.circ(x + 150 * s + math.cos(a) * r * .6, y + 40 * s + math.sin(a) * r * .6, (26 - k * 1.6) * s, col)
    for dx in (-70, 70): P.line([(x + dx * s, y + 40 * s), (x + dx * s + 15 * s, y + 130 * s)], dark, 18 * s)
    P.ell(x, y, 150 * s, 75 * s, col)
    P.poly([(x - 120 * s, y - 50 * s), (x + 120 * s, y - 60 * s), (x, y - 95 * s)], dark)       # Rückenkamm
    if stripes:
        for k in range(4): P.line([(x - 80 * s + k * 50 * s, y - 50 * s), (x - 70 * s + k * 50 * s, y + 55 * s)], stripes, 14 * s)
    hx, hy = x - 170 * s, y - 20 * s
    P.poly([(hx + 60 * s, hy - 60 * s), (hx - 60 * s, hy - 10 * s), (hx - 50 * s, hy + 40 * s), (hx + 70 * s, hy + 50 * s)], col)
    P.poly([(hx + 60 * s, hy - 60 * s), (hx + 10 * s, hy - 95 * s), (hx - 30 * s, hy - 30 * s)], dark)
    P.circ(hx, hy - 5 * s, 32 * s, dark); P.circ(hx, hy - 5 * s, 22 * s, (250, 250, 230))
    a = eye_rot + math.sin(t * 1.7) * .8; P.circ(hx + math.cos(a) * 9 * s, hy - 5 * s + math.sin(a) * 9 * s, 9 * s, NIGHT)

def SC(i, P, t, u):
    G, R, Y, B = (90, 190, 90), (240, 80, 60), (250, 200, 50), (60, 160, 230)
    if i == 0:
        P.rrect(100, CENTER - 420, 980, CENTER + 120, 40, (230, 120, 170))     # pinker Vorhang-Test
        for k in range(6): P.line([(160 + k * 150, CENTER - 420), (160 + k * 150, CENTER + 120)], (210, 90, 150), 16)
        branch(P); cham(P, 560, CENTER + 90, 1.2, t, G)
        P.text(560, CENTER - 160, "?", 150 * back(seg(u, .4, .9)), GLIM)
    elif i == 1:
        branch(P); cham(P, 560, CENTER + 90, 1.3, t, G)
        P.stamp(540, CENTER - 330, "MYTH", seg(u, .25, .7))
    elif i == 2:
        branch(P)
        k = eio(seg(u, .5, 2.0))
        cham(P, 330, CENTER + 90, .9, t, lc(G, R, k), stripes=lc(G, Y, k))
        cham(P, 820, CENTER + 60, .8, t, lc(G, (240, 150, 200), eio(seg(u, 2.5, 3.8))), eye_rot=3.1)
        P.badge(330, CENTER - 250, "stay away!", 54, HOOK, CLOUD, back(seg(u, 1.0, 1.5)))
        P.badge(800, CENTER - 250, "I like you", 54, (220, 110, 170), CLOUD, back(seg(u, 3.0, 3.5)))
    elif i == 3:
        hot = u > 2.4
        P.circ(860, CENTER - 360, 100 if hot else 50, (255, 210, 90), glow=mul(GLIM, 200 if hot else 60))
        branch(P)
        k = eio(seg(u, .3, 1.5)) if not hot else 1 - eio(seg(u, 2.6, 3.8))
        cham(P, 540, CENTER + 90, 1.2, t, lc((150, 220, 140), (40, 80, 50), k))
        P.circ(160, CENTER - 200, 60, (240, 240, 250), outline=(150, 150, 170), w=6)
        P.rrect(140, CENTER - 360, 180, CENTER - 200, 18, (240, 240, 250), outline=(150, 150, 170), w=6)
        P.rrect(150, CENTER - 300 + (0 if hot else 70), 170, CENTER - 210, 8, HOOK if hot else B)
        P.badge(540, CENTER + 470, "cold: dark   hot: light", 52, NIGHT, CLOUD, 1)
    elif i == 4:
        P.rrect(120, CENTER - 300, 960, CENTER + 300, 50, (25, 35, 60), outline=(90, 110, 150), w=8)
        gap = 1 + .6 * (math.sin(u * 1.8) + 1) / 2
        col = lc(B, R, (math.sin(u * 1.8) + 1) / 2)
        for r_ in range(5):
            for c_ in range(6):
                P.circ(540 + (c_ - 2.5) * 70 * gap, CENTER + (r_ - 2) * 70 * gap, 22, (210, 220, 235))
        for k in range(4):
            q = (t + k / 4) % 1; P.line([(150 + q * 300, CENTER - 280 + q * 200), (190 + q * 300, CENTER - 250 + q * 200)], col, 10, glow=mul(col, 200))
        P.badge(540, CENTER + 400, "nano-crystals", 60, NIGHT, GLIM, back(seg(u, .5, 1.0)))
    else:
        branch(P)
        cols = [G, Y, R, B, (200, 120, 220)]
        c = lc(cols[int(u / .9) % 5], cols[(int(u / .9) + 1) % 5], (u / .9) % 1)
        cham(P, 540, CENTER + 90, 1.25, t, c)
        P.stamp(540, CENTER - 330, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
