# Thema: Is a banana a berry?
CENTER = 1050
YEL, YEL2, TIP = (255, 214, 70), (230, 180, 40), (110, 80, 40)
FLESH = (250, 240, 200)
PAL = ((255, 236, 190), (250, 200, 170))
HI = {"berry?", "yes!", "true", "berry.", "flower", "ovary,", "seeds", "black", "dots", "outside,", "not", "grapes", "tomatoes"}
WOW = (1, 4)

def banana(P, x, y, s, t, rot=0., face=True):
    pts_o, pts_i = [], []
    for j in range(21):
        q = j / 20; a = math.radians(lerp(200, 340, q)) + rot
        th = 70 * s * math.sin(q * math.pi) + 8 * s
        pts_o.append((x + math.cos(a) * 260 * s, y - 150 * s - math.sin(a) * 200 * s + th * 0))
        pts_i.append((x + math.cos(a) * (260 * s - th * .3), y - 150 * s - math.sin(a) * (200 * s - th * 1.6)))
    P.poly(pts_o + pts_i[::-1], YEL, outline=YEL2, w=6)
    P.line(pts_o[3:18], YEL2, 6)
    P.circ(*pts_o[0], 12 * s, TIP); P.line([pts_o[-1], (pts_o[-1][0] + 30 * s, pts_o[-1][1] - 40 * s)], (120, 140, 60), 18 * s)
    if face:
        mx, my = pts_i[10][0], (pts_i[10][1] + pts_o[10][1]) / 2
        for ex in (-28, 28): P.circ(mx + ex * s, my - 8 * s, 8 * s, NIGHT)
        P.arc(mx, my + 2 * s, 16 * s, 20, 160, NIGHT, 5 * s)

def section(P, x, y, r, t, pulse=0.):
    P.circ(x, y, r, YEL, outline=YEL2, w=8); P.circ(x, y, r * .86, FLESH)
    for k in range(3):
        a = k * 2.094 + .5; P.line([(x, y), (x + math.cos(a) * r * .32, y + math.sin(a) * r * .32)], (235, 215, 160), r * .06)
    for k in range(9):
        a = k * .698; rr = r * .2
        P.circ(x + math.cos(a) * rr, y + math.sin(a) * rr, r * .035 * (1 + pulse * .6 * (.5 + .5 * math.sin(t * 6 + k))), (50, 35, 25))

def flower(P, x, y, s, t):
    P.line([(x, y), (x, y + 220 * s)], (90, 150, 70), 14 * s)
    for k in range(6):
        a = k * 1.047 + t * .3; P.ell(x + math.cos(a) * 55 * s, y + math.sin(a) * 55 * s, 38 * s, 38 * s, (250, 150, 180))
    P.circ(x, y, 32 * s, GLIM)

def strawberry(P, x, y, s, t):
    P.poly([(x - 150 * s, y - 90 * s), (x + 150 * s, y - 90 * s), (x + 110 * s, y + 60 * s), (x, y + 190 * s), (x - 110 * s, y + 60 * s)], (230, 60, 70))
    P.circ(x - 75 * s, y - 80 * s, 78 * s, (230, 60, 70)); P.circ(x + 75 * s, y - 80 * s, 78 * s, (230, 60, 70))
    for k in range(5):
        a = math.radians(-160 + k * 35); P.ell(x + math.cos(a) * 70 * s, y - 150 * s + math.sin(a) * 30 * s, 42 * s, 16 * s, (70, 160, 70))
    random.seed(2)
    for k in range(22):
        px, py = x + (random.random() - .5) * 230 * s, y - 100 * s + random.random() * 230 * s
        if abs(px - x) < 140 * s - (py - y) * .45: P.ell(px, py, 6 * s, 9 * s, (255, 220, 110))
    for ex in (-30, 30): P.circ(x + ex * s, y - 20 * s, 9 * s, NIGHT)

def grapes(P, x, y, s):
    for r, row in enumerate((4, 3, 2, 1)):
        for c in range(row): P.circ(x + (c - (row - 1) / 2) * 52 * s, y + r * 46 * s, 30 * s, (140, 80, 170), outline=(100, 50, 130), w=4)
    P.line([(x, y - 30 * s), (x + 10 * s, y - 80 * s)], (110, 80, 40), 10 * s)

def tomato(P, x, y, s):
    P.ell(x, y, 85 * s, 75 * s, (235, 70, 55)); 
    for k in range(5):
        a = k * 1.256 - 1.57; P.ell(x + math.cos(a) * 26 * s, y - 70 * s + math.sin(a) * 10 * s, 22 * s, 9 * s, (70, 160, 70))

def SC(i, P, t, u):
    if i == 0:
        banana(P, 520, CENTER + 120, 1.3, t, rot=math.sin(t * 1.2) * .05)
        for k, (bx, by) in enumerate(((220, CENTER - 360), (330, CENTER - 420), (270, CENTER - 300))):
            P.circ(bx, by, 36 * back(seg(u, .3 + k * .15, .7 + k * .15)), (80, 100, 190), outline=(50, 60, 130), w=4)
        P.text(820, CENTER - 360, "?", 150 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        banana(P, 540, CENTER + 160, 1.2, t, rot=math.sin(t * 2) * .06)
        P.badge(540, CENTER - 160, "a true berry", 66, HOPE, CLOUD, back(seg(u, 1.6, 2.1)))
        P.stamp(540, CENTER - 430, "TRUE", seg(u, .25, .7), col=HOPE, rot=8)
    elif i == 2:
        flower(P, 230, CENTER - 160, 1.1, t)
        k = eout(seg(u, 1.4, 2.4)); P.line([(370, CENTER - 160), (370 + 230 * k, CENTER - 160)], NIGHT, 14)
        if k > .95: P.poly([(610, CENTER - 160), (580, CENTER - 190), (580, CENTER - 130)], NIGHT)
        section(P, 800, CENTER - 160, 170 * back(seg(u, 2.2, 2.8)), t)
        P.badge(300, CENTER + 200, "1 flower", 52, NIGHT, GLIM, back(seg(u, .8, 1.3)))
        P.badge(700, CENTER + 200, "1 ovary", 52, NIGHT, GLIM, back(seg(u, 1.6, 2.1)))
        P.badge(540, CENTER + 320, "seeds inside", 52, HOPE, CLOUD, back(seg(u, 3.4, 3.9)))
    elif i == 3:
        section(P, 540, CENTER - 120, 300 * back(seg(u, .1, .6)), t, pulse=seg(u, 1.4, 2.0))
        P.badge(540, CENTER + 280, "tiny seeds that never grew", 52, NIGHT, GLIM, back(seg(u, 1.8, 2.3)))
    elif i == 4:
        strawberry(P, 540, CENTER + 20, 1.3, t)
        P.badge(540, CENTER + 360, "seeds on the outside", 54, NIGHT, GLIM, back(seg(u, 1.6, 2.1)))
        P.stamp(540, CENTER - 290, "NOT A BERRY", seg(u, .25, .7), rot=-8)
    else:
        grapes(P, 230, CENTER - 130, 1.0); tomato(P, 540, CENTER - 50, 1.1)
        banana(P, 860, CENTER - 40, .55, t, face=False)
        for j, x in enumerate((230, 540, 850)): P.check(x, CENTER + 140, 40, k=back(seg(u, .8 + j * .35, 1.2 + j * .35)))
        P.badge(540, CENTER - 430, "all berries!", 64, HOPE, CLOUD, back(seg(u, .3, .8)))
