# Thema: Do sharks die if they stop swimming?  (Mythos-Format)
CENTER = 1050
SH, SH2, BELLY = (110, 135, 160), (80, 100, 125), (225, 232, 238)
PAL = ((5, 40, 80), (20, 110, 150))
HI = {"stop", "swimming?", "few", "rest", "gills", "cheek", "muscles.", "switch", "two", "dozen", "five", "hundred", "naps!"}
WOW = (1, 4)

def seafloor(P, y=CENTER + 330):
    P.poly([(0, y), (W, y - 30), (W, H), (0, H)], (210, 190, 140))
    for k in range(5): P.ell(120 + k * 210, y + 40 + (k % 2) * 40, 50, 16, (190, 170, 120))
    for x in (140, 900): P.line([(x, y), (x + 20, y - 200)], (60, 160, 100), 18)

def bubbles(P, t, x=540):
    for k in range(6):
        q = (t * .35 + k / 6) % 1; P.circ(x - 300 + k * 120, lerp(CENTER + 400, CENTER - 500, q), 8 + k % 3 * 5, (160, 210, 240))

def shark(P, x, y, s, t, swim=True, flip=1, col=SH, spots=False):
    f = flip; tw = math.sin(t * (6 if swim else 1.5)) * (30 if swim else 6) * s
    P.poly([(x + f * 170 * s, y), (x + f * 260 * s, y - 80 * s + tw), (x + f * 240 * s, y + tw * .4), (x + f * 260 * s, y + 70 * s + tw)], lc(col, (0, 0, 0), .2))
    P.poly([(x - f * 20 * s, y - 50 * s), (x + f * 40 * s, y - 130 * s), (x + f * 70 * s, y - 45 * s)], lc(col, (0, 0, 0), .2))
    P.ell(x, y, 200 * s, 62 * s, col)
    P.ell(x - f * 20 * s, y + 25 * s, 160 * s, 32 * s, BELLY)
    P.poly([(x - f * 10 * s, y + 30 * s), (x + f * 50 * s, y + 100 * s), (x + f * 70 * s, y + 35 * s)], lc(col, (0, 0, 0), .2))
    for k in range(4): P.line([(x - f * (100 - k * 16) * s, y - 25 * s), (x - f * (95 - k * 16) * s, y + 15 * s)], lc(col, (0, 0, 0), .35), 4 * s)
    if spots:
        for k in range(6): P.circ(x + (k - 2.5) * 50 * s, y - 20 * s + (k % 2) * 15 * s, 8 * s, lc(col, (0, 0, 0), .25))
    P.circ(x - f * 150 * s, y - 15 * s, 9 * s, NIGHT); P.circ(x - f * 147 * s, y - 18 * s, 3 * s, (255, 255, 255))
    P.arc(x - f * 165 * s, y + 18 * s, 20 * s, 20, 160, NIGHT, 4 * s)

def flow(P, x0, y0, x1, y1, t, col=(150, 220, 255)):
    for k in range(5):
        q = (t * 1.2 + k / 5) % 1; P.circ(lerp(x0, x1, q), lerp(y0, y1, q), 9, col, glow=mul(col, 150))

def SC(i, P, t, u):
    if i == 0:
        bubbles(P, t); seafloor(P)
        shark(P, 540 + math.sin(t * .6) * 120, CENTER - 40, 1.25, t, flip=1 if math.cos(t * .6) < 0 else -1)
        P.text(540, CENTER - 330, "?!", 130 * back(seg(u, .4, .9)), GLIM)
    elif i == 1:
        bubbles(P, t); seafloor(P)
        shark(P, 540, CENTER + 240, 1.1, t, swim=False, col=(170, 140, 100), spots=True)
        P.stamp(540, CENTER - 300, "MYTH", seg(u, .25, .7))
    elif i == 2:
        seafloor(P)
        shark(P, 520, CENTER + 240, 1.2, t, swim=False, col=(170, 140, 100), spots=True)
        flow(P, 300, CENTER + 260, 470, CENTER + 230, t)
        k = .5 + .5 * math.sin(t * 5); P.ell(370, CENTER + 270, 40, 18 + 12 * k, (140, 110, 80))
        P.badge(540, CENTER - 300, "nurse shark", 60, NIGHT, GLIM, back(seg(u, .3, .8)))
        P.badge(540, CENTER - 180, "cheek pump", 56, HOPE, CLOUD, back(seg(u, 2.0, 2.5)))
    elif i == 3:
        bubbles(P, t)
        x = lerp(1250, -250, (u / 5) % 1)
        shark(P, x, CENTER - 20, 1.1, t)
        flow(P, x - 260, CENTER, x - 100, CENTER, t * 2)
        P.badge(540, CENTER + 330, "ram breathing", 60, NIGHT, GLIM, back(seg(u, .5, 1.0)))
    elif i == 4:
        k = eio(seg(u, .4, 2.2))
        for j in range(25):
            c_, r_ = j % 5, j // 5
            col = HOOK if j < 1 else (90, 160, 210)
            P.circ(300 + c_ * 120, CENTER - 280 + r_ * 120, 44 * back(seg(u, .2 + j * .05, .5 + j * .05)), col)
        P.text(540, CENTER + 380, "~24 of 500+ species", 58, GLIM)
        P.badge(540, CENTER + 480, "must keep swimming", 48, HOOK, CLOUD, back(seg(u, 2.5, 3.0)))
    else:
        seafloor(P); bubbles(P, t)
        shark(P, 520, CENTER + 240, 1.15, t, swim=False, col=(170, 140, 100), spots=True)
        for j in range(3):
            kk = back(seg(u, .3 + j * .3, .6 + j * .3)); P.text(700 + j * 60, CENTER + 60 - j * 70, "z", (50 + j * 15) * kk, CLOUD)
        P.stamp(540, CENTER - 300, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
