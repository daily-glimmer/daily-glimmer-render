# Thema: Why do frogs croak?
CENTER = 1050
GR, GR2, SAC = (90, 190, 90), (50, 130, 60), (240, 225, 180)
PAL = ((20, 40, 70), (40, 90, 90))
HI = {"frogs", "croak?", "males,", "mate", "lungs", "vocal", "cords,", "mouth.", "sac", "balloon", "louder.", "own", "call,", "lawn", "mower!"}
WOW = (3, 5)

def pond(P):
    P.ell(540, CENTER + 420, 620, 160, (40, 90, 130))
    P.ell(540, CENTER + 400, 560, 120, (60, 120, 160))
    for x, h in ((80, 380), (130, 300), (960, 360), (1010, 290)):
        P.line([(x, CENTER + 380), (x + 10, CENTER + 380 - h)], (80, 140, 70), 12)
        P.ell(x + 10, CENTER + 380 - h, 14, 40, (120, 80, 50))

def lily(P, x, y, s=1.):
    P.ell(x, y, 170 * s, 50 * s, (70, 160, 80), outline=(40, 110, 60), w=4 * s)

def frog(P, x, y, s, t, sac=0., col=GR, flip=1):
    c2 = lc(col, (0, 0, 0), .35)
    for d in (-1, 1): P.ell(x + d * 110 * s, y + 70 * s, 70 * s, 35 * s, col, outline=c2, w=4 * s)   # Hinterbeine
    P.ell(x, y, 140 * s, 95 * s, col, outline=c2, w=5 * s)
    if sac > 0: P.ell(x, y + 45 * s, 75 * s * sac, 60 * s * sac, SAC, outline=c2, w=4 * s)
    for d in (-1, 1):
        P.circ(x + d * 65 * s, y - 85 * s, 42 * s, col, outline=c2, w=4 * s)
        P.circ(x + d * 65 * s, y - 85 * s, 27 * s, (250, 245, 220))
        P.circ(x + d * 65 * s, y - 85 * s, 15 * s, NIGHT)
    P.arc(x, y - 10 * s, 70 * s, 20, 160, c2, 6 * s)
    for d in (-1, 1): P.ell(x + d * 60 * s, y + 85 * s, 30 * s, 16 * s, col, outline=c2, w=3 * s)

def notes(P, x, y, t, col=GLIM, n=3):
    for k in range(n):
        q = (t * .6 + k / n) % 1
        nx, ny = x + k * 40 + math.sin(t * 3 + k) * 20, y - q * 180
        P.circ(nx, ny, 16 * (1 - q * .4), col); P.line([(nx + 14, ny), (nx + 14, ny - 50)], col, 6)

def SC(i, P, t, u):
    pond(P)
    if i == 0:
        lily(P, 540, CENTER + 260)
        frog(P, 540, CENTER + 160, 1.15, t, sac=.6 + .5 * abs(math.sin(t * 3)))
        P.text(880, CENTER - 290, "?", 150 * back(seg(u, .4, .9)), HOOK)
    elif i == 1:
        lily(P, 300, CENTER + 260, .8); lily(P, 790, CENTER + 260, .8)
        frog(P, 300, CENTER + 180, .8, t, sac=.5 + .6 * abs(math.sin(t * 3)))
        notes(P, 330, CENTER - 30, t)
        P.heart(790, CENTER - 20, 50 * back(seg(u, .8, 1.3)), HOOK)
        frog(P, 790, CENTER + 180, .8, t, col=(140, 190, 110))
        P.badge(540, CENTER + 430, "calling a mate", 58, HOOK, CLOUD, back(seg(u, 1.2, 1.7)))
    elif i == 2:
        P.ell(540, CENTER + 20, 330, 260, GR, outline=GR2, w=6)
        for d in (-1, 1): P.ell(540 + d * 120, CENTER - 20, 80, 120, (240, 150, 160))
        P.rrect(520, CENTER - 230, 560, CENTER + 120, 18, (230, 170, 170))
        q = (u * .8) % 1
        for d in (-1, 1): P.circ(540 + d * 120, lerp(CENTER + 60, CENTER - 140, q), 18, CLOUD)
        P.line([(500, CENTER + 120), (580, CENTER + 120)], GLIM, 14)
        P.badge(540, CENTER + 400, "mouth stays shut", 56, (50, 70, 140), GLIM, back(seg(u, 1.6, 2.1)))
    elif i == 3:
        k = .3 + .9 * abs(math.sin(u * 2.2))
        lily(P, 540, CENTER + 270)
        frog(P, 540, CENTER + 150, 1.25, t, sac=k * 1.4)
        waves(P, 540, CENTER + 210, t, GLIM, n=3, r0=150, dr=60, a0=-40, a1=40)
        waves(P, 540, CENTER + 210, t, GLIM, n=3, r0=150, dr=60, a0=140, a1=220)
        P.badge(540, CENTER - 260, "vocal sac", 60, HOPE, CLOUD, back(seg(u, 1.0, 1.5)))
    elif i == 4:
        cols = [(90, 190, 90), (230, 160, 60), (120, 170, 230)]
        for j, col in enumerate(cols):
            x = 220 + j * 320; s_ = .55
            lily(P, x, CENTER + 250, .6)
            frog(P, x, CENTER + 180, s_, t, sac=.4 + .6 * abs(math.sin(t * (2 + j))), col=col)
            for k in range(3 + j):
                P.rrect(x - 60 + k * 30, CENTER - 40 - (20 + 30 * ((k + j) % 3)) * abs(math.sin(t * 3 + k)), x - 40 + k * 30, CENTER - 20, 6, col)
        P.badge(540, CENTER + 430, "every species: own call", 50, (50, 70, 140), GLIM, back(seg(u, 1.4, 1.9)))
    else:
        lily(P, 400, CENTER + 260, .7)
        frog(P, 400, CENTER + 190, .6, t, sac=.6 + .7 * abs(math.sin(t * 4)))
        waves(P, 400, CENTER + 200, t, HOOK, n=4, r0=90, dr=60, a0=-50, a1=50)
        P.badge(540, CENTER - 330, "LOUD!", 70, HOOK, CLOUD, back(seg(u, .6, 1.1)))
