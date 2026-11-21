# Thema: Are sharks really older than trees?  (Mythos-Format, TRUE in Satz 2, FACT in Satz 6)
# Figuren: shark/seafloor/bubbles aus sharks.py, tree aus leaves.py
CENTER = 1050
exec(open(os.path.join(HERE, "topics", "sharks.py")).read(), globals())
_shark = shark
exec(open(os.path.join(HERE, "topics", "leaves.py")).read(), globals())
shark = _shark
PAL = ((10, 45, 85), (40, 120, 140))
HI = {"older", "trees?", "true!", "long", "before", "four", "fifty", "million", "eighty", "five", "tiny", "mosses", "dinosaurs!"}
WOW = (1,)
SEA = (25, 90, 140)

def water(P, t, top=CENTER - 120):
    P.poly([(0, top), (W, top), (W, H), (0, H)], SEA)
    for k in range(6):
        x = (k * 210 + t * 50) % (W + 200) - 100; P.arc(x, top, 50, 200, 340, (120, 190, 230), 8)

def timeline(P, k, y=CENTER + 470):
    P.rrect(80, y - 14, 1000, y + 14, 14, (240, 240, 230))
    for lab, x in (("450", 160), ("385", 450), ("66", 840), ("now", 960)):
        P.line([(x, y - 30), (x, y + 30)], (240, 240, 230), 8)
        P.text(x, y + 75, lab, 40, CLOUD)
    P.circ(lerp(160, 960, k), y, 26, GLIM)

def moss(P, x, y, s, t):
    for j in range(5):
        P.line([(x + (j - 2) * 14 * s, y), (x + (j - 2) * 20 * s + math.sin(t * 2 + j) * 4 * s, y - (40 + j % 2 * 20) * s)], (90, 170, 80), 8 * s)
        P.circ(x + (j - 2) * 20 * s, y - (44 + j % 2 * 20) * s, 9 * s, (140, 200, 90))

def dino(P, x, y, s):
    c = (110, 150, 90)
    P.ell(x, y, 150 * s, 80 * s, c); P.line([(x + 110 * s, y - 30 * s), (x + 170 * s, y - 170 * s)], c, 50 * s)
    P.ell(x + 190 * s, y - 190 * s, 55 * s, 35 * s, c); P.line([(x - 130 * s, y), (x - 290 * s, y + 40 * s)], c, 36 * s)
    for dx in (-70, 60): P.line([(x + dx * s, y + 50 * s), (x + dx * s, y + 150 * s)], c, 34 * s)
    P.circ(x + 200 * s, y - 200 * s, 7 * s, NIGHT)

def SC(i, P, t, u):
    if i == 0:
        water(P, t, CENTER + 60)
        tree(P, 300, CENTER - 200, .8, [(70, 160, 70), (90, 180, 80)], t)
        shark(P, 640 + math.sin(t * .7) * 80, CENTER + 330, 1.05, t)
        P.text(800, CENTER - 230, "?", 170 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        water(P, t, CENTER - 300); bubbles(P, t); seafloor(P)
        shark(P, 540 + math.sin(t * .8) * 60, CENTER + 20, 1.3, t)
        P.stamp(540, CENTER - 220, "TRUE", seg(u, .25, .7), col=HOPE, rot=-6)
        timeline(P, 0)
    elif i == 2:
        water(P, t, CENTER - 300); bubbles(P, t)
        k = back(seg(u, .4, 1.0))
        for j in range(5):   # Hautzähnchen (Schuppen)
            x = 260 + j * 140; y = CENTER - 20 + (j % 2) * 60
            P.poly([(x - 50 * k, y + 40 * k), (x, y - 70 * k), (x + 50 * k, y + 40 * k)], (200, 215, 230), outline=(120, 140, 160), w=5)
        P.badge(540, CENTER + 230, "fossil shark scales", 56, NIGHT, CLOUD, back(seg(u, 1.0, 1.5)))
        timeline(P, 0); P.badge(160, CENTER + 360, "sharks", 44, GLIM, NIGHT, back(seg(u, 2.0, 2.5)))
    elif i == 3:
        P.poly([(0, CENTER + 260), (W, CENTER + 240), (W, H), (0, H)], (120, 150, 80))
        g = eout(seg(u, .3, 2.5))
        tree(P, 540, CENTER - 180 + (1 - g) * 300, .4 + .6 * g, [(70, 160, 70), (90, 180, 80), (60, 140, 60)], t)
        timeline(P, .36 * eio(seg(u, .2, 1.5))); P.badge(450, CENTER + 360, "first trees", 44, HOPE, CLOUD, back(seg(u, 1.5, 2.0)))
    elif i == 4:
        P.poly([(0, CENTER + 200), (W, CENTER + 190), (W, H), (0, H)], (150, 130, 95))
        for j in range(7): moss(P, 120 + j * 140, CENTER + 200, 1.3 + (j % 3) * .3, t)
        k = back(seg(u, 1.2, 1.7))
        P.line([(960, CENTER + 200), (960, CENTER + 60)], CLOUD, 6); P.line([(940, CENTER + 60), (980, CENTER + 60)], CLOUD, 6)
        P.badge(540, CENTER - 100, "a few cm tall", 60, NIGHT, GLIM, k)
        timeline(P, .2)
    else:
        P.poly([(0, CENTER + 140), (W, CENTER + 130), (W, H), (0, H)], (140, 150, 90))
        water(P, t, CENTER + 260)
        dino(P, 330, CENTER - 20, .85)
        shark(P, 640, CENTER + 400, .9, t)
        P.cross(330, CENTER - 50, 90, k=back(seg(u, .9, 1.4)))
        P.stamp(780, CENTER - 230, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
