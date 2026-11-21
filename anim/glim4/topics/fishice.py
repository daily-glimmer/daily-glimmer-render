# Thema: Why don't fish freeze when a lake turns to ice?  (Wissensformat, Stempel TRUE in Satz 2, FACT in Satz 6)
CENTER = 1050
PAL = ((110, 140, 190), (200, 220, 240))
HI = {"freeze", "ice?", "surprise:", "safe!", "heaviest", "four", "degrees", "sinks", "float", "lid", "slow", "spring.", "cozy"}
WOW = (1,)
ICE_Y = CENTER - 200

def lake(P, t, ice=1., warm=0.):
    P.poly([(0, ICE_Y - 40), (W, ICE_Y - 40), (W, ICE_Y), (0, ICE_Y)], (240, 245, 250))
    P.rrect(-20, ICE_Y, W + 20, CENTER + 520, 0, (70, 140, 200))
    if warm > 0: P.rrect(-20, CENTER + 220, W + 20, CENTER + 520, 0, lc((70, 140, 200), (40, 90, 170), warm))
    if ice > 0: P.rrect(-20, ICE_Y - 10, W + 20, ICE_Y + 70 * ice, 0, (215, 235, 250), outline=(180, 210, 235), w=6)
    P.poly([(0, CENTER + 460), (W, CENTER + 440), (W, H), (0, H)], (110, 90, 70))
    for j in range(3): P.line([(150 + j * 360, CENTER + 450), (160 + j * 360 + math.sin(t + j) * 20, CENTER + 250)], (60, 140, 80), 16)

def fish(P, x, y, s, t, slow=0., col=(255, 150, 60), f=1):
    w_ = math.sin(t * (8 - 6 * slow)) * 25 * s
    P.poly([(x - f * 60 * s, y), (x - f * 120 * s, y - 45 * s + w_), (x - f * 120 * s, y + 45 * s + w_)], col)
    P.ell(x, y, 80 * s, 42 * s, col); P.circ(x + f * 45 * s, y - 10 * s, 9 * s, NIGHT)

def SC(i, P, t, u):
    if i == 0:
        lake(P, t, ice=back(seg(u, .3, 1.2)))
        fish(P, 500 + math.sin(t * .6) * 120, CENTER + 200, 1.2, t)
        P.text(820, CENTER - 60, "?", 140 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        lake(P, t, ice=1.)
        fish(P, 540, CENTER + 200, 1.3, t)
        P.heart(540, CENTER - 40, 50 * back(seg(u, 1.0, 1.5)), HOOK)
        P.stamp(540, CENTER - 310, "TRUE", seg(u, .25, .7), col=HOPE, rot=-6) if False else None
        P.badge(540, CENTER + 360, "ice = shield", 60, NIGHT, GLIM, back(seg(u, 1.2, 1.7)))
        P.stamp(780, CENTER + 40, "SAFE", seg(u, .25, .7), col=HOPE, rot=-6)
    elif i == 2:
        lake(P, t, ice=0., warm=eio(seg(u, .5, 2.5)))
        for j in range(6):
            q = (u * .35 + j / 6) % 1
            P.circ(160 + j * 150, lerp(ICE_Y + 60, CENTER + 400, q), 16, (40, 90, 170))
        P.badge(540, CENTER + 330, "4 °C sinks", 60, NIGHT, GLIM, back(seg(u, 1.6, 2.1)))
    elif i == 3:
        lake(P, t, ice=1., warm=1.)
        k = back(seg(u, 1.0, 1.5))
        P.badge(540, ICE_Y + 160, "ice = lid", 58, NIGHT, CLOUD, k)
        P.badge(540, CENTER + 330, "warmer at the bottom", 52, HOOK, CLOUD, back(seg(u, 2.5, 3.0)))
    elif i == 4:
        lake(P, t, ice=1., warm=1.)
        fish(P, 380, CENTER + 380, 1.0, t, slow=1.); fish(P, 700, CENTER + 400, .9, t + 1, slow=1., f=-1)
        for j in range(3):
            q = (t * .4 + j / 3) % 1; P.text(420 + q * 60, CENTER + 280 - q * 150, "z", 40 + 30 * q, CLOUD)
        P.badge(540, CENTER + 60, "slow mode", 58, NIGHT, GLIM, back(seg(u, .6, 1.1)))
    else:
        lake(P, t, ice=1., warm=1.)
        fish(P, 540, CENTER + 330, 1.2, t, slow=.6)
        P.stamp(780, CENTER + 60, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
