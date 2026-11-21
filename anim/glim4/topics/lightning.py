# Thema: Does lightning never strike the same place twice?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6)
CENTER = 1050
PAL = ((25, 25, 55), (70, 70, 110))
HI = {"never", "twice?", "myth!", "again", "tall,", "pointy", "towers", "skyscrapers", "twenty", "five", "eight", "four", "tree"}
WOW = (1, 4)
BOLT = (255, 245, 170)
CITY = (40, 45, 75)

def cloud(P, x, y, s, col=(90, 90, 120)):
    for dx, dy, r in ((-120, 20, 90), (-30, -20, 120), (90, 10, 100), (170, 40, 70)):
        P.circ(x + dx * s, y + dy * s, r * s, col)

def bolt(P, x0, y0, x1, y1, seed, k=1.):
    if k <= 0: return
    random.seed(seed); pts = [(x0, y0)]
    for j in range(1, 8):
        q = j / 8; pts.append((lerp(x0, x1, q) + (random.random() - .5) * 90, lerp(y0, y1, q)))
    pts.append((x1, y1)); n = max(2, int(len(pts) * k))
    P.line(pts[:n], BOLT, 14, glow=(200, 190, 120))

def skyline(P, y=CENTER + 330, tower=True):
    for x, h, w_ in ((90, 260, 140), (250, 380, 120), (720, 300, 150), (900, 220, 140)):
        P.rrect(x - w_ / 2, y - h, x + w_ / 2, y + 400, 8, CITY)
    if tower:
        P.rrect(420, y - 380, 660, y + 400, 10, (55, 60, 95))
        P.rrect(470, y - 480, 610, y - 370, 8, (55, 60, 95)); P.rrect(510, y - 570, 570, y - 470, 6, (55, 60, 95))
        P.line([(540, y - 570), (540, y - 650)], (180, 185, 210), 10)
        for r_ in range(5):
            for c in range(4): P.rrect(440 + c * 55, y - 350 + r_ * 70, 470 + c * 55, y - 320 + r_ * 70, 4, (250, 220, 120) if (r_ + c) % 3 else (80, 90, 130))

def flash(P, t, k):
    if k > 0: P.rrect(0, 0, W, H, 0, lc(PAL[0], (200, 200, 230), k * .25))

def SC(i, P, t, u):
    tip = (540, CENTER + 330 - 650)
    if i == 0:
        cloud(P, 540, CENTER - 480, .9); skyline(P, tower=False)
        P.text(540, CENTER - 100, "?", 180 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        cloud(P, 540, CENTER - 500, .85); skyline(P)
        for j, a in enumerate((.3, 1.3, 2.3)):
            bolt(P, 540 + (j - 1) * 90, CENTER - 470, *tip, j, seg(u, a, a + .25) * (1 - seg(u, a + .5, a + .7)))
        P.stamp(820, CENTER - 300, "MYTH", seg(u, .25, .7))
    elif i == 2:
        cloud(P, 540, CENTER - 500, .85); skyline(P)
        k = back(seg(u, .4, 1.0))
        for x, y in ((90, CENTER + 70), (250, CENTER - 50), (540, tip[1])):
            P.line([(x, y - 140 * k), (x, y - 40)], GLIM, 8); P.poly([(x - 20, y - 70), (x + 20, y - 70), (x, y - 30)], GLIM)
        P.badge(540, CENTER + 530, "tall = closer to clouds", 50, NIGHT, CLOUD, back(seg(u, 1.6, 2.1)))
    elif i == 3:
        cloud(P, 540, CENTER - 500, .85); skyline(P)
        a = (u * 1.4) % 1.4
        bolt(P, 520, CENTER - 470, *tip, int(u * 1.4), seg(a, 0, .2) * (1 - seg(a, .4, .6)))
        n = min(23, int(23 * eio(seg(u, .5, 4.0))))
        P.badge(540, CENTER + 530, f"~{n} hits a year", 60, NIGHT, GLIM, back(seg(u, .5, 1.0)))
    elif i == 4:
        cloud(P, 540, CENTER - 500, .85); skyline(P)
        n = min(8, int(u * 2.2) + 1)
        a = (u * 2.2) % 1
        bolt(P, 480 + (n % 3) * 60, CENTER - 470, *tip, n, seg(a, 0, .2) * (1 - seg(a, .5, .8)))
        P.badge(250, CENTER - 150, f"{n} x", 70, HOOK, CLOUD, back(seg(u, .2, .6)))
        P.badge(540, CENTER + 530, "in 24 minutes", 58, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
    else:
        cloud(P, 540, CENTER - 560, 1.1)
        P.poly([(0, CENTER + 330), (W, CENTER + 310), (W, H), (0, H)], (40, 70, 50))
        P.rrect(280, CENTER + 40, 320, CENTER + 330, 10, (90, 65, 45)); P.circ(300, CENTER - 30, 140, (40, 100, 60))
        P.cross(300, CENTER - 30, 110, k=back(seg(u, .9, 1.4)))
        P.stamp(720, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
