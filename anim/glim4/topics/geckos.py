# Thema: How do geckos climb walls?
CENTER = 1050
GK, GK2, SPOT = (120, 190, 90), (90, 150, 70), (250, 150, 60)
PAL = ((255, 214, 170), (170, 210, 240))
HI = {"walls?", "glue", "millions", "setae.", "hundreds", "tips,", "molecule", "van", "der", "waals", "billions", "peels", "clean"}
WOW = (2, 3, 5)

def toe(P, x, y, a, s, col):
    ex, ey = x + math.cos(a) * 70 * s, y + math.sin(a) * 70 * s
    P.line([(x, y), (ex, ey)], col, 18 * s); P.circ(ex, ey, 20 * s, col)
    for k in range(3):
        bx, by = x + math.cos(a) * (38 + k * 11) * s, y + math.sin(a) * (38 + k * 11) * s
        P.line([(bx - math.sin(a) * 12 * s, by + math.cos(a) * 12 * s), (bx + math.sin(a) * 12 * s, by - math.cos(a) * 12 * s)], lc(col, (0, 0, 0), .3), 3 * s)

def gecko(P, x, y, s, t, up=True, walk=1.):
    """Gecko von oben, Kopf nach oben (klettert an der Wand)."""
    ph = math.sin(t * 5) * walk
    P.line([(x, y + 120 * s), (x + 40 * s * math.sin(t * 2), y + 260 * s), (x - 20 * s, y + 340 * s)], GK2, 34 * s)
    for sy, sx, ph2 in ((-60, -1, ph), (-60, 1, -ph), (70, -1, -ph), (70, 1, ph)):
        lx, ly = x + sx * 95 * s, y + (sy + 20 * ph2 * sx) * s
        P.line([(x + sx * 30 * s, y + sy * s), (lx, ly)], GK2, 22 * s)
        for a in (-.6, 0, .6):
            toe(P, lx, ly, (-math.pi / 2 if sy < 0 else math.pi / 2) * .5 + (0 if sx > 0 else math.pi) + a * sx, .55 * s, GK2)
    P.ell(x, y, 62 * s, 150 * s, GK, outline=lc(GK, (0, 0, 0), .3), w=4 * s)
    for k in range(4): P.circ(x + (k % 2 * 2 - 1) * 20 * s, y - 70 * s + k * 45 * s, 11 * s, SPOT)
    P.ell(x, y - 175 * s, 52 * s, 62 * s, GK, outline=lc(GK, (0, 0, 0), .3), w=4 * s)
    for dx in (-30, 30):
        P.circ(x + dx * s, y - 195 * s, 18 * s, (250, 220, 80)); P.ell(x + dx * s, y - 195 * s, 4 * s, 14 * s, NIGHT)

def hairs(P, x0, x1, ybase, h, n, col, t, tips=0):
    for k in range(n):
        x = lerp(x0, x1, k / (n - 1)); sw = math.sin(t * 2 + k) * 4
        P.line([(x, ybase), (x + sw, ybase - h)], col, 6)
        if tips:
            for j in range(-tips, tips + 1): P.line([(x + sw, ybase - h), (x + sw + j * 9, ybase - h - 26)], col, 3)

def SC(i, P, t, u):
    if i == 0:
        P.rrect(80, CENTER - 420, 1000, CENTER + 480, 30, (235, 225, 210), outline=(200, 185, 165), w=4)
        for k in range(1, 6): P.line([(80, CENTER - 420 + k * 150), (1000, CENTER - 420 + k * 150)], (215, 200, 180), 4)
        y = lerp(CENTER + 260, CENTER - 60, eio(seg(u, .1, 1.8)))
        gecko(P, 540, y, 1.25, t)
        P.text(840, CENTER + 330, "?", 150 * back(seg(u, .6, 1.1)), HOOK)
    elif i == 1:
        P.cross(300, CENTER - 300, 70, HOOK, back(seg(u, .2, .6)))
        P.badge(300, CENTER - 160, "no glue", 54, HOOK, CLOUD, back(seg(u, .3, .8)))
        # Zeh in Großaufnahme mit Lamellen voller Härchen
        P.rrect(380, CENTER - 120, 980, CENTER + 220, 160, GK, outline=lc(GK, (0, 0, 0), .3), w=6)
        g = eio(seg(u, 1.0, 2.6))
        for r in range(4):
            yb = CENTER + 210 - r * 0
            hairs(P, 450 + r * 130, 540 + r * 130, CENTER + 220, 60 * g, 6, (90, 140, 70), t)
        P.badge(680, CENTER + 360, "millions of setae", 58, NIGHT, GLIM, back(seg(u, 2.0, 2.5)))
    elif i == 2:
        g = eio(seg(u, .3, 2.0))
        P.line([(540, CENTER + 320), (540, CENTER - 40)], (90, 140, 70), 26)
        for j in range(12):
            a = -math.pi / 2 + (j - 5.5) * .14 * g
            ex, ey = 540 + math.cos(a) * 320 * g, CENTER - 40 + math.sin(a) * 320 * g
            P.line([(540, CENTER - 40), (ex, ey)], (90, 140, 70), 8)
            P.ell(ex, ey, 22 * g + 1, 8 * g + 1, (60, 110, 50))
        P.rrect(120, CENTER - 420, 960, CENTER - 370, 10, (180, 170, 160))
        P.badge(540, CENTER + 420, "hundreds of tips per hair", 52, NIGHT, GLIM, back(seg(u, 1.6, 2.1)))
    elif i == 3:
        P.rrect(80, CENTER + 120, 1000, CENTER + 480, 20, (180, 170, 160))
        for k in range(9):                      # Wand-Moleküle
            P.circ(140 + k * 100, CENTER + 150, 36, (140, 150, 200), outline=(90, 100, 150), w=4)
        d = 1 - eio(seg(u, .2, 1.4))
        for k in range(9):                      # Spatel-Spitzen kommen nah
            x = 140 + k * 100; y = CENTER - 20 - 160 * d
            P.ell(x, y, 40, 16, (60, 110, 50)); P.line([(x, y - 16), (x, y - 220)], (90, 140, 70), 10)
        if u > 1.4:
            for k in range(9):
                q = (t * 1.5 + k * .3) % 1
                P.line([(140 + k * 100, CENTER + 2), (140 + k * 100, CENTER + 2 + 80 * q)], GLIM, 6)
        P.badge(540, CENTER - 330, "van der Waals force", 56, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
    elif i == 4:
        P.rrect(80, CENTER - 520, 1000, CENTER + 480, 30, (200, 230, 250), outline=(160, 190, 220), w=4)   # Glasscheibe
        P.line([(160, CENTER - 460), (330, CENTER - 290)], CLOUD, 14); P.line([(200, CENTER - 460), (300, CENTER - 360)], CLOUD, 8)
        gecko(P, 540, CENTER + 20 + math.sin(t * 1.2) * 20, 1.2, t, walk=.4)
        P.badge(540, CENTER + 400, "billions of tips", 58, HOPE, CLOUD, back(seg(u, .8, 1.3)))
    else:
        P.rrect(80, CENTER - 380, 1000, CENTER + 480, 30, (235, 225, 210), outline=(200, 185, 165), w=4)
        x = lerp(220, 860, (t * .1) % 1)
        gecko(P, 540, CENTER + 120, 1.0, t)
        random.seed(8)
        for k in range(10):                     # Staub fällt ab
            q = (t * .6 + random.random()) % 1
            P.circ(400 + random.random() * 280, lerp(CENTER + 40, CENTER + 460, q), 6 + random.random() * 6, (150, 130, 110))
        P.badge(540, CENTER - 300, "self-cleaning feet", 60, NIGHT, GLIM, back(seg(u, .8, 1.3)))
