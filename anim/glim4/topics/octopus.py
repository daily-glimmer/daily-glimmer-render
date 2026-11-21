# Thema: Does an octopus really have three hearts?  (Mythos-Format, TRUE in Satz 2, FACT in Satz 6)
CENTER = 1050
OC, OC2, SUCK = (235, 110, 90), (200, 80, 70), (255, 200, 180)
BLUEB, REDB = (60, 130, 255), (220, 40, 60)
PAL = ((10, 40, 90), (30, 110, 150))
HI = {"three", "hearts?", "true!", "gills,", "body.", "blue,", "copper", "iron.", "cold", "stops", "crawl.", "blood!"}
WOW = (1,)

def seabed(P, t, y=CENTER + 360):
    P.poly([(0, y), (W, y - 30), (W, H), (0, H)], (190, 170, 130))
    for k in range(3): P.ell(200 + k * 330, y + 40, 70, 24, (160, 140, 110))
    for k in range(6):
        q = (t * .3 + k / 6) % 1; P.circ(100 + k * 170, lerp(y, CENTER - 500, q), 8 + k % 3 * 4, (160, 210, 240))

def heart(P, x, y, r, col, beat=1., t=0.):
    k = 1 + .12 * beat * max(0, math.sin(t * 7))
    P.heart(x, y, r * k, col)

def octopus(P, x, y, s, t, hearts=0., swim=False, beat_main=1., blood=None):
    for j in range(8):          # Arme
        a = math.pi * (.15 + .7 * j / 7)
        pts = []
        for q in range(7):
            r = q * 45 * s; w_ = math.sin(t * (5 if swim else 2) + j + q * .7) * 18 * s * q / 6
            pts.append((x + math.cos(a) * r * 1.4 + w_, y + 60 * s + math.sin(a) * r * (0.5 if swim else 1.1) + (q * 25 * s if swim else 0)))
        P.line(pts, OC2, (34 - 0 * j) * s)
        for px, py in pts[1:6:2]: P.circ(px, py, 7 * s, SUCK)
    P.ell(x, y - 70 * s, 150 * s, 175 * s, OC)
    P.ell(x - 50 * s, y - 130 * s, 40 * s, 60 * s, lc(OC, (255, 255, 255), .25))
    for f in (-1, 1):
        P.circ(x + f * 60 * s, y + 20 * s, 30 * s, CLOUD); P.circ(x + f * 62 * s, y + 22 * s, 14 * s, NIGHT)
    if hearts > .02:
        P.ell(x, y - 110 * s, 100 * s, 85 * s, (255, 220, 210))
        heart(P, x - 50 * s, y - 85 * s, 26 * s * hearts, BLUEB, 1, t)
        heart(P, x + 50 * s, y - 85 * s, 26 * s * hearts, BLUEB, 1, t + .5)
        heart(P, x, y - 140 * s, 38 * s * hearts, BLUEB, beat_main, t + .2)

def SC(i, P, t, u):
    if i == 0:
        seabed(P, t); octopus(P, 520, CENTER + 120, 1.2, t)
        P.text(820, CENTER - 250, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        seabed(P, t); octopus(P, 520, CENTER + 140, 1.3, t, hearts=back(seg(u, .4, 1.0)))
        P.stamp(820, CENTER - 280, "TRUE", seg(u, .25, .7), col=HOPE, rot=-6)
        P.badge(260, CENTER - 160, "gills x2", 46, NIGHT, CLOUD, back(seg(u, 1.6, 2.1)))
        P.badge(540, CENTER + 560, "1 body heart", 54, NIGHT, GLIM, back(seg(u, 3.0, 3.5)))
    elif i == 2:
        k = eio(seg(u, .4, 2.0))
        P.rrect(100, CENTER - 140, 980, CENTER + 140, 140, (40, 70, 120))
        for j in range(8):
            x = (j * 140 + u * 200) % 840 + 160; P.circ(x, CENTER + (j % 2) * 40 - 20, 34, lc(REDB, BLUEB, k))
        P.badge(300, CENTER + 270, "iron", 54, REDB, CLOUD, back(seg(u, .5, 1.0)))
        P.cross(300, CENTER + 270, 50, k=back(seg(u, 1.6, 2.0)))
        P.badge(760, CENTER + 270, "copper", 54, BLUEB, CLOUD, back(seg(u, 2.0, 2.5)))
    elif i == 3:
        seabed(P, t)
        for j in range(30): P.circ((j * 97) % W, (j * 173) % 900 + CENTER - 500, 3 + j % 3, (230, 245, 255))
        octopus(P, 520, CENTER + 150, 1.1, t)
        P.badge(540, CENTER - 200, "cold & low oxygen", 56, NIGHT, CLOUD, back(seg(u, .5, 1.0)))
    elif i == 4:
        seabed(P, t)
        sw = u < 3.0
        x = lerp(300, 700, seg(u, 0, 3.0)); y = CENTER - 40 + (0 if sw else 220 * eio(seg(u, 3.0, 4.0)))
        octopus(P, x, y, 1.0, t, hearts=1., swim=sw, beat_main=0. if sw else 1.)
        if sw: P.badge(540, CENTER + 520, "main heart: stop", 54, HOOK, CLOUD, back(seg(u, .8, 1.3)))
        else: P.badge(540, CENTER + 520, "crawling is easier", 54, NIGHT, GLIM, back(seg(u, 3.2, 3.7)))
    else:
        seabed(P, t); octopus(P, 400, CENTER + 140, 1.1, t, hearts=1.)
        P.stamp(780, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
