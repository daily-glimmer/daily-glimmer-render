# Thema: Why does your stomach growl?
CENTER = 1050
PAL = ((255, 200, 170), (240, 160, 150))
HI = {"growl?", "muscles", "squeeze", "gas", "liquid", "bubbling", "empty,", "cleanup", "waves", "muffle", "louder!", "borborygmi.", "worst"}
WOW = (1, 4)
ST, ST2 = (240, 130, 140), (200, 90, 110)

def tummy(P, x, y, s, t, squeeze=0., food=0., bubbles=0, wave=0.):
    pts = []
    for k in range(25):
        a = k / 24 * math.pi
        r = 1 - .18 * squeeze * math.exp(-((k / 24 - (t * .5 % 1)) * 6) ** 2)
        pts.append((x + math.cos(a + math.pi) * 230 * s * r, y + math.sin(a + math.pi) * 120 * s * r - 20 * s))
    P.ell(x, y, 230 * s, 160 * s, ST, outline=ST2, w=10 * s)
    P.line([(x + 180 * s, y - 110 * s), (x + 240 * s, y - 260 * s)], ST2, 50 * s)
    P.line([(x - 200 * s, y + 70 * s), (x - 260 * s, y + 220 * s)], ST2, 50 * s)
    if wave > 0:
        q = (t * .8) % 1; wx = x - 220 * s + q * 440 * s
        P.ell(wx, y, 30 * s, 165 * s, ST2)
    if food: 
        for j in range(6): P.circ(x - 100 * s + j * 40 * s, y + 60 * s - (j % 2) * 30 * s, 26 * s * food, (240, 200, 110))
    for j in range(bubbles):
        q = (t * .7 + j / max(1, bubbles)) % 1
        P.circ(x - 150 * s + (j * 71 % 300) * s, y + 80 * s - q * 160 * s, (12 + j % 3 * 6) * s, (255, 235, 240), outline=ST2, w=3 * s)

def SC(i, P, t, u):
    if i == 0:
        tummy(P, 540, CENTER + 40, 1.4, t, bubbles=6, wave=1)
        for k in range(3): P.text(250 + k * 290, CENTER - 230 + (k % 2) * 40, "GRR", 70 * back(seg(u, .4 + k * .3, .8 + k * .3)), HOOK)
        P.text(860, CENTER - 300, "?", 140 * back(seg(u, .4, .9)), HOOK)
    elif i == 1:
        tummy(P, 540, CENTER + 40, 1.4, t, food=1, wave=seg(u, 1.5, 2))
        P.badge(540, CENTER + 400, "muscle squeeze", 58, NIGHT, GLIM, back(seg(u, 1.6, 2.1)))
    elif i == 2:
        tummy(P, 540, CENTER + 40, 1.4, t, food=.6, bubbles=10, wave=1)
        P.badge(300, CENTER - 260, "gas", 56, HOOK, CLOUD, back(seg(u, 1.4, 1.8)))
        P.badge(760, CENTER - 260, "liquid", 56, (60, 150, 220), CLOUD, back(seg(u, 2.0, 2.4)))
    elif i == 3:
        tummy(P, 540, CENTER + 40, 1.4, t, wave=1)
        P.badge(540, CENTER - 260, "every 1-2 hours", 58, NIGHT, GLIM, back(seg(u, 2.8, 3.3)))
    elif i == 4:
        tummy(P, 540, CENTER + 40, 1.4, t, bubbles=12, wave=1)
        for k in range(3): waves(P, 540, CENTER + 40, t, HOOK, n=3, r0=340, dr=50, a0=-40 + k * 120, a1=40 + k * 120)
        P.text(540, CENTER - 280, "RUMBLE!", 110 * back(seg(u, 1.6, 2.0)), HOOK)
    else:
        tummy(P, 540, CENTER + 60, 1.0, t, bubbles=6, wave=1)
        P.badge(540, CENTER - 210, "borborygmi", 64, HOOK, CLOUD, back(seg(u, .6, 1.1)))
