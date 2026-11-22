# Thema: Can a blanket of snow actually keep animals warm?  (Mythos-Format, TRUE in Satz 2, FACT in Satz 6)
# Quellen: Michigan State University Extension "The Subnivean Zone" (~0 °C unter der Schneedecke), Illinois DNR,
# Northern Woodlands "Subnivean shelter" (~6 inch / 15 cm Schnee reichen; Mäuse, Wühlmäuse, Spitzmäuse), NWF.
CENTER = 1050
SNOWC, SNOW2, SOIL, MOUSE = (245, 248, 255), (215, 228, 245), (120, 95, 70), (150, 140, 135)
COLD, WARM = (90, 150, 230), (240, 150, 70)
PAL = ((70, 100, 160), (170, 195, 230))
HI = {"snow", "warm?", "true!", "insulator,", "air.", "fifteen", "zero", "twenty", "below", "mice,", "voles", "subnivean", "roof!"}
WOW = (1,)
STOP_, SBOT = CENTER - 40, CENTER + 360

def section(P, t, bubbles=True):
    P.rrect(-20, SBOT, W + 20, H + 40, 0, SOIL)
    P.rrect(-20, STOP_, W + 20, SBOT, 0, SNOWC)
    P.line([(-20, STOP_), (W + 20, STOP_)], SNOW2, 10)
    if bubbles:
        random.seed(2)
        for j in range(40): P.circ(30 + random.random() * 1020, STOP_ + 30 + random.random() * (SBOT - STOP_ - 60), 6 + random.random() * 8, SNOW2)

def mouse(P, x, y, s, t, flip=1):
    f = flip; b = abs(math.sin(t * 6)) * 6 * s
    P.line([(x - f * 60 * s, y), (x - f * 140 * s, y - 30 * s + math.sin(t * 3) * 10 * s)], (220, 170, 170), 6 * s)
    P.ell(x, y - b, 75 * s, 45 * s, MOUSE)
    P.circ(x + f * 60 * s, y - 20 * s - b, 34 * s, MOUSE)
    P.circ(x + f * 48 * s, y - 52 * s - b, 18 * s, (235, 180, 180))
    P.circ(x + f * 78 * s, y - 26 * s - b, 6 * s, NIGHT); P.circ(x + f * 94 * s, y - 14 * s - b, 6 * s, (230, 140, 150))

def thermo(P, x, y, k):
    P.rrect(x - 26, y - 170, x + 26, y + 60, 26, CLOUD, outline=(150, 160, 180), w=6)
    P.circ(x, y + 70, 42, lc(COLD, WARM, k)); P.rrect(x - 12, y + 60 - 220 * k, x + 12, y + 60, 12, lc(COLD, WARM, k))

def SC(i, P, t, u):
    if i == 0:
        section(P, t, bubbles=False)
        for j in range(25): P.circ((j * 131 + t * 25) % W, (j * 197 + t * 70) % 900 + CENTER - 650, 5 + j % 3, (255, 255, 255))
        mouse(P, 420, STOP_ - 10, 1.3, t)
        P.text(780, CENTER - 280, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        section(P, t)
        P.stamp(560, CENTER - 300, "TRUE", seg(u, .25, .7), col=HOPE, rot=-6)
        P.badge(540, CENTER + 160, "trapped air", 60, NIGHT, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 2:
        section(P, t)
        P.line([(900, STOP_), (900, STOP_ + 180 * eout(seg(u, .2, .8)))], (110, 120, 150), 8)
        thermo(P, 640, CENTER + 180, .45)
        P.badge(380, CENTER + 180, "15 cm of snow", 52, NIGHT, CLOUD, back(seg(u, .6, 1.1)))
        P.text(640, CENTER + 330, "0 °C", 70, NIGHT)
    elif i == 3:
        section(P, t)
        k = eio(seg(u, .4, 2.4)); c = int(lerp(0, -20, k))
        thermo(P, 300, CENTER - 300, .45 - .4 * k)
        P.text(560, CENTER - 300, f"{c} °C", 90, lc(CLOUD, COLD, k))
        thermo(P, 640, CENTER + 180, .45)
        P.text(840, CENTER + 180, "0 °C", 80, NIGHT)
    elif i == 4:
        section(P, t, bubbles=False)
        P.rrect(80, SBOT - 120, 1000, SBOT - 20, 50, (205, 215, 232))
        P.rrect(600, CENTER + 90, 700, SBOT - 70, 40, (205, 215, 232))
        x = lerp(180, 520, (u * .25) % 1)
        mouse(P, x, SBOT - 50, .7, t); mouse(P, 860, SBOT - 50, .6, t, flip=-1)
        P.badge(540, CENTER - 300, "subnivean zone", 60, GLIM, NIGHT, back(seg(u, 2.2, 2.7)))
    else:
        section(P, t, bubbles=False)
        P.rrect(80, SBOT - 120, 700, SBOT - 20, 50, (205, 215, 232))
        mouse(P, 380, SBOT - 50, .8, t)
        P.stamp(780, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
