# Thema: Is a spider an insect?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6) – Spinne aus spiderweb.py
CENTER = 1050
exec(open(os.path.join(HERE, "topics", "spiderweb.py")).read(), globals())
PAL = ((90, 130, 90), (180, 200, 150))
HI = {"insect?", "myth!", "arachnids,", "six", "eight.", "three", "two.", "antennae", "wings,", "scorpions", "ticks", "insects?"}
WOW = (1,)
ANT = (60, 40, 35)

def ant(P, x, y, s, t, hl=0.):
    for j, dx in enumerate((-50, 0, 50)):
        for f in (-1, 1):
            ph = math.sin(t * 8 + j + f) * 10 * s
            P.line([(x + dx * s, y), (x + dx * s + ph, y + f * 60 * s), (x + dx * s + 20 * s + ph, y + f * 100 * s)], ANT, 7 * s)
    cols = [ANT, ANT, ANT] if hl <= 0 else [lc(ANT, GLIM, hl), lc(ANT, HOOK, hl), lc(ANT, HOPE, hl)]
    P.ell(x - 110 * s, y, 70 * s, 50 * s, cols[2]); P.ell(x, y, 45 * s, 32 * s, cols[1]); P.circ(x + 80 * s, y, 38 * s, cols[0])
    P.line([(x + 100 * s, y - 25 * s), (x + 160 * s, y - 90 * s)], ANT, 5 * s); P.line([(x + 100 * s, y + 25 * s), (x + 160 * s, y + 90 * s)], ANT, 5 * s)

def leaf(P, y=CENTER + 300): P.poly([(0, y), (W, y - 20), (W, H), (0, H)], (70, 120, 60))

def SC(i, P, t, u):
    if i == 0:
        leaf(P); spider(P, 330, CENTER + 60, 1.4, t, walk=.5); ant(P, 760, CENTER + 120, 1.1, t)
        P.text(540, CENTER - 250, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        leaf(P); spider(P, 540, CENTER + 60, 1.8, t, walk=.3)
        P.stamp(780, CENTER - 280, "MYTH", seg(u, .25, .7))
        P.badge(540, CENTER + 480, "arachnid", 64, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
    elif i == 2:
        leaf(P); ant(P, 300, CENTER + 60, 1.2, t); spider(P, 780, CENTER + 20, 1.2, t, walk=.5)
        P.badge(300, CENTER - 200, "6 legs", 60, NIGHT, CLOUD, back(seg(u, .4, .9)))
        P.badge(780, CENTER - 200, "8 legs", 60, HOOK, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 3:
        leaf(P); ant(P, 300, CENTER + 60, 1.2, t, hl=eio(seg(u, .3, 1.0)))
        spider(P, 780, CENTER + 20, 1.2, t, walk=0.)
        P.badge(300, CENTER - 200, "3 parts", 60, NIGHT, CLOUD, back(seg(u, .4, .9)))
        P.badge(780, CENTER - 200, "2 parts", 60, HOOK, CLOUD, back(seg(u, 1.6, 2.1)))
    elif i == 4:
        leaf(P); spider(P, 540, CENTER + 60, 1.6, t, walk=.3)
        P.cross(300, CENTER - 180, 50, k=back(seg(u, .6, 1.0))); P.badge(300, CENTER - 300, "antennae", 46, NIGHT, CLOUD, back(seg(u, .3, .7)))
        P.cross(780, CENTER - 180, 50, k=back(seg(u, 1.6, 2.0))); P.badge(780, CENTER - 300, "wings", 46, NIGHT, CLOUD, back(seg(u, 1.3, 1.7)))
    else:
        leaf(P); spider(P, 330, CENTER + 60, 1.2, t, walk=.5)
        k = back(seg(u, 1.0, 1.5)); x, y = 760, CENTER + 160      # Skorpion
        P.ell(x, y, 90 * k, 40 * k, (150, 100, 60))
        P.line([(x - 80 * k, y), (x - 150 * k, y - 80 * k), (x - 100 * k, y - 150 * k)], (150, 100, 60), 22 * k)
        for f in (-1, 1): P.line([(x + 80 * k, y), (x + 150 * k, y + f * 40 * k)], (150, 100, 60), 14 * k); P.circ(x + 160 * k, y + f * 45 * k, 18 * k, (150, 100, 60))
        P.stamp(720, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
