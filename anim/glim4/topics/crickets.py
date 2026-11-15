# Thema: How do crickets chirp?
CENTER = 1050
PAL = ((140, 200, 120), (90, 160, 90))
HI = {"chirp?", "voice.", "wings", "violin!", "scraper,", "ridges", "file.", "buzz", "males", "ears", "legs.", "faster", "warmer!"}
WOW = (1, 5)
BODY, WINGC = (110, 70, 40), (160, 110, 60)
GROUND = CENTER + 380

def grass(P, t):
    P.poly([(0, GROUND), (W, GROUND - 30), (W, H), (0, H)], (80, 140, 60))
    for k in range(14):
        x = 30 + k * 78; P.line([(x, GROUND + 10), (x + math.sin(t * 1.5 + k) * 20, GROUND - 120 - (k % 3) * 40)], (60, 130, 50), 12)

def cricket(P, x, y, s, t, chirp=0., flip=1, ears=False):
    f = flip; lift = abs(math.sin(t * 30)) * 12 * chirp
    P.line([(x - f * 40 * s, y + 20 * s), (x - f * 120 * s, y - 60 * s), (x - f * 170 * s, y + 60 * s)], BODY, 16 * s)
    P.ell(x, y, 150 * s, 55 * s, BODY)
    P.poly([(x + f * 90 * s, y - 30 * s - lift * s), (x - f * 150 * s, y - 40 * s - lift * s), (x - f * 140 * s, y + 10 * s)], WINGC, outline=dk(WINGC, .7), w=4 * s)
    P.circ(x + f * 140 * s, y - 10 * s, 50 * s, BODY)
    P.circ(x + f * 160 * s, y - 25 * s, 12 * s, CLOUD); P.circ(x + f * 163 * s, y - 25 * s, 6 * s, NIGHT)
    for k in (-1, 1): P.line([(x + f * 175 * s, y - 40 * s), (x + f * (330 + k * 30) * s, y - (200 - k * 30) * s)], BODY, 4 * s)
    P.line([(x + f * 100 * s, y + 30 * s), (x + f * 130 * s, y + 90 * s)], BODY, 10 * s)
    P.line([(x + f * 20 * s, y + 40 * s), (x + f * 10 * s, y + 100 * s)], BODY, 10 * s)
    if ears: P.ell(x + f * 118 * s, y + 62 * s, 10 * s, 16 * s, GLIM)
    if chirp > 0: waves(P, x + f * 40 * s, y - 60 * s, t, GLIM, n=3, r0=60 * s, dr=40 * s, a0=-150, a1=-30)

def dk(c, k): return tuple(int(v * k) for v in c)

def SC(i, P, t, u):
    grass(P, t)
    if i == 0:
        cricket(P, 540, CENTER + 100, 1.5, t, chirp=1)
        P.text(840, CENTER - 300, "?", 140 * back(seg(u, .4, .9)), GLIM)
    elif i == 1:
        cricket(P, 540, CENTER + 120, 1.5, t, chirp=seg(u, 1.6, 2))
        P.cross(300, CENTER - 160, 60, k=back(seg(u, .3, .8)))
        P.badge(620, CENTER - 160, "wings!", 62, HOPE, CLOUD, back(seg(u, 1.6, 2.1)))
    elif i == 2:
        P.rrect(180, CENTER - 180, 900, CENTER - 60, 30, WINGC, outline=dk(WINGC, .7), w=6)
        for j in range(26): P.line([(250 + j * 24, CENTER - 160), (250 + j * 24, CENTER - 80)], dk(WINGC, .55), 8)
        P.badge(540, CENTER - 280, "file", 58, NIGHT, GLIM, back(seg(u, 2.2, 2.7)))
        P.rrect(180, CENTER + 100, 900, CENTER + 220, 30, WINGC, outline=dk(WINGC, .7), w=6)
        P.poly([(700, CENTER + 100), (780, CENTER + 30), (860, CENTER + 100)], dk(WINGC, .5))
        P.badge(540, CENTER + 330, "scraper", 58, HOOK, CLOUD, back(seg(u, .8, 1.3)))
    elif i == 3:
        x = 250 + (math.sin(u * 7) * .5 + .5) * 560
        P.rrect(180, CENTER - 60, 900, CENTER + 40, 30, WINGC, outline=dk(WINGC, .7), w=6)
        for j in range(26): P.line([(250 + j * 24, CENTER - 40), (250 + j * 24, CENTER + 20)], dk(WINGC, .55), 8)
        P.poly([(x - 40, CENTER - 140), (x, CENTER - 40), (x + 40, CENTER - 140)], dk(WINGC, .5))
        waves(P, 540, CENTER + 120, t, GLIM, n=3, r0=60, dr=60, a0=30, a1=150)
        P.text(540, CENTER - 280, "CHIRP!", 110 * back(seg(u, 1.0, 1.4)), GLIM)
    elif i == 4:
        cricket(P, 330, CENTER + 120, 1.0, t, chirp=1)
        cricket(P, 780, CENTER + 160, .9, t, flip=-1, ears=u > 2.8)
        P.heart(560, CENTER - 60, 40 * back(seg(u, 1.5, 2.0)), HOOK)
        if u > 2.8: P.circ(780 - 118 * .9, CENTER + 160 + 62 * .9, 40, None, outline=GLIM, w=6)
    else:
        cricket(P, 400, CENTER + 120, 1.1, t, chirp=1)
        P.rrect(760, CENTER - 200, 840, CENTER + 120, 40, CLOUD, outline=(150, 150, 160), w=6)
        lvl = .4 + .5 * seg(u, .3, 2.0)
        P.rrect(780, CENTER + 100 - 280 * lvl, 820, CENTER + 100, 20, HOOK)
        P.circ(800, CENTER + 140, 50, HOOK)
