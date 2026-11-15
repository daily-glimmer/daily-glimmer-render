# Thema: Why do male seahorses give birth?
CENTER = 1050
def dk(c, k): return tuple(int(v * k) for v in c)
PAL = ((40, 120, 170), (20, 70, 120))
HI = {"male", "birth?", "eggs", "pouch", "dad's", "womb.", "oxygen", "food,", "safe.", "hundreds", "thousand!", "sooner.", "dads?"}
WOW = (1, 4)
SH, SH2 = (255, 170, 80), (220, 120, 50)

def seaweed(P, t):
    for k, x in enumerate((70, 180, 900, 1010)):
        pts = [(x + math.sin(t * 1.3 + j * .6 + k) * 18 * j / 6, H - 80 - j * 70) for j in range(9)]
        P.line(pts, (50, 150, 100) if k % 2 else (40, 120, 90), 26)
    P.poly([(0, H - 120), (W, H - 160), (W, H), (0, H)], (230, 205, 150))

def bubbles(P, t, n=8):
    for k in range(n):
        q = (t * .25 + k / n) % 1
        P.circ(120 + (k * 137) % 840 + math.sin(t * 2 + k) * 15, H - 200 - q * 1500, 10 + k % 3 * 6, None, outline=(200, 235, 255), w=4)

def seahorse(P, x, y, s, t, col=SH, belly=0., flip=1):
    f = flip; b = math.sin(t * 2.4) * 8 * s
    d2 = dk(col, .78) if 'dk' in globals() else tuple(int(c * .78) for c in col)
    tail = [(x + f * (10 + 30 * math.cos(a)) * s, y + (150 + 40 * a) * s + b) for a in [j * .5 for j in range(10)]]
    tail = [(x + f * 20 * s, y + 120 * s + b)] + [(x + f * (20 - 50 * math.sin(j * .55)) * s * (1 - j * .06), y + (130 + j * 18 - (j * j) * 1.2) * s + b) for j in range(12)]
    P.line(tail, d2, 30 * s)
    P.ell(x, y + 40 * s + b, (70 + belly * 45) * s, 105 * s, col, outline=d2, w=5 * s)
    if belly > .05: P.ell(x - f * 20 * s, y + 70 * s + b, (40 + belly * 40) * s, (55 + belly * 25) * s, (255, 215, 150))
    for j in range(5): P.line([(x - f * 55 * s, y + (-20 + j * 30) * s + b), (x - f * 25 * s, y + (-20 + j * 30) * s + b)], d2, 4 * s)
    P.poly([(x + f * 60 * s, y + 10 * s + b), (x + f * 110 * s, y - 10 * s + b + math.sin(t * 9) * 8 * s), (x + f * 100 * s, y + 50 * s + b)], (255, 220, 160))
    P.circ(x + f * 5 * s, y - 70 * s + b, 55 * s, col, outline=d2, w=5 * s)
    P.poly([(x - f * 20 * s, y - 120 * s + b), (x + f * 5 * s, y - 160 * s + b), (x + f * 25 * s, y - 115 * s + b)], d2)
    P.rrect(x - f * 110 * s, y - 85 * s + b, x - f * 30 * s, y - 55 * s + b, 14 * s, col)
    P.circ(x - f * 10 * s, y - 80 * s + b, 15 * s, CLOUD); P.circ(x - f * 14 * s, y - 80 * s + b, 8 * s, NIGHT)

def egg(P, x, y, r): P.circ(x, y, r, (255, 200, 90), outline=(230, 150, 50), w=3)

def SC(i, P, t, u):
    seaweed(P, t); bubbles(P, t)
    if i == 0:
        seahorse(P, 540, CENTER - 20, 2.0, t, belly=.8)
        P.text(830, CENTER - 300, "?", 140 * back(seg(u, .4, .9)), GLIM)
    elif i == 1:
        seahorse(P, 330, CENTER, 1.4, t, col=(240, 140, 170), flip=1)
        seahorse(P, 760, CENTER, 1.5, t, flip=-1)
        q = seg(u, .8, 2.6)
        for j in range(6):
            e = clamp(q * 1.4 - j * .08)
            egg(P, lerp(420, 700, e) + j * 6, CENTER + 90 - math.sin(e * 3.14) * 80 + j * 8, 14)
        P.badge(760, CENTER + 330, "dad's pouch", 58, NIGHT, GLIM, back(seg(u, 1.6, 2.1)))
    elif i == 2:
        P.circ(540, CENTER + 20, 300, (255, 225, 170), outline=SH2, w=12)
        for j in range(14):
            a = j * 2.4; r = 60 + (j % 5) * 40
            egg(P, 540 + math.cos(a) * r, CENTER + 20 + math.sin(a) * r * .8, 26 * back(seg(u, .2 + j * .05, .6 + j * .05)))
        k = seg(u, 1.6, 2.4)
        P.line([(300, CENTER - 230), (lerp(300, 780, k), CENTER - 230)], SH2, 24)
        P.badge(540, CENTER + 400, "sealed tight", 58, HOPE, CLOUD, back(seg(u, 2.2, 2.7)))
    elif i == 3:
        seahorse(P, 540, CENTER - 20, 2.0, t, belly=.5 + .5 * seg(u, 0, 4))
        P.badge(300, CENTER - 280, "oxygen", 52, (60, 150, 220), CLOUD, back(seg(u, 1.0, 1.4)))
        P.badge(780, CENTER - 280, "food", 52, HOPE, CLOUD, back(seg(u, 1.6, 2.0)))
        P.badge(540, CENTER + 420, "2-4 weeks", 62, NIGHT, GLIM, back(seg(u, .4, .9)))
    elif i == 4:
        seahorse(P, 330, CENTER - 60, 1.5, t, belly=1 - seg(u, .3, 3))
        random.seed(7)
        for j in range(40):
            q = clamp(u * .5 - j * .02); a = random.uniform(-1.0, 1.0); d = 100 + q * random.uniform(250, 600)
            if q > 0: seahorse(P, 380 + math.cos(a) * d, CENTER + 20 + math.sin(a) * d * .8, .22, t + j)
        P.badge(620, CENTER + 420, "up to 1,000+", 64, HOOK, CLOUD, back(seg(u, 1.8, 2.3)))
    else:
        seahorse(P, 300, CENTER + 40, 1.2, t, col=(240, 140, 170))
        for j in range(6): egg(P, 470 + j * 45, CENTER + 120 - abs(math.sin(t * 3 + j)) * 30, 18)
        seahorse(P, 650, CENTER - 40, 1.1, t, flip=-1)
        P.heart(470, CENTER - 230, 50 * back(seg(u, .5, 1.0)), HOOK)
