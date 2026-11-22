# Thema: Do carrots really help you see in the dark?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6)
# Quellen: Smithsonian Magazine (WWII-Propaganda, RAF-Radar 1940, John Cunningham "Cat's Eyes"),
# Live Science / The Ophthalmologist 2026 (Vitamin A hilft nur bei Mangel, keine Supersicht).
CENTER = 1050
ORANGE, ORANGE2, LEAF = (245, 140, 40), (215, 110, 30), (70, 160, 80)
PAL = ((30, 40, 80), (90, 80, 130))
HI = {"carrots", "dark?", "myth!", "night", "vision.", "vitamin", "a", "blindness,", "won't", "radar", "carrots.", "trick,", "wrong"}
WOW = (1,)
GROUND = CENTER + 330

def ground(P):
    P.poly([(0, GROUND), (W, GROUND - 30), (W, H), (0, H)], (60, 90, 70))

def carrot(P, x, y, s, t, rot=0.):
    """Karotte mit Spitze nach unten bei (x, y + 260 s)."""
    c, sn = math.cos(rot), math.sin(rot)
    R = lambda dx, dy: (x + (dx * c - dy * sn) * s, y + (dx * sn + dy * c) * s)
    for k, a in enumerate((-.5, 0, .5)):
        sw = math.sin(t * 2 + k) * 8
        P.line([R(0, -120), R(a * 90 + sw, -260)], LEAF, 26 * s)
        P.ell(*R(a * 95 + sw, -270), 34 * s, 22 * s, LEAF)
    P.poly([R(-75, -125), R(75, -125), R(8, 260), R(-8, 260)], ORANGE)
    P.poly([R(20, -125), R(75, -125), R(8, 260)], ORANGE2)
    for j in range(4): P.line([R(-50 + j * 8, -60 + j * 70), R(-15 + j * 8, -55 + j * 70)], ORANGE2, 8 * s)

def eye(P, x, y, s, k=1., glow=False):
    P.ell(x, y, 150 * s, 90 * s * max(.08, k), CLOUD, glow=mul(GLIM, 160) if glow else None)
    if k > .3:
        P.circ(x, y, 55 * s, (80, 130, 200)); P.circ(x, y, 26 * s, NIGHT); P.circ(x + 14 * s, y - 14 * s, 9 * s, (255, 255, 255))

def moon(P, x, y, r=70):
    P.circ(x, y, r, (250, 245, 220), glow=(90, 90, 60))

def plane(P, x, y, s, t):
    P.ell(x, y, 170 * s, 34 * s, (180, 190, 205))
    P.poly([(x - 20 * s, y), (x + 40 * s, y), (x - 60 * s, y + 130 * s), (x - 100 * s, y + 130 * s)], (150, 160, 180))
    P.poly([(x - 20 * s, y), (x + 40 * s, y), (x - 60 * s, y - 130 * s), (x - 100 * s, y - 130 * s)], (150, 160, 180))
    P.poly([(x - 150 * s, y), (x - 120 * s, y), (x - 175 * s, y - 70 * s), (x - 195 * s, y - 70 * s)], (150, 160, 180))
    P.circ(x + 110 * s, y - 8 * s, 18 * s, (120, 200, 240))

def SC(i, P, t, u):
    if i == 0:
        ground(P); moon(P, 840, CENTER - 230)
        carrot(P, 380, CENTER + 20, 1.1, t, rot=-.25)
        eye(P, 760, CENTER + 140, .8, k=.55 + .45 * abs(math.sin(t * 1.5)))
        P.text(860, CENTER - 20, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        ground(P); moon(P, 840, CENTER - 230)
        carrot(P, 330, CENTER + 40, 1.0, t, rot=-.2)
        eye(P, 740, CENTER + 120, .9, glow=True)
        P.cross(740, CENTER + 120, 130, k=back(seg(u, 1.0, 1.4)))
        P.stamp(560, CENTER + 470, "MYTH", seg(u, .25, .7), rot=-6)
    elif i == 2:
        carrot(P, 230, CENTER + 40, .85, t)
        k = eout(seg(u, .6, 1.6))
        P.line([(370, CENTER + 60), (lerp(370, 520, k), CENTER + 60)], CLOUD, 16)
        if k > .95: P.poly([(520, CENTER + 30), (560, CENTER + 60), (520, CENTER + 90)], CLOUD)
        P.badge(700, CENTER + 60, "vitamin A", 62, GLIM, NIGHT, back(seg(u, 1.4, 1.9)))
        eye(P, 700, CENTER + 330, .7, k=eout(seg(u, 2.2, 2.8)))
        P.badge(540, CENTER - 200, "beta-carotene", 52, ORANGE2, CLOUD, back(seg(u, .3, .8)))
    elif i == 3:
        k = eio(seg(u, .4, 1.6))
        eye(P, 300, CENTER + 40, .75, k=1 - .85 * k)
        P.badge(300, CENTER + 230, "too little: night blindness", 44, HOOK, CLOUD, back(seg(u, .8, 1.3)))
        eye(P, 780, CENTER + 40, .75)
        carrot(P, 900, CENTER + 330, .45, t, rot=.4); carrot(P, 700, CENTER + 340, .45, t, rot=-.3)
        P.badge(780, CENTER + 230, "extra: no super eyes", 44, NIGHT, CLOUD, back(seg(u, 2.2, 2.7)))
    elif i == 4:
        moon(P, 880, CENTER - 250, 55)
        x = lerp(-100, 1180, (u * .12) % 1)
        plane(P, 420, CENTER + 60, 1.1, t)
        waves(P, 560, CENTER + 50, t, GLIM, n=3, r0=60, dr=70, a0=-40, a1=40)
        P.ell(880, CENTER + 20, 70, 22, (60, 60, 70)); P.poly([(870, CENTER + 20), (910, CENTER + 20), (850, CENTER + 90), (830, CENTER + 90)], (60, 60, 70))
        P.badge(540, CENTER + 330, "secret radar, 1940", 58, NIGHT, GLIM, back(seg(u, .6, 1.1)))
        P.badge(540, CENTER + 470, "cover story: carrots", 52, ORANGE2, CLOUD, back(seg(u, 2.6, 3.1)))
    else:
        ground(P); moon(P, 200, CENTER - 230, 55)
        carrot(P, 380, CENTER + 100, 1.0, t, rot=math.sin(t * 2) * .1)
        P.stamp(780, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
