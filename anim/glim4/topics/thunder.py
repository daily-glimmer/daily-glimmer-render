# Thema: Why do we see lightning before we hear thunder? (G60, Erde/Wetter)
CENTER = 1050
PAL = ((60, 70, 110), (110, 120, 160))
HI = {"lightning", "thunder?", "five", "hotter", "Sun.", "booms,", "boom", "instantly,", "three", "seconds", "kilometer.", "divide", "inside!"}
WOW = (1, 4)
CLOUDC, CLOUDD, BOLT = (150, 160, 185), (95, 105, 135), (255, 235, 120)

def cloud(P, x, y, s, col=CLOUDC):
    for dx, dy, r in ((-150, 20, 110), (-40, -40, 140), (90, -10, 120), (190, 40, 90), (20, 50, 120)):
        P.circ(x + dx * s, y + dy * s, r * s, col, outline=CLOUDD, w=5 * s)

def bolt(P, x, y, s, k, t):
    if k <= 0: return
    pts = [(0, 0), (-50, 160), (20, 160), (-40, 340), (90, 120), (20, 120), (70, 0)]
    fl = .7 + .3 * abs(math.sin(t * 30))
    P.poly([(x + px * s, y + py * s * k) for px, py in pts], BOLT if fl > .8 else (240, 215, 100), outline=(255, 200, 60), w=4 * s)

def sun(P, x, y, r, t):
    for a in range(12):
        an = a * math.pi / 6 + t * .4
        P.line([(x + math.cos(an) * r * 1.15, y + math.sin(an) * r * 1.15), (x + math.cos(an) * r * 1.45, y + math.sin(an) * r * 1.45)], (255, 190, 60), 14)
    P.circ(x, y, r, (255, 200, 70), outline=(240, 150, 40), w=6)

def eye(P, x, y, s):
    P.ell(x, y, 70 * s, 42 * s, CLOUD, outline=NIGHT, w=6 * s); P.circ(x, y, 24 * s, (70, 130, 200)); P.circ(x, y, 11 * s, NIGHT)

def ear(P, x, y, s):
    P.ell(x, y, 50 * s, 75 * s, (255, 205, 170), outline=(200, 140, 110), w=6 * s); P.arc(x + 5 * s, y, 26 * s, 120, 330, (200, 140, 110), 6 * s)

def SC(i, P, t, u):
    if i == 0:
        cloud(P, 540, CENTER - 120, 1.2)
        bolt(P, 520, CENTER - 20, 1.3, eio(seg(u % 2.0, 0, .12)) if (u % 2.0) < .6 else 0, t)
        P.text(860, CENTER + 380, "?", 170 * back(seg(u, .6, 1.1)), GLIM)
    elif i == 1:
        cloud(P, 330, CENTER - 140, .8)
        bolt(P, 310, CENTER - 60, .9, 1, t)
        sun(P, 800, CENTER + 80, 110 * back(seg(u, 1.8, 2.3)), t)
        P.badge(540, CENTER + 430, "5x hotter than the Sun", 54, HOOK, CLOUD, back(seg(u, 2.6, 3.1)))
    elif i == 2:
        bolt(P, 500, CENTER - 200, 1.1, 1, t)
        for k in range(4):
            r = ((u * 160 + k * 110) % 440)
            P.arc(540, CENTER + 50, 60 + r, 0, 360, (200, 210, 255), max(2, 14 - r / 40))
        P.text(540, CENTER + 520, "BOOM!", 120 * back(seg(u, 1.6, 2.0)), GLIM)
    elif i == 3:
        cloud(P, 240, CENTER - 160, .55); bolt(P, 230, CENTER - 110, .6, 1, t)
        eye(P, 820, CENTER - 40, 1.0); ear(P, 820, CENTER + 300, 1.0)
        q = seg(u, .5, .8); P.line([(320, CENTER - 40), (320 + 420 * q, CENTER - 40)], BOLT, 12)
        w = seg(u, 1.5, 5.0); P.line([(320, CENTER + 300), (320 + 420 * w, CENTER + 300)], (150, 200, 255), 12)
        P.text(520, CENTER + 120, "light: instant", 48 * back(seg(u, .8, 1.2)), BOLT)
        P.text(520, CENTER + 450, "sound: 3 s per km", 48 * back(seg(u, 3.0, 3.4)), (150, 200, 255))
    elif i == 4:
        n = min(9, int(u * 2.3))
        P.circ(540, CENTER + 60, 220, CLOUD, outline=NIGHT, w=12)
        an = -math.pi / 2 + n / 12 * 2 * math.pi
        P.line([(540, CENTER + 60), (540 + math.cos(an) * 180, CENTER + 60 + math.sin(an) * 180)], HOOK, 14)
        P.text(540, CENTER + 60, str(n), 140, NIGHT)
        P.badge(540, CENTER + 410, "9 s / 3 = 3 km", 60, NIGHT, GLIM, back(seg(u, 4.0, 4.5)))
    else:
        cloud(P, 300, CENTER - 140, .6); bolt(P, 290, CENTER - 90, .6, 1 if (u % 1.8) < .3 else 0, t)
        P.poly([(560, CENTER + 60), (760, CENTER - 110), (960, CENTER + 60)], HOOK)
        P.rrect(600, CENTER + 60, 920, CENTER + 330, 10, CLOUD, outline=NIGHT, w=6)
        P.rrect(720, CENTER + 180, 800, CENTER + 330, 8, (150, 100, 60))
        P.rrect(630, CENTER + 100, 700, CENTER + 160, 6, BOLT)
        P.heart(380, CENTER + 260, 46 * back(seg(u, 1.2, 1.7)), HOPE)
