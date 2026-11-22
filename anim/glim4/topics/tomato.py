# Thema: Is a tomato really a fruit?  (Mythos-Format, TRUE in Satz 2, FACT in Satz 6)
# Quellen: Britannica "Is a tomato a fruit or a vegetable?" (botanisch Frucht/Beere aus der Blüte mit Samen),
# Nix v. Hedden, 149 U.S. 304 (1893): Supreme Court stuft Tomaten für Zölle als Gemüse ein.
CENTER = 1050
RED, RED2, LEAFC, SEED, FLESH = (230, 60, 50), (190, 40, 35), (70, 150, 70), (250, 225, 150), (240, 110, 90)
PAL = ((240, 200, 150), (250, 230, 200))
HI = {"tomato", "fruit?", "true!", "berry.", "flower", "seeds,", "vegetable", "savory,", "1893,", "supreme", "court", "garden,", "kitchen!"}
WOW = (1,)

def tomato(P, x, y, r, t, cut=False):
    if cut:
        P.circ(x, y, r, RED); P.circ(x, y, r * .85, FLESH)
        for a in range(4):
            ang = a * math.pi / 2 + .4
            P.ell(x + math.cos(ang) * r * .45, y + math.sin(ang) * r * .45, r * .22, r * .3, RED2)
            for k in range(3): P.ell(x + math.cos(ang) * r * (.38 + k * .07), y + math.sin(ang) * r * (.38 + k * .07), r * .04, r * .06, SEED)
        P.circ(x, y, r * .15, (250, 160, 140))
    else:
        P.circ(x, y, r, RED); P.ell(x - r * .35, y - r * .35, r * .25, r * .15, (250, 140, 120))
        for a in range(5):
            ang = -math.pi / 2 + (a - 2) * .5
            P.poly([(x, y - r * .9), (x + math.cos(ang) * r * .5, y - r * .9 + math.sin(ang) * r * .2 + r * .15), (x + math.cos(ang + .2) * r * .2, y - r * .85)], LEAFC)
        P.line([(x, y - r * .9), (x + 8, y - r * 1.15)], LEAFC, 10)

def flower(P, x, y, s):
    for a in range(5): P.ell(x + math.cos(a * 1.26) * 40 * s, y + math.sin(a * 1.26) * 40 * s, 30 * s, 22 * s, (250, 215, 60))
    P.circ(x, y, 20 * s, (230, 150, 40))

def SC(i, P, t, u):
    if i == 0:
        tomato(P, 460, CENTER + 60, 220 * (1 + .03 * math.sin(t * 3)), t)
        P.text(800, CENTER - 230, "?", 160 * back(seg(u, .5, 1.0)), (120, 60, 50))
    elif i == 1:
        tomato(P, 460, CENTER + 60, 220, t)
        P.stamp(560, CENTER - 290, "TRUE", seg(u, .25, .7), col=HOPE, rot=-6)
        P.badge(540, CENTER + 420, "fruit, even a berry", 58, NIGHT, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 2:
        k = eio(seg(u, .3, 1.6))
        P.line([(260, CENTER + 400), (260, CENTER - 60)], LEAFC, 14)
        if k < .5: flower(P, 260, CENTER - 100, 1.6 * (1 - k * 2) + .01)
        else: tomato(P, 260, CENTER - 40, 140 * (k - .5) * 2 + 1, t)
        tomato(P, 720, CENTER + 60, 220, t, cut=True)
        P.badge(720, CENTER + 360, "full of seeds", 56, GLIM, NIGHT, back(seg(u, 1.8, 2.3)))
    elif i == 3:
        P.ell(540, CENTER + 200, 380, 140, (240, 240, 235)); P.ell(540, CENTER + 160, 340, 100, (110, 170, 90))
        for dx in (-180, 0, 170): tomato(P, 540 + dx, CENTER + 120, 70, t, cut=dx == 0)
        P.ell(330, CENTER + 60, 90, 40, (90, 160, 80)); P.ell(760, CENTER + 50, 80, 36, (90, 160, 80))
        P.badge(540, CENTER - 280, "kitchen: vegetable", 58, NIGHT, CLOUD, back(seg(u, .6, 1.1)))
    elif i == 4:
        P.poly([(240, CENTER - 120), (840, CENTER - 120), (540, CENTER - 300)], (230, 225, 210))
        for j in range(5): P.rrect(270 + j * 120, CENTER - 110, 320 + j * 120, CENTER + 220, 8, (240, 235, 222))
        P.rrect(220, CENTER + 220, 860, CENTER + 270, 8, (210, 205, 190))
        P.text(540, CENTER - 380, "1893", 110 * back(seg(u, .3, .8)), NIGHT)
        k = back(seg(u, 1.6, 2.1)); P.rrect(640, CENTER + 330, 640 + 220 * k, CENTER + 380, 20, (140, 90, 50))
        P.badge(400, CENTER + 400, "ruled: vegetable", 54, HOOK, CLOUD, back(seg(u, 2.2, 2.7)))
    else:
        tomato(P, 380, CENTER + 80, 180, t)
        P.stamp(780, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
