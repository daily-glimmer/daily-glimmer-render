# Thema: Why do dogs have wet noses?
CENTER = 1050
FUR, FUR2, NOSE = (200, 150, 95), (150, 105, 60), (45, 40, 50)
PAL = ((200, 230, 250), (170, 210, 190))
HI = {"wet", "noses?", "mucus", "scent", "particles", "lick", "organ", "cold,", "warmth", "dry", "sick.", "unique,", "fingerprint!"}
WOW = (2, 5)

def doghead(P, x, y, s, t, lick=0., shine=True, sad=False):
    for d in (-1, 1):   # Schlappohren
        sw = math.sin(t * 2.5 + d) * 6 * s
        P.ell(x + d * 150 * s + sw, y + 10 * s, 55 * s, 130 * s, FUR2)
    P.ell(x, y - 20 * s, 160 * s, 150 * s, FUR, outline=FUR2, w=6 * s)
    P.ell(x, y + 80 * s, 110 * s, 80 * s, lc(FUR, CLOUD, .5))
    for d in (-1, 1):
        if sad: P.arc(x + d * 60 * s, y - 50 * s, 20 * s, 20, 160, NIGHT, 7 * s)
        else:
            P.circ(x + d * 60 * s, y - 50 * s, 22 * s, NIGHT); P.circ(x + d * 60 * s + 7 * s, y - 58 * s, 7 * s, CLOUD)
    P.ell(x, y + 40 * s, 52 * s, 36 * s, NOSE)
    if shine:
        P.ell(x - 15 * s, y + 28 * s, 16 * s, 9 * s, (200, 220, 255))
        P.circ(x + 22 * s, y + 50 * s, 6 * s, (200, 220, 255))
    P.line([(x, y + 75 * s), (x, y + 105 * s)], NIGHT, 5 * s)
    P.arc(x - 30 * s, y + 105 * s, 30 * s, 0, 180, NIGHT, 5 * s); P.arc(x + 30 * s, y + 105 * s, 30 * s, 0, 180, NIGHT, 5 * s)
    if lick > 0:
        P.ell(x + 10 * s, y + 130 * s - lick * 70 * s, 28 * s, 45 * s * (.5 + lick * .5), (240, 120, 130))

def SC(i, P, t, u):
    P.rrect(-20, CENTER + 340, W + 20, H + 20, 0, (140, 190, 120))
    if i == 0:
        doghead(P, 540, CENTER + 40, 1.3, t)
        P.text(880, CENTER - 290, "?", 150 * back(seg(u, .4, .9)), HOOK)
    elif i == 1:
        P.ell(540, CENTER + 80, 300, 200, NOSE)
        for d in (-1, 1): P.ell(540 + d * 110, CENTER + 120, 55, 40, (20, 18, 25))
        P.ell(540, CENTER - 40, 260, 40 * eout(seg(u, .2, 1.0)), (150, 200, 240))
        for j in range(12):
            q = (t * .5 + j / 12) % 1
            x = 140 + (j * 83) % 800; y = lerp(CENTER - 330, CENTER - 60, q)
            P.circ(x + math.sin(t * 2 + j) * 20, y, 14 * (1 - q * .5), [HOOK, GLIM, HOPE][j % 3])
        P.badge(540, CENTER + 400, "sticky mucus", 60, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
    elif i == 2:
        lk = max(0, math.sin(u * 4)) if u < 3.4 else 0
        doghead(P, 540, CENTER + 20, 1.2, t, lick=lk)
        P.rrect(560, CENTER + 180, 760, CENTER + 220, 20, GLIM)
        P.arc(660, CENTER + 120, 70, 200, 340, GLIM, 6 * seg(u, 1.8, 2.2))
        P.badge(540, CENTER + 410, "scent organ", 60, HOPE, CLOUD, back(seg(u, 2.0, 2.5)))
    elif i == 3:
        doghead(P, 330, CENTER + 60, .95, t)
        # Maus als warmes Tier
        mx, my = 810, CENTER + 250
        waves(P, mx, my - 40, t, HOOK, n=3, r0=60, dr=45, a0=150, a1=230)
        P.ell(mx, my, 70, 45, (160, 160, 175)); P.circ(mx - 60, my - 25, 30, (160, 160, 175))
        P.circ(mx - 70, my - 55, 18, (245, 170, 180)); P.circ(mx - 75, my - 30, 6, NIGHT)
        P.line([(mx + 65, my), (mx + 130, my - 40)], (160, 160, 175), 6)
        P.badge(540, CENTER + 420, "senses warmth", 60, HOOK, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 4:
        doghead(P, 540, CENTER + 60, 1.15, t, shine=False)
        P.check(540, CENTER - 260, 70, HOPE, back(seg(u, 1.6, 2.1)))
        P.badge(540, CENTER + 410, "dry nose = OK", 60, HOPE, CLOUD, back(seg(u, 1.2, 1.7)))
    else:
        k = eout(seg(u, .2, 1.3))
        P.rrect(240, CENTER - 160, 840, CENTER + 260, 30, CLOUD, outline=FUR2, w=6)
        for r in range(9):
            for c in range(14):
                x = 290 + c * 38 + (r % 2) * 19; y = CENTER - 120 + r * 40
                if (x - 540) ** 2 / 270 ** 2 + (y - CENTER - 50) ** 2 / 190 ** 2 < k:
                    P.poly([(x, y - 16), (x + 16, y - 6), (x + 12, y + 14), (x - 12, y + 14), (x - 16, y - 6)], NOSE)
        P.badge(540, CENTER - 300, "unique nose print", 56, NIGHT, GLIM, back(seg(u, 1.3, 1.8)))
