# Thema: Can touching a toad really give you warts?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6)
# Quellen: Forest Preserve District of Will County "Myth buster: Frogs and toads don't cause warts" (Warzen = HPV,
# Toad-Höcker = Drüsen mit Abwehrgift, Hände waschen), Wonderopolis / HowStuffWorks; PMC8731828 "Toads and Warts".
CENTER = 1050
TOAD, TOAD2, BELLY, GLAND = (140, 120, 70), (110, 95, 55), (220, 205, 150), (165, 145, 90)
SKINH = (240, 195, 160)
PAL = ((90, 140, 100), (190, 210, 160))
HI = {"toad", "warts?", "myth!", "virus", "hpv,", "people.", "glands", "poison.", "wash", "hands", "warts!"}
WOW = (1,)
GROUND = CENTER + 300

def ground(P):
    P.poly([(0, GROUND), (W, GROUND - 25), (W, H), (0, H)], (110, 90, 60))
    for x in (100, 520, 960): P.ell(x, GROUND - 5, 80, 26, (80, 140, 70))

def toad(P, x, y, s, t, blink=True):
    br = 1 + .04 * math.sin(t * 3)
    for dx in (-120, 120): P.ell(x + dx * s, y - 10 * s, 70 * s, 40 * s, TOAD2)
    P.ell(x, y - 80 * s, 190 * s, 120 * s * br, TOAD)
    P.ell(x, y - 30 * s, 120 * s, 50 * s, BELLY)
    random.seed(11)
    for j in range(14):
        a = random.random() * math.pi; r = .4 + .5 * random.random()
        P.circ(x + math.cos(a) * 160 * s * r, y - 90 * s - math.sin(a) * 90 * s * r, (10 + 8 * random.random()) * s, GLAND)
    for ex in (-75, 75):
        P.circ(x + ex * s, y - 190 * s, 38 * s, TOAD); P.circ(x + ex * s, y - 192 * s, 24 * s, (230, 190, 60))
        P.ell(x + ex * s, y - 192 * s, 18 * s, 6 * s if (blink and (t % 3) < .12) else 16 * s, NIGHT)
    P.arc(x, y - 120 * s, 90 * s, 20, 160, NIGHT, 6 * s)

def virus(P, x, y, r, t):
    P.circ(x, y, r, (200, 90, 160))
    for k in range(10):
        a = k * math.pi / 5 + t * .4
        P.line([(x + math.cos(a) * r, y + math.sin(a) * r), (x + math.cos(a) * (r + 24), y + math.sin(a) * (r + 24))], (200, 90, 160), 8)
        P.circ(x + math.cos(a) * (r + 28), y + math.sin(a) * (r + 28), 9, (240, 150, 200))

def SC(i, P, t, u):
    if i == 0:
        ground(P); toad(P, 470, GROUND - 10, 1.3, t)
        P.ell(lerp(1000, 820, eout(seg(u, .3, 1.3))), CENTER - 120, 60, 110, SKINH)
        P.text(820, CENTER - 330, "?", 160 * back(seg(u, .8, 1.3)), GLIM)
    elif i == 1:
        ground(P); toad(P, 470, GROUND - 10, 1.3, t)
        P.stamp(560, CENTER - 300, "MYTH", seg(u, .25, .7), rot=-6)
        P.badge(540, CENTER + 470, "no warts from toads", 58, NIGHT, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 2:
        virus(P, 540, CENTER - 60, 120 * back(seg(u, .3, .9)), t)
        P.badge(540, CENTER + 170, "HPV virus", 60, HOOK, CLOUD, back(seg(u, .9, 1.4)))
        P.badge(540, CENTER + 330, "spreads between people", 54, NIGHT, CLOUD, back(seg(u, 2.0, 2.5)))
    elif i == 3:
        P.circ(540, CENTER + 20, 330, TOAD)
        for j, (dx, dy) in enumerate(((-150, -90), (60, -150), (170, 40), (-60, 120), (-200, 120), (80, 200))):
            P.circ(540 + dx, CENTER + 20 + dy, 55, GLAND)
            q = (u * .8 + j / 6) % 1
            if u > 1: P.ell(540 + dx, CENTER + 20 + dy - 60 - q * 40, 12, 18, (235, 240, 210))
        P.badge(540, CENTER - 380, "poison glands", 60, GLIM, NIGHT, back(seg(u, .8, 1.3)))
    elif i == 4:
        ground(P); toad(P, 330, GROUND - 10, .9, t)
        P.badge(330, CENTER - 120, "predators: yuck!", 50, HOOK, CLOUD, back(seg(u, .4, .9)))
        for j in range(6):
            q = (u * 1.2 + j / 6) % 1
            P.circ(780 + math.sin(j * 2) * 60, CENTER - 60 + q * 260, 14 * (1 - q), (120, 190, 240))
        P.ell(740, CENTER + 120, 60, 110, SKINH); P.ell(830, CENTER + 120, 60, 110, SKINH)
        P.badge(790, CENTER + 330, "wash your hands", 52, NIGHT, CLOUD, back(seg(u, 2.0, 2.5)))
    else:
        ground(P); toad(P, 380, GROUND - 10, 1.0, t)
        P.stamp(780, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
