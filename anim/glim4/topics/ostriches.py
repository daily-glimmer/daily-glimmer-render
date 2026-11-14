# Thema: Do ostriches bury their heads in the sand?  (Mythos-Format)
CENTER = 1050
OST, OST2, SKIN = (50, 45, 50), (240, 240, 235), (235, 170, 160)
SAND, SAND2 = (232, 196, 130), (210, 170, 105)
PAL = ((80, 60, 40), (230, 170, 90))
HI = {"heads", "sand?", "never!", "breathe.", "eggs", "hole", "turn", "beaks.", "flat", "bush.", "gone!", "myth"}
WOW = (1,)

def ground(P, y=CENTER + 230):
    P.poly([(0, y), (W, y - 20), (W, H), (0, H)], SAND)
    for k in range(5): P.ell(120 + k * 220, y + 120 + (k % 2) * 60, 60, 14, SAND2)

def ostrich(P, x, y, s, t, neck="up", head_hidden=False, flat=False):
    if flat:
        P.ell(x, y + 60 * s, 170 * s, 70 * s, OST)
        P.ell(x + 60 * s, y + 40 * s, 80 * s, 40 * s, OST2)
        P.line([(x - 150 * s, y + 90 * s), (x - 380 * s, y + 110 * s)], SKIN, 22 * s)
        P.ell(x - 400 * s, y + 108 * s, 30 * s, 20 * s, SKIN); P.circ(x - 405 * s, y + 100 * s, 6 * s, NIGHT)
        return
    st = math.sin(t * 2) * 5 * s
    for dx in (-30, 30):
        P.line([(x + dx * s, y + 50 * s), (x + dx * s + 15 * s, y + 160 * s), (x + dx * s, y + 260 * s)], SKIN, 18 * s)
        P.ell(x + dx * s + 15 * s, y + 262 * s, 30 * s, 10 * s, SKIN)
    P.ell(x, y, 150 * s, 95 * s, OST)
    for k in range(4): P.ell(x + 90 * s + k * 18 * s, y - 25 * s + k * 15 * s, 55 * s, 25 * s, OST2)   # Schwanzfedern
    if neck == "up":
        hx, hy = x - 110 * s, y - 330 * s + st
        P.line([(x - 100 * s, y - 40 * s), (x - 120 * s, y - 180 * s), (hx, hy)], SKIN, 26 * s)
    else:
        hx, hy = x - 230 * s, y + 160 * s
        P.line([(x - 110 * s, y - 20 * s), (x - 210 * s, y + 40 * s), (hx, hy)], SKIN, 26 * s)
    if not head_hidden:
        P.ell(hx, hy, 38 * s, 30 * s, SKIN)
        P.circ(hx - 8 * s, hy - 6 * s, 12 * s, NIGHT); P.circ(hx - 4 * s, hy - 10 * s, 4 * s, (255, 255, 255))
        P.poly([(hx - 30 * s, hy), (hx - 75 * s, hy + 10 * s), (hx - 30 * s, hy + 16 * s)], (230, 150, 80))

def eggs(P, x, y, s, rot=0.):
    for k in range(5):
        a = k * 1.25 + rot; P.ell(x + math.cos(a) * 70 * s, y + math.sin(a) * 18 * s, 34 * s, 42 * s, (252, 248, 236), outline=(220, 210, 190), w=3)

def SC(i, P, t, u):
    if i == 0:
        ground(P); ostrich(P, 600, CENTER - 20, 1.1, t, neck="down", head_hidden=True)
        P.ell(600 - 253, CENTER + 230, 70, 22, SAND2)
        P.text(350, CENTER - 200, "?", 150 * back(seg(u, .4, .9)), GLIM)
    elif i == 1:
        ground(P); ostrich(P, 560, CENTER - 20, 1.15, t)
        P.stamp(800, CENTER - 380, "MYTH", seg(u, .25, .7))
        P.badge(540, CENTER + 470, "they'd suffocate", 58, NIGHT, CLOUD, back(seg(u, 1.0, 1.5)))
    elif i == 2:
        ground(P)
        k = eout(seg(u, .2, 1.5))
        P.ell(540, CENTER + 260, 330 * k, 80 * k, SAND2)
        for j in range(5):
            if seg(u, 1.0 + j * .25, 1.3 + j * .25) > 0:
                a = j * 1.25; P.ell(540 + math.cos(a) * 140, CENTER + 250 + math.sin(a) * 30, 46, 58, (252, 248, 236), outline=(220, 210, 190), w=3)
        ostrich(P, 820, CENTER - 60, .9, t)
        P.badge(540, CENTER + 470, "a shallow nest", 58, HOPE, CLOUD, back(seg(u, .6, 1.1)))
    elif i == 3:
        ground(P)
        P.ell(390, CENTER + 260, 300, 70, SAND2); eggs(P, 390, CENTER + 250, 1.6, rot=math.sin(t * 2) * .3)
        ostrich(P, 640, CENTER + 10, 1.0, t, neck="down")
        for k in range(2):
            q = (t * .8 + k / 2) % 1; P.arc(390, CENTER + 250, 150 + q * 60, 200, 340, lc(GLIM, (0, 0, 0), q), 8)
        P.badge(540, CENTER - 330, "turning the eggs", 58, NIGHT, GLIM, back(seg(u, .5, 1.0)))
    elif i == 4:
        ground(P)
        for k in range(3): P.circ(160 + k * 70, CENTER + 140 - (k % 2) * 30, 70, (120, 150, 70))
        ostrich(P, 640, CENTER + 70, 1.0, t, flat=True)
        P.badge(540, CENTER - 330, "hiding in plain sight", 54, HOPE, CLOUD, back(seg(u, .6, 1.1)))
    else:
        ground(P)
        P.rrect(120, CENTER - 200, 960, CENTER + 330, 40, (255, 250, 235), outline=(200, 170, 120), w=8)
        ostrich(P, 600, CENTER + 10, .75, t, neck="down")
        P.arc(600, CENTER - 20, 230, 0, 360, NIGHT, 10)
        P.line([(760, CENTER + 140), (900, CENTER + 290)], NIGHT, 26)
        P.stamp(540, CENTER - 380, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
