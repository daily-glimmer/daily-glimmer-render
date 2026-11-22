# Thema: Do dogs sweat through their tongues?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6)
# Quellen: American Kennel Club "Do Dogs Sweat?" (merokrine Schweißdrüsen in den Pfotenballen, Kühlung v. a. durch Hecheln),
# PetMD / Live Science (Zunge ohne Schweißdrüsen; Verdunstung beim Hecheln kühlt).
exec(open(os.path.join(HERE, "topics", "dogs.py")).read(), globals())      # dog(), grass()
exec(open(os.path.join(HERE, "topics", "dognose.py")).read(), globals())   # doghead()
CENTER = 1050
PAL = ((250, 190, 110), (250, 225, 170))
HI = {"sweat", "tongues?", "myth!", "no", "glands", "paw", "pads,", "panting.", "evaporates", "cools", "paws,", "tongue!"}
WOW = (1,)
SUN = (255, 205, 70)

def sun(P, x, y, r, t):
    for k in range(12):
        a = k * math.pi / 6 + t * .3
        P.line([(x + math.cos(a) * (r + 15), y + math.sin(a) * (r + 15)), (x + math.cos(a) * (r + 55), y + math.sin(a) * (r + 55))], SUN, 12)
    P.circ(x, y, r, SUN)

def paw(P, x, y, s, wet=0., t=0.):
    P.ell(x, y + 40 * s, 90 * s, 70 * s, (90, 70, 70))
    for dx, dy in ((-80, -50), (-28, -85), (28, -85), (80, -50)): P.ell(x + dx * s, y + dy * s, 32 * s, 40 * s, (90, 70, 70))
    if wet > 0:
        for j in range(5):
            q = (t * .6 + j / 5) % 1
            P.ell(x + (j - 2) * 40 * s, y + 40 * s - q * 30 * s, 10 * s * wet, 15 * s * wet, (140, 200, 250))

def pant(P, x, y, s, t, fast=9):
    doghead(P, x, y, s, t, lick=0., shine=True)
    P.ell(x + 8 * s, y + 160 * s + math.sin(t * fast) * 8 * s, 30 * s, 55 * s, (240, 120, 130))
    P.line([(x + 8 * s, y + 125 * s), (x + 8 * s, y + 190 * s + math.sin(t * fast) * 8 * s)], (210, 90, 105), 4 * s)

def SC(i, P, t, u):
    if i == 0:
        sun(P, 860, CENTER - 280, 80, t); grass(P, CENTER + 320, (110, 170, 80))
        pant(P, 470, CENTER + 20, 1.2, t)
        P.text(800, CENTER - 60, "?", 160 * back(seg(u, .5, 1.0)), (60, 50, 90))
    elif i == 1:
        pant(P, 470, CENTER + 20, 1.2, t)
        P.cross(480, CENTER + 260, 90, k=back(seg(u, 1.2, 1.6)))
        P.stamp(560, CENTER - 300, "MYTH", seg(u, .25, .7), rot=-6)
        P.badge(540, CENTER + 480, "no sweat glands here", 56, NIGHT, CLOUD, back(seg(u, 1.6, 2.1)))
    elif i == 2:
        paw(P, 540, CENTER, 1.8, wet=eio(seg(u, .5, 1.5)), t=t)
        for j in range(3): paw(P, 220 + j * 320, CENTER + 420 - (j % 2) * 40, .5, wet=.6, t=t)
        P.badge(540, CENTER - 320, "sweaty paw pads", 60, GLIM, NIGHT, back(seg(u, .8, 1.3)))
    elif i == 3:
        sun(P, 860, CENTER - 280, 80, t); grass(P, CENTER + 320, (110, 170, 80))
        dog(P, 560, CENTER + 120, 1.3, t)
        P.badge(540, CENTER + 450, "panting = main cooling", 54, NIGHT, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 4:
        pant(P, 470, CENTER + 60, 1.3, t)
        waves(P, 480, CENTER + 260, t, (140, 200, 250), n=3, r0=60, dr=60, a0=200, a1=340, speed=2.)
        P.badge(540, CENTER - 300, "evaporation cools", 58, NIGHT, CLOUD, back(seg(u, 1.0, 1.5)))
    else:
        grass(P, CENTER + 320, (110, 170, 80)); dog(P, 480, CENTER + 120, 1.1, t)
        P.stamp(780, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
