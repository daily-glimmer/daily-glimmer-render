# Thema: Can elephants jump?  (Mythos-Format, NO in Satz 2 (Stempel TRUE: they can't), FACT in Satz 6) – Elefant aus elephants.py
CENTER = 1050
exec(open(os.path.join(HERE, "topics", "elephants.py")).read(), globals())
PAL = ((200, 140, 80), (240, 200, 140))
HI = {"jump?", "no!", "can't", "jump", "one", "foot", "ground.", "five", "thousand", "kilograms,", "pillar-like", "weight,", "never!"}
WOW = (1,)
GROUND = CENTER + 250

def hippo(P, x, y, s, t, air=0.):
    y -= air
    for dx in (-80, 80): P.rrect(x + dx * s - 25 * s, y + 30 * s, x + dx * s + 25 * s, y + 110 * s, 12 * s, (130, 110, 140))
    P.ell(x, y, 150 * s, 85 * s, (150, 130, 160)); P.ell(x + 150 * s, y - 20 * s, 80 * s, 60 * s, (150, 130, 160))
    P.circ(x + 130 * s, y - 70 * s, 10 * s, NIGHT); P.circ(x + 190 * s, y - 15 * s, 8 * s, (100, 80, 110))

def SC(i, P, t, u):
    if i == 0:
        savanna(P); elephant(P, 560, CENTER + 50, 1.1, t, trunk="up")
        P.text(820, CENTER - 280, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        savanna(P); elephant(P, 560, CENTER + 50, 1.1, t)
        P.cross(560, CENTER - 230, 90, k=back(seg(u, .4, .9)))
        P.stamp(560, CENTER + 470, "TRUE", seg(u, .25, .7), col=HOPE, rot=-6)
        P.badge(560, CENTER - 380, "no jumping", 56, NIGHT, CLOUD, back(seg(u, 1.0, 1.5)))
    elif i == 2:
        savanna(P)
        x = lerp(900, 300, (u * .25) % 1)
        elephant(P, x, CENTER + 50 + abs(math.sin(t * 6)) * 8, 1.0, t)
        for j, dx in enumerate((-90, -40, 60, 110)):
            on = math.sin(t * 6 + j * 1.6) > -.6
            P.circ(x + dx, GROUND + 30, 16, HOPE if on else (180, 160, 110))
        P.badge(540, CENTER + 480, "always a foot down", 56, NIGHT, GLIM, back(seg(u, .8, 1.3)))
    elif i == 3:
        savanna(P)
        P.rrect(140, GROUND - 10, 940, GROUND + 40, 20, (90, 90, 100))
        elephant(P, 560, CENTER - 40, 1.0, t)
        n = int(5000 * eio(seg(u, .4, 3.0)))
        P.badge(540, CENTER + 440, f"{n:,} kg+".replace(",", " "), 64, HOOK, CLOUD, back(seg(u, .3, .8)))
    elif i == 4:
        P.rrect(120, CENTER - 360, 960, CENTER + 320, 50, (230, 220, 200))
        for x in (330, 750):
            P.rrect(x - 70, CENTER - 300, x + 70, CENTER + 260, 30, GRAY2)
            for j in range(4): P.line([(x - 70, CENTER - 200 + j * 120), (x + 70, CENTER - 200 + j * 120)], GRAY, 6)
        P.badge(540, CENTER + 400, "built like pillars", 56, NIGHT, CLOUD, back(seg(u, .6, 1.1)))
    else:
        savanna(P); elephant(P, 320, CENTER + 60, .8, t)
        hippo(P, 750, CENTER + 220, .8, t, air=abs(math.sin(t * 4)) * 60)
        P.stamp(700, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
