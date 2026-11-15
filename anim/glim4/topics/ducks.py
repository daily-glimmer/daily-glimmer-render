# Thema: Does a duck's quack really not echo?  (Mythos-Format)
CENTER = 1050
PAL = ((40, 110, 150), (90, 170, 190))
HI = {"echo?", "myth,", "tested", "2003,", "Salford", "echo", "slowly,", "blends", "walls", "cliffs", "females", "quack!"}
WOW = (1, 3)
WATER = CENTER + 260

def pond(P, t):
    P.poly([(0, WATER), (W, WATER), (W, H), (0, H)], (60, 140, 180))
    for k in range(6):
        x = (k * 210 + t * 30) % (W + 200) - 100; P.arc(x, WATER + 60 + k % 3 * 50, 50, 200, 340, (150, 210, 230), 5)
    for x in (90, 1000):
        for j in range(4): P.line([(x + j * 18, WATER), (x + j * 18 + math.sin(t + j) * 10, WATER - 150 - j * 25)], (70, 140, 70), 10)

def duck(P, x, y, s, t, female=True, quack=0., flip=False):
    f = -1 if flip else 1; bob = math.sin(t * 2.2) * 6 * s
    body = (150, 110, 70) if female else (200, 200, 200)
    P.ell(x, y + bob, 130 * s, 70 * s, body)
    P.poly([(x - f * 120 * s, y - 20 * s + bob), (x - f * 175 * s, y - 60 * s + bob), (x - f * 150 * s, y + 10 * s + bob)], body)
    P.ell(x - f * 10 * s, y + 5 * s + bob, 70 * s, 35 * s, lc(body, (0, 0, 0), .15))
    if female:
        for k in range(5): P.arc(x - f * (60 - k * 30) * s, y - 10 * s + bob, 16 * s, 20, 160, (110, 75, 45), 4 * s)
    hx, hy = x + f * 95 * s, y - 85 * s + bob
    P.circ(hx, hy, 52 * s, body if female else (40, 120, 70))
    if not female: P.line([(hx - 40 * s, hy + 45 * s), (hx + 40 * s, hy + 45 * s)], CLOUD, 8 * s)
    op = 18 * s * quack
    P.poly([(hx + f * 35 * s, hy - 6 * s - op), (hx + f * 105 * s, hy + 2 * s - op * .5), (hx + f * 40 * s, hy + 8 * s)], (245, 160, 50))
    P.poly([(hx + f * 35 * s, hy + 10 * s), (hx + f * 100 * s, hy + 14 * s + op * .5), (hx + f * 38 * s, hy + 24 * s + op)], (225, 140, 40))
    P.circ(hx + f * 12 * s, hy - 14 * s, 8 * s, NIGHT); P.circ(hx + f * 15 * s, hy - 17 * s, 3 * s, CLOUD)

def wavesR(P, x, y, t, col, n=3, flip=False, fade=1.):
    a0, a1 = (120, 240) if flip else (-60, 60)
    for k in range(n):
        q = (t * .9 + k / n) % 1; r = 60 + q * 260
        P.arc(x, y, r, a0, a1, lc(col, PAL[0], q * fade), max(3, int(10 * (1 - q))))

def cliff(P, x):
    P.poly([(x, CENTER - 500), (W, CENTER - 520), (W, WATER), (x - 40, WATER)], (130, 110, 95))
    for k in range(5): P.line([(x + 20, CENTER - 420 + k * 140), (x + 120, CENTER - 400 + k * 140)], (100, 85, 75), 6)

def SC(i, P, t, u):
    if i == 0:
        pond(P, t); q = .5 + .5 * math.sin(t * 7)
        duck(P, 430, WATER - 30, 1.4, t, quack=q)
        wavesR(P, 640, WATER - 150, t, GLIM)
        P.text(860, CENTER - 300, "?", 150 * back(seg(u, .4, .9)), GLIM)
    elif i == 1:
        pond(P, t); duck(P, 430, WATER - 30, 1.3, t, quack=.5 + .5 * math.sin(t * 7))
        P.badge(540, CENTER - 200, "no echo?", 62, NIGHT, CLOUD, back(seg(u, .5, 1.0))); P.cross(800, CENTER - 200, 36, k=back(seg(u, .9, 1.3)))
        P.stamp(540, CENTER - 430, "MYTH", seg(u, .25, .7))
    elif i == 2:
        P.rrect(80, CENTER - 420, 1000, CENTER + 300, 40, (25, 45, 70), outline=CLOUD, w=6)
        for k in range(9):
            for j in range(6): P.poly([(120 + k * 100, CENTER - 380 + j * 110), (170 + k * 100, CENTER - 330 + j * 110), (120 + k * 100, CENTER - 280 + j * 110)], (60, 80, 110))
        duck(P, 360, CENTER + 120, 1.0, t, quack=.5 + .5 * math.sin(t * 7))
        P.line([(760, CENTER + 260), (760, CENTER - 20)], (180, 180, 190), 12); P.rrect(730, CENTER - 110, 790, CENTER - 10, 28, (70, 70, 80))
        wavesR(P, 500, CENTER + 40, t, GLIM, 3)
        P.badge(540, CENTER + 400, "University of Salford, 2003", 50, NIGHT, GLIM, back(seg(u, .6, 1.1)))
    elif i == 3:
        x0, x1, y = 110, 970, CENTER - 60
        P.rrect(x0 - 30, y - 230, x1 + 30, y + 230, 40, (25, 45, 70))
        ke = eout(seg(u, .3, 3.5)); n = 160
        for j in range(int(n * ke)):
            q = j / n; x = lerp(x0, x1, q)
            amp = 180 * math.exp(-q * 3.2) * abs(math.sin(j * .9))
            P.line([(x, y - amp), (x, y + amp)], GLIM, 4)
            if q > .18:
                q2 = q - .18; amp2 = 110 * math.exp(-q2 * 3.2) * abs(math.sin(j * 1.3)) * seg(u, 2.0, 2.6)
                P.line([(x + 2, y - amp2), (x + 2, y + amp2)], HOOK, 3)
        P.badge(330, y - 300, "quack", 52, NIGHT, GLIM, back(seg(u, .4, .9)))
        P.badge(740, y - 300, "echo", 52, HOOK, CLOUD, back(seg(u, 2.0, 2.5)))
        P.badge(540, y + 330, "they blend together", 54, NIGHT, CLOUD, back(seg(u, 2.8, 3.3)))
    elif i == 4:
        pond(P, t); cliff(P, 820); duck(P, 330, WATER - 30, 1.1, t, quack=.5 + .5 * math.sin(t * 7))
        wavesR(P, 480, WATER - 130, t, GLIM, 3)
        if u > 1.6: wavesR(P, 800, WATER - 130, t + .5, HOOK, 2, flip=True)
        P.badge(400, CENTER - 280, "rarely near walls", 54, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
    else:
        pond(P, t)
        duck(P, 320, WATER - 30, 1.1, t, female=True, quack=.5 + .5 * math.sin(t * 7))
        duck(P, 760, WATER - 20, .9, t, female=False, flip=True)
        wavesR(P, 480, WATER - 150, t, GLIM, 3)
        P.badge(320, WATER + 140, "loud quack", 48, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
        P.badge(760, WATER + 140, "quiet rasp", 48, NIGHT, CLOUD, back(seg(u, 1.6, 2.1)))
        P.stamp(540, CENTER - 430, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
