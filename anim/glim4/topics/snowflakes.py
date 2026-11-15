# Thema: Why does every snowflake have six sides?
CENTER = 1050
ICE, ICE2 = (215, 238, 255), (120, 175, 230)
PAL = ((40, 60, 120), (110, 150, 210))
HI = {"snowflake", "six", "sides?", "water", "molecules,", "hexagon", "prism,", "corners", "arms.", "same", "alike.", "path!"}
WOW = (3, 5)

def hexagon(P, x, y, r, fill, rot=0., outline=None, w=0):
    pts = [(x + r * math.cos(rot + k * math.pi / 3), y + r * math.sin(rot + k * math.pi / 3)) for k in range(6)]
    P.poly(pts, fill, outline=outline, w=w)

def flake(P, x, y, r, rot, k=1., seed=0, col=ICE):
    """Sechsarmige Schneeflocke; k = Wachstum 0..1, seed variiert die Seitenäste."""
    rnd = random.Random(seed); br = [(rnd.uniform(.3, .5), rnd.uniform(.2, .4)), (rnd.uniform(.6, .75), rnd.uniform(.12, .25))]
    hexagon(P, x, y, r * .16, col, rot)
    for a in range(6):
        ang = rot + a * math.pi / 3; L_ = r * k
        ex, ey = x + math.cos(ang) * L_, y + math.sin(ang) * L_
        P.line([(x, y), (ex, ey)], col, max(2, r * .07), glow=ICE2)
        for pos, ln in br:
            if k > pos:
                bx, by = x + math.cos(ang) * r * pos, y + math.sin(ang) * r * pos
                for d in (-1, 1):
                    a2 = ang + d * math.pi / 3; l2 = r * ln * clamp((k - pos) / .3)
                    P.line([(bx, by), (bx + math.cos(a2) * l2, by + math.sin(a2) * l2)], col, max(2, r * .05))

def molecule(P, x, y, s):
    P.circ(x, y, 26 * s, HOOK, outline=CLOUD, w=3)
    for d in (-1, 1): P.circ(x + d * 26 * s, y + 22 * s, 15 * s, CLOUD, outline=ICE2, w=3)

def SC(i, P, t, u):
    for j in range(18):   # fallender Schnee im Hintergrund
        q = (t * .08 + j / 18) % 1
        P.circ((j * 137) % W + math.sin(t + j) * 30, lerp(450, H, q), 5 + j % 3 * 2, (235, 245, 255))
    if i == 0:
        flake(P, 540, CENTER + 60, 330 * back(seg(u, .1, .8)), t * .3, 1, 3)
        P.text(880, CENTER - 290, "?", 150 * back(seg(u, .4, .9)), HOOK)
    elif i == 1:
        k = eout(seg(u, .3, 2.4))
        for a in range(6):
            ang = a * math.pi / 3 + t * .1
            x, y = 540 + math.cos(ang) * 230 * (2 - k), CENTER + 60 + math.sin(ang) * 230 * (2 - k)
            if k > .9:
                ang2 = (a + 1) * math.pi / 3 + t * .1
                P.line([(x, y), (540 + math.cos(ang2) * 230, CENTER + 60 + math.sin(ang2) * 230)], GLIM, 6)
            molecule(P, x, y, 1.3)
        P.badge(540, CENTER + 400, "hexagon pattern", 60, NIGHT, GLIM, back(seg(u, 2.0, 2.5)))
    elif i == 2:
        k = back(seg(u, .2, 1.0))
        P.ell(300, CENTER - 160, 220, 80, (235, 240, 250)); P.ell(780, CENTER - 140, 240, 90, (235, 240, 250))
        hexagon(P, 540, CENTER + 40, 200 * k, ICE, t * .2, outline=ICE2, w=8)
        hexagon(P, 540, CENTER + 40, 120 * k, lc(ICE, CLOUD, .5), t * .2)
        P.badge(540, CENTER + 400, "six-sided prism", 60, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
    elif i == 3:
        k = eout(seg(u, .3, 3.2))
        hexagon(P, 540, CENTER + 60, 110, ICE, 0, outline=ICE2, w=6)
        for a in range(6):
            ang = a * math.pi / 3
            x0, y0 = 540 + math.cos(ang) * 110, CENTER + 60 + math.sin(ang) * 110
            x1, y1 = 540 + math.cos(ang) * (110 + 220 * k), CENTER + 60 + math.sin(ang) * (110 + 220 * k)
            P.line([(x0, y0), (x1, y1)], ICE, 26, glow=ICE2)
            P.circ(x1, y1, 22, GLIM, glow=GLIM)
        for j in range(10):
            q = (t * .6 + j / 10) % 1; a = j * .63
            P.circ(540 + math.cos(a) * lerp(470, 150, q), CENTER + 60 + math.sin(a) * lerp(470, 150, q), 9, (200, 230, 255))
        P.badge(540, CENTER + 420, "corners grow fastest", 54, HOPE, CLOUD, back(seg(u, 1.8, 2.3)))
    elif i == 4:
        x = 540 + math.sin(u * .8) * 160; y = lerp(CENTER - 200, CENTER + 150, seg(u, 0, 4))
        flake(P, x, y, 220, t * .4, eout(seg(u, .1, 3)), 7)
        P.badge(540, CENTER + 410, "same conditions", 60, NIGHT, GLIM, back(seg(u, 1.6, 2.1)))
    else:
        for j, (x, y, r) in enumerate(((270, CENTER - 40, 150), (780, CENTER - 20, 140), (530, CENTER + 230, 170))):
            flake(P, x, y, r * back(seg(u, .2 + j * .3, .8 + j * .3)), t * .3 * (1 if j % 2 else -1), 1, 11 + j * 5)
        P.badge(540, CENTER - 330, "no two alike", 60, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
