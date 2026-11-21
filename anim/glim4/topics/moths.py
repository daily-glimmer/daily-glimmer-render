# Thema: Do moths eat your clothes?  (Mythos-Format, NOT QUITE in Satz 2, FACT in Satz 6)
CENTER = 1050
MW, MW2, LARVA = (215, 195, 150), (180, 160, 115), (245, 240, 225)
WOOL = (200, 70, 80)
PAL = ((60, 50, 80), (150, 120, 140))
HI = {"clothes?", "not", "quite!", "don't", "eat", "mouthparts.", "caterpillars,", "larvae,", "wool,", "keratin,", "babies!", "culprits?"}
WOW = (1,)

def moth(P, x, y, s, t):
    fl = math.sin(t * 18) * .25
    for f in (-1, 1):
        P.poly([(x, y), (x + f * 150 * s, y - (70 + 40 * fl) * s), (x + f * 130 * s, y + 50 * s)], MW, outline=MW2, w=4 * s)
        P.poly([(x, y + 10 * s), (x + f * 90 * s, y + 80 * s), (x + f * 30 * s, y + 90 * s)], MW2)
    P.ell(x, y + 20 * s, 22 * s, 70 * s, (150, 130, 100))
    P.circ(x, y - 55 * s, 24 * s, (150, 130, 100))
    for f in (-1, 1): P.line([(x + f * 8 * s, y - 70 * s), (x + f * 50 * s, y - 130 * s)], (150, 130, 100), 5 * s)

def sweater(P, x, y, s, holes=0.):
    P.rrect(x - 200 * s, y - 180 * s, x + 200 * s, y + 220 * s, 40 * s, WOOL)
    P.poly([(x - 200 * s, y - 180 * s), (x - 330 * s, y + 60 * s), (x - 250 * s, y + 100 * s), (x - 200 * s, y - 40 * s)], WOOL)
    P.poly([(x + 200 * s, y - 180 * s), (x + 330 * s, y + 60 * s), (x + 250 * s, y + 100 * s), (x + 200 * s, y - 40 * s)], WOOL)
    P.ell(x, y - 180 * s, 70 * s, 30 * s, lc(WOOL, (0, 0, 0), .2))
    for j in range(4): P.line([(x - 180 * s, y + (-100 + j * 80) * s), (x + 180 * s, y + (-100 + j * 80) * s)], lc(WOOL, (255, 255, 255), .2), 6 * s)
    random.seed(9)
    for j in range(int(6 * holes)): P.circ(x + (random.random() - .5) * 300 * s, y + (random.random() - .4) * 300 * s, 22 * s, PAL[0])

def larva(P, x, y, s, t):
    for j in range(6): P.circ(x + j * 22 * s + math.sin(t * 6 + j) * 3 * s, y - abs(math.sin(t * 3 + j * .5)) * 6 * s, 16 * s, LARVA)
    P.circ(x + 130 * s, y - 4 * s, 18 * s, (180, 120, 80))

def SC(i, P, t, u):
    if i == 0:
        sweater(P, 540, CENTER + 120, 1.1, holes=1.)
        moth(P, 540 + math.sin(t) * 120, CENTER - 230 + math.cos(t * 1.3) * 40, 1.0, t)
        P.text(860, CENTER - 290, "?", 140 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        sweater(P, 540, CENTER + 220, 1.0, holes=1.)
        moth(P, 540, CENTER - 60, 1.1, t)
        P.stamp(540, CENTER - 300, "NOT QUITE", seg(u, .25, .7), col=HOOK, rot=-6)
    elif i == 2:
        P.circ(540, CENTER, 300, (240, 235, 225))
        moth(P, 540, CENTER + 60, 2.0, t * .2)
        P.cross(540, CENTER - 60, 60, k=back(seg(u, .8, 1.3)))
        P.badge(540, CENTER + 400, "no working mouth", 58, NIGHT, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 3:
        sweater(P, 540, CENTER + 60, 1.2, holes=eio(seg(u, .5, 3.5)))
        larva(P, 400 + u * 40, CENTER - 20, 1.3, t); larva(P, 520, CENTER + 160, 1.1, t + 1)
        P.badge(540, CENTER - 300, "hungry larvae", 58, HOOK, CLOUD, back(seg(u, .8, 1.3)))
    elif i == 4:
        P.rrect(140, CENTER - 280, 940, CENTER + 280, 60, (60, 45, 70))
        for j in range(5):
            y = CENTER - 180 + j * 90
            P.line([(200, y), (880, y + math.sin(t + j) * 20)], WOOL, 18)
        larva(P, 420, CENTER - 40, 2.0, t)
        P.badge(540, CENTER + 380, "keratin = food", 58, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
    else:
        sweater(P, 380, CENTER + 120, .9, holes=1.)
        larva(P, 300, CENTER + 60, 1.0, t)
        moth(P, 820, CENTER - 60, .8, t)
        P.stamp(700, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
