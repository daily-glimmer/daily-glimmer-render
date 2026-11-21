# Thema: Do camels really spit at people?  (Mythos-Format, NOT QUITE in Satz 2, FACT in Satz 6)
# Figuren camel/dunes/sun aus camels.py
CENTER = 1050
exec(open(os.path.join(HERE, "topics", "camels.py")).read(), globals())
PAL = ((80, 50, 70), (225, 150, 90))
HI = {"spit", "people?", "not", "quite!", "half-digested", "stomach.", "cud,", "threatened,", "goo", "three", "chambers,", "throwing"}
WOW = (1,)
GOO = (140, 190, 70)

def splat(P, x0, y0, x1, y1, k, t):
    for j in range(9):
        q = clamp(k * 1.2 - j * .05)
        if q <= 0: continue
        x = lerp(x0, x1, q) + math.sin(j * 2.1) * 30; y = lerp(y0, y1, q) - math.sin(q * math.pi) * 120 + math.cos(j * 1.7) * 25
        P.circ(x, y, 18 + (j % 3) * 8, GOO)

def person(P, x, y, s, shock=0.):
    P.circ(x, y - 230 * s, 50 * s, (240, 200, 160))
    P.rrect(x - 55 * s, y - 175 * s, x + 55 * s, y + 20 * s, 30 * s, (90, 130, 200))
    P.line([(x - 25 * s, y + 20 * s), (x - 30 * s, y + 160 * s)], (60, 70, 90), 26 * s); P.line([(x + 25 * s, y + 20 * s), (x + 30 * s, y + 160 * s)], (60, 70, 90), 26 * s)
    P.circ(x - 18 * s, y - 238 * s, 6 * s, NIGHT); P.circ(x + 18 * s, y - 238 * s, 6 * s, NIGHT)
    P.ell(x, y - 205 * s, 12 * s, 8 * s + 10 * s * shock, (140, 40, 40))

def SC(i, P, t, u):
    if i == 0:
        sun(P, 830, CENTER - 330, 80); dunes(P, t)
        camel(P, 380, CENTER + 120, 1.0, t, walk=False)
        person(P, 860, CENTER + 260, 1.0)
        P.text(620, CENTER - 280, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        dunes(P, t)
        camel(P, 330, CENTER + 130, 1.0, t, walk=False)
        person(P, 880, CENTER + 260, 1.0, shock=1.)
        splat(P, 600, CENTER - 60, 860, CENTER + 20, seg(u, .3, 1.3), t)
        P.stamp(540, CENTER - 250, "NOT QUITE", seg(u, .25, .7), col=HOOK, rot=-6)
        P.badge(540, CENTER + 520, "stomach food!", 60, NIGHT, GLIM, back(seg(u, 1.6, 2.1)))
    elif i == 2:
        dunes(P, t)
        camel(P, 470, CENTER + 140, 1.3, t, walk=False)
        k = (u * .6) % 1     # Bissen wandert den Hals hoch
        P.circ(lerp(600, 780, k), lerp(CENTER + 100, CENTER - 90, k), 26, GOO)
        P.badge(540, CENTER + 520, "chewing cud", 60, NIGHT, CLOUD, back(seg(u, .6, 1.1)))
    elif i == 3:
        dunes(P, t)
        camel(P, 300, CENTER + 130, 1.0, t, walk=False)
        for j in range(3):
            P.circ(560 + j * 50, CENTER - 140 - j * 10, 20 * back(seg(u, .5 + j * .3, .9 + j * .3)), (220, 235, 255))
        splat(P, 600, CENTER - 60, 1000, CENTER + 120, seg(u, 2.5, 3.8), t)
        P.badge(540, CENTER + 520, "goo + saliva", 60, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
    elif i == 4:
        for j in range(3):
            k = back(seg(u, .3 + j * .5, .8 + j * .5))
            x = 230 + j * 310
            P.circ(x, CENTER, 130 * k, (240, 170, 160), outline=(190, 110, 100), w=8)
            P.circ(x, CENTER + 30, 70 * k, GOO)
            P.text(x, CENTER - 200, str(j + 1), 90 * k, GLIM)
        for j in range(2): P.line([(230 + j * 310 + 130, CENTER), (230 + (j + 1) * 310 - 130, CENTER)], (190, 110, 100), 20)
        P.badge(540, CENTER + 330, "3 stomach chambers", 58, NIGHT, CLOUD, back(seg(u, 2.0, 2.5)))
    else:
        sun(P, 200, CENTER - 330, 70); dunes(P, t)
        camel(P, 380, CENTER + 130, 1.0, t, walk=False)
        person(P, 900, CENTER + 260, .9, shock=.5)
        P.stamp(620, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
