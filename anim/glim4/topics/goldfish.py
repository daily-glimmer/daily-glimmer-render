# Thema: Do goldfish really have a three second memory?  (Mythos-Format)
CENTER = 1050
GOLD, GOLD2 = (255, 150, 40), (230, 110, 20)
PAL = ((10, 50, 90), (40, 140, 170))
HI = {"three", "second", "memory?", "myth.", "lever", "hour", "schedule,", "months", "sounds,", "colors,", "face", "months,", "seconds!"}
WOW = (1,)

def tank(P, t, x0=150, y0=CENTER - 300, x1=930, y1=CENTER + 380):
    P.rrect(x0, y0, x1, y1, 50, (150, 215, 240), outline=(230, 245, 255), w=12)
    P.rrect(x0 + 14, y0 + 60, x1 - 14, y1 - 14, 40, (70, 170, 220))
    P.poly([(x0 + 14, y1 - 80), (x1 - 14, y1 - 100), (x1 - 14, y1 - 14), (x0 + 14, y1 - 14)], (235, 210, 150))
    for k in range(3):
        bx = x0 + 140 + k * 220; P.line([(bx, y1 - 90), (bx + math.sin(t * 2 + k) * 30, y1 - 300)], (60, 170, 90), 18)
    for k in range(5):
        q = (t * .4 + k / 5) % 1; P.circ(x0 + 100 + k * 150, lerp(y1 - 100, y0 + 70, q), 10 + k % 3 * 4, (200, 240, 255))

def goldfish(P, x, y, s, t, flip=1, happy=True):
    f = flip; wig = math.sin(t * 8) * 15 * s
    P.poly([(x - f * 70 * s, y), (x - f * 160 * s, y - 70 * s + wig), (x - f * 135 * s, y + wig * .3), (x - f * 160 * s, y + 70 * s + wig)], GOLD2)
    P.ell(x, y, 100 * s, 68 * s, GOLD)
    P.poly([(x - 20 * s, y - 55 * s), (x + 30 * s, y - 110 * s), (x + 50 * s, y - 50 * s)], GOLD2)
    P.ell(x - f * 10 * s, y + 20 * s, 40 * s, 18 * s, (255, 200, 120))
    P.circ(x + f * 55 * s, y - 15 * s, 20 * s, (255, 255, 255)); P.circ(x + f * 60 * s, y - 15 * s, 11 * s, NIGHT)
    if happy: P.arc(x + f * 75 * s, y + 18 * s, 16 * s, 20, 160, NIGHT, 5 * s)

def lever(P, x, y, down):
    P.rrect(x - 30, y - 10, x + 30, y + 160, 12, (90, 100, 120))
    a = math.radians(-40 + 60 * down); P.line([(x, y + 10), (x + math.cos(a) * 140, y + 10 + math.sin(a) * 140)], (220, 60, 60), 18)
    P.circ(x + math.cos(a) * 140, y + 10 + math.sin(a) * 140, 26, HOOK)

def SC(i, P, t, u):
    if i == 0:
        tank(P, t); goldfish(P, 540 + math.sin(t * 1.2) * 200, CENTER + 20, 1.3, t, flip=1 if math.cos(t * 1.2) > 0 else -1)
        k = back(seg(u, .5, 1.0)); P.badge(540, CENTER + 470, "3 seconds?", 70, NIGHT, GLIM, k)
    elif i == 1:
        tank(P, t); goldfish(P, 540, CENTER + 20, 1.5, t)
        P.stamp(540, CENTER - 420, "MYTH", seg(u, .25, .7))
    elif i == 2:
        tank(P, t)
        press = 1 if (u % 2.2) < .5 else 0
        lever(P, 780, CENTER - 60, press)
        goldfish(P, lerp(520, 640, press), CENTER + 40, 1.0, t)
        if press:
            for k in range(4): P.circ(700 + k * 22, CENTER - 140 + ((u % 2.2) * 400) + k * 15, 10, (160, 100, 60))
        P.circ(310, CENTER - 160, 95, (250, 250, 250), outline=(60, 60, 80), w=10)
        a = t * 1.5; P.line([(310, CENTER - 160), (310 + math.cos(a) * 70, CENTER - 160 + math.sin(a) * 70)], NIGHT, 10)
        P.badge(310, CENTER + 470, "1 hour a day", 56, HOOK, CLOUD, back(seg(u, .8, 1.3)))
    elif i == 3:
        tank(P, t); goldfish(P, 400, CENTER + 60, 1.1, t)
        months = ["JAN", "FEB", "MAR", "APR", "MAY"]
        for k, m in enumerate(months):
            kk = back(seg(u, .3 + k * .45, .7 + k * .45))
            if kk > .02:
                P.rrect(600 + (k % 2) * 160, CENTER - 230 + k * 95, 740 + (k % 2) * 160, CENTER - 160 + k * 95, 14, CLOUD)
                P.text(670 + (k % 2) * 160, CENTER - 195 + k * 95, m, 44 * kk, HOOK)
        P.check(560, CENTER - 360, 60, k=back(seg(u, 2.8, 3.3)))
    elif i == 4:
        tank(P, t); goldfish(P, 420, CENTER + 60, 1.1, t)
        items = [(780, CENTER - 160, "note"), (780, CENTER + 20, "color"), (780, CENTER + 200, "face")]
        for k, (x, y, kind) in enumerate(items):
            kk = back(seg(u, .3 + k * 1.0, .8 + k * 1.0))
            if kk < .02: continue
            P.circ(x, y, 70 * kk, CLOUD)
            if kind == "note": P.circ(x - 12 * kk, y + 22 * kk, 18 * kk, (60, 120, 255)); P.line([(x + 4 * kk, y + 22 * kk), (x + 4 * kk, y - 35 * kk), (x + 30 * kk, y - 20 * kk)], (60, 120, 255), 9 * kk)
            elif kind == "color": P.circ(x - 20 * kk, y, 25 * kk, HOOK); P.circ(x + 20 * kk, y, 25 * kk, (60, 120, 255))
            else:
                P.circ(x, y, 42 * kk, (240, 200, 170)); P.circ(x - 14 * kk, y - 8 * kk, 6 * kk, NIGHT); P.circ(x + 14 * kk, y - 8 * kk, 6 * kk, NIGHT)
                P.arc(x, y + 6 * kk, 16 * kk, 20, 160, NIGHT, 5 * kk)
    else:
        tank(P, t); goldfish(P, 460, CENTER + 40, 1.3, t)
        P.stamp(540, CENTER - 420, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
        P.badge(700, CENTER - 170, "months!", 64, HOPE, CLOUD, back(seg(u, .9, 1.4)))
