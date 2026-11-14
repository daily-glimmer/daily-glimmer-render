# Thema: Can owls turn their heads all the way around?  (Mythos-Format: „almost“)
CENTER = 1050
OWL, OWL2, BELLY = (150, 110, 75), (115, 80, 55), (225, 200, 160)
PAL = ((20, 30, 60), (70, 90, 130))
HI = {"all", "around?", "almost,", "seventy", "degrees.", "fixed", "whole", "fourteen", "twice", "blood", "pools", "back,", "safely!"}
WOW = (1, 4)

def branch(P, y=CENTER + 250):
    P.line([(0, y), (1080, y - 40)], (110, 75, 45), 34)
    for k in range(4): P.ell(140 + k * 260, y - 40 - (k % 2) * 20, 70, 28, (70, 140, 80))

def owl(P, x, y, s, t, turn=0., blink=False):
    P.ell(x, y + 40 * s, 120 * s, 160 * s, OWL)
    P.ell(x, y + 70 * s, 80 * s, 115 * s, BELLY)
    for k in range(3):
        for j in (-1, 1): P.arc(x + j * 30 * s, y + (20 + k * 45) * s, 18 * s, 20, 160, OWL2, 5 * s)
    for side in (-1, 1): P.ell(x + side * 105 * s, y + 50 * s, 40 * s, 110 * s, OWL2)
    for dx in (-30, 30): P.line([(x + dx * s, y + 190 * s), (x + dx * s, y + 215 * s)], (240, 180, 60), 12 * s)
    # Kopf mit Drehung (turn in Grad, ±; Gesicht wandert seitlich, ab 90° sieht man den Hinterkopf)
    hx, hy = x, y - 130 * s
    P.circ(hx, hy, 105 * s, OWL)
    a = math.radians(turn); vis = math.cos(a); off = math.sin(a) * 70 * s
    for side in (-1, 1): P.poly([(hx + side * 60 * s, hy - 70 * s), (hx + side * 95 * s, hy - 140 * s), (hx + side * 95 * s, hy - 60 * s)], OWL2)
    if vis > -.2:
        w = max(.15, vis)
        for side in (-1, 1):
            ex = hx + off + side * 42 * s * w
            P.ell(ex, hy - 5 * s, 40 * s * w, 40 * s, (250, 240, 220))
            if blink: P.arc(ex, hy - 5 * s, 22 * s * w, 200, 340, NIGHT, 6 * s)
            else: P.ell(ex, hy - 5 * s, 26 * s * w, 26 * s, (255, 190, 40)); P.ell(ex, hy - 5 * s, 13 * s * w, 14 * s, NIGHT)
        P.poly([(hx + off - 12 * s * w, hy + 30 * s), (hx + off + 12 * s * w, hy + 30 * s), (hx + off, hy + 60 * s)], (240, 180, 60))
    else:
        for k in range(3): P.arc(hx, hy + (k * 25 - 20) * s, 50 * s, 20, 160, OWL2, 6 * s)

def dial(P, x, y, r, deg, col=GLIM):
    P.circ(x, y, r, (30, 40, 70), outline=(90, 110, 160), w=8)
    if deg > 1: P.arc(x, y, r - 18, -90, -90 + deg, col, 30)
    P.text(x, y, f"{int(deg)}°", r * .42, CLOUD)

def SC(i, P, t, u):
    if i == 0:
        branch(P); owl(P, 540, CENTER + 10, 1.4, t, turn=math.sin(u * 1.5) * 150)
        P.text(540, CENTER - 450, "360?", 120 * back(seg(u, .4, .9)), GLIM)
    elif i == 1:
        k = eio(seg(u, .3, 2.5)); dial(P, 540, CENTER - 40, 260, 270 * k)
        P.cross(540, CENTER - 330, 50, k=back(seg(u, 2.6, 3.1)))
        P.stamp(820, CENTER + 330, "ALMOST", seg(u, .2, .6), col=HOOK, rot=-8)
    elif i == 2:
        branch(P); owl(P, 540, CENTER + 10, 1.3, t, turn=math.sin(u * 2) * 70)
        for side in (-1, 1): P.rrect(540 + side * 330 - 90, CENTER - 340, 540 + side * 330 + 90, CENTER - 250, 30, NIGHT)
        P.text(210, CENTER - 295, "eyes", 50, GLIM); P.text(870, CENTER - 295, "fixed", 50, GLIM)
    elif i == 3:
        for k in range(14):
            kk = back(seg(u, .1 + k * .12, .4 + k * .12))
            P.rrect(330, CENTER - 420 + k * 58, 330 + 120 * kk, CENTER - 380 + k * 58, 12, (235, 230, 215))
        for k in range(7):
            kk = back(seg(u, 2.0 + k * .12, 2.3 + k * .12))
            P.rrect(640, CENTER - 420 + k * 116, 640 + 120 * kk, CENTER - 350 + k * 116, 12, (200, 200, 210))
        P.text(390, CENTER + 430, "owl 14", 60, GLIM); P.text(700, CENTER + 430, "you 7", 60, CLOUD)
    elif i == 4:
        P.ell(540, CENTER - 80, 200, 220, OWL)
        P.line([(540, CENTER + 140), (540, CENTER + 480)], OWL, 120)
        P.line([(500, CENTER + 480), (500, CENTER - 40)], (210, 50, 70), 22)
        P.line([(580, CENTER + 480), (580, CENTER - 40)], (210, 50, 70), 22)
        k = .7 + .3 * math.sin(t * 3)
        for x in (500, 580): P.circ(x, CENTER + 90, 50 * k, (230, 60, 80), glow=mul(HOOK, 160))
        P.badge(540, CENTER - 360, "blood reservoirs", 58, HOOK, CLOUD, back(seg(u, .5, 1.0)))
    else:
        branch(P); owl(P, 540, CENTER + 10, 1.35, t, turn=180 if (u % 3) < 1.6 else 0)
        P.stamp(540, CENTER - 430, "270°", seg(u, .3, .7), col=HOPE, rot=8)
