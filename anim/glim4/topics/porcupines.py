# Thema: Can porcupines shoot their quills?  (Mythos-Format)
CENTER = 1050
BODY, QUILL, TIP = (110, 85, 65), (235, 225, 200), (60, 45, 35)
PAL = ((40, 45, 35), (120, 140, 90))
HI = {"shoot", "quills?", "inch!", "thirty", "thousand", "barbs", "hooks.", "loosely,", "rattles", "tail", "hugging", "hug?"}
WOW = (1,)

def forest(P, y=CENTER + 250):
    P.poly([(0, y), (W, y - 20), (W, H), (0, H)], (90, 120, 60))
    for x in (110, 960): P.rrect(x - 40, CENTER - 520, x + 40, y, 20, (90, 65, 45))

def porcupine(P, x, y, s, t, raised=0., tail_swing=0., flip=1):
    f = flip; n = 34
    for k in range(n):                                   # Stacheln als Fächer
        a = math.pi * (1.05 + .9 * k / (n - 1)); L = (90 + 60 * raised + (k % 3) * 18) * s
        jit = math.sin(t * 30 + k) * 4 * s * raised
        bx, by = x + math.cos(a) * 110 * s, y + math.sin(a) * 70 * s
        ex, ey = bx + math.cos(a) * L + jit, by + math.sin(a) * L
        P.line([(bx, by), (ex, ey)], QUILL, 9 * s); P.line([lerp_pt((bx, by), (ex, ey), .8), (ex, ey)], TIP, 9 * s)
    ta = math.radians(10 + tail_swing * 70)
    P.ell(x + f * 140 * s + math.cos(ta) * 30 * s * f, y + 20 * s - math.sin(ta) * 40 * s, 60 * s, 34 * s, BODY)
    P.ell(x, y, 150 * s, 85 * s, BODY)
    P.ell(x - f * 140 * s, y + 20 * s, 60 * s, 48 * s, (140, 110, 85))
    P.circ(x - f * 190 * s, y + 25 * s, 12 * s, NIGHT)
    P.circ(x - f * 150 * s, y + 5 * s, 9 * s, NIGHT); P.circ(x - f * 147 * s, y + 2 * s, 3 * s, (255, 255, 255))
    for dx in (-80, 70): P.ell(x + dx * s, y + 80 * s, 26 * s, 16 * s, (80, 60, 45))

def lerp_pt(a, b, k): return (lerp(a[0], b[0], k), lerp(a[1], b[1], k))

def quill_zoom(P, x, y, L, t):
    P.line([(x - L / 2, y), (x + L / 2, y)], QUILL, 30); P.line([(x + L * .3, y), (x + L / 2, y)], TIP, 30)
    for k in range(7):
        bx = x + L * .3 + k * 22; P.line([(bx, y - 14), (bx - 30, y - 34)], TIP, 7); P.line([(bx, y + 14), (bx - 30, y + 34)], TIP, 7)

def SC(i, P, t, u):
    if i == 0:
        forest(P); porcupine(P, 560, CENTER + 150, 1.15, t, raised=.5)
        for k in range(4):
            q = (u * .8 + k / 4) % 1
            if u < 3: P.line([(620 + q * 400, CENTER - 60 - k * 40), (690 + q * 400, CENTER - 60 - k * 40)], QUILL, 10)
        P.text(800, CENTER - 300, "?", 140 * back(seg(u, .4, .9)), GLIM)
    elif i == 1:
        forest(P); porcupine(P, 560, CENTER + 150, 1.15, t, raised=.3)
        P.stamp(540, CENTER - 330, "MYTH", seg(u, .25, .7))
    elif i == 2:
        forest(P); porcupine(P, 300, CENTER + 230, .7, t)
        P.circ(700, CENTER - 60, 260, (30, 40, 30), outline=GLIM, w=10)
        quill_zoom(P, 700, CENTER - 60, 380, t)
        P.badge(540, CENTER - 400, "~30,000 quills", 62, NIGHT, GLIM, back(seg(u, .4, .9)))
        P.badge(700, CENTER + 260, "barbs!", 56, HOOK, CLOUD, back(seg(u, 2.2, 2.7)))
    elif i == 3:
        forest(P); porcupine(P, 520, CENTER + 150, 1.1, t, raised=1)
        k = eout(seg(u, .6, 1.6))
        P.circ(lerp(1000, 820, k), CENTER + 40, 50, (230, 120, 80))           # neugierige Pfote/Nase
        if k > .95:
            for j in range(3): P.line([(800 - j * 20, CENTER + 20 + j * 25), (860 - j * 20, CENTER - 20 + j * 25)], QUILL, 9)
        P.badge(540, CENTER - 360, "pop off on touch", 58, HOOK, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 4:
        forest(P)
        rattle = u < 2.0
        porcupine(P, 520, CENTER + 150, 1.1, t, raised=1, tail_swing=0 if rattle else (math.sin(u * 6) + 1) / 2)
        if rattle:
            for j in range(3):
                q = (t * 2 + j / 3) % 1; P.arc(520, CENTER + 60, 220 + q * 200, 200, 340, lc(GLIM, (0, 0, 0), q), 8)
        P.badge(540, CENTER - 360, "1. rattle   2. tail swing", 54, NIGHT, GLIM, 1)
    else:
        forest(P); porcupine(P, 540, CENTER + 150, 1.1, t, raised=.6)
        P.heart(540, CENTER - 160, 70, (255, 120, 150)); P.cross(540, CENTER - 160, 90, k=back(seg(u, .9, 1.4)))
        P.stamp(540, CENTER - 400, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
