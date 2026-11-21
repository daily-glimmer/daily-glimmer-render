# Thema: Is a koala a bear?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6) – Koala/Baum aus koalas.py
CENTER = 1050
exec(open(os.path.join(HERE, "topics", "koalas.py")).read(), globals())
PAL = ((200, 230, 210), (160, 205, 180))
HI = {"bear?", "myth!", "marsupial,", "pouch", "joey,", "jelly", "bean.", "six", "months,", "back.", "bears!"}
WOW = (1, 3)

def joey(P, x, y, s):
    P.ell(x, y, 40 * s, 30 * s, (240, 170, 170)); P.circ(x + 30 * s, y - 15 * s, 18 * s, (240, 170, 170))

def bean(P, x, y, s, col=(240, 90, 120)): P.ell(x, y, 45 * s, 28 * s, col); P.ell(x - 12 * s, y - 8 * s, 14 * s, 6 * s, lc(col, (255, 255, 255), .5))

def SC(i, P, t, u):
    if i == 0:
        tree(P, 300); koala(P, 340, CENTER + 60, 1.1, t, sleep=0.)
        P.badge(780, CENTER - 200, "bear?", 70, NIGHT, GLIM, back(seg(u, .5, 1.0)))
    elif i == 1:
        tree(P, 300); koala(P, 340, CENTER + 60, 1.1, t, sleep=0.)
        P.stamp(780, CENTER - 230, "MYTH", seg(u, .25, .7))
        P.badge(760, CENTER + 200, "marsupial", 60, HOPE, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 2:
        koala(P, 540, CENTER + 20, 1.5, t, sleep=0.)
        k = back(seg(u, .5, 1.1))
        P.ell(540, CENTER + 200, 110 * k, 70 * k, (200, 205, 215), outline=FUR2, w=6)
        if k > .5: joey(P, 530, CENTER + 190, 1.2)
        P.badge(540, CENTER + 460, "pouch", 60, NIGHT, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 3:
        k = back(seg(u, .3, .8))
        P.circ(540, CENTER, 300, (240, 240, 235))
        joey(P, 400, CENTER, 2.2 * k); bean(P, 720, CENTER, 2.2 * back(seg(u, 1.0, 1.5)))
        P.text(560, CENTER, "=", 100 * back(seg(u, 1.5, 2.0)), GLIM)
        P.badge(540, CENTER + 380, "jelly bean size", 58, NIGHT, GLIM, back(seg(u, 2.0, 2.5)))
    elif i == 4:
        tree(P, 300); koala(P, 340, CENTER + 80, 1.1, t, sleep=0.)
        koala(P, 340, CENTER - 110, .45, t, sleep=0.)
        P.badge(760, CENTER - 160, "6 months", 58, NIGHT, CLOUD, back(seg(u, .5, 1.0)))
        P.badge(760, CENTER + 220, "piggyback!", 58, HOOK, CLOUD, back(seg(u, 2.2, 2.7)))
    else:
        tree(P, 300); koala(P, 340, CENTER + 60, 1.1, t, sleep=0.)
        P.stamp(760, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
