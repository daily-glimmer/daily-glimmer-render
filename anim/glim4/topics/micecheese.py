# Thema: Do mice really love cheese?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6)
CENTER = 1050
MF, MF2, PINKC = (165, 160, 170), (130, 125, 140), (245, 170, 180)
CHEESE, CH2 = (255, 205, 70), (230, 170, 40)
PAL = ((120, 80, 60), (220, 170, 120))
HI = {"cheese?", "myth!", "grains,", "seeds", "fruit.", "sweet", "starchy", "smelly", "sensitive.", "cartoons,", "grains", "sweet!"}
WOW = (1,)
FLOOR = CENTER + 300

def floor(P): P.poly([(0, FLOOR), (W, FLOOR - 10), (W, H), (0, H)], (170, 120, 80)); P.line([(0, FLOOR), (W, FLOOR - 10)], (130, 90, 60), 10)

def mouse(P, x, y, s, t, f=1, sniff=0., happy=True):
    P.line([(x - f * 100 * s, y + 20 * s), (x - f * 200 * s, y - 20 * s + math.sin(t * 3) * 15 * s), (x - f * 260 * s, y + 10 * s)], PINKC, 8 * s)
    P.ell(x, y, 115 * s, 75 * s, MF)
    P.ell(x + f * 20 * s, y + 20 * s, 70 * s, 40 * s, lc(MF, CLOUD, .4))
    hx, hy = x + f * 110 * s, y - 30 * s + sniff * math.sin(t * 15) * 4 * s
    P.circ(hx - f * 30 * s, hy - 55 * s, 40 * s, MF); P.circ(hx - f * 30 * s, hy - 55 * s, 26 * s, PINKC)
    P.ell(hx, hy, 70 * s, 50 * s, MF)
    P.circ(hx + f * 65 * s, hy + 5 * s, 12 * s, PINKC)
    for dy in (-6, 6): P.line([(hx + f * 60 * s, hy + dy * s), (hx + f * 120 * s, hy + dy * 3 * s)], MF2, 3 * s)
    P.circ(hx + f * 20 * s, hy - 12 * s, 9 * s, NIGHT); P.circ(hx + f * 22 * s, hy - 15 * s, 3 * s, CLOUD)
    if happy: P.arc(hx + f * 35 * s, hy + 15 * s, 14 * s, 20, 160, NIGHT, 4 * s)

def cheese(P, x, y, s):
    P.poly([(x - 110 * s, y + 50 * s), (x + 110 * s, y + 50 * s), (x + 110 * s, y - 40 * s), (x - 110 * s, y + 10 * s)], CHEESE)
    P.poly([(x - 110 * s, y + 10 * s), (x + 110 * s, y - 40 * s), (x + 60 * s, y - 70 * s)], lc(CHEESE, (255, 255, 255), .3))
    for dx, dy, r in ((-50, 25, 14), (30, 10, 18), (70, 30, 10)): P.circ(x + dx * s, y + dy * s, r * s, CH2)

def grain(P, x, y, s, k=1.):
    for j in range(7): P.ell(x + (j - 3) * 26 * s, y - abs(j - 3) * 10 * s, 12 * s * k, 22 * s * k, (230, 190, 110))
    P.line([(x, y + 20 * s), (x, y + 120 * s)], (190, 160, 90), 8 * s)

def berry(P, x, y, s): P.circ(x, y, 30 * s, (220, 60, 90)); P.poly([(x - 14 * s, y - 28 * s), (x + 14 * s, y - 28 * s), (x, y - 44 * s)], (70, 150, 70))

def SC(i, P, t, u):
    if i == 0:
        floor(P); mouse(P, 380, FLOOR - 70, 1.1, t, sniff=1.); cheese(P, 780, FLOOR - 50, 1.2)
        P.heart(560, CENTER - 160, 40 * back(seg(u, .5, 1.0)), HOOK); P.text(660, CENTER - 230, "?", 120 * back(seg(u, .8, 1.3)), GLIM)
    elif i == 1:
        floor(P); cheese(P, 230, FLOOR - 50, 1.0)
        mouse(P, 600, FLOOR - 70, 1.1, t, sniff=1.)
        grain(P, 860, FLOOR - 140, 1.2); berry(P, 900, FLOOR - 30, 1.2)
        P.stamp(540, CENTER - 280, "MYTH", seg(u, .25, .7))
    elif i == 2:
        floor(P)
        for j, (x, lab) in enumerate(((220, "grains"), (540, "fruit"), (860, "sweet"))):
            k = back(seg(u, .3 + j * .5, .8 + j * .5))
            if j == 0: grain(P, x, FLOOR - 200, 1.2, k)
            elif j == 1: berry(P, x, FLOOR - 150, 1.6 * k)
            else: P.rrect(x - 60 * k, FLOOR - 220 * k, x + 60 * k, FLOOR - 100, 14, (120, 70, 40))
            P.badge(x, FLOOR - 330, lab, 48, NIGHT, CLOUD, k)
        mouse(P, 540, FLOOR + 140, .9, t)
    elif i == 3:
        floor(P); cheese(P, 780, FLOOR - 50, 1.2)
        for j in range(3):
            q = (u * .7 + j / 3) % 1
            P.line([(700 - q * 220, FLOOR - 140 - math.sin(q * 6 + j) * 30), (680 - q * 220, FLOOR - 170 - math.sin(q * 6 + j) * 30)], (150, 190, 80), 10)
        mouse(P, 300, FLOOR - 70, 1.0, t, f=-1, happy=False)
        P.badge(540, CENTER - 230, "too smelly!", 58, HOOK, CLOUD, back(seg(u, 1.0, 1.5)))
    elif i == 4:
        P.rrect(160, CENTER - 300, 920, CENTER + 220, 30, (250, 245, 235), outline=NIGHT, w=10)
        mouse(P, 400, CENTER + 60, .8, t); cheese(P, 720, CENTER + 80, .8)
        P.badge(540, CENTER - 200, "cartoon myth", 56, HOOK, CLOUD, back(seg(u, .4, .9)))
        P.badge(540, CENTER + 360, "cheese was easy to reach", 50, NIGHT, CLOUD, back(seg(u, 2.0, 2.5)))
    else:
        floor(P); mouse(P, 360, FLOOR - 70, 1.1, t); grain(P, 700, FLOOR - 160, 1.1); berry(P, 860, FLOOR - 40, 1.3)
        P.stamp(620, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
