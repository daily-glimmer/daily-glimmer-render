# Thema: Can hippos swim?  (Mythos-Format: „NOPE“ / „FACT“)
CENTER = 1050
HIP, HIP2, PINK = (130, 110, 140), (105, 88, 115), (225, 150, 160)
PAL = ((20, 80, 110), (15, 45, 70))
HI = {"swim?", "heavy", "float.", "dense", "sink,", "bounce", "bottom.", "five", "minutes,", "sleep", "underwater", "moonwalks"}
WOW = (1, 4)
SURF, BED = CENTER - 250, CENTER + 360

def water(P, t):
    P.rrect(-20, SURF, W + 20, H + 20, 0, (40, 120, 160))
    for k in range(9):
        x = k * 135 + (t * 40) % 135; P.arc(x, SURF + 6, 40, 200, 340, (150, 210, 235), 6)
    P.poly([(0, BED), (W, BED - 30), (W, H), (0, H)], (120, 100, 70))
    for x in (160, 470, 820): P.ell(x, BED + 40, 60, 18, (100, 82, 58))

def bubbles(P, t, x, y):
    for k in range(4):
        q = (t * .6 + k / 4) % 1; P.circ(x + math.sin(q * 9 + k) * 20, lerp(y, SURF + 20, q), 8 + k * 3, (170, 220, 245))

def hippo(P, x, y, s, t, sleepy=False, flip=1):
    f = flip
    for dx in (-90, -30, 50, 110):
        P.rrect(x + dx * s - 22 * s, y + 40 * s, x + dx * s + 22 * s, y + 120 * s, 14 * s, HIP2)
    P.ell(x, y, 190 * s, 110 * s, HIP)
    P.ell(x + f * 30 * s, y + 40 * s, 140 * s, 50 * s, lc(HIP, PINK, .35))
    hx = x - f * 190 * s; hy = y - 30 * s
    P.ell(hx - f * 40 * s, hy + 30 * s, 95 * s, 65 * s, lc(HIP, PINK, .25))
    P.ell(hx + f * 10 * s, hy - 20 * s, 80 * s, 62 * s, HIP)
    for ex in (-20, 30):
        P.ell(hx + f * ex * s, hy - 82 * s, 14 * s, 20 * s, HIP2)
    for ex in (-10, 30):
        if sleepy: P.arc(hx + f * ex * s, hy - 52 * s, 9 * s, 20, 160, NIGHT, 4 * s)
        else: P.circ(hx + f * ex * s, hy - 50 * s, 10 * s, NIGHT); P.circ(hx + f * ex * s + 3 * s, hy - 53 * s, 3 * s, CLOUD)
    for nx in (-90, -55): P.circ(hx + f * nx * s, hy + 4 * s, 7 * s, NIGHT)
    P.arc(hx - f * 45 * s, hy + 50 * s, 30 * s, 20, 160, NIGHT, 4 * s)

def SC(i, P, t, u):
    if i == 0:
        water(P, t); hippo(P, 540, SURF + 40 + math.sin(t * 1.5) * 10, 1.2, t)
        P.text(820, SURF - 190, "?", 140 * back(seg(u, .4, .9)), GLIM)
    elif i == 1:
        water(P, t); y = lerp(SURF + 40, BED - 120, eio(seg(u, .3, 2.2)))
        hippo(P, 540, y, 1.1, t); bubbles(P, t, 380, y - 80)
        P.badge(540, BED + 110, "1.5 to 3 tonnes", 54, NIGHT, GLIM, back(seg(u, 1.6, 2.1)))
        P.stamp(540, SURF - 210, "NOPE", seg(u, .25, .7))
    elif i == 2:
        water(P, t); x = lerp(900, 200, (u / 6) % 1); hop = abs(math.sin(u * 2.4)) * 160
        hippo(P, x, BED - 120 - hop, 1.0, t)
        if hop < 20: P.ell(x, BED - 4, 160, 20, (150, 130, 95))
        P.badge(540, BED + 110, "walk & bounce", 60, NIGHT, GLIM, back(seg(u, .5, 1.0)))
    elif i == 3:
        water(P, t)
        k = seg(u, .2, 3.0); P.circ(780, SURF + 260, 110, (20, 60, 90), outline=CLOUD, w=8)
        P.arc(780, SURF + 260, 90, -90, -90 + 360 * k, GLIM, 22)
        P.text(780, SURF + 260, "5 min", 54, CLOUD)
        up = eio(seg(u, 3.0, 4.2)); hippo(P, 360, lerp(BED - 120, SURF + 40, up), .9, t)
        if up > .9: bubbles(P, t, 200, SURF + 40)
    elif i == 4:
        water(P, t); q = (u % 4) / 4; up = math.sin(q * math.pi) ** 4
        hippo(P, 540, lerp(BED - 120, SURF + 40, up), 1.0, t, sleepy=True)
        for j in range(3):
            kk = back(seg(u, .3 + j * .3, .6 + j * .3)); P.text(700 + j * 60, CENTER - 60 - j * 70 - up * 300, "z", (50 + j * 15) * kk, CLOUD)
    else:
        water(P, t); x = lerp(850, 250, (u / 6) % 1); hop = abs(math.sin(u * 2.4)) * 150
        hippo(P, x, BED - 120 - hop, .95, t)
        P.stamp(540, SURF + 110, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
