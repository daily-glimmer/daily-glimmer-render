# Thema: Do birds fly south just because they get cold?  (Mythos-Format, NOT QUITE in Satz 2, FACT in Satz 6)
# Quellen: Cornell Lab, All About Birds "The Basics of Bird Migration" (Zugvögel folgen Nahrung/Brutplätzen;
# viele Arten halten Frost aus, wenn Futter da ist); Egevang et al. 2010, PNAS (Küstenseeschwalbe ~70.000 km/Jahr).
exec(open(os.path.join(HERE, "topics", "birdtouch.py")).read(), globals())   # bird(), branch()
CENTER = 1050
PAL = ((110, 170, 220), (200, 225, 245))
HI = {"south", "cold?", "not", "quite!", "food,", "warmth.", "insects,", "nectar", "seeds", "feathers", "seventy", "thousand", "food", "trip!"}
WOW = (1,)
SNOWC = (245, 248, 255)

def flyer(P, x, y, s, t, flip=1):
    flap = math.sin(t * 10)
    P.poly([(x - 20 * s, y), (x + 20 * s, y), (x - 10 * s, y - 120 * s * flap)], (95, 70, 55))
    bird(P, x, y, s, t, flip=flip)
    P.poly([(x - 30 * s, y + 5 * s), (x + 10 * s, y + 5 * s), (x - 20 * s, y + 110 * s * flap)], (120, 90, 70))

def bug(P, x, y, t, k=1.):
    if k <= .02: return
    P.circ(x, y, 12 * k, NIGHT); P.ell(x - 10, y - 12, 12 * k, 7 * k, (220, 235, 250)); P.ell(x + 10, y - 12, 12 * k, 7 * k, (220, 235, 250))

def flower(P, x, y, k):
    if k <= .02: return
    P.line([(x, y), (x, y - 120 * k)], (80, 150, 70), 10)
    for a in range(5): P.circ(x + math.cos(a * 1.26) * 26 * k, y - 120 * k + math.sin(a * 1.26) * 26 * k, 20 * k, (240, 120, 160))
    P.circ(x, y - 120 * k, 16 * k, GLIM)

def snowfall(P, t, k=1.):
    for j in range(25):
        P.circ((j * 131 + t * 25) % W, (j * 197 + t * 70) % 1100 + CENTER - 700, (5 + j % 3) * k, (255, 255, 255))

def SC(i, P, t, u):
    if i == 0:
        snowfall(P, t, .8)
        flyer(P, 430 + math.sin(t) * 20, CENTER + 40, 1.4, t)
        P.badge(540, CENTER + 420, "south?", 60, NIGHT, CLOUD, back(seg(u, .8, 1.3)))
        P.text(800, CENTER - 230, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        flyer(P, 380, CENTER + 40, 1.3, t)
        for j in range(4): bug(P, 700 + (j % 2) * 120 + math.sin(t * 3 + j) * 20, CENTER - 40 + (j // 2) * 120, t)
        P.stamp(560, CENTER - 290, "NOT QUITE", seg(u, .25, .7), rot=-6)
        P.badge(540, CENTER + 420, "chasing food", 60, GLIM, NIGHT, back(seg(u, 1.5, 2.0)))
    elif i == 2:
        k = 1 - eio(seg(u, 1.8, 3.8))
        P.poly([(0, CENTER + 330), (W, CENTER + 300), (W, H), (0, H)], lc(SNOWC, (110, 170, 90), k))
        for j, x in enumerate((180, 420, 660, 900)): flower(P, x, CENTER + 320, k)
        for j in range(5): bug(P, 150 + j * 190 + math.sin(t * 3 + j) * 20, CENTER - 60 + (j % 2) * 80, t, k)
        snowfall(P, t, 1 - k)
        P.badge(540, CENTER + 480, "food gets scarce", 58, NIGHT, CLOUD, back(seg(u, 2.0, 2.5)))
    elif i == 3:
        snowfall(P, t); branch(P)
        P.line([(-20, CENTER + 160), (1100, CENTER + 90)], SNOWC, 18)
        bird(P, 540, CENTER + 20, 1.6 + .08 * math.sin(t * 2), t)
        P.badge(540, CENTER + 420, "fluffy feathers = warm coat", 50, NIGHT, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 4:
        P.circ(540, CENTER + 40, 300, (60, 120, 200)); P.ell(450, CENTER - 60, 110, 80, (90, 170, 100)); P.ell(640, CENTER + 160, 90, 110, (90, 170, 100))
        k = eio(seg(u, .4, 3.0))
        pts = [(540 + math.sin(a / 20 * math.pi * 2 * k) * 340, CENTER + 40 - math.cos(a / 20 * math.pi * 2 * k) * 340) for a in range(21)]
        P.line(pts, GLIM, 10)
        P.text(540, CENTER - 360, f"{int(lerp(0, 70000, k)):,} km".replace(",", " "), 90, CLOUD)
        P.badge(540, CENTER + 470, "Arctic tern, every year", 54, NIGHT, CLOUD, back(seg(u, 1.0, 1.5)))
    else:
        flyer(P, 380, CENTER + 60, 1.2, t)
        for j in range(3): bug(P, 700 + j * 90, CENTER + 120 + math.sin(t * 3 + j) * 30, t)
        P.stamp(780, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
