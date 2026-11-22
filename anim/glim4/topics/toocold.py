# Thema: Can it really be too cold to snow?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6)
# Quellen: National Snow and Ice Data Center (NSIDC) "it can be too warm to snow, but not too cold"; kalte Luft hält
# wenig Wasserdampf; viel Schnee meist knapp unter 0 °C; Antarktis-Trockentäler (The Weather Network, Popular Science).
CENTER = 1050
SNOWC, CLOUDC, CLOUD2 = (250, 252, 255), (200, 210, 225), (160, 170, 190)
COLD, WARM = (90, 150, 230), (240, 150, 70)
PAL = ((60, 80, 130), (160, 180, 215))
HI = {"cold", "snow?", "myth!", "too", "warm", "moisture.", "water", "vapor,", "less", "zero,", "flakes.", "antarctica", "dry,", "snow!"}
WOW = (1,)

def cloud(P, x, y, s, col=CLOUDC):
    for dx, dy, r in ((-120, 10, 80), (-40, -40, 105), (70, -20, 95), (150, 20, 70), (0, 30, 90)):
        P.circ(x + dx * s, y + dy * s, r * s, col)

def snow(P, t, n=25, x0=0, x1=W, y0=CENTER - 300, y1=CENTER + 400, sp=70):
    for j in range(n):
        x = x0 + (j * 131) % max(1, x1 - x0); y = y0 + (j * 197 + t * sp) % (y1 - y0)
        P.circ(x + math.sin(t + j) * 10, y, 6 + j % 4, SNOWC)

def flake(P, x, y, r, t):
    for k in range(6):
        a = k * math.pi / 3 + t * .2
        P.line([(x, y), (x + math.cos(a) * r, y + math.sin(a) * r)], SNOWC, 10)
        P.line([(x + math.cos(a) * r * .55, y + math.sin(a) * r * .55), (x + math.cos(a + .5) * r * .75, y + math.sin(a + .5) * r * .75)], SNOWC, 6)

def ground(P): P.poly([(0, CENTER + 400), (W, CENTER + 380), (W, H), (0, H)], SNOWC)

def drops(P, x, y, n, t):
    for j in range(n):
        a = j * 2.4; r = 30 + (j * 37) % 120
        P.ell(x + math.cos(a) * r, y + math.sin(a) * r * .5 + math.sin(t * 2 + j) * 6, 9, 13, (140, 200, 250))

def SC(i, P, t, u):
    if i == 0:
        ground(P); cloud(P, 540, CENTER - 200, 1.4, CLOUD2)
        P.text(540, CENTER + 120, "-30 °C", 120, COLD)
        P.text(840, CENTER - 360, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        ground(P); cloud(P, 540, CENTER - 200, 1.4, CLOUD2); snow(P, t, 12, 250, 830, CENTER - 120, CENTER + 400, 60)
        P.stamp(560, CENTER + 200, "MYTH", seg(u, .25, .7), rot=-6)
    elif i == 2:
        cloud(P, 540, CENTER - 160, 1.5)
        k = eio(seg(u, .5, 2.0))
        drops(P, 540, CENTER - 160, 14, t)
        flake(P, 540, CENTER + 220, 110 * k, t)
        P.badge(540, CENTER - 400, "snow needs water vapor", 54, NIGHT, CLOUD, back(seg(u, .4, .9)))
    elif i == 3:
        for j, (x, c, n) in enumerate(((290, COLD, 3), (790, WARM, 14))):
            cloud(P, x, CENTER - 160, .9, CLOUD2 if j == 0 else CLOUDC)
            drops(P, x, CENTER - 160, n, t)
        P.badge(290, CENTER + 120, "very cold: dry", 52, NIGHT, CLOUD, back(seg(u, .4, .9)))
        P.badge(790, CENTER + 120, "near 0 °C: moist", 52, GLIM, NIGHT, back(seg(u, 1.0, 1.5)))
        snow(P, t, 14, 640, 940, CENTER - 60, CENTER + 420, 80)
    elif i == 4:
        P.poly([(0, CENTER + 380), (200, CENTER + 120), (420, CENTER + 300), (650, CENTER + 60), (880, CENTER + 280), (W, CENTER + 180), (W, H), (0, H)], (225, 235, 248))
        P.poly([(0, CENTER + 420), (W, CENTER + 400), (W, H), (0, H)], (240, 245, 252))
        P.circ(820, CENTER - 280, 70, (255, 230, 140))
        P.text(540, CENTER - 120, "-40 °C", 110 * back(seg(u, .4, .9)), COLD)
        P.badge(540, CENTER + 520, "Antarctica: freezing but dry", 50, NIGHT, CLOUD, back(seg(u, 1.2, 1.7)))
        P.badge(540, CENTER + 10, "barely any snow", 50, HOOK, CLOUD, back(seg(u, 2.4, 2.9)))
    else:
        ground(P); cloud(P, 420, CENTER - 150, 1.0); snow(P, t, 12, 200, 650, CENTER - 60, CENTER + 400, 60)
        P.stamp(800, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
