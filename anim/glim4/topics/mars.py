# Thema: Why is Mars red?
CENTER = 1050
MR, MR2, MR3 = (205, 90, 55), (150, 60, 40), (235, 140, 90)
PAL = ((14, 20, 45), (40, 30, 70))
HI = {"mars", "red?", "dust", "iron.", "iron", "water", "oxygen", "rust.", "storms", "rusty", "2025", "wetter.", "blue!", "planet?"}
WOW = (2, 5)

def stars(P, t):
    for k in range(40):
        x, y = (k * 263) % 1080, 150 + (k * 397) % 1700
        P.circ(x, y, 3 + (k % 3) * 2 * (.6 + .4 * math.sin(t * 2 + k)), CLOUD)

def planet(P, x, y, r, col=MR, rust=1.):
    c = lc((120, 120, 130), col, rust)
    P.circ(x, y, r, c, outline=lc((80, 80, 90), MR2, rust), w=6)
    for k, (dx, dy, rr) in enumerate(((-.35, -.2, .18), (.25, .3, .14), (.4, -.35, .1), (-.1, .45, .12))):
        P.circ(x + dx * r, y + dy * r, rr * r, lc((90, 90, 100), MR2, rust))
    P.ell(x, y - r * .82, r * .35, r * .1, CLOUD)

def rock(P, x, y, s, rust):
    c = lc((130, 130, 140), MR, rust)
    P.poly([(x - 80 * s, y + 40 * s), (x - 60 * s, y - 40 * s), (x + 10 * s, y - 70 * s), (x + 80 * s, y - 20 * s), (x + 70 * s, y + 40 * s)], c, outline=lc((70, 70, 80), MR2, rust), w=5 * s)

def SC(i, P, t, u):
    stars(P, t)
    if i == 0:
        planet(P, 540, CENTER + 60, 300 * eout(seg(u, 0, .8)) + 5)
        P.text(900, CENTER - 300, "?", 150 * back(seg(u, .4, .9)), HOOK)
    elif i == 1:
        P.rrect(-20, CENTER + 200, W + 20, H + 20, 0, MR)
        for k in range(3): rock(P, 240 + k * 300, CENTER + 220, 1.2 - .2 * k, 1)
        P.badge(540, CENTER - 40, "Fe = iron", 70, NIGHT, GLIM, back(seg(u, .8, 1.3)))
    elif i == 2:
        r = eio(seg(u, .6, 3.0))
        rock(P, 540, CENTER + 60, 2.6, r)
        for k in range(4):
            q = (u * .8 + k / 4) % 1
            P.circ(260 + k * 60, CENTER - 200 + q * 180, 18, (120, 180, 240))
        P.badge(300, CENTER + 330, "water", 52, (50, 110, 190), CLOUD, back(seg(u, .4, .8)))
        P.badge(780, CENTER + 330, "oxygen", 52, HOPE, CLOUD, back(seg(u, .9, 1.3)))
        P.badge(540, CENTER - 330, "= rust", 64, HOOK, CLOUD, back(seg(u, 2.4, 2.9)))
    elif i == 3:
        planet(P, 540, CENTER + 60, 300)
        for k in range(14):
            a = t * .8 + k * .45
            rr = 330 + 40 * math.sin(t * 2 + k)
            P.circ(540 + math.cos(a) * rr, CENTER + 60 + math.sin(a) * rr * .4, 16 + k % 3 * 8, MR3)
        P.badge(540, CENTER + 460, "dust storms", 60, NIGHT, GLIM, back(seg(u, .8, 1.3)))
    elif i == 4:
        P.rrect(-20, CENTER + 200, W + 20, H + 20, 0, MR)
        k = eout(seg(u, .4, 2.0))
        P.ell(540, CENTER + 260, 380 * k + 1, 70 * k + 1, (70, 140, 210))
        P.line([(200, CENTER + 200), (330, CENTER + 120), (470, CENTER + 180), (620, CENTER + 90), (880, CENTER + 200)], MR2, 10)
        P.badge(540, CENTER - 200, "2025 study", 60, NIGHT, GLIM, back(seg(u, .3, .8)))
        P.badge(540, CENTER + 460, "once wetter", 58, HOPE, CLOUD, back(seg(u, 2.2, 2.7)))
    else:
        P.rrect(-20, CENTER - 340, W + 20, CENTER + 200, 0, (40, 70, 130))
        P.circ(540, CENTER + 120, 70, (190, 220, 255), glow=(120, 170, 255))
        P.rrect(-20, CENTER + 150, W + 20, H + 20, 0, MR)
        P.badge(540, CENTER - 240, "blue sunset", 58, NIGHT, GLIM, back(seg(u, .8, 1.3)))
