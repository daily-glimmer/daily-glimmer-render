# Thema: Can a cockroach really live without its head?  (Mythos-Format, TRUE in Satz 2, FACT in Satz 6)
CENTER = 1050
RB, RB2, RL = (140, 75, 40), (105, 55, 30), (90, 50, 30)
PAL = ((40, 30, 50), (120, 90, 80))
HI = {"without", "head?", "true!", "weeks.", "holes", "low", "pressure,", "clot.", "nerve", "clusters", "eat", "drink!"}
WOW = (1,)

def floor(P, y=CENTER + 260):
    P.poly([(0, y), (W, y - 20), (W, H), (0, H)], (170, 140, 110))
    for k in range(6): P.line([(k * 200 - 40, y - 4 * k), (k * 200 + 120, H)], (150, 120, 95), 6)

def roach(P, x, y, s, t, walk=True, head=True, spiracles=0., nerves=0., f=1):
    ph = t * 9 if walk else 0
    for side in (-1, 1):
        for j, dx in enumerate((-70, 0, 70)):
            sw = math.sin(ph + j * 2 + side) * 18 * s if walk else 0
            bx, by = x + f * dx * s, y + side * 30 * s
            P.line([(bx, by), (bx + sw + f * dx * .3 * s, by + side * 90 * s), (bx + sw * 1.5 + f * dx * .6 * s, by + side * 150 * s)], RL, 12 * s)
    P.ell(x - f * 30 * s, y, 170 * s, 72 * s, RB)                                 # Hinterleib + Flügel
    P.line([(x - f * 20 * s, y - 60 * s), (x - f * 20 * s, y + 60 * s)], RB2, 5 * s)
    P.ell(x + f * 115 * s, y, 60 * s, 62 * s, RB2)                                # Brust
    if spiracles > .02:
        for j in range(6):
            P.circ(x - f * (150 - j * 50) * s, y - 38 * s, 9 * s * spiracles, (255, 230, 160), glow=(140, 120, 60))
    if nerves > .02:
        pts = [(x + f * (110 - j * 50) * s, y) for j in range(6)]
        P.line(pts, (255, 230, 120), 6 * s)
        for px, py in pts: P.circ(px, py, 16 * s * nerves, GLIM, glow=mul(GLIM, 160))
    if head:
        hx = x + f * 195 * s
        P.ell(hx, y, 42 * s, 48 * s, RB2)
        P.circ(hx + f * 15 * s, y - 22 * s, 8 * s, NIGHT); P.circ(hx + f * 15 * s, y + 22 * s, 8 * s, NIGHT)
        for side in (-1, 1):
            P.line([(hx + f * 30 * s, y + side * 20 * s), (hx + f * 160 * s, y + side * (90 + math.sin(t * 4) * 20) * s), (hx + f * 260 * s, y + side * 60 * s)], RL, 5 * s)

def SC(i, P, t, u):
    if i == 0:
        floor(P)
        roach(P, 450 + math.sin(t * .8) * 80, CENTER + 60, 1.2, t)
        P.text(820, CENTER - 200, "?", 170 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        floor(P)
        roach(P, 470, CENTER + 60, 1.25, t, walk=False, head=False)
        P.stamp(780, CENTER - 230, "TRUE", seg(u, .25, .7), col=HOPE, rot=-6)
        k = back(seg(u, 1.4, 1.9))
        P.rrect(250, CENTER + 360, 830, CENTER + 540, 30, CLOUD, outline=HOOK, w=8)
        P.rrect(250, CENTER + 360, 830, CENTER + 410, 30, HOOK)
        P.text(540, CENTER + 475, "WEEKS", 66 * k, CLOUD)
    elif i == 2:
        floor(P)
        roach(P, 520, CENTER + 60, 1.4, t, walk=False, head=False, spiracles=back(seg(u, .4, 1.0)))
        for j in range(6):
            q = (t * .8 + j / 6) % 1; x = 520 - (210 - j * 70) * 1.0
            P.circ(x, CENTER - 40 - q * 200, 10 * (1 - q) + 3, (200, 230, 255))
        P.badge(540, CENTER + 470, "breathing holes", 58, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
    elif i == 3:
        P.rrect(80, CENTER - 200, 1000, CENTER + 200, 180, (90, 120, 70))       # Röhre (Blut)
        P.rrect(100, CENTER - 175, 980, CENTER + 175, 160, (190, 220, 150))
        for j in range(7):
            x = (j * 160 + u * 90) % 1100 - 40; P.circ(x, CENTER - 60 + (j % 3) * 60, 22, (230, 250, 200))
        P.badge(540, CENTER + 320, "low pressure", 56, NIGHT, CLOUD, back(seg(u, .5, 1.0)))
        k = back(seg(u, 2.5, 3.0))
        P.circ(900, CENTER - 300, 70 * k, (240, 220, 150), outline=(190, 160, 90), w=6)
        P.badge(820, CENTER - 420, "clot seals it", 46, HOOK, CLOUD, k)
    elif i == 4:
        floor(P)
        roach(P, 470 + u * 30, CENTER + 60, 1.3, t, walk=True, head=False, nerves=back(seg(u, .4, 1.0)))
        P.badge(540, CENTER + 470, "mini brains in each segment", 50, NIGHT, GLIM, back(seg(u, 1.2, 1.7)))
    else:
        floor(P)
        roach(P, 420, CENTER + 80, 1.0, t, walk=False, head=False)
        P.rrect(760, CENTER - 40, 880, CENTER + 200, 30, (120, 190, 255), outline=(60, 120, 200), w=6)
        P.cross(820, CENTER + 80, 70, k=back(seg(u, .9, 1.4)))
        P.stamp(540, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
