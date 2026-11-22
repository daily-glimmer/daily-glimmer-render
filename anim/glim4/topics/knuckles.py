# Thema: Does cracking your knuckles really cause arthritis?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6)
# Quellen: Kawchuk et al. 2015, PLOS ONE / University of Alberta (MRI-Video: Knacken = Bildung einer Gasblase);
# Unger, Arthritis & Rheumatism 1998 (jahrzehntelang nur linke Hand geknackt, keine Arthritis; Ig-Nobelpreis 2009).
CENTER = 1050
SKIN, SKIN2, BONE, FLUID = (240, 190, 150), (215, 160, 125), (245, 240, 225), (150, 200, 240)
PAL = ((120, 90, 160), (200, 170, 220))
HI = {"cracking", "arthritis?", "myth!", "no", "link", "pop", "gas", "bubble", "mri", "2015", "left", "decades,", "neither", "gentle!"}
WOW = (1,)

def hand(P, x, y, s, t, bend=0., flip=1):
    """Hand von vorn, Finger nach oben; bend 0..1 = Finger einknicken."""
    P.rrect(x - 120 * s, y - 40 * s, x + 120 * s, y + 160 * s, 50 * s, SKIN)
    for j in range(4):
        fx = x + (-90 + j * 60) * s; L = (150 - abs(j - 1.5) * 25) * s * (1 - .55 * bend)
        P.rrect(fx - 26 * s, y - 40 * s - L, fx + 26 * s, y, 24 * s, SKIN)
        P.line([(fx - 14 * s, y - 40 * s - L * .45), (fx + 14 * s, y - 40 * s - L * .45)], SKIN2, 5 * s)
    tx = x - flip * 125 * s
    P.ell(tx - flip * 25 * s, y + 40 * s, 38 * s, 75 * s, SKIN)

def pop(P, x, y, k):
    if k <= .02: return
    for a in range(8):
        ang = a * math.pi / 4
        P.line([(x + math.cos(ang) * 30 * k, y + math.sin(ang) * 30 * k), (x + math.cos(ang) * 70 * k, y + math.sin(ang) * 70 * k)], GLIM, 10)

def joint(P, x, y, b):
    P.rrect(x - 380, y - 70, x - 30, y + 70, 60, BONE); P.rrect(x + 30, y - 70, x + 380, y + 70, 60, BONE)
    P.ell(x, y, 120, 110, None, outline=(180, 140, 200), w=8)
    P.ell(x, y, 60, 90, FLUID)
    if b > .02: P.circ(x, y, 50 * b, CLOUD, glow=(80, 80, 90))

def SC(i, P, t, u):
    if i == 0:
        hand(P, 540, CENTER + 120, 1.3, t, bend=.4 + .3 * math.sin(t * 3))
        pop(P, 470, CENTER - 90, (u * 1.5) % 1)
        P.text(800, CENTER - 230, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        hand(P, 540, CENTER + 120, 1.2, t, bend=.5)
        P.stamp(540, CENTER - 230, "MYTH", seg(u, .25, .7), rot=-6)
        P.badge(540, CENTER + 480, "no link found", 60, NIGHT, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 2:
        b = eout(seg(u, .8, 1.4))
        joint(P, 540, CENTER + 40, b)
        pop(P, 540, CENTER - 140, seg(u, 1.0, 1.5) * (1 - seg(u, 2.0, 2.6)))
        P.badge(540, CENTER + 330, "gas bubble", 60, NIGHT, GLIM, back(seg(u, 1.5, 2.0)))
    elif i == 3:
        P.circ(540, CENTER + 40, 330, (210, 215, 225)); P.circ(540, CENTER + 40, 210, (60, 70, 90))
        hand(P, 540, CENTER + 110, .6, t, bend=.2)
        k = seg(u, .8, 1.4)
        if k > 0: P.circ(520, CENTER - 20, 22 * eout(k), CLOUD, glow=(120, 120, 140))
        P.badge(540, CENTER + 470, "MRI video, 2015", 58, NIGHT, CLOUD, back(seg(u, .5, 1.0)))
    elif i == 4:
        hand(P, 300, CENTER + 120, .9, t, bend=.5 + .3 * math.sin(t * 4), flip=-1)
        hand(P, 780, CENTER + 120, .9, t)
        pop(P, 260, CENTER - 40, (u * 1.4) % 1)
        P.badge(300, CENTER - 160, "cracked", 52, HOOK, CLOUD, back(seg(u, .4, .9)))
        P.badge(780, CENTER - 160, "never", 52, NIGHT, CLOUD, back(seg(u, .8, 1.3)))
        P.badge(540, CENTER + 420, "decades later: both fine", 52, HOPE, CLOUD, back(seg(u, 2.4, 2.9)))
    else:
        hand(P, 380, CENTER + 140, 1.0, t, bend=.3 + .2 * math.sin(t * 2))
        P.stamp(780, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
