# Thema: Why don't spiders get stuck in their own webs?
CENTER = 1050
PAL = ((60, 90, 140), (30, 60, 90))
HI = {"stuck", "webs?", "sticky.", "dry,", "hairs,", "tips", "glue.", "coating", "less.", "carefully,", "tightrope.", "free!"}
WOW = (1, 5)
SILK, GLUE = (235, 240, 250), (255, 210, 80)

def web(P, x, y, R, t, glue=True, hl_spokes=0., hl_glue=0.):
    n = 12
    for k in range(n):
        a = k / n * 6.28
        P.line([(x, y), (x + math.cos(a) * R, y + math.sin(a) * R)], lc(SILK, HOPE, hl_spokes), 4 + 4 * hl_spokes)
    for r in range(4):
        rr = R * (.3 + r * .18)
        pts = [(x + math.cos(k / n * 6.28) * rr, y + math.sin(k / n * 6.28) * rr) for k in range(n + 1)]
        P.line(pts, SILK, 3)
        if glue:
            for k in range(n):
                for j in (1, 2):
                    a = (k + j / 3) / n * 6.28
                    P.circ(x + math.cos(a) * rr * .99, y + math.sin(a) * rr * .99, 5 + 5 * hl_glue, lc(GLUE, HOOK, hl_glue))

def spider(P, x, y, s, t, walk=1.):
    for f in (-1, 1):
        for k in range(4):
            ph = math.sin(t * 8 * walk + k * 1.3 + (f > 0) * 1.5) * 12 * walk
            kx, ky = x + f * (70 + k * 10) * s, y + (-50 + k * 35) * s - 40 * s
            P.line([(x + f * 30 * s, y + (-20 + k * 14) * s), (kx, ky + ph * s), (x + f * (120 + k * 15) * s, y + (-30 + k * 45) * s + ph * s)], NIGHT, 9 * s)
    P.ell(x, y + 60 * s, 55 * s, 70 * s, (70, 50, 70)); P.circ(x, y - 15 * s, 42 * s, (90, 65, 85))
    for f in (-1, 1): P.circ(x + f * 15 * s, y - 25 * s, 10 * s, CLOUD); P.circ(x + f * 15 * s, y - 24 * s, 5 * s, NIGHT)
    P.ell(x, y + 70 * s, 20 * s, 26 * s, GLIM)

def fly(P, x, y, s, t):
    P.ell(x - 25 * s, y - 25 * s, 25 * s, 15 * s, (220, 235, 255)); P.ell(x + 25 * s, y - 25 * s, 25 * s, 15 * s, (220, 235, 255))
    P.ell(x, y, 30 * s, 22 * s, (60, 70, 70)); P.circ(x - 30 * s, y, 15 * s, (140, 40, 40))

def SC(i, P, t, u):
    if i == 0:
        web(P, 540, CENTER, 420, t); spider(P, 540, CENTER - 30, 1.1, t, .2)
        fly(P, 760, CENTER + 180 + math.sin(t * 12) * 4, 1, t)
        P.text(840, CENTER - 330, "?", 140 * back(seg(u, .4, .9)), GLIM)
    elif i == 1:
        web(P, 540, CENTER, 420, t, hl_spokes=seg(u, 1.6, 2.4))
        a = -1.05; d = lerp(380, 90, eio(seg(u, 2.0, 4.5)))
        spider(P, 540 + math.cos(a) * d, CENTER + math.sin(a) * d, .8, t)
        P.badge(540, CENTER + 470, "dry spokes", 58, HOPE, CLOUD, back(seg(u, 1.8, 2.3)))
    elif i == 2:
        P.circ(540, CENTER, 340, (245, 240, 230), outline=GLIM, w=10)
        P.line([(260, CENTER + 200), (820, CENTER + 200)], SILK, 10)
        for j in range(7): P.circ(300 + j * 80, CENTER + 200, 16, GLUE)
        P.line([(540, CENTER - 300), (540, CENTER + 120)], NIGHT, 50)
        for j in range(8):
            yy = CENTER - 260 + j * 50; f = 1 if j % 2 else -1
            P.line([(540, yy), (540 + f * 70, yy + 40), (540 + f * 100, yy + 30)], NIGHT, 7)
        for f in (-1, 0, 1): P.line([(540, CENTER + 110), (540 + f * 40, CENTER + 175)], NIGHT, 8)
        P.badge(540, CENTER + 420, "tiny hairs", 58, NIGHT, GLIM, back(seg(u, .8, 1.3)))
    elif i == 3:
        web(P, 540, CENTER - 40, 380, t, hl_glue=seg(u, .2, 1.0) * .6); spider(P, 540, CENTER - 40, 1.2, t, .3)
        for k in range(8):
            a = k / 8 * 6.28 + t * .5
            P.circ(540 + math.cos(a) * 230, CENTER - 40 + math.sin(a) * 230, 12 * back(seg(u, .8 + k * .1, 1.2 + k * .1)), HOPE)
        P.badge(540, CENTER + 420, "anti-stick coating", 54, HOPE, CLOUD, back(seg(u, 1.2, 1.7)))
    elif i == 4:
        P.line([(60, CENTER + 50), (1020, CENTER + 50)], SILK, 8)
        x = lerp(200, 880, seg(u, .2, 3.4))
        spider(P, x, CENTER - 60, 1.0, t, .6)
        P.badge(540, CENTER + 330, "step by step", 58, NIGHT, GLIM, back(seg(u, .6, 1.1)))
    else:
        web(P, 540, CENTER - 60, 380, t)
        fly(P, 660, CENTER + 60 + math.sin(t * 14) * 4, 1, t)
        spider(P, 420 + math.sin(t * 2) * 30, CENTER - 160, .9, t, .6)
