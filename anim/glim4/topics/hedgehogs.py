# Thema: Do hedgehogs really sleep all winter?  (Mythos-Format, TRUE in Satz 2, FACT in Satz 6)
# Quellen: British Hedgehog Preservation Society, Leaflet L2 "Hedgehog Hibernation" (Herzschlag ~190 -> ~20/min,
# Körpertemperatur 35 °C -> 10 °C oder weniger, Winterschlaf etwa Nov.-März/April, Nestwechsel möglich); Woodland Trust.
CENTER = 1050
BODY, SPIKE, FACE = (120, 85, 60), (85, 60, 40), (215, 175, 135)
LEAF = [(200, 110, 50), (220, 160, 60), (170, 80, 40)]
COLD, WARM = (90, 150, 230), (240, 90, 70)
PAL = ((40, 50, 80), (120, 120, 150))
HI = {"winter?", "true!", "hibernate,", "heart", "twenty.", "thirty", "ten", "fat", "wake", "pause!"}
WOW = (1,)
GROUND = CENTER + 300

def ground(P, t, snow=True):
    P.poly([(0, GROUND), (W, GROUND - 20), (W, H), (0, H)], (90, 75, 60))
    if snow:
        P.poly([(0, GROUND), (W, GROUND - 20), (W, GROUND + 40), (0, GROUND + 60)], (240, 245, 252))
        for j in range(20): P.circ((j * 131 + t * 20) % W, (j * 197 + t * 60) % 900 + CENTER - 600, 5 + j % 3, (250, 250, 255))

def leaves(P, x, y, s):
    random.seed(4)
    for j in range(26):
        a = random.random() * math.pi; r = random.random()
        P.ell(x + math.cos(a) * 230 * s * r * 1.2, y - math.sin(a) * 130 * s * r, 42 * s, 20 * s, LEAF[j % 3])

def hedgehog(P, x, y, s, t, curl=0., walk=False):
    """Igel (Bauch bei y); curl 0..1 = eingerollt (schläft)."""
    br = 1 + .03 * math.sin(t * (1 if curl > .5 else 4))
    rx, ry = lerp(140, 115, curl) * s, lerp(95, 105, curl) * s * br
    for j in range(16):
        a = math.pi * (.05 + .9 * j / 15) + (math.pi * .15 if curl > .5 else 0) * 0
        px, py = x + math.cos(a) * rx, y - 10 * s - math.sin(a) * ry
        P.poly([(px - 18 * s, py + 6 * s), (px + 18 * s, py + 6 * s), (x + math.cos(a) * (rx + 45 * s), y - 10 * s - math.sin(a) * (ry + 45 * s))], SPIKE)
    P.ell(x, y - 10 * s, rx, ry, BODY)
    if curl < .5:
        ph = t * 8 if walk else 0
        for dx in (-70, 60): P.ell(x + dx * s + math.sin(ph + dx) * 8 * s, y + 70 * s, 22 * s, 14 * s, FACE)
        hx = x + rx * .95
        P.ell(hx, y + 15 * s, 70 * s, 50 * s, FACE)
        P.circ(hx + 62 * s, y + 18 * s, 13 * s, NIGHT)
        P.circ(hx + 12 * s, y - 5 * s, 9 * s, NIGHT)
    else:
        P.ell(x + 60 * s, y + 30 * s, 50 * s, 30 * s, FACE)
        P.line([(x + 40 * s, y + 25 * s), (x + 65 * s, y + 25 * s)], NIGHT, 5 * s)

def zzz(P, x, y, t):
    for j in range(3):
        q = (t * .5 + j / 3) % 1
        P.text(x + q * 60, y - q * 160, "z", (40 + 30 * q) * (1 - q * .3), lc(CLOUD, (120, 120, 150), q))

def thermo(P, x, y, k):
    P.rrect(x - 30, y - 220, x + 30, y + 60, 30, CLOUD, outline=(150, 160, 180), w=6)
    P.circ(x, y + 75, 48, lc(COLD, WARM, k)); P.rrect(x - 14, y + 60 - 270 * k, x + 14, y + 60, 14, lc(COLD, WARM, k))

def SC(i, P, t, u):
    if i == 0:
        ground(P, t); leaves(P, 540, GROUND, 1.1)
        hedgehog(P, 470, GROUND - 85, 1.2, t, walk=True)
        P.text(800, CENTER - 200, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        ground(P, t); leaves(P, 540, GROUND, 1.3)
        hedgehog(P, 520, GROUND - 100, 1.2, t, curl=1.)
        zzz(P, 640, CENTER - 20, t)
        P.stamp(560, CENTER - 260, "TRUE", seg(u, .25, .7), col=HOPE, rot=-6)
        P.badge(540, CENTER + 480, "about Nov to March", 56, NIGHT, CLOUD, back(seg(u, 1.6, 2.1)))
    elif i == 2:
        k = eio(seg(u, .6, 3.0)); n = int(lerp(190, 20, k))
        beat = 1 + .12 * max(0, math.sin(t * lerp(20, 3, k)))
        P.heart(540, CENTER - 40, 150 * beat, HOOK)
        P.text(540, CENTER + 230, f"{n}", 150, CLOUD)
        P.badge(540, CENTER + 400, "beats per minute", 54, NIGHT, CLOUD, back(seg(u, .3, .8)))
    elif i == 3:
        k = eio(seg(u, .6, 3.0)); c = int(lerp(35, 10, k))
        thermo(P, 330, CENTER + 20, lerp(.9, .25, k))
        P.text(720, CENTER - 20, f"{c} °C", 140, lc(WARM, COLD, k))
        hedgehog(P, 720, CENTER + 330, .7, t, curl=1.)
    elif i == 4:
        ground(P, t); leaves(P, 860, GROUND, .8)
        x = lerp(200, 600, eio(seg(u, .5, 3.5)))
        hedgehog(P, x, GROUND - 75, 1.0, t, walk=True)
        P.badge(400, CENTER - 230, "living on autumn fat", 54, GLIM, NIGHT, back(seg(u, .3, .8)))
        P.badge(800, CENTER + 120, "new nest", 50, NIGHT, CLOUD, back(seg(u, 2.6, 3.1)))
    else:
        ground(P, t); leaves(P, 400, GROUND, 1.1)
        hedgehog(P, 400, GROUND - 90, 1.0, t, curl=1.); zzz(P, 500, CENTER + 40, t)
        P.stamp(780, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
