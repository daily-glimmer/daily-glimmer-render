# Thema: How do pufferfish puff up?
CENTER = 1050
PF, PF2, BEL = (235, 190, 80), (170, 120, 40), (250, 240, 210)
PAL = ((15, 45, 85), (20, 80, 120))
HI = {"pufferfish", "puff", "predator", "gulps", "water", "stretchy,", "three", "times", "spines,", "poison", "exhausting", "danger.", "shrink"}
WOW = (2, 5)

def bubbles(P, t, n=8):
    for k in range(n):
        q = (t * .25 + k / n) % 1
        P.circ(100 + (k * 137) % 880, CENTER + 400 - q * 900, 10 + k % 3 * 6, (90, 160, 210), outline=(140, 200, 240), w=3)

def puffer(P, x, y, s, t, p=0., spines=True, flip=1):
    r = (110 + 110 * p) * s
    P.poly([(x - flip * r * .85, y), (x - flip * (r + 90 * s), y - 60 * s), (x - flip * (r + 90 * s), y + 60 * s)], PF, outline=PF2, w=4 * s)
    if spines and p > .2:
        for k in range(18):
            a = k / 18 * 2 * math.pi
            P.line([(x + math.cos(a) * r * .95, y + math.sin(a) * r * .95 * (1 - .25 * (1 - p))),
                    (x + math.cos(a) * (r + 30 * s * p), y + math.sin(a) * (r + 30 * s * p) * (1 - .25 * (1 - p)))], PF2, 7 * s)
    P.ell(x, y, r, r * (1 - .25 * (1 - p)), PF, outline=PF2, w=5 * s)
    P.ell(x, y + r * .35, r * .75, r * .45, BEL)
    for k in range(5): P.circ(x - r * .4 + k * r * .18, y - r * .45 + (k % 2) * 20 * s, 9 * s, PF2)
    ex = x + flip * r * .55
    P.circ(ex, y - r * .2, 30 * s, CLOUD, outline=PF2, w=3 * s); P.circ(ex + flip * 8 * s, y - r * .2, 15 * s, NIGHT)
    P.circ(x + flip * r * .95, y + r * .1, 14 * s, (200, 100, 80))

def shark(P, x, y, s):
    G = (120, 140, 170)
    P.poly([(x, y), (x + 260 * s, y - 70 * s), (x + 360 * s, y), (x + 260 * s, y + 60 * s)], G, outline=(70, 90, 120), w=5 * s)
    P.poly([(x + 200 * s, y - 55 * s), (x + 240 * s, y - 140 * s), (x + 280 * s, y - 62 * s)], G)
    P.poly([(x + 340 * s, y), (x + 430 * s, y - 70 * s), (x + 420 * s, y + 60 * s)], G)
    P.circ(x + 70 * s, y - 15 * s, 10 * s, NIGHT)

def SC(i, P, t, u):
    bubbles(P, t)
    P.rrect(-20, CENTER + 380, W + 20, H + 20, 0, (200, 180, 130))
    if i == 0:
        puffer(P, 540, CENTER + 50, 1.0, t, p=.5 + .5 * math.sin(u * 2.5))
        P.text(860, CENTER - 300, "?", 150 * back(seg(u, .4, .9)), HOOK)
    elif i == 1:
        shark(P, lerp(1100, 600, eout(seg(u, .2, 1.5))), CENTER - 150, 1.0)
        puffer(P, 300, CENTER + 120, .9, t, p=0)
        for k in range(4):
            q = (u * 1.5 + k / 4) % 1
            P.line([(470 - q * 120, CENTER + 80 + k * 20), (430 - q * 120, CENTER + 80 + k * 20)], (150, 210, 250), 8)
        P.badge(540, CENTER + 460, "gulp!", 64, NIGHT, GLIM, back(seg(u, .9, 1.4)))
    elif i == 2:
        p = eout(seg(u, .3, 1.8))
        puffer(P, 540, CENTER + 40, 1.0, t, p=p)
        P.badge(540, CENTER + 460, "about 3x bigger", 60, NIGHT, GLIM, back(seg(u, 1.6, 2.1)))
    elif i == 3:
        puffer(P, 400, CENTER + 40, .95, t, p=1)
        P.badge(820, CENTER - 200, "spines", 52, HOOK, CLOUD, back(seg(u, .5, 1.0)))
        P.rrect(760, CENTER + 120, 900, CENTER + 300, 20, (90, 60, 130), outline=CLOUD, w=5)
        P.text(830, CENTER + 210, "!", 100 * back(seg(u, 1.4, 1.9)), GLIM)
        P.badge(540, CENTER + 460, "poison", 58, HOOK, CLOUD, back(seg(u, 1.6, 2.1)))
    elif i == 4:
        puffer(P, 420, CENTER + 40, .9, t, p=.9 + .05 * math.sin(t * 6))
        P.rrect(760, CENTER - 60, 960, CENTER + 40, 16, CLOUD, outline=NIGHT, w=6)
        lv = 1 - .85 * eout(seg(u, .4, 2.6))
        P.rrect(772, CENTER - 48, 772 + 168 * lv, CENTER + 28, 10, HOOK if lv < .4 else HOPE)
        P.badge(540, CENTER + 460, "only in danger", 58, NIGHT, GLIM, back(seg(u, 1.2, 1.7)))
    else:
        p = 1 - eout(seg(u, .3, 1.6))
        puffer(P, 540, CENTER + 20, .9, t, p=p)
        for k in range(5):
            q = (u * 1.2 + k / 5) % 1
            P.circ(540 + (110 + 110 * p) * .9 + q * 200, CENTER + 40 - k * 15, 12, (150, 210, 250))
        P.badge(540, CENTER - 420, "back to normal", 56, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
