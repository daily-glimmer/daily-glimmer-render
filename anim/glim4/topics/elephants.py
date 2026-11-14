# Thema: Do elephants drink through their trunks like a straw?  (Mythos-Format)
CENTER = 1050
GRAY, GRAY2 = (150, 155, 170), (120, 125, 140)
PAL = ((40, 60, 70), (170, 150, 110))
HI = {"straw?", "water", "bottle.", "squirts", "mouth.", "three", "liters", "second!", "stretch", "nine", "trunk,", "straw!"}
WOW = (1, 3)

def savanna(P, y=CENTER + 250):
    P.poly([(0, y), (W, y - 20), (W, H), (0, H)], (200, 180, 110))
    P.line([(900, y - 10), (920, y - 260)], (110, 80, 50), 22); P.ell(920, y - 280, 140, 50, (90, 140, 70))

def pool(P, x, y, rx): P.ell(x, y, rx, rx * .22, (70, 150, 220))

def elephant(P, x, y, s, t, trunk="down", fill=0.):
    for dx in (-90, -40, 60, 110): P.rrect(x + dx * s - 28 * s, y + 40 * s, x + dx * s + 28 * s, y + 200 * s, 14 * s, GRAY2)
    P.ell(x, y, 170 * s, 110 * s, GRAY)
    P.line([(x + 165 * s, y - 20 * s), (x + 195 * s, y + 50 * s)], GRAY2, 8 * s)
    hx, hy = x - 160 * s, y - 70 * s
    P.ell(hx + 50 * s, hy + 10 * s, 85 * s, 110 * s, GRAY2)                     # Ohr
    P.circ(hx, hy, 85 * s, GRAY)
    P.circ(hx - 30 * s, hy - 15 * s, 10 * s, NIGHT); P.circ(hx - 27 * s, hy - 18 * s, 3 * s, (255, 255, 255))
    P.poly([(hx - 30 * s, hy + 40 * s), (hx - 70 * s, hy + 60 * s), (hx - 40 * s, hy + 75 * s)], (245, 240, 225))   # Stoßzahn
    if trunk == "down":
        pts = [(hx - 60 * s, hy + 30 * s), (hx - 110 * s, hy + 130 * s), (hx - 120 * s, hy + 240 * s)]
    elif trunk == "mouth":
        pts = [(hx - 60 * s, hy + 30 * s), (hx - 130 * s, hy + 110 * s), (hx - 90 * s, hy + 150 * s), (hx - 40 * s, hy + 80 * s)]
    else:
        pts = [(hx - 60 * s, hy + 30 * s), (hx - 140 * s, hy - 40 * s), (hx - 150 * s, hy - 140 * s)]
    P.line(pts, GRAY, 40 * s)
    if fill > 0: P.line(pts[:2] + [lerp_pt(pts[1], pts[2], fill)], (90, 170, 240), 18 * s)

def lerp_pt(a, b, k): return (lerp(a[0], b[0], k), lerp(a[1], b[1], k))

def straw(P, x, y, s):
    P.rrect(x - 18 * s, y - 220 * s, x + 18 * s, y, 8 * s, (255, 120, 150))
    for k in range(4): P.line([(x - 18 * s, y - 200 * s + k * 50 * s), (x + 18 * s, y - 180 * s + k * 50 * s)], CLOUD, 8 * s)

def SC(i, P, t, u):
    if i == 0:
        savanna(P); pool(P, 320, CENTER + 300, 220)
        elephant(P, 650, CENTER + 50, 1.1, t, "down")
        straw(P, 220, CENTER + 120, 1.2 * back(seg(u, .4, .9)))
        P.text(220, CENTER - 180, "?", 140 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        savanna(P); elephant(P, 600, CENTER + 50, 1.15, t, "down")
        P.stamp(540, CENTER - 340, "MYTH", seg(u, .25, .7))
        P.rrect(820, CENTER - 160, 920, CENTER + 60, 30, (120, 190, 255), outline=(60, 120, 200), w=6)
        P.check(870, CENTER - 230, 40, k=back(seg(u, 1.0, 1.5)))
    elif i == 2:
        savanna(P); pool(P, 260, CENTER + 300, 200)
        ph = (u % 4) / 4
        if ph < .5:
            elephant(P, 620, CENTER + 50, 1.0, t, "down", fill=eio(ph * 2))
        else:
            elephant(P, 620, CENTER + 50, 1.0, t, "mouth")
            for k in range(5):
                q = (t * 3 + k / 5) % 1; P.circ(lerp(470, 520, q), lerp(CENTER + 60, CENTER - 20, q), 14, (90, 170, 240))
        P.badge(540, CENTER - 330, "1. suck up   2. squirt in", 50, NIGHT, GLIM, back(seg(u, .4, .9)))
    elif i == 3:
        P.circ(540, CENTER - 60, 220, (240, 245, 255), outline=(150, 170, 200), w=10)
        a = (u * 2 * math.pi) % (2 * math.pi) - math.pi / 2
        P.line([(540, CENTER - 60), (540 + math.cos(a) * 180, CENTER - 60 + math.sin(a) * 180)], HOOK, 14)
        P.text(540, CENTER - 360, "1 second", 60, CLOUD)
        k = (u % 1)
        for j in range(3):
            kk = back(seg(u, .3 + j * .5, .7 + j * .5))
            P.rrect(330 + j * 150, CENTER + 260, 430 + j * 150, CENTER + 420, 20, (120, 190, 255) if kk > .5 else (60, 80, 110))
            P.text(380 + j * 150, CENTER + 340, "1 L", 40 * max(.3, kk), CLOUD)
    elif i == 4:
        k = (math.sin(u * 2.5) + 1) / 2
        P.rrect(140, CENTER - 160, 940, CENTER + 160, 160, GRAY, outline=GRAY2, w=10)
        for side in (-1, 1):
            P.ell(540, CENTER + side * (60 + 20 * k), 360, 40 + 30 * k, (90, 170, 240), outline=(60, 120, 200), w=4)
        P.badge(540, CENTER - 300, "up to ~9 liters", 62, HOPE, CLOUD, back(seg(u, .5, 1.0)))
        P.text(540, CENTER + 300, "+64% stretch", 56, GLIM)
    else:
        savanna(P); elephant(P, 560, CENTER + 50, 1.1, t, "up")
        for k in range(8):
            q = (t * 1.5 + k / 8) % 1; P.circ(560 - 225 + math.sin(k) * 60 * q, CENTER - 210 - q * 250, 14 * (1 - q) + 4, (120, 190, 255))
        P.stamp(540, CENTER - 360, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
