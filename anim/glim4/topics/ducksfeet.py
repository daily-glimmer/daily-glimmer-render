# Thema: Do ducks get cold feet standing on ice?  (Mythos-Format, NOT REALLY in Satz 2, FACT in Satz 6) – Ente aus ducks.py
CENTER = 1050
exec(open(os.path.join(HERE, "topics", "ducks.py")).read(), globals())
PAL = ((70, 110, 160), (170, 205, 230))
HI = {"cold", "feet", "ice?", "not", "really!", "never", "freeze.", "warm", "blood", "heat,", "five", "percent", "heat", "exchanger"}
WOW = (1,)
ICE = (215, 235, 250); FOOT = (245, 150, 50)
WARM, COLD = (235, 60, 60), (70, 130, 240)

def ice(P, t, y=CENTER + 300):
    P.poly([(0, y), (W, y - 20), (W, H), (0, H)], ICE)
    for k in range(5): P.line([(80 + k * 220, y + 60 + (k % 2) * 50), (200 + k * 220, y + 90 + (k % 2) * 50)], (250, 252, 255), 6)

def standing_duck(P, x, y, s, t, foot_col=FOOT, **kw):
    for dx in (-35, 35):
        P.line([(x + dx * s, y - 60 * s), (x + dx * s, y + 70 * s)], foot_col, 12 * s)
        P.poly([(x + dx * s - 10 * s, y + 70 * s), (x + dx * s + 60 * s, y + 80 * s), (x + dx * s - 20 * s, y + 85 * s)], foot_col)
    duck(P, x, y - 110 * s, s, t, **kw)

def thermo(P, x, y, k, lab):
    P.rrect(x - 26, y - 170, x + 26, y + 60, 26, CLOUD, outline=(150, 160, 180), w=6)
    P.circ(x, y + 70, 42, lc(COLD, WARM, k)); P.rrect(x - 12, y + 60 - 220 * k, x + 12, y + 60, 12, lc(COLD, WARM, k))
    P.badge(x, y + 160, lab, 40, NIGHT, CLOUD, 1.)

def SC(i, P, t, u):
    if i == 0:
        ice(P, t); standing_duck(P, 500, CENTER + 220, 1.3, t, female=False)
        P.text(820, CENTER - 230, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
        for j in range(12): P.circ((j * 97 + t * 30) % W, (j * 151 + t * 80) % 900 + CENTER - 600, 6, (250, 252, 255))
    elif i == 1:
        ice(P, t); standing_duck(P, 470, CENTER + 220, 1.3, t, female=False, foot_col=lc(FOOT, (255, 200, 120), .3))
        P.stamp(540, CENTER - 280, "NOT REALLY", seg(u, .25, .7), col=HOOK, rot=-6)
        P.check(820, CENTER + 120, 60, k=back(seg(u, 1.6, 2.0)))
    elif i == 2:
        k = seg(u, .3, 3.0)
        P.rrect(330, CENTER - 360, 750, CENTER + 420, 60, (240, 200, 150))
        P.line([(470, CENTER - 330), (470, CENTER + 390)], WARM, 40)
        P.line([(610, CENTER + 390), (610, CENTER - 330)], COLD, 40)
        for j in range(4):
            q = (u * .5 + j / 4) % 1
            P.circ(470, lerp(CENTER - 330, CENTER + 390, q), 16, (255, 220, 220))
            P.circ(610, lerp(CENTER + 390, CENTER - 330, q), 16, (220, 235, 255))
        P.badge(180, CENTER - 200, "warm down", 44, WARM, CLOUD, back(seg(u, .5, 1.0)))
        P.badge(900, CENTER + 200, "cold up", 44, COLD, CLOUD, back(seg(u, 1.2, 1.7)))
    elif i == 3:
        P.rrect(330, CENTER - 360, 750, CENTER + 420, 60, (240, 200, 150))
        k = eio(seg(u, .3, 2.5))
        P.line([(470, CENTER - 330), (470, CENTER + 390)], WARM, 40)
        P.line([(610, CENTER + 390), (610, CENTER - 330)], lc(COLD, WARM, k * .8), 40)
        for j in range(5):
            y = CENTER - 250 + j * 140; P.line([(500, y), (580, y - 30)], GLIM, 12)
            P.poly([(580, y - 30), (555, y - 44), (562, y - 14)], GLIM)
        thermo(P, 160, CENTER - 60, .9, "body"); thermo(P, 920, CENTER - 60, .18, "feet")
    elif i == 4:
        ice(P, t); standing_duck(P, 400, CENTER + 220, 1.1, t, female=True)
        k = back(seg(u, .5, 1.0))
        P.circ(800, CENTER - 80, 150 * k, (40, 60, 100))
        P.d.pieslice([*P.c.p(800 - 150 * k, CENTER - 230 * k + 150 - 150), *P.c.p(800 + 150 * k, CENTER - 80 + 150 * k)], -90, -90 + 18 * eio(seg(u, 1.0, 2.0)), fill=HOOK) if k > .1 else None
        P.badge(800, CENTER + 130, "5% heat loss", 50, HOOK, CLOUD, back(seg(u, 1.6, 2.1)))
    else:
        ice(P, t); standing_duck(P, 330, CENTER + 220, 1.1, t, female=False); standing_duck(P, 760, CENTER + 230, .9, t, female=True)
        P.stamp(560, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
