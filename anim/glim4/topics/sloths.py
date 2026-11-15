# Thema: Why are sloths so slow?
CENTER = 1050
FUR, FUR2, MASK, FACE = (150, 125, 95), (120, 98, 72), (70, 50, 35), (225, 205, 170)
PAL = ((20, 70, 50), (90, 150, 80))
HI = {"slow?", "leaves,", "energy.", "weeks,", "stomach", "muscle", "temperature", "hide:", "algae", "green!", "once", "week!"}
WOW = (2, 4)

def branch(P, y, x0=-50, x1=W + 50):
    P.line([(x0, y), (x1, y + 30)], (95, 65, 40), 34)
    for x in (180, 520, 880):
        P.ell(x, y - 30, 46, 22, (60, 140, 70)); P.ell(x + 40, y - 46, 38, 18, (80, 165, 85))

def sloth(P, x, y, s, t, col=FUR, swing=1., sleepy=0.):
    by = y - 190 * s; sw = math.sin(t * .8) * 18 * s * swing
    bx = x + sw
    for dx in (-80, 80):     # Arme/Beine zum Ast
        P.line([(bx + dx * s, y + 10 * s), (x + dx * 1.2 * s, by)], lc(col, (0, 0, 0), .22), 34 * s)
        for c in (-12, 0, 12): P.arc(x + dx * 1.2 * s + c * s, by + 8 * s, 14 * s, 180, 360, (60, 45, 30), 5 * s)
    P.ell(bx, y + 30 * s, 120 * s, 90 * s, col)
    hx, hy = bx - 120 * s, y + 40 * s
    P.circ(hx, hy, 62 * s, col); P.ell(hx, hy + 6 * s, 50 * s, 40 * s, FACE)
    for ex in (-20, 20):
        P.ell(hx + ex * s, hy, 18 * s, 11 * s, MASK)
        if sleepy > .5: P.arc(hx + ex * s, hy - 2 * s, 7 * s, 20, 160, CLOUD, 3 * s)
        else: P.circ(hx + ex * s, hy - 1 * s, 5 * s, (20, 20, 20))
    P.circ(hx, hy + 18 * s, 7 * s, (40, 30, 25)); P.arc(hx, hy + 22 * s, 16 * s, 30, 150, (60, 40, 30), 4 * s)

def leaf(P, x, y, s, col=(80, 170, 80)):
    P.ell(x, y, 34 * s, 16 * s, col); P.line([(x - 30 * s, y), (x + 30 * s, y)], lc(col, (0, 0, 0), .33), 3 * s)

def SC(i, P, t, u):
    if i == 0:
        branch(P, CENTER - 260); sloth(P, 560, CENTER - 40, 1.25, t)
        P.text(800, CENTER + 260, "?", 140 * back(seg(u, .4, .9)), GLIM)
    elif i == 1:
        branch(P, CENTER - 260); sloth(P, 600, CENTER - 40, 1.1, t)
        for k in range(4):
            q = seg(u, .3 + k * .25, 1.0 + k * .25); leaf(P, lerp(200 + k * 60, 400, eio(q)), lerp(CENTER + 400, CENTER + 10, eio(q)), 1.2 * (1 - .7 * q))
        P.rrect(300, CENTER + 330, 780, CENTER + 400, 30, (40, 50, 60))
        P.rrect(306, CENTER + 336, 306 + 70 * back(seg(u, 1.2, 1.8)), CENTER + 394, 26, HOOK)
        P.badge(540, CENTER + 480, "low energy", 56, NIGHT, GLIM, back(seg(u, 1.5, 2.0)))
    elif i == 2:
        cx, cy = 540, CENTER - 20
        for k, (dx, dy, r) in enumerate(((-150, -60, 120), (40, -110, 105), (150, 60, 115), (-30, 120, 110))):
            P.circ(cx + dx, cy + dy, r * back(seg(u, .2 + k * .2, .6 + k * .2)), lc((240, 160, 150), (200, 110, 110), k / 4), outline=(150, 70, 70), w=6)
        for k in range(5):
            q = ((t * .15) + k / 5) % 1; a = q * 6.28
            leaf(P, cx + math.cos(a) * 130, cy + math.sin(a) * 110, .9)
        P.badge(540, CENTER + 330, "many-chambered stomach", 52, NIGHT, GLIM, back(seg(u, .6, 1.1)))
        P.badge(540, CENTER + 440, "up to weeks per meal", 52, HOOK, CLOUD, back(seg(u, 2.0, 2.5)))
    elif i == 3:
        branch(P, CENTER - 300); sloth(P, 330, CENTER - 80, .8, t, swing=.4)
        for k, (lab, v, col) in enumerate((("sloth", .55, HOPE), ("others", 1., (120, 140, 170)))):
            x = 640 + k * 190; h = 360 * v * eout(seg(u, .4 + k * .3, 1.4 + k * .3))
            P.rrect(x - 60, CENTER + 260 - h, x + 60, CENTER + 260, 16, col)
            P.text(x, CENTER + 310, lab, 44, CLOUD)
        P.text(735, CENTER - 160, "muscle", 58, GLIM)
        th = .5 + .5 * math.sin(t * 1.3)
        P.rrect(140, CENTER + 120, 190, CENTER + 330, 25, CLOUD); P.circ(165, CENTER + 345, 40, HOOK)
        P.rrect(152, CENTER + 330 - 160 * th, 178, CENTER + 340, 13, HOOK)
    elif i == 4:
        branch(P, CENTER - 260)
        g = eio(seg(u, .5, 3.0)); col = lc(FUR, (110, 150, 90), g)
        sloth(P, 560, CENTER - 40, 1.25, t, col=col)
        random.seed(5)
        for k in range(26):
            px, py = 440 + random.random() * 240, CENTER - 20 + random.random() * 140
            P.circ(px, py, 7 * g, (70, 170, 70))
        P.badge(540, CENTER + 330, "algae in the fur", 58, HOPE, CLOUD, back(seg(u, 1.0, 1.5)))
    else:
        P.rrect(470, CENTER - 600, 610, CENTER + 420, 30, (95, 65, 40))
        y = lerp(CENTER - 320, CENTER + 120, eio(seg(u, .2, 4.0)))
        P.ell(540, y, 90, 120, FUR); P.circ(540, y + 120, 58, FUR); P.ell(540, y + 126, 46, 36, FACE)
        for ex in (-18, 18): P.ell(540 + ex, y + 120, 16, 10, MASK); P.circ(540 + ex, y + 119, 4, (20, 20, 20))
        P.arc(540, y + 138, 14, 30, 150, (60, 40, 30), 4)
        P.ell(540, CENTER + 470, 600, 60, (100, 130, 60))
        P.badge(540, CENTER - 420, "about 1x per week", 58, NIGHT, GLIM, back(seg(u, 1.2, 1.7)))
