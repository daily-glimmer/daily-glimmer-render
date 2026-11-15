# Thema: Do pigs really sweat a lot?  (Mythos-Format)
CENTER = 1050
PIG, PIG2, MUD = (250, 175, 180), (230, 140, 150), (120, 85, 55)
PAL = ((80, 150, 200), (150, 180, 90))
HI = {"sweat", "lot?", "hardly", "glands.", "overheat", "cool", "mud!", "slowly", "sunscreen", "insects.", "smart", "pig!"}
WOW = (1, 3)
GROUND = CENTER + 260

def farm(P, mud=False):
    P.poly([(0, GROUND), (W, GROUND - 30), (W, H), (0, H)], (120, 165, 80))
    for x in (60, 220, 860, 1020): P.rrect(x - 12, GROUND - 200, x + 12, GROUND + 10, 6, (170, 130, 90))
    P.rrect(40, GROUND - 170, 240, GROUND - 145, 8, (170, 130, 90)); P.rrect(840, GROUND - 170, 1040, GROUND - 145, 8, (170, 130, 90))
    if mud: P.ell(540, GROUND + 90, 380, 90, MUD); P.ell(500, GROUND + 80, 250, 50, lc(MUD, (0, 0, 0), .15))

def pig(P, x, y, s, t, mud=0., happy=False, flip=1):
    f = flip; body = lc(PIG, MUD, mud)
    for dx in (-90, -40, 50, 100): P.rrect(x + dx * s - 20 * s, y + 40 * s, x + dx * s + 20 * s, y + 130 * s, 12 * s, lc(PIG2, MUD, mud))
    P.ell(x, y, 170 * s, 105 * s, body)
    tx = x + f * 165 * s; P.arc(tx + f * 20 * s, y - 30 * s, 22 * s, 0, 300 + 40 * math.sin(t * 6), lc(PIG2, MUD, mud), 8 * s)
    hx = x - f * 170 * s
    P.circ(hx, y - 30 * s, 85 * s, body)
    for ex in (-45, 40): P.poly([(hx + ex * s - 30 * s, y - 95 * s), (hx + ex * s, y - 160 * s), (hx + ex * s + 30 * s, y - 100 * s)], lc(PIG2, MUD, mud))
    P.ell(hx - f * 50 * s, y - 10 * s, 42 * s, 32 * s, lc(PIG2, MUD, mud * .7))
    for nx in (-12, 12): P.ell(hx - f * 50 * s + nx * s, y - 10 * s, 7 * s, 11 * s, (120, 60, 70))
    for ex in (-20, 25):
        if happy: P.arc(hx + ex * s, y - 50 * s, 10 * s, 200, 340, NIGHT, 5 * s)
        else: P.circ(hx + ex * s, y - 50 * s, 9 * s, NIGHT)
    P.arc(hx - f * 10 * s, y + 25 * s, 22 * s, 30, 150, NIGHT, 4 * s)

def sun(P, t, x=870, y=CENTER - 470, r=90, hot=1.):
    for k in range(10):
        a = k / 10 * 6.28 + t * .3; P.line([(x + math.cos(a) * (r + 20), y + math.sin(a) * (r + 20)), (x + math.cos(a) * (r + 60), y + math.sin(a) * (r + 60))], GLIM, 12)
    P.circ(x, y, r, lc(GLIM, HOOK, hot * .4), glow=(120, 90, 20))

def SC(i, P, t, u):
    if i == 0:
        farm(P); pig(P, 560, GROUND - 120, 1.15, t)
        for k in range(3):
            q = (u * .9 + k / 3) % 1; P.ell(350 + k * 50, GROUND - 260 + q * 120, 12, 18, (140, 200, 250))
        P.text(820, GROUND - 420, "?", 140 * back(seg(u, .4, .9)), GLIM)
    elif i == 1:
        farm(P); pig(P, 560, GROUND - 120, 1.15, t)
        P.circ(820, GROUND - 400, 110, (30, 40, 50), outline=GLIM, w=10)
        P.text(820, GROUND - 400, "0", 100, HOOK); P.cross(820, GROUND - 400, 95, k=back(seg(u, 1.4, 1.9)))
        P.stamp(540, CENTER - 420, "MYTH", seg(u, .25, .7))
    elif i == 2:
        farm(P); sun(P, t); pig(P, 480, GROUND - 120, 1.05, t)
        th = eout(seg(u, .3, 2.8))
        P.rrect(150, CENTER - 420, 210, CENTER - 100, 30, CLOUD); P.circ(180, CENTER - 80, 50, HOOK)
        P.rrect(165, CENTER - 100 - 300 * th, 195, CENTER - 80, 15, HOOK)
        P.badge(540, CENTER - 200, "too hot!", 60, HOOK, CLOUD, back(seg(u, 1.5, 2.0)))
    elif i == 3:
        farm(P, mud=True); sun(P, t, hot=.5)
        k = eio(seg(u, .2, 1.6)); pig(P, 540, lerp(GROUND - 120, GROUND - 20, k), 1.05, t, mud=.65 * k, happy=k > .8)
        for j in range(4):
            q = (t * .7 + j / 4) % 1; P.line([(380 + j * 110, GROUND - 260 - q * 160), (380 + j * 110, GROUND - 300 - q * 160)], (150, 210, 255), 10)
        P.badge(540, CENTER - 300, "evaporation cools", 56, NIGHT, GLIM, back(seg(u, 1.8, 2.3)))
    elif i == 4:
        farm(P, mud=True); sun(P, t, hot=.3); pig(P, 540, GROUND - 20, 1.05, t, mud=.65, happy=True)
        P.arc(540, GROUND - 60, 300, 200, 340, (150, 210, 255), 12)
        for j in range(3):
            q = (t * .8 + j / 3) % 1; a = 3.6 + q * 2.0
            P.circ(540 + math.cos(a) * 360, GROUND - 60 + math.sin(a) * 360, 12, NIGHT)
        P.badge(540, CENTER - 300, "sunscreen + bug shield", 54, HOPE, CLOUD, back(seg(u, .6, 1.1)))
    else:
        farm(P, mud=True); pig(P, 540, GROUND - 20 - abs(math.sin(t * 3)) * 20, 1.05, t, mud=.65, happy=True)
        P.heart(540, CENTER - 130, 60, (255, 120, 150))
        P.stamp(540, CENTER - 320, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
