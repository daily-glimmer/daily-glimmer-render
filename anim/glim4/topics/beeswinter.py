# Thema: Do honeybees sleep through the winter?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6) – Biene aus bees.py
CENTER = 1050
exec(open(os.path.join(HERE, "topics", "bees.py")).read(), globals())
PAL = ((60, 80, 130), (170, 190, 220))
HI = {"sleep", "winter?", "myth!", "awake", "ball.", "shiver", "heat.", "twenty", "seven", "thirty", "five", "honey.", "heater"}
WOW = (1,)
HONEY, WOOD = (240, 170, 40), (190, 140, 90)

def hive(P, x, y, s):
    for j in range(4): P.rrect(x - (160 - j * 10) * s, y - (j * 110) * s - 100 * s, x + (160 - j * 10) * s, y - j * 110 * s, 40 * s, WOOD, outline=(150, 105, 60), w=6 * s)
    P.ell(x, y - 30 * s, 40 * s, 20 * s, NIGHT)

def snowy(P, t, y=CENTER + 330):
    P.rrect(-20, y, W + 20, H + 50, 0, (242, 247, 252))
    for j in range(25): P.circ((j * 131 + t * 25) % W, (j * 197 + t * 70) % 1000 + CENTER - 650, 5 + j % 3, (255, 255, 255))

def cluster(P, x, y, r, t, heat=0.):
    if heat > 0: P.circ(x, y, r * .75, lc((150, 105, 60), (255, 140, 60), heat))
    random.seed(4)
    for j in range(60):
        a = random.random() * 6.28; rr = math.sqrt(random.random()) * r
        bx, by = x + math.cos(a) * rr + math.sin(t * 20 + j) * 3, y + math.sin(a) * rr * .85
        P.ell(bx, by, 22, 15, YEL); P.line([(bx - 6, by - 14), (bx - 6, by + 14)], NIGHT, 5); P.line([(bx + 7, by - 14), (bx + 7, by + 14)], NIGHT, 5)

def SC(i, P, t, u):
    if i == 0:
        snowy(P, t); hive(P, 540, CENTER + 340, 1.2)
        P.text(540, CENTER - 160, "z", 90, CLOUD); P.text(760, CENTER - 300, "?", 150 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        P.rrect(100, CENTER - 360, 980, CENTER + 360, 60, (120, 85, 50))
        for j in range(6): P.rrect(140 + j * 140, CENTER - 330, 220 + j * 140, CENTER + 330, 20, (200, 150, 70))
        cluster(P, 540, CENTER, 260 * eout(seg(u, .2, 1.2)) + 10, t)
        P.stamp(780, CENTER - 280, "MYTH", seg(u, .25, .7))
    elif i == 2:
        bee(P, 540, CENTER, 2.4, t * .05, sting=False)
        for j in range(3): P.arc(540, CENTER, 260 + j * 40 + math.sin(t * 30) * 6, 200, 340, HOOK, 8)
        P.badge(540, CENTER + 300, "shivering = heat", 58, HOOK, CLOUD, back(seg(u, .8, 1.3)))
    elif i == 3:
        P.rrect(100, CENTER - 360, 980, CENTER + 360, 60, (120, 85, 50))
        cluster(P, 540, CENTER, 280, t, heat=eio(seg(u, .3, 2.0)))
        P.badge(540, CENTER - 420, "27 to 35 °C inside", 56, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
    elif i == 4:
        P.rrect(100, CENTER - 360, 980, CENTER + 360, 60, (120, 85, 50))
        for j in range(5): P.rrect(140 + j * 170, CENTER + 180, 260 + j * 170, CENTER + 320, 20, HONEY)
        cluster(P, 540, CENTER - 60, 220, t, heat=.7)
        q = (u * .4) % 1; a = q * 6.28
        bee(P, 540 + math.cos(a) * 300, CENTER - 60 + math.sin(a) * 240, .5, t, sting=False)
        P.badge(540, CENTER + 420, "eating stored honey", 54, NIGHT, CLOUD, back(seg(u, 2.5, 3.0)))
    else:
        snowy(P, t); hive(P, 380, CENTER + 340, 1.1)
        P.circ(380, CENTER + 50, 70, (255, 150, 60))
        P.stamp(720, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
