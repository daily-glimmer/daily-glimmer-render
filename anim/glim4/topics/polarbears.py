# Thema: How do polar bears stay warm in the Arctic?
CENTER = 1050
FUR, FUR2, SKIN = (245, 240, 225), (205, 200, 185), (40, 40, 50)
PAL = ((190, 220, 240), (150, 190, 225))
HI = {"warm", "Arctic?", "fat,", "11", "centimeters", "two", "layers", "fur", "jacket.", "see-through,", "black!", "small", "ears", "short", "tail", "overheat!"}
WOW = (1, 3)

def ice(P, y=CENTER + 300):
    P.poly([(0, y), (W, y - 30), (W, H), (0, H)], (235, 245, 252), outline=(170, 200, 225), w=6)
    for k in range(4): P.line([(100 + k * 260, y + 40), (180 + k * 260, y + 80)], (190, 215, 235), 6)

def bear(P, x, y, s, t, walk=0., flip=1, hot=False):
    f = flip; sw = math.sin(t * 8) * 30 * s * walk
    for k, (dx, ph) in enumerate(((-130, 0), (-60, 3.1), (90, 3.1), (160, 0))):
        o = math.sin(t * 8 + ph) * 25 * s * walk
        P.rrect(x + f * dx * s - 32 * s + o, y + 20 * s, x + f * dx * s + 32 * s + o, y + 170 * s, 26 * s, FUR2 if k % 2 else FUR, outline=FUR2, w=4 * s)
    P.ell(x, y, 220 * s, 115 * s, FUR, outline=FUR2, w=5 * s)
    P.circ(x - f * 205 * s, y - 15 * s, 22 * s, FUR, outline=FUR2, w=4 * s)
    hx, hy = x + f * 220 * s, y - 70 * s
    P.ell(hx, hy, 95 * s, 75 * s, FUR, outline=FUR2, w=5 * s)
    P.ell(hx + f * 80 * s, hy + 18 * s, 50 * s, 38 * s, FUR, outline=FUR2, w=4 * s)
    P.circ(hx + f * 120 * s, hy + 8 * s, 14 * s, SKIN)
    for d in (-1, 1): P.circ(hx - f * 25 * s + d * 22 * s, hy - 62 * s, 20 * s, FUR, outline=FUR2, w=4 * s)
    P.circ(hx + f * 30 * s, hy - 14 * s, 10 * s, SKIN)
    if hot:
        for k in range(3):
            q = (t * .9 + k / 3) % 1
            P.circ(hx + f * (40 + k * 30) * s, hy - 110 * s - q * 120 * s, 16 * s * (1 - q), (140, 200, 240))

def layers(P, x, y, w, h, k, t):
    P.rrect(x - w / 2, y - h / 2, x + w / 2, y - h / 2 + h * .2, 14, FUR)             # Fell außen
    P.rrect(x - w / 2, y - h / 2 + h * .2, x + w / 2, y - h / 2 + h * .32, 10, SKIN)   # schwarze Haut
    P.rrect(x - w / 2, y - h / 2 + h * .32, x + w / 2, y - h / 2 + h * .32 + h * .42 * k, 10, (250, 215, 120))  # Fett
    P.rrect(x - w / 2, y + h * .24, x + w / 2, y + h / 2, 14, (220, 110, 110))         # Körper

def SC(i, P, t, u):
    ice(P)
    for k in range(10):
        q = (t * .15 + k / 10) % 1
        P.circ(80 + k * 100 + math.sin(t + k) * 20, lerp(500, CENTER + 300, q), 7, (255, 255, 255))
    if i == 0:
        bear(P, 470, CENTER + 120, 1.15, t)
        P.text(860, CENTER - 280, "?", 150 * back(seg(u, .4, .9)), HOOK)
    elif i == 1:
        k = eout(seg(u, .3, 2.2))
        layers(P, 540, CENTER - 20, 560, 560, k, t)
        P.badge(540, CENTER - 230, "fur", 42, NIGHT, CLOUD, back(seg(u, .2, .6)))
        P.badge(540, CENTER - 125, "black skin", 38, SKIN, CLOUD, back(seg(u, .3, .7)))
        P.badge(540, CENTER + 10 + 60 * k, f"fat: up to {int(11 * k)} cm", 44, NIGHT, GLIM, back(seg(u, .4, .8)))
        P.badge(540, CENTER + 380, "thick fat", 60, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
    elif i == 2:
        P.rrect(240, CENTER - 230, 840, CENTER + 230, 40, (215, 210, 195))
        for j in range(26):
            x = 270 + j * 22; ww = math.sin(t * 2 + j) * 6
            P.line([(x, CENTER + 220), (x + ww, CENTER - 210)], FUR, 10)
        for j in range(60):
            x = 260 + (j * 37) % 570; y = CENTER + 60 + (j * 53) % 160
            P.arc(x, y, 12, 0, 300, FUR2, 4)
        P.badge(540, CENTER + 380, "2 layers of fur", 60, HOPE, CLOUD, back(seg(u, 1.0, 1.5)))
    elif i == 3:
        k = back(seg(u, .1, .6))
        P.rrect(140, CENTER + 140, 940, CENTER + 260, 30, SKIN)
        for j in range(4):
            x = 260 + j * 190
            P.rrect(x - 28 * k, CENTER - 300, x + 28 * k, CENTER + 140, 28, (235, 245, 255), outline=(150, 180, 210), w=6)
            P.rrect(x - 10 * k, CENTER - 280, x + 10 * k, CENTER + 120, 10, (200, 225, 245))
        P.badge(540, CENTER + 400, "black skin!", 60, NIGHT, GLIM, back(seg(u, 2.0, 2.5)))
    elif i == 4:
        bear(P, 540, CENTER + 120, 1.15, t)
        P.arc(540 - 205 * 1.15, CENTER + 103, 60, 0, 360, HOOK, 8 * seg(u, 1.6, 2.0))
        P.arc(540 + 220 * 1.15 - 25, CENTER + 120 - 80 - 70 * 1.15, 60, 0, 360, HOOK, 8 * seg(u, .5, .9))
        P.badge(540, CENTER + 420, "less heat lost", 60, HOPE, CLOUD, back(seg(u, 2.0, 2.5)))
    else:
        x = lerp(200, 640, (u / 6) % 1)
        bear(P, x, CENTER + 140, 1.0, t, walk=1., hot=True)
        P.badge(540, CENTER - 310, "too warm!", 60, HOOK, CLOUD, back(seg(u, 1.6, 2.1)))
