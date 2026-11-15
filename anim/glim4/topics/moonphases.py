# Thema: Why does the Moon change shape?
CENTER = 1050
PAL = ((6, 10, 32), (20, 28, 70))
HI = {"shape?", "doesn't!", "round", "half.", "circles", "different", "sunny", "away.", "new", "full", "whole", "bright", "twenty", "nine", "days."}
WOW = (1, 4)
MOON, CRATER, DARKM = (215, 215, 220), (180, 180, 188), (48, 52, 72)

def sun(P, x, y, r, t):
    for k in range(12):
        a = k / 12 * 6.28 + t * .2; P.line([(x + math.cos(a) * (r + 15), y + math.sin(a) * (r + 15)), (x + math.cos(a) * (r + 55), y + math.sin(a) * (r + 55))], GLIM, 10)
    P.circ(x, y, r, GLIM)

def earth(P, x, y, r):
    P.circ(x, y, r, (40, 110, 190)); P.ell(x - r * .25, y - r * .2, r * .35, r * .25, (90, 170, 100)); P.ell(x + r * .3, y + r * .2, r * .25, r * .3, (90, 170, 100))

def phase_moon(P, x, y, r, ph):
    """ph 0 = Neumond, .5 = Vollmond, 1 = Neumond (zunehmend rechts beleuchtet)."""
    P.circ(x, y, r, DARKM)
    c = math.cos(ph * 2 * math.pi)   # 1 neu, -1 voll
    right = ph < .5
    pts = []
    for k in range(41):
        a = -math.pi / 2 + k / 40 * math.pi
        pts.append((x + (1 if right else -1) * math.cos(a) * r, y + math.sin(a) * r))
    for k in range(41):
        a = math.pi / 2 - k / 40 * math.pi
        pts.append((x + (1 if right else -1) * c * math.cos(a) * r, y + math.sin(a) * r))
    if abs(c) < .999 or c < 0: P.poly(pts, MOON)
    for dx, dy, rr in ((-.3, -.3, .16), (.35, .1, .13), (-.05, .4, .11)):
        P.circ(x + dx * r, y + dy * r, rr * r, lc(CRATER, DARKM, .0))

def halflit(P, x, y, r, sx):
    """Kugel, Hälfte zur Sonne (Richtung sx) beleuchtet – Draufsicht."""
    P.circ(x, y, r, DARKM)
    a0 = math.atan2(0, sx - x)
    P.poly([(x + math.cos(a0 + (k / 20 - .5) * math.pi) * r, y + math.sin(a0 + (k / 20 - .5) * math.pi) * r) for k in range(21)], MOON)

def SC(i, P, t, u):
    if i == 0:
        for j in range(5): phase_moon(P, 140 + j * 200, CENTER - 20, 80, .1 + j * .2)
        phase_moon(P, 540, CENTER + 260, 150, (t * .05) % 1)
        P.text(840, CENTER - 300, "?", 140 * back(seg(u, .4, .9)), GLIM)
    elif i == 1:
        sun(P, 120, CENTER - 10, 70, t)
        halflit(P, 600, CENTER - 10, 230, 120)
        P.badge(600, CENTER + 330, "half lit, always", 56, NIGHT, GLIM, back(seg(u, 2.0, 2.5)))
    elif i == 2:
        sun(P, 120, CENTER - 280, 60, t)
        earth(P, 560, CENTER + 40, 90)
        P.arc(560, CENTER + 40, 300, 0, 360, (80, 90, 130), 4)
        a = u * .9 + 1.0
        halflit(P, 560 + math.cos(a) * 300, CENTER + 40 + math.sin(a) * 300, 60, -2000)
        phase_moon(P, 860, CENTER - 300, 70, (a / 6.28 + .25) % 1)
    elif i == 3:
        sun(P, 110, CENTER, 70, t)
        halflit(P, 460, CENTER, 100, 110); earth(P, 860, CENTER, 110)
        P.line([(770, CENTER - 40), (580, CENTER - 40)], (120, 200, 255), 6)
        phase_moon(P, 540, CENTER + 330, 110, .0)
        P.badge(540, CENTER - 280, "new moon", 60, NIGHT, GLIM, back(seg(u, 2.4, 2.9)))
    elif i == 4:
        sun(P, 110, CENTER, 70, t)
        earth(P, 480, CENTER, 100); halflit(P, 900, CENTER, 90, 110)
        phase_moon(P, 540, CENTER + 330, 130, .5)
        P.badge(540, CENTER - 280, "full moon", 60, GLIM, NIGHT, back(seg(u, 2.4, 2.9)))
    else:
        for j in range(8):
            a = -math.pi / 2 + j / 8 * 6.28
            phase_moon(P, 540 + math.cos(a) * 280, CENTER + 20 + math.sin(a) * 280, 62 * back(seg(u, .2 + j * .12, .5 + j * .12)), j / 8)
        P.text(540, CENTER + 20, "29.5", 110 * back(seg(u, 1.5, 2.0)), GLIM)
        P.text(540, CENTER + 120, "days", 60 * back(seg(u, 1.7, 2.2)), CLOUD)
