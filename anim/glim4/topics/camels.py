# Thema: Do camels store water in their humps?  (Mythos-Format, Stempel in Satz 1)
CENTER = 1050
SAND, SAND2, CAMEL, CAMEL2 = (238, 196, 120), (220, 170, 95), (205, 150, 85), (175, 120, 65)
PAL = ((70, 40, 60), (230, 140, 80))
HI = {"humps?", "fat,", "eighty", "pounds", "energy", "backpack", "blood:", "oval", "hundred", "liters", "lunchbox,", "myth"}
WOW = (1,)

def dunes(P, t, y=CENTER + 260):
    P.ell(250, y + 240, 520, 260, SAND2); P.ell(860, y + 280, 560, 300, SAND)
    P.poly([(0, y + 200), (W, y + 160), (W, H), (0, H)], SAND)

def sun(P, x, y, r):
    P.circ(x, y, r, (255, 214, 110), glow=mul(GLIM, 150))

def camel(P, x, y, s, t, walk=True, hump_fill=None, flip=1, head_down=0.):
    f = flip; ph = t * 5 if walk else 0
    for k, dx in enumerate((-95, -55, 70, 110)):          # Beine mit Kniegelenk
        sw = math.sin(ph + k * math.pi / 2) * 22 * s if walk else 0
        kx, ky = x + f * dx * s + sw * .5, y + 120 * s
        P.line([(x + f * dx * s, y + 40 * s), (kx, ky), (kx + sw, y + 215 * s)], CAMEL2, 20 * s)
    P.line([(x - f * 150 * s, y - 10 * s), (x - f * 175 * s, y + 70 * s + math.sin(t * 3) * 6 * s)], CAMEL2, 10 * s)  # Schwanz
    P.ell(x, y, 165 * s, 80 * s, CAMEL)                     # Körper
    P.ell(x, y - 70 * s, 95 * s, 85 * s, CAMEL)             # Höcker
    if hump_fill: hump_fill(P, x, y - 75 * s, s)
    hy = head_down * 150 * s
    P.line([(x + f * 130 * s, y - 20 * s), (x + f * 205 * s, y - 120 * s + hy * .6), (x + f * 235 * s, y - 175 * s + hy)], CAMEL, 46 * s)   # Hals
    hx, hhy = x + f * 255 * s, y - 185 * s + hy
    P.ell(hx, hhy, 55 * s, 34 * s, CAMEL)                   # Kopf
    P.ell(hx + f * 45 * s, hhy + 10 * s, 26 * s, 22 * s, CAMEL2)
    P.circ(hx + f * 5 * s, hhy - 12 * s, 7 * s, NIGHT); P.circ(hx + f * 8 * s, hhy - 15 * s, 2.5 * s, (255, 255, 255))
    P.ell(hx - f * 25 * s, hhy - 35 * s, 10 * s, 16 * s, CAMEL2)

def drop(P, x, y, r, col=(80, 170, 255)):
    P.circ(x, y + r * .3, r, col); P.poly([(x - r * .82, y), (x + r * .82, y), (x, y - r * 1.5)], col)

def SC(i, P, t, u):
    if i == 0:
        sun(P, 820, CENTER - 330, 90); dunes(P, t)
        camel(P, 520 + math.sin(t * .5) * 40, CENTER + 120, 1.15, t)
        k = back(seg(u, .4, .9))
        if k > .02:
            drop(P, 520 + math.sin(t * .5) * 40, CENTER - 140, 60 * k)
            P.text(520 + math.sin(t * .5) * 40, CENTER - 300, "?", 150 * k, GLIM)
    elif i == 1:
        dunes(P, t)
        k = eout(seg(u, .2, 1.2))
        def fill(P, x, y, s):
            P.ell(x, y + 10 * s, 78 * s * k, 66 * s * k, (255, 222, 140), outline=(230, 180, 80), w=4)
            for j in range(5):
                a = j * 1.3 + t; P.circ(x + math.cos(a) * 40 * s * k, y + math.sin(a) * 30 * s * k, 14 * s * k, (255, 240, 190))
        camel(P, 540, CENTER + 140, 1.35, t, walk=False, hump_fill=fill)
        drop(P, 250, CENTER - 160, 70)
        P.cross(250, CENTER - 175, 80, k=back(seg(u, .3, .8)))
        P.badge(540, CENTER + 470, "FAT, not water", 64, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
        P.stamp(780, CENTER - 200, "MYTH", seg(u, .25, .7))
    elif i == 2:
        sun(P, 200, CENTER - 360, 70); dunes(P, t, CENTER + 200)
        def pack(P, x, y, s):
            P.rrect(x - 60 * s, y - 40 * s, x + 60 * s, y + 50 * s, 18 * s, HOPE, outline=(20, 130, 80), w=5)
            P.poly([(x + 6 * s, y - 28 * s), (x - 20 * s, y + 12 * s), (x + 2 * s, y + 12 * s), (x - 8 * s, y + 42 * s), (x + 26 * s, y - 2 * s), (x + 4 * s, y - 2 * s)], GLIM)
        x = lerp(-150, 1230, (u / 5.5) % 1)
        camel(P, x, CENTER + 110, 1.0, t, hump_fill=pack)
        for j in range(4): P.circ(x - 230 - j * 70, CENTER + 330, 10, SAND2)   # Fußspuren
        P.badge(540, CENTER + 470, "energy reserve", 62, HOPE, CLOUD, back(seg(u, .5, 1.0)))
    elif i == 3:
        P.rrect(60, CENTER - 210, 1020, CENTER + 210, 200, (150, 40, 60), outline=(110, 20, 40), w=10)   # Blutgefäß
        P.rrect(80, CENTER - 185, 1000, CENTER + 185, 180, (255, 210, 200))
        for j in range(9):
            x = (j * 150 + u * 260) % 1200 - 60; y = CENTER - 90 + (j % 3) * 90
            P.ell(x, y, 62, 30, (220, 40, 60), outline=(170, 20, 40), w=4)
        P.badge(300, CENTER - 300, "camel: oval", 52, HOOK, CLOUD, back(seg(u, .4, .9)))
        P.badge(540, CENTER + 330, "slips through thick blood", 46, NIGHT, CLOUD, back(seg(u, 2.0, 2.5)))
    elif i == 4:
        P.poly([(0, CENTER + 220), (W, CENTER + 220), (W, H), (0, H)], SAND)
        P.ell(540, CENTER + 330, 420, 70, (70, 160, 230))                                  # Oase
        for x in (170, 920):
            P.line([(x, CENTER + 260), (x + 20, CENTER - 120)], (140, 100, 60), 26)
            for a in range(5): P.line([(x + 20, CENTER - 120), (x + 20 + math.cos(a * 1.2 + 3.6) * 150, CENTER - 120 + math.sin(a * 1.2 + 3.6) * 70 + 40)], (60, 160, 80), 22)
        camel(P, 470, CENTER + 60, .95, t, walk=False, head_down=.9 + math.sin(t * 4) * .05)
        k = eio(seg(u, .3, 4.5))
        P.rrect(760, CENTER - 330, 900, CENTER + 60, 30, (240, 245, 255), outline=(150, 170, 200), w=8)
        P.rrect(772, CENTER + 48 - 370 * k, 888, CENTER + 48, 22, (80, 170, 255))
        P.text(830, CENTER - 400, f"{int(100 * k)} L", 90, CLOUD)
        P.badge(400, CENTER - 330, "in 10 minutes!", 58, HOOK, CLOUD, back(seg(u, 1.0, 1.5)))
    else:
        dunes(P, t)
        def box(P, x, y, s):
            P.rrect(x - 70 * s, y - 35 * s, x + 70 * s, y + 45 * s, 14 * s, (255, 120, 150), outline=(200, 70, 100), w=5)
            P.rrect(x - 25 * s, y - 55 * s, x + 25 * s, y - 35 * s, 8 * s, (200, 70, 100))
        camel(P, 420, CENTER + 140, 1.1, t, walk=False, hump_fill=box)
        P.check(420, CENTER - 230, 60, k=back(seg(u, .2, .7)))
        P.rrect(790, CENTER - 140, 890, CENTER + 120, 30, (120, 190, 255), outline=(60, 120, 200), w=6)
        P.rrect(815, CENTER - 190, 865, CENTER - 140, 10, (60, 120, 200))
        P.cross(840, CENTER - 10, 80, k=back(seg(u, .9, 1.4)))
