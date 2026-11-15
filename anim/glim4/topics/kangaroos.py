# Thema: How do kangaroos hop so far?
CENTER = 1050
FUR, FUR2, BELLY = (205, 120, 75), (160, 85, 50), (240, 200, 160)
PAL = ((255, 220, 170), (245, 175, 120))
HI = {"kangaroos", "hop", "far?", "eight", "meters", "tendons,", "springs", "energy", "free.", "faster", "barely", "tail", "fifth", "leg!"}
WOW = (2, 4)

def roo(P, x, y, s, t, crouch=0., air=0., tailleg=False):
    """Känguru seitlich nach rechts; crouch 0..1 = eingefedert, air = Beine gestreckt."""
    c = crouch
    ty = y + 120 * s + (40 if tailleg else 0) * s
    P.line([(x - 60 * s, y + 60 * s), (x - 220 * s, ty + 60 * s), (x - 330 * s, ty + (130 if tailleg else 40) * s - air * 60 * s)], FUR2, 40 * s)
    # Hinterbein: Oberschenkel + langer Fuß
    kx, ky = x - 10 * s, y + (120 + 40 * c) * s
    fx, fy = x + (40 - 50 * air) * s, y + (230 - 30 * c + 40 * air) * s
    P.ell(x - 30 * s, y + 70 * s, 95 * s, 110 * s, FUR, outline=FUR2, w=5 * s)
    P.line([(kx, ky), (fx, fy)], FUR2, 26 * s)
    P.line([(fx, fy), (fx + (150 - 30 * air) * s, fy + (5 + 30 * air) * s)], FUR2, 22 * s)
    P.ell(x + 30 * s, y - 40 * s, 80 * s, 120 * s, FUR, outline=FUR2, w=5 * s)         # Oberkörper
    P.ell(x + 50 * s, y - 20 * s, 40 * s, 80 * s, BELLY)
    P.line([(x + 80 * s, y - 60 * s), (x + 120 * s, y + 10 * s)], FUR2, 14 * s)       # Ärmchen
    hx, hy = x + 80 * s, y - 170 * s
    for d in (-1, 1): P.ell(hx - 20 * s + d * 22 * s, hy - 70 * s, 18 * s, 48 * s, FUR, outline=FUR2, w=4 * s)
    P.ell(hx, hy, 60 * s, 48 * s, FUR, outline=FUR2, w=5 * s)
    P.ell(hx + 60 * s, hy + 12 * s, 40 * s, 26 * s, FUR, outline=FUR2, w=4 * s)
    P.circ(hx + 95 * s, hy + 6 * s, 9 * s, NIGHT)
    P.circ(hx + 15 * s, hy - 10 * s, 10 * s, NIGHT); P.circ(hx + 18 * s, hy - 14 * s, 3 * s, CLOUD)

def spring(P, x0, y0, x1, y1, n, col, w=8):
    pts = []
    for k in range(n * 2 + 1):
        q = k / (n * 2); off = (20 if k % 2 else -20) if 0 < k < n * 2 else 0
        dx, dy = x1 - x0, y1 - y0; L_ = math.hypot(dx, dy) or 1
        pts.append((x0 + dx * q - dy / L_ * off, y0 + dy * q + dx / L_ * off))
    P.line(pts, col, w)

def SC(i, P, t, u):
    P.rrect(-20, CENTER + 330, W + 20, H + 20, 0, (215, 140, 80))
    for x in (120, 950): P.circ(x, CENTER + 300, 50, (130, 160, 80))
    if i == 0:
        ph = (u * .9) % 1; hop = math.sin(ph * math.pi)
        roo(P, 420, CENTER + 70 - hop * 160, 1.0, t, crouch=max(0, 1 - hop * 3), air=hop)
        P.text(880, CENTER - 290, "?", 150 * back(seg(u, .4, .9)), HOOK)
    elif i == 1:
        q = seg(u, .4, 2.4); hop = math.sin(q * math.pi)
        x = lerp(220, 760, q)
        P.line([(220, CENTER + 330), (760, CENTER + 330)], GLIM, 8 * seg(u, .4, .6))
        for k in range(9): P.line([(220 + k * 67.5, CENTER + 310), (220 + k * 67.5, CENTER + 350)], GLIM, 5)
        roo(P, x, CENTER + 60 - hop * 260, .75, t, crouch=0, air=hop)
        P.badge(540, CENTER + 420, "up to 8 m!", 64, NIGHT, GLIM, back(seg(u, 1.6, 2.1)))
    elif i == 2:
        c = .5 + .5 * math.sin(u * 3)
        roo(P, 360, CENTER + 70, 1.0, t, crouch=c)
        P.rrect(620, CENTER - 200, 960, CENTER + 260, 30, CLOUD, outline=FUR2, w=6)
        spring(P, 790, CENTER - 160, 790, CENTER + 50 + 150 * c, 6, HOOK, 12)
        P.badge(790, CENTER + 200, "tendon", 48, HOOK, CLOUD, back(seg(u, .6, 1.1)))
        P.badge(540, CENTER + 420, "like a spring", 60, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
    elif i == 3:
        for j in range(3):
            q = ((u * .8) + j / 3) % 1
        ph = (u * 1.1) % 1; hop = math.sin(ph * math.pi)
        x = 200 + (u * 120) % 700
        P.arc(x + 150, CENTER + 200, 160, 200, 340, GLIM, 8)
        roo(P, x, CENTER + 70 - hop * 200, .85, t, crouch=max(0, 1 - hop * 3), air=hop)
        P.badge(540, CENTER + 420, "energy bounces back", 56, HOPE, CLOUD, back(seg(u, 1.2, 1.7)))
    elif i == 4:
        k = eout(seg(u, .3, 2.5))
        P.rrect(160, CENTER - 200, 920, CENTER + 260, 30, CLOUD, outline=NIGHT, w=6)
        P.line([(220, CENTER + 200), (860, CENTER + 200)], NIGHT, 6); P.line([(220, CENTER + 200), (220, CENTER - 160)], NIGHT, 6)
        P.line([(240, CENTER - 40), (240 + 600 * k, CENTER - 40 - 30 * k)], HOPE, 14)
        P.badge(540, CENTER - 110, "energy", 44, HOPE, CLOUD, back(seg(u, .6, 1.1)))
        P.badge(540, CENTER + 420, "faster, same cost!", 58, NIGHT, GLIM, back(seg(u, 2.0, 2.5)))
    else:
        sw = math.sin(u * 2.5)
        roo(P, 500, CENTER + 40, 1.0, t, crouch=.6, tailleg=True)
        P.arc(500 - 300, CENTER + 220, 80, 0, 360, GLIM, 8 * seg(u, .8, 1.2))
        P.badge(540, CENTER - 330, "tail = 5th leg", 60, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
