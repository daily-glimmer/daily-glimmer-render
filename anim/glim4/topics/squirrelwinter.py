# Thema: Do squirrels sleep through the whole winter?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6) – Figuren aus squirrels.py
CENTER = 1050
exec(open(os.path.join(HERE, "topics", "squirrels.py")).read(), globals())
PAL = ((90, 120, 170), (190, 210, 235))
HI = {"sleep", "winter?", "myth!", "never", "hibernate.", "active", "buried", "thousand", "memory", "smell", "nests", "ground", "snow?"}
WOW = (1,)
SNOW = (242, 247, 252)

def snowground(P, t, y=CENTER + 240):
    P.rrect(-20, y, W + 20, H + 50, 0, SNOW); P.ell(300, y, 400, 40, SNOW); P.ell(800, y + 10, 360, 36, SNOW)
    for j in range(25): P.circ((j * 131 + t * 25) % W, (j * 197 + t * 70) % 1000 + CENTER - 650, 5 + j % 3, (255, 255, 255))

def tree(P, x, y=CENTER + 250):
    P.rrect(x - 60, CENTER - 480, x + 60, y + 10, 30, (110, 80, 55))
    P.ell(x, CENTER - 200, 34, 46, (60, 40, 30))

def zz(P, x, y, t):
    for k in range(3):
        q = (t * .45 + k / 3) % 1; P.text(x + q * 80, y - q * 200, "z", 40 + 40 * q, CLOUD)

def SC(i, P, t, u):
    if i == 0:
        snowground(P, t); tree(P, 860)
        squirrel(P, 460, CENTER + 220, 1.3, t)
        zz(P, 380, CENTER - 60, t)
        P.text(700, CENTER - 230, "?", 150 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        snowground(P, t); tree(P, 860)
        squirrel(P, 480 + math.sin(t * 3) * 40, CENTER + 220, 1.3, t, sniff=1.)
        P.cross(330, CENTER - 120, 70, k=back(seg(u, .9, 1.4))); P.text(330, CENTER - 120, "z", 90, CLOUD)
        P.stamp(760, CENTER - 280, "MYTH", seg(u, .25, .7))
    elif i == 2:
        snowground(P, t)
        k = eout(seg(u, .6, 2.2))
        squirrel(P, 480, CENTER + 220, 1.3, t, dig=1.)
        P.ell(360, CENTER + 260, 90, 30, (120, 85, 55))
        acorn(P, 360, CENTER + 260 - 140 * k, 1.1)
        P.badge(540, CENTER + 480, "winter snack!", 58, NIGHT, GLIM, back(seg(u, 2.0, 2.5)))
    elif i == 3:
        snowground(P, t)
        n = int(30 * eio(seg(u, .3, 3.5)))
        for j in range(n): acorn(P, 120 + (j * 83) % 840, CENTER + 300 + (j * 53) % 220, .55)
        squirrel(P, 540, CENTER + 180, 1.1, t, sniff=1.)
        P.badge(540, CENTER - 260, "thousands of hiding spots", 52, NIGHT, CLOUD, back(seg(u, .6, 1.1)))
    elif i == 4:
        snowground(P, t); tree(P, 540)
        P.rrect(380, CENTER - 330, 700, CENTER - 60, 120, (110, 80, 55))
        P.ell(540, CENTER - 190, 135, 100, (60, 40, 30))
        for dx in (-55, 50):
            P.circ(540 + dx, CENTER - 185, 55, FUR); P.ell(540 + dx + 10, CENTER - 245, 12, 20, FUR)
            P.arc(540 + dx - 18, CENTER - 195, 9, 200, 340, NIGHT, 4); P.arc(540 + dx + 14, CENTER - 195, 9, 200, 340, NIGHT, 4)
        P.badge(540, CENTER + 60, "cuddle for warmth", 56, HOOK, CLOUD, back(seg(u, .8, 1.3)))
    else:
        snowground(P, t); tree(P, 860)
        squirrel(P, 440, CENTER + 220, 1.2, t)
        acorn(P, 330, CENTER + 80, 1.0)
        P.stamp(620, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
