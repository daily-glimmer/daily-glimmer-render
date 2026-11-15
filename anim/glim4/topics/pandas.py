# Thema: Why do pandas eat so much bamboo?
CENTER = 1050
WH, BK = (245, 243, 238), (35, 35, 42)
BAM, BAM2 = (120, 190, 80), (70, 140, 50)
PAL = ((205, 235, 200), (160, 210, 170))
HI = {"bamboo?", "meat", "eater.", "fifth", "fourteen", "hours", "thirty", "eight", "kilograms!", "wrist", "bone", "thumb,", "all", "year,", "nobody"}
WOW = (1, 3)

def stalk(P, x, y0, y1, w=34, lean=0.):
    P.line([(x, y0), (x + lean, y1)], BAM, w)
    n = int(abs(y0 - y1) / 110)
    for k in range(1, n + 1):
        yy = y0 + (y1 - y0) * k / (n + 1); xx = x + lean * k / (n + 1)
        P.line([(xx - w * .65, yy), (xx + w * .65, yy)], BAM2, 8)
    P.poly([(x + lean, y1), (x + lean + 90, y1 - 40), (x + lean + 20, y1 + 15)], BAM2)

def panda(P, x, y, s, t, chew=0., hold=False, happy=False):
    P.ell(x, y + 120 * s, 190 * s, 170 * s, WH, outline=(200, 200, 205), w=5 * s)           # Körper (sitzend)
    P.ell(x, y + 70 * s, 200 * s, 70 * s, BK)                                                # Schulterband
    for d in (-1, 1): P.ell(x + d * 120 * s, y + 260 * s, 75 * s, 55 * s, BK)               # Füße
    for d in (-1, 1): P.circ(x + d * 115 * s, y - 135 * s, 50 * s, BK)                      # Ohren
    P.ell(x, y - 40 * s, 150 * s, 130 * s, WH, outline=(200, 200, 205), w=5 * s)
    for d in (-1, 1):
        P.ell(x + d * 55 * s, y - 50 * s, 38 * s, 50 * s, BK)
        if happy: P.arc(x + d * 55 * s, y - 45 * s, 16 * s, 200, 340, CLOUD, 6 * s)
        else: P.circ(x + d * 55 * s, y - 52 * s, 13 * s, CLOUD); P.circ(x + d * 55 * s + 2 * s, y - 50 * s, 7 * s, NIGHT)
    P.ell(x, y + 10 * s, 26 * s, 17 * s, BK)
    m = abs(math.sin(t * 9)) * chew
    P.ell(x, y + 50 * s, 30 * s, (6 + 16 * m) * s, (140, 50, 60))
    if hold:
        P.line([(x - 130 * s, y + 60 * s), (x + 60 * s, y + 40 * s)], BAM, 26 * s)
        P.poly([(x + 60 * s, y + 40 * s), (x + 160 * s, y - 10 * s), (x + 80 * s, y + 55 * s)], BAM2)
    for d in (-1, 1): P.ell(x + d * 95 * s, y + 70 * s, 50 * s, 45 * s, BK)                # Arme/Pfoten

def SC(i, P, t, u):
    P.rrect(-20, CENTER + 330, W + 20, H + 20, 0, (120, 170, 100))
    for x, lean in ((80, 10), (180, -15), (930, 12), (1020, -8)): stalk(P, x, CENTER + 360, CENTER - 300, 30, lean)
    if i == 0:
        panda(P, 540, CENTER + 40, 1.0, t, chew=1, hold=True)
        P.text(880, CENTER - 290, "?", 150 * back(seg(u, .4, .9)), HOOK)
    elif i == 1:
        P.ell(540, CENTER + 40, 300, 300, (250, 225, 225), outline=(220, 160, 160), w=8)
        k = eout(seg(u, .3, 1.5))
        P.ell(470, CENTER - 40, 140 * k, 100 * k, (240, 150, 150), outline=(200, 100, 110), w=6)
        P.line([(560, CENTER + 10), (620, CENTER + 120), (520, CENTER + 180), (600, CENTER + 240)], (230, 130, 140), 36 * k)
        P.badge(540, CENTER + 410, "meat-eater gut", 60, HOOK, CLOUD, back(seg(u, 1.0, 1.5)))
    elif i == 2:
        k = eout(seg(u, .3, 2.0))
        for j in range(5):
            x = 220 + j * 160; used = j == 0
            P.rrect(x - 55, CENTER - 160, x + 55, CENTER + 260, 30, BAM if used else lc(BAM, (230, 230, 220), .6 * k), outline=BAM2, w=6)
        P.badge(540, CENTER + 410, "under 1/5 digested", 56, NIGHT, GLIM, back(seg(u, 1.2, 1.7)))
    elif i == 3:
        panda(P, 360, CENTER + 60, .8, t, chew=1, hold=True)
        cx, cy = 790, CENTER - 40
        P.circ(cx, cy, 150, CLOUD, outline=NIGHT, w=8)
        a = (u / 4) * 6.283 * 2
        P.line([(cx, cy), (cx + math.sin(a) * 120, cy - math.cos(a) * 120)], HOOK, 10)
        P.line([(cx, cy), (cx + math.sin(a / 12) * 80, cy - math.cos(a / 12) * 80)], NIGHT, 12)
        P.badge(790, CENTER + 160, "14 h/day", 56, NIGHT, GLIM, back(seg(u, .6, 1.1)))
        n = int(clamp(seg(u, 1.5, 3.5)) * 38)
        P.badge(540, CENTER + 420, f"up to {max(12, n)} kg", 60, HOPE, CLOUD, back(seg(u, 1.5, 2.0)))
    elif i == 4:
        k = eout(seg(u, .2, 1.0))
        P.ell(540, CENTER + 40, 230, 170, BK)
        for j in range(5): P.ell(380 + j * 80, CENTER - 110, 40, 55, BK)
        P.ell(760, CENTER + 120, 50 * k, 70 * k, BK)
        P.circ(760, CENTER + 120, 22 * k, (90, 90, 100))
        P.line([(200, CENTER + 150), (900, CENTER + 60)], BAM, 50)
        P.arc(760, CENTER + 120, 100, 0, 360, GLIM, 8 * seg(u, 1.0, 1.4))
        P.badge(540, CENTER + 410, "a 'thumb' bone", 60, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
    else:
        panda(P, 540, CENTER + 80, .95, t, chew=.5, hold=True, happy=True)
        P.badge(540, CENTER - 330, "grows all year", 58, HOPE, CLOUD, back(seg(u, 1.0, 1.5)))
