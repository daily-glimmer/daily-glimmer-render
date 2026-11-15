# Thema: How do bears survive winter without eating?
CENTER = 1050
FUR, FUR2, SNOUT = (110, 75, 50), (85, 55, 35), (190, 150, 110)
PAL = ((12, 22, 50), (50, 70, 110))
HI = {"winter", "eating?", "nonstop", "fat.", "heart", "forty", "eight.", "months", "fat", "recycles", "protein,", "cubs", "sleep!"}
WOW = (2, 4, 5)

def bear(P, x, y, s, t, sleep=0., fat=1.):
    b = 1 + .04 * math.sin(t * (1.0 if sleep > .5 else 2.5))
    P.ell(x, y, 170 * s * fat * b, 120 * s * b, FUR, outline=FUR2, w=4 * s)
    for dx in (-110, 90): P.ell(x + dx * s, y + 100 * s, 45 * s, 30 * s, FUR2)
    hx, hy = x - 170 * s, y - 40 * s + (40 * s if sleep > .5 else 0)
    for ex in (-35, 35): P.circ(hx + ex * s, hy - 60 * s, 26 * s, FUR); P.circ(hx + ex * s, hy - 60 * s, 12 * s, SNOUT)
    P.circ(hx, hy, 72 * s, FUR); P.ell(hx - 30 * s, hy + 20 * s, 38 * s, 28 * s, SNOUT); P.circ(hx - 50 * s, hy + 12 * s, 11 * s, NIGHT)
    if sleep > .5:
        P.arc(hx + 8 * s, hy - 14 * s, 12 * s, 20, 160, NIGHT, 4 * s)
        for k in range(3):
            q = (t * .5 + k / 3) % 1
            P.text(hx + 60 * s + q * 80 * s, hy - 90 * s - q * 160 * s, "z", (40 + 30 * q) * s, CLOUD)
    else:
        P.circ(hx + 8 * s, hy - 14 * s, 9 * s, NIGHT)

def den(P):
    P.ell(540, CENTER + 60, 470, 360, (60, 70, 90)); P.ell(540, CENTER + 90, 410, 300, (30, 35, 50))
    P.ell(540, CENTER + 420, 560, 70, (225, 235, 250))

def berry(P, x, y, r): P.circ(x, y, r, (90, 60, 160)); P.circ(x - r * .3, y - r * .3, r * .3, (170, 150, 220))

def SC(i, P, t, u):
    if i == 0:
        random.seed(4)
        for k in range(22):
            q = (t * .08 + random.random()) % 1
            P.circ(80 + random.random() * 920, lerp(CENTER - 500, CENTER + 500, q), 6 + random.random() * 5, CLOUD)
        den(P); bear(P, 600, CENTER + 120, 1.0, t, sleep=1)
        P.text(840, CENTER - 300, "?", 150 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        fat = 1 + .35 * eio(seg(u, .5, 3.5))
        bear(P, 600, CENTER + 60, 1.1, t, fat=fat)
        for k in range(8):
            q = ((t * .6) + k / 8) % 1
            fx, fy = lerp(120, 360, q), CENTER - 120 + math.sin(q * 6 + k) * 60
            if k % 2: berry(P, fx, fy, 22)
            else: P.ell(fx, fy, 40, 18, (230, 120, 90))
        P.badge(540, CENTER + 330, "eating nonstop", 58, HOOK, CLOUD, back(seg(u, .6, 1.1)))
        P.badge(540, CENTER + 440, "fat = winter fuel", 52, NIGHT, GLIM, back(seg(u, 2.0, 2.5)))
    elif i == 2:
        den(P); bear(P, 600, CENTER + 120, .9, t, sleep=1)
        rate = lerp(40, 8, eio(seg(u, .8, 3.0)))
        ph = (t * rate / 60) % 1; k = 1 + .25 * math.exp(-ph * 8)
        P.heart(540, CENTER - 310, 60 * k, HOOK)
        P.badge(540, CENTER - 170, f"{int(round(rate))} beats / min", 56, NIGHT, GLIM, back(seg(u, .3, .8)))
    elif i == 3:
        den(P); bear(P, 600, CENTER + 120, .9, t, sleep=1)
        items = ["eat", "drink", "pee", "poop"]
        for k, w in enumerate(items):
            x = 210 + k * 220; q = back(seg(u, .3 + k * .35, .8 + k * .35))
            P.badge(x, CENTER - 300, w, 50, NIGHT, CLOUD, q)
            P.cross(x, CENTER - 200, 34, HOOK, back(seg(u, .6 + k * .35, 1.0 + k * .35)))
        P.badge(540, CENTER - 100, "for months", 56, GLIM, NIGHT, back(seg(u, 2.2, 2.7)))
    elif i == 4:
        cx, cy = 540, CENTER - 40
        P.circ(cx, cy, 300, (40, 55, 90), outline=(90, 110, 160), w=6)
        for k in range(8):
            a = t * .9 + k * .785
            x, y = cx + math.cos(a) * 200, cy + math.sin(a) * 200
            g = (math.sin(a * 1 + t) + 1) / 2
            P.circ(x, y, 26, lc((150, 140, 100), HOPE, (k % 2)))
        P.text(cx, cy - 30, "waste", 52, CLOUD); P.text(cx, cy + 40, "-> protein", 52, HOPE)
        P.badge(540, CENTER + 380, "muscles stay strong", 56, NIGHT, GLIM, back(seg(u, 1.6, 2.1)))
    else:
        den(P); bear(P, 640, CENTER + 120, .9, t, sleep=1)
        for k, dx in enumerate((-60, 40)):
            q = back(seg(u, .6 + k * .4, 1.1 + k * .4))
            x, y = 330 + dx, CENTER + 230
            P.ell(x, y, 46 * q, 30 * q, FUR); P.circ(x - 40 * q, y - 14 * q, 24 * q, FUR)
            P.circ(x - 52 * q, y - 34 * q, 9 * q, FUR)
        P.heart(330, CENTER + 120, 30 * back(seg(u, 1.5, 2.0)), HOOK)
        P.badge(540, CENTER - 160, "cubs born in the den", 54, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
