# Thema: Why do we yawn?
CENTER = 1050
def dk(c, k): return tuple(int(v * k) for v in c)
PAL = ((250, 200, 160), (200, 160, 220))
HI = {"yawn?", "oxygen,", "not", "cool", "air", "blood,", "brain.", "alert", "focused,", "contagious,", "friends", "family.", "yawn!", "honest:"}
WOW = (2, 4)
SKIN = [(255, 214, 170), (205, 150, 105), (150, 100, 70), (240, 190, 150)]

def head(P, x, y, s, t, yawn=0., col=SKIN[0], hair=(90, 60, 40), eyes=1.):
    P.circ(x, y, 150 * s, col, outline=dk(col, .8) if 'dk' in globals() else None, w=5 * s)
    P.ell(x, y - 120 * s, 150 * s, 60 * s, hair)
    P.circ(x - 150 * s, y, 26 * s, col); P.circ(x + 150 * s, y, 26 * s, col)
    e = max(.08, eyes * (1 - yawn * .9))
    for f in (-1, 1): P.ell(x + f * 55 * s, y - 25 * s, 16 * s, 18 * s * e, NIGHT)
    if yawn > .05:
        P.ell(x, y + 70 * s, 45 * s * (.6 + yawn * .5), 60 * s * yawn, (120, 40, 50)); P.ell(x, y + 70 * s + 35 * s * yawn, 24 * s * yawn, 15 * s * yawn, (230, 110, 120))
    else: P.arc(x, y + 50 * s, 40 * s, 30, 150, NIGHT, 7 * s)

def ybrain(P, x, y, s, temp=0.):
    col = lc((255, 140, 150), (140, 200, 255), temp)
    for dx, dy in ((-60, -20), (0, -50), (60, -20), (-40, 30), (40, 30)): P.circ(x + dx * s, y + dy * s, 60 * s, col, outline=dk(col, .8), w=5 * s)

def yawn_of(u, a=.5, b=2.2): q = seg(u, a, b); return math.sin(q * math.pi) ** .7

def SC(i, P, t, u):
    if i == 0:
        head(P, 540, CENTER, 1.6, t, yawn_of(u, .2, 2.0))
        P.text(830, CENTER - 300, "?", 140 * back(seg(u, .4, .9)), HOOK)
    elif i == 1:
        head(P, 400, CENTER + 20, 1.1, t, yawn_of(u, .3, 2.0))
        P.rrect(640, CENTER - 160, 840, CENTER + 200, 40, (120, 190, 240))
        P.text(740, CENTER + 20, "O2", 90, CLOUD)
        P.cross(740, CENTER + 20, 120, k=back(seg(u, 3.0, 3.5)))
        P.badge(540, CENTER + 330, "more oxygen?", 56, NIGHT, GLIM, back(seg(u, .9, 1.4)))
    elif i == 2:
        y = yawn_of(u, .3, 3.2)
        head(P, 540, CENTER + 100, 1.5, t, y)
        for k in range(5):
            q = (u * .9 + k / 5) % 1
            P.line([(200 + q * 250, CENTER + 50 + k * 30), (240 + q * 250, CENTER + 50 + k * 30)], (140, 200, 255), 10 * (1 - q) + 2)
        ybrain(P, 540, CENTER - 170, .9, seg(u, 1.5, 4.0))
    elif i == 3:
        head(P, 540, CENTER + 40, 1.5, t, 0, eyes=1.25)
        for k in range(6):
            a = k / 6 * 6.28 + t; P.line([(540 + math.cos(a) * 260, CENTER + 40 + math.sin(a) * 260), (540 + math.cos(a) * 310, CENTER + 40 + math.sin(a) * 310)], GLIM, 12)
        P.badge(540, CENTER + 380, "more alert", 62, HOPE, CLOUD, back(seg(u, .6, 1.1)))
    elif i == 4:
        for j in range(4):
            x = 200 + j * 230
            head(P, x, CENTER + 60 + (j % 2) * 60, .7, t, yawn_of(u, .4 + j * .6, 1.6 + j * .6), col=SKIN[j], hair=((90, 60, 40), (30, 25, 25), (20, 20, 20), (200, 150, 70))[j])
        for j in range(3): P.heart(315 + j * 230, CENTER - 140, 30 * back(seg(u, 1.0 + j * .5, 1.4 + j * .5)), HOOK)
    else:
        head(P, 540, CENTER - 20, 1.2, t, yawn_of(u, 1.0, 3.0))
        P.badge(540, CENTER + 260, "yaaawn...", 58, NIGHT, GLIM, back(seg(u, 1.2, 1.7)))
