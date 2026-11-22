# Thema: Is it winter because Earth is farther from the Sun?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6)
# Quellen: NASA Space Place "What Causes the Seasons?" (Neigung ~23,5°, Erde Anfang Januar am sonnennächsten,
# ca. 147 statt 152 Mio. km), NOAA/NWS (Perihel Anfang Januar).
CENTER = 1050
SUN, SUN2 = (255, 205, 70), (255, 150, 40)
OCEAN, LAND, SNOW = (60, 130, 210), (90, 175, 95), (245, 248, 255)
PAL = ((14, 20, 50), (40, 50, 100))
HI = {"winter", "farther", "myth!", "closest", "january.", "tilted", "twenty", "three", "away", "low,", "weak", "shorter", "australia", "summer!", "tilt!"}
WOW = (1,)
TILT = math.radians(23.5)

def sun(P, x, y, r, t):
    for k in range(12):
        a = k * math.pi / 6 + t * .3
        P.line([(x + math.cos(a) * (r + 15), y + math.sin(a) * (r + 15)), (x + math.cos(a) * (r + 55), y + math.sin(a) * (r + 55))], SUN, 14)
    P.circ(x, y, r, SUN, glow=mul(SUN2, 200)); P.circ(x - r * .25, y - r * .25, r * .35, (255, 230, 140))

def earth(P, x, y, r, t, axis=True, north_snow=False, south_sun=False):
    if axis:
        dx, dy = math.sin(TILT) * r * 1.45, -math.cos(TILT) * r * 1.45
        P.line([(x - dx, y - dy), (x + dx, y + dy)], CLOUD, 8)
    P.circ(x, y, r, OCEAN)
    sp = t * .5
    for k, (a, b, s) in enumerate(((.2, -.35, .38), (1.9, .15, .32), (3.6, -.1, .42), (5.0, .4, .28))):
        xx = math.sin(a + sp)
        if math.cos(a + sp) > -.2: P.ell(x + xx * r * .7, y + b * r, r * s * (.4 + .6 * abs(math.cos(a + sp))), r * s * .7, LAND)
    if north_snow: P.ell(x + math.sin(TILT) * r * .55, y - r * .78, r * .55, r * .2, SNOW)
    if axis: P.line([(x, y), (x + math.sin(TILT) * r * 1.45, y - math.cos(TILT) * r * 1.45)], CLOUD, 8)

def orbit(P, cx, cy, rx, ry):
    for k in range(48):
        a0, a1 = k / 48 * 2 * math.pi, (k + .5) / 48 * 2 * math.pi
        P.line([(cx + math.cos(a0) * rx, cy + math.sin(a0) * ry), (cx + math.cos(a1) * rx, cy + math.sin(a1) * ry)], (120, 130, 180), 6)

def SC(i, P, t, u):
    if i == 0:
        sun(P, 200, CENTER - 20, 120, t)
        x = lerp(560, 840, eio(seg(u, .3, 1.8)))
        earth(P, x, CENTER + 40, 120, t, north_snow=True)
        P.text(x + 40, CENTER - 230, "?", 150 * back(seg(u, 1.0, 1.5)), GLIM)
    elif i == 1:
        orbit(P, 540, CENTER + 40, 380, 230)
        sun(P, 470, CENTER + 40, 90, t)
        a = math.pi + .2 * math.sin(t * .4)
        earth(P, 540 + math.cos(a) * 380, CENTER + 40 + math.sin(a) * 230, 60, t, axis=False)
        P.badge(220, CENTER - 230, "January: closest", 50, GLIM, NIGHT, back(seg(u, 1.2, 1.7)))
        P.stamp(700, CENTER + 420, "MYTH", seg(u, .25, .7), rot=-6)
    elif i == 2:
        sun(P, 140, CENTER + 40, 90, t)
        earth(P, 620, CENTER + 40, 190, t)
        k = eout(seg(u, .5, 1.5))
        P.arc(620, CENTER + 40, 300, -90, -90 + 23.5 * k, GLIM, 10)
        P.line([(620, CENTER + 40), (620, CENTER - 270)], (150, 160, 200), 4)
        P.badge(620, CENTER + 400, "tilted 23.5 degrees", 56, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
    elif i == 3:
        sun(P, 120, CENTER + 40, 80, t)
        earth(P, 640, CENTER + 40, 200, t, north_snow=True)
        for j in range(5):
            y = CENTER - 200 + j * 90; k = eout(seg(u, .3 + j * .1, 1.2 + j * .1))
            P.line([(230, y), (lerp(230, 640 - math.sqrt(max(0, 200 ** 2 - (y - CENTER - 40) ** 2)) + 10, k), y)], (255, 225, 120), 10)
        P.badge(640, CENTER - 280, "low, weak sunlight", 54, NIGHT, CLOUD, back(seg(u, 1.6, 2.1)))
    elif i == 4:
        earth(P, 540, CENTER + 40, 220, t, north_snow=True)
        P.badge(540, CENTER - 300, "north: winter", 56, NIGHT, CLOUD, back(seg(u, .4, .9)))
        sun(P, 860, CENTER + 230, 40, t)
        P.badge(540, CENTER + 400, "Australia: summer", 56, GLIM, NIGHT, back(seg(u, 1.6, 2.1)))
    else:
        sun(P, 160, CENTER + 40, 90, t)
        earth(P, 600, CENTER + 60, 170, t, north_snow=True)
        P.stamp(800, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
