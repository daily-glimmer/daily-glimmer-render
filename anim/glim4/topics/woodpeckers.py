# Thema: Why don't woodpeckers get headaches?
CENTER = 1050
RED, BLK, WHT, BARK = (220, 50, 50), (35, 35, 40), (245, 245, 240), (130, 90, 60)
PAL = ((140, 200, 230), (200, 230, 190))
HI = {"headaches?", "twenty", "second,", "thousands", "cushion", "shock.", "2022", "stiff", "hammer.", "tiny,", "small", "brains", "safe"}
WOW = (1, 3, 4)

def trunk(P, x=820, top=620):
    P.rrect(x - 110, CENTER - top, x + 110, CENTER + 560, 40, BARK)
    for k in range(7): P.line([(x - 70 + (k % 3) * 50, CENTER - top + 100 + k * 150), (x - 60 + (k % 3) * 50, CENTER - top + 160 + k * 150)], lc(BARK, (0, 0, 0), .3), 6)

def wpecker(P, x, y, s, t, peck=0.):
    a = peck * .35
    P.ell(x, y + 40 * s, 70 * s, 130 * s, BLK)
    P.ell(x - 20 * s, y + 60 * s, 40 * s, 90 * s, WHT)
    P.poly([(x + 20 * s, y + 150 * s), (x + 50 * s, y + 260 * s), (x - 10 * s, y + 170 * s)], BLK)
    hx, hy = x + 40 * s * math.cos(a), y - 90 * s
    P.circ(hx, hy, 52 * s, BLK); P.circ(hx - 6 * s, hy - 24 * s, 34 * s, RED)
    P.ell(hx + 4 * s, hy + 12 * s, 30 * s, 16 * s, WHT)
    P.circ(hx + 18 * s, hy - 4 * s, 9 * s, WHT); P.circ(hx + 20 * s, hy - 4 * s, 5 * s, NIGHT)
    P.poly([(hx + 44 * s, hy - 8 * s), (hx + 44 * s, hy + 12 * s), (hx + (110 + 20 * peck) * s, hy + 4 * s)], (90, 90, 95))

def SC(i, P, t, u):
    if i == 0:
        trunk(P); pk = max(0., math.sin(t * 14)) if u > .8 else 0
        wpecker(P, 560 + 40 * pk, CENTER, 1.4, t, pk)
        P.text(300, CENTER - 300, "?", 150 * back(seg(u, .5, 1.0)), HOOK)
    elif i == 1:
        trunk(P); pk = max(0., math.sin(t * 22))
        wpecker(P, 560 + 40 * pk, CENTER, 1.3, t, pk)
        if pk > .8:
            for k in range(5): P.line([(720, CENTER - 110 + k * 22 - 44), (690 - k * 6, CENTER - 140 + k * 25)], GLIM, 5)
        P.badge(330, CENTER - 300, "20x / second", 60, HOOK, CLOUD, back(seg(u, .5, 1.0)))
        P.badge(330, CENTER + 380, "thousands a day", 52, NIGHT, GLIM, back(seg(u, 2.2, 2.7)))
    elif i == 2:
        P.circ(540, CENTER - 20, 230, (240, 230, 220), outline=(170, 160, 150), w=8)
        for k in range(14):
            a = k * .45 + t * .4
            P.circ(540 + math.cos(a) * 170, CENTER - 20 + math.sin(a) * 170, 30, (250, 210, 180))
        P.circ(540, CENTER - 20, 110, (240, 170, 170))
        P.badge(540, CENTER + 340, "soft cushion?", 60, NIGHT, GLIM, back(seg(u, .8, 1.3)))
        P.text(860, CENTER - 250, "?", 120 * back(seg(u, 1.6, 2.0)), HOOK)
    elif i == 3:
        trunk(P)
        pk = max(0., math.sin(t * 6)); wpecker(P, 560 + 40 * pk, CENTER, 1.3, t, pk)
        P.rrect(140, CENTER - 360, 420, CENTER - 260, 20, NIGHT)
        P.circ(190, CENTER - 310, 18, HOOK if int(t * 2) % 2 else (90, 30, 30)); P.text(305, CENTER - 310, "SLOW-MO", 44, CLOUD)
        P.badge(330, CENTER + 380, "stiff like a hammer", 54, HOOK, CLOUD, back(seg(u, 1.6, 2.1)))
    elif i == 4:
        q = back(seg(u, .3, .8)); q2 = back(seg(u, 1.0, 1.5))
        P.circ(330, CENTER - 20, 160 * q, (240, 170, 170), outline=(180, 110, 110), w=6)
        for k in range(5): P.arc(330, CENTER - 20, (40 + k * 25) * q, 200 + k * 20, 320 + k * 20, (200, 120, 120), 6)
        P.circ(770, CENTER + 80, 34 * q2, (240, 170, 170), outline=(180, 110, 110), w=4)
        P.badge(330, CENTER + 220, "big brain", 46, NIGHT, CLOUD, q); P.badge(770, CENTER + 220, "tiny brain", 46, NIGHT, CLOUD, q2)
        P.check(770, CENTER - 120, 60, HOPE, back(seg(u, 2.4, 2.9)))
        P.badge(540, CENTER + 380, "small = safer", 60, HOPE, CLOUD, back(seg(u, 2.8, 3.3)))
    else:
        trunk(P, top=440)
        pk = max(0., math.sin(t * 16)); wpecker(P, 560 + 40 * pk, CENTER + 60, 1.2, t, pk)
        for k in range(3):
            nx, ny = 300 + k * 90, CENTER - 140 - 30 * math.sin(t * 3 + k)
            P.ell(nx, ny, 22, 16, NIGHT); P.line([(nx + 18, ny), (nx + 18, ny - 80)], NIGHT, 8); P.line([(nx + 18, ny - 80), (nx + 44, ny - 60)], NIGHT, 8)
        P.badge(400, CENTER + 400, "safe & sound", 60, HOPE, CLOUD, back(seg(u, .6, 1.1)))
