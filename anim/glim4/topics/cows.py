# Thema: Do cows really have four stomachs?  (Mythos-Format, Stempel NOT QUITE / FACT)
CENTER = 1050
COW, SPOT, NOSE = (250, 248, 240), (40, 40, 50), (240, 170, 170)
GRASS = (110, 180, 80)
ROOMS = ((230, 150, 120), (240, 190, 110), (170, 200, 120), (150, 170, 230))
PAL = ((140, 200, 240), (190, 225, 150))
HI = {"four", "stomachs?", "one", "four", "rooms.", "rumen,", "150", "liters,", "microbes.", "tough", "grass", "burp", "chew", "eight", "hours", "cud."}
WOW = (1, 2)
GROUND = CENTER + 260

def meadow(P):
    P.poly([(0, GROUND), (W, GROUND - 20), (W, H), (0, H)], GRASS)
    for k in range(14):
        x = 40 + k * 75; P.line([(x, GROUND + 30 + (k % 3) * 20), (x + 8, GROUND + 5 + (k % 3) * 20)], lc(GRASS, (0, 0, 0), .25), 6)

def cow(P, x, y, s, t, chew=0., happy=False):
    for dx in (-110, -60, 70, 120): P.rrect(x + dx * s - 18 * s, y + 40 * s, x + dx * s + 18 * s, y + 170 * s, 10 * s, COW, outline=SPOT, w=3 * s)
    for dx in (-110, -60, 70, 120): P.rrect(x + dx * s - 18 * s, y + 150 * s, x + dx * s + 18 * s, y + 175 * s, 6 * s, SPOT)
    P.ell(x, y, 190 * s, 105 * s, COW, outline=SPOT, w=4 * s)
    P.ell(x + 60 * s, y - 30 * s, 50 * s, 38 * s, SPOT); P.ell(x - 70 * s, y + 30 * s, 40 * s, 30 * s, SPOT); P.ell(x + 130 * s, y + 40 * s, 28 * s, 22 * s, SPOT)
    P.ell(x - 10 * s, y + 95 * s, 30 * s, 18 * s, NOSE)
    P.line([(x + 185 * s, y - 20 * s), (x + 215 * s, y + 60 * s + 15 * s * math.sin(t * 3))], SPOT, 6 * s)
    hx, hy = x - 205 * s, y - 60 * s
    for d in (-1, 1): P.ell(hx + d * 70 * s, hy - 40 * s, 36 * s, 16 * s, COW, outline=SPOT, w=3 * s)
    for d in (-1, 1): P.poly([(hx + d * 30 * s, hy - 60 * s), (hx + d * 45 * s, hy - 110 * s), (hx + d * 50 * s, hy - 55 * s)], (230, 210, 170))
    P.ell(hx, hy, 70 * s, 80 * s, COW, outline=SPOT, w=4 * s)
    P.ell(hx + 20 * s, hy - 40 * s, 26 * s, 20 * s, SPOT)
    m = math.sin(t * 9) * 8 * s * chew
    P.ell(hx, hy + 50 * s + m * .3, 58 * s, 36 * s + abs(m), NOSE)
    for d in (-1, 1): P.ell(hx + d * 20 * s, hy + 45 * s, 7 * s, 10 * s, (170, 100, 110))
    for d in (-1, 1):
        if happy: P.arc(hx + d * 30 * s, hy - 10 * s, 12 * s, 200, 340, NIGHT, 5 * s)
        else: P.circ(hx + d * 30 * s, hy - 10 * s, 10 * s, NIGHT)

def stomach(P, x, y, s, k=1., big=0):
    """Ein Magen mit vier Kammern; big = Pansen hervorheben."""
    P.ell(x - 70 * s, y, 230 * s * k, 190 * s * k, ROOMS[0], outline=NIGHT, w=6 * s)          # Pansen
    P.circ(x + 130 * s, y - 110 * s, 80 * s * k, ROOMS[1], outline=NIGHT, w=6 * s)          # Netzmagen
    P.circ(x + 200 * s, y + 30 * s, 70 * s * k, ROOMS[2], outline=NIGHT, w=6 * s)           # Blättermagen
    P.ell(x + 140 * s, y + 170 * s, 110 * s * k, 55 * s * k, ROOMS[3], outline=NIGHT, w=6 * s)  # Labmagen
    if big:
        P.ell(x - 70 * s, y, 245 * s, 205 * s, None, outline=GLIM, w=12 * s)

def microbes(P, x, y, r, t, n=14):
    for j in range(n):
        a = j * 2.4 + t * (.6 + j % 3 * .2); rr = r * (.25 + .7 * ((j * 37) % 10) / 10)
        px, py = x + math.cos(a) * rr, y + math.sin(a) * rr * .8
        col = (HOPE, (120, 200, 255), (255, 150, 200))[j % 3]
        P.ell(px, py, 16, 10, col); P.circ(px - 4, py - 2, 3, NIGHT)

def SC(i, P, t, u):
    if i == 0:
        meadow(P); cow(P, 560, GROUND - 170, 1.25, t)
        P.text(840, CENTER - 300, "4?", 130 * back(seg(u, .6, 1.1)), HOOK)
    elif i == 1:
        stomach(P, 500, CENTER + 60, 1.1, back(seg(u, .2, .8)))
        for j, (dx, dy) in enumerate(((-150, 0), (143, -121), (220, 33), (154, 187))):
            q = back(seg(u, 1.2 + j * .25, 1.6 + j * .25))
            P.circ(500 + dx * 1.1, CENTER + 60 + dy * 1.1, 34 * q, NIGHT); P.text(500 + dx * 1.1, CENTER + 60 + dy * 1.1, str(j + 1), 40 * q, CLOUD)
        P.stamp(540, CENTER - 270, "NOT QUITE", seg(u, .25, .7), col=HOOK)
    elif i == 2:
        stomach(P, 540, CENTER + 60, 1.1, 1, big=1)
        microbes(P, 540 - 77, CENTER + 60, 220, t)
        P.badge(540, CENTER + 420, "rumen: ~150 liters", 58, NIGHT, GLIM, back(seg(u, 1.2, 1.7)))
    elif i == 3:
        P.circ(540, CENTER + 40, 300, (240, 200, 170), outline=ROOMS[0], w=12)
        for j in range(7):
            b = eio(seg(u, .6 + j * .15, 1.6 + j * .15))
            gx = 340 + j * 65; gy = CENTER + 40
            P.line([(gx, gy + 120), (gx + 10, gy - 120 + b * 160)], lc(GRASS, (200, 180, 90), b), 14)
        microbes(P, 540, CENTER + 40, 260, t, n=18)
        P.badge(540, CENTER + 420, "microbes digest grass", 54, HOPE, CLOUD, back(seg(u, 1.6, 2.1)))
    elif i == 4:
        meadow(P); cow(P, 600, GROUND - 170, 1.15, t, chew=1.)
        cx, cy = 820, CENTER - 290
        P.circ(cx, cy, 95, CLOUD, outline=NIGHT, w=8)
        a = math.radians(-90 + 360 * eio(seg(u, .5, 3.5)) * 8 / 12)
        P.line([(cx, cy), (cx + math.cos(a) * 70, cy + math.sin(a) * 70)], HOOK, 10)
        P.line([(cx, cy), (cx, cy - 50)], NIGHT, 10)
        P.badge(300, CENTER - 290, "up to 8 h/day", 54, NIGHT, GLIM, back(seg(u, 2.2, 2.7)))
    else:
        meadow(P); cow(P, 560, GROUND - 170, 1.2, t, chew=.6, happy=True)
        P.badge(540, CENTER - 140, "chewing the cud", 58, NIGHT, GLIM, back(seg(u, .5, 1.0)))
        P.stamp(540, CENTER - 330, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
