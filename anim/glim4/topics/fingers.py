# Thema: Why do our fingers get wrinkly in water?
CENTER = 1050
SK, SK2 = (240, 190, 150), (190, 130, 100)
PAL = ((225, 235, 245), (190, 215, 235))
HI = {"fingers", "wrinkly", "water?", "not", "sponge.", "five", "minutes,", "nerves", "blood", "vessels", "shrink.", "folds,", "grip", "tire", "treads.", "nerves"}
WOW = (2, 4)

def hand(P, x, y, s, wr=0.):
    P.rrect(x - 150 * s, y, x + 150 * s, y + 330 * s, 70 * s, SK, outline=SK2, w=6 * s)
    for k, h in enumerate((200, 250, 260, 230)):
        fx = x - 112 * s + k * 75 * s
        P.rrect(fx - 32 * s, y - h * s + 20 * s, fx + 32 * s, y + 60 * s, 32 * s, SK, outline=SK2, w=6 * s)
        if wr > 0:
            for j in range(4):
                yy = y - h * s + 50 * s + j * 22 * s
                P.arc(fx, yy, 22 * s, 200, 340, SK2, 4 * s * wr)
    P.rrect(x + 120 * s, y + 60 * s, x + 200 * s, y + 200 * s, 40 * s, SK, outline=SK2, w=6 * s)

def water(P, t, top=CENTER + 120):
    P.rrect(-20, top, W + 20, H + 20, 0, (120, 180, 230))
    pts = [(x, top + 12 * math.sin(t * 2 + x / 60)) for x in range(0, 1101, 50)]
    P.line(pts, (180, 220, 250), 10)

def SC(i, P, t, u):
    if i == 0:
        hand(P, 540, CENTER - 40, 1.1, wr=1)
        P.text(860, CENTER - 330, "?", 150 * back(seg(u, .4, .9)), HOOK)
    elif i == 1:
        P.rrect(330, CENTER - 160, 750, CENTER + 160, 40, (250, 220, 90), outline=(200, 160, 40), w=8)
        for k in range(10): P.circ(390 + (k * 97) % 320, CENTER - 110 + (k * 61) % 220, 18, (210, 170, 50))
        P.cross(540, CENTER, 200, HOOK, back(seg(u, 1.0, 1.5)))
        P.badge(540, CENTER + 330, "not a sponge", 60, NIGHT, GLIM, back(seg(u, 1.4, 1.9)))
    elif i == 2:
        P.rrect(160, CENTER - 230, 920, CENTER + 230, 40, CLOUD, outline=SK2, w=6)
        w = 60 - 35 * eout(seg(u, 1.2, 3.0))
        P.rrect(200, CENTER - w, 880, CENTER + w, w, (220, 70, 70))
        P.line([(540, CENTER - 200), (560, CENTER - 120), (530, CENTER - 80)], GLIM, 10, glow=GLIM)
        P.badge(540, CENTER + 330, "5 min", 60, NIGHT, GLIM, back(seg(u, .3, .8)))
        P.badge(540, CENTER - 320, "nerve signal", 52, HOPE, CLOUD, back(seg(u, .8, 1.3)))
    elif i == 3:
        hand(P, 540, CENTER - 20, 1.2, wr=eout(seg(u, .4, 2.4)))
        water(P, t, CENTER + 260)
        P.badge(540, CENTER + 420, "folds", 60, NIGHT, GLIM, back(seg(u, 1.6, 2.1)))
    elif i == 4:
        P.rrect(150, CENTER - 250, 930, CENTER + 260, 40, (60, 60, 70))
        for k in range(8):
            P.poly([(200 + k * 90, CENTER - 200), (260 + k * 90, CENTER - 200), (230 + k * 90, CENTER + 200), (170 + k * 90, CENTER + 200)], (100, 100, 110))
        P.ell(540, CENTER, 140, 80, (120, 180, 230), outline=CLOUD, w=6)
        P.badge(540, CENTER + 350, "better grip", 60, HOPE, CLOUD, back(seg(u, 1.0, 1.5)))
    else:
        hand(P, 540, CENTER + 20, 1.0, wr=0)
        water(P, t, CENTER + 280)
        P.badge(540, CENTER - 420, "no nerves = no wrinkles", 50, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
