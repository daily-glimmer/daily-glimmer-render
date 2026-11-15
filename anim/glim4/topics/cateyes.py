# Thema: Why do cats' eyes glow in the dark?
CENTER = 1050
FUR, FUR2 = (90, 95, 120), (60, 65, 90)
IRIS, GLOWC = (150, 200, 90), (190, 255, 140)
BEAM = (255, 240, 170)
PAL = ((20, 24, 50), (60, 50, 90))
HI = {"glow", "dark?", "shiny", "layer", "mirror.", "bounces", "second", "chance.", "glow", "flashlight", "one", "sixth", "red", "photos."}
WOW = (2, 4)

def catface(P, x, y, s, t, glow=0., blink=True):
    P.circ(x, y, 220 * s, FUR)
    for d in (-1, 1):
        P.poly([(x + d * 200 * s, y - 70 * s), (x + d * 170 * s, y - 300 * s), (x + d * 50 * s, y - 190 * s)], FUR)
        P.poly([(x + d * 170 * s, y - 110 * s), (x + d * 160 * s, y - 240 * s), (x + d * 90 * s, y - 180 * s)], (200, 140, 160))
    bl = 1.
    if blink:
        q = (t % 3.4)
        if q < .15: bl = .15
    for d in (-1, 1):
        ex, ey = x + d * 85 * s, y - 30 * s
        col = lc(IRIS, GLOWC, glow)
        P.ell(ex, ey, 55 * s, 48 * s * bl, col, glow=(int(120 * glow), int(200 * glow), int(80 * glow)) if glow > .05 else None)
        P.ell(ex, ey, 14 * s, 42 * s * bl, NIGHT)
        if bl > .5: P.circ(ex + 16 * s, ey - 16 * s, 8 * s, CLOUD)
    P.poly([(x - 22 * s, y + 50 * s), (x + 22 * s, y + 50 * s), (x, y + 75 * s)], (220, 140, 160))
    P.arc(x - 22 * s, y + 80 * s, 22 * s, 0, 150, NIGHT, 5 * s); P.arc(x + 22 * s, y + 80 * s, 22 * s, 30, 180, NIGHT, 5 * s)
    for d in (-1, 1):
        for k in (-1, 0, 1): P.line([(x + d * 70 * s, y + 70 * s), (x + d * 250 * s, y + (60 + k * 30) * s)], CLOUD, 3 * s)

def eyeball(P, x, y, r, t, mirror=1., rays=0., second=0.):
    """Querschnitt: Linse links, Netzhaut + Spiegel rechts."""
    P.circ(x, y, r, CLOUD, outline=FUR2, w=8)
    P.arc(x, y, r - 18, -70, 70, (230, 120, 120), 22)                  # Netzhaut (Sensoren)
    if mirror > .02: P.arc(x, y, r - 2, -70, 70, lc((200, 205, 220), (255, 255, 255), .5 + .5 * math.sin(t * 5)), 16 * mirror)
    P.ell(x - r + 30, y, 30, 70, (160, 200, 240), outline=FUR2, w=5)   # Linse
    if rays > 0:
        for k in (-1, 0, 1):
            ly = y + k * 50
            xe = lerp(x - r - 300, x + r - 30, rays)
            P.line([(x - r - 300, ly), (xe, ly + k * 30 * rays)], BEAM, 12, glow=(90, 80, 40))
    if second > 0:
        for k in (-1, 0, 1):
            ly = y + k * 50 + k * 30
            xs = x + r - 30; xe = lerp(xs, x - r - 260, second)
            P.line([(xs, ly), (xe, ly + k * 20 * second)], GLOWC, 10, glow=(60, 110, 40))

def flashlight(P, x, y, s, on=1.):
    if on > 0:
        P.poly([(x + 60 * s, y - 30 * s), (x + 60 * s + 500 * on, y - 170 * s), (x + 60 * s + 500 * on, y + 170 * s), (x + 60 * s, y + 30 * s)], (90, 85, 70))
    P.rrect(x - 160 * s, y - 30 * s, x + 20 * s, y + 30 * s, 14 * s, (200, 60, 60))
    P.rrect(x + 10 * s, y - 50 * s, x + 70 * s, y + 50 * s, 12 * s, (230, 230, 230))

def SC(i, P, t, u):
    if i == 0:
        k = eio(seg(u, .5, 1.6))
        catface(P, 540, CENTER + 80, 1.3, t, glow=k * (.7 + .3 * math.sin(t * 3)))
        P.text(860, CENTER - 300, "?", 150 * back(seg(u, .8, 1.3)), GLIM)
    elif i == 1:
        eyeball(P, 540, CENTER + 40, 260, t, mirror=back(seg(u, .6, 1.2)))
        P.badge(540, CENTER + 420, "shiny mirror layer", 58, NIGHT, GLIM, back(seg(u, 1.2, 1.7)))
    elif i == 2:
        eyeball(P, 640, CENTER + 40, 260, t, rays=eio(seg(u, .2, 1.4)), second=eio(seg(u, 1.8, 3.0)))
        P.badge(540, CENTER + 420, "second chance!", 60, HOPE, CLOUD, back(seg(u, 2.4, 2.9)))
    elif i == 3:
        on = eio(seg(u, .3, 1.0))
        flashlight(P, 160, CENTER + 360, 1.0, on)
        catface(P, 640, CENTER - 20, 1.05, t, glow=on)
    elif i == 4:
        P.rrect(150, CENTER - 160, 510, CENTER + 260, 30, (40, 45, 70), outline=CLOUD, w=6)
        P.rrect(570, CENTER - 160, 930, CENTER + 260, 30, (40, 45, 70), outline=CLOUD, w=6)
        P.text(330, CENTER - 90, "CAT", 56, GLIM); P.text(750, CENTER - 90, "YOU", 56, CLOUD)
        for k in range(1):
            P.circ(330, CENTER + 70, 40, BEAM, glow=(60, 60, 30))
        for k in range(6):
            P.circ(690 + (k % 3) * 60, CENTER + 30 + (k // 3) * 80, 26, BEAM, glow=(60, 60, 30))
        P.badge(540, CENTER + 420, "1/6 of the light", 60, NIGHT, GLIM, back(seg(u, 1.0, 1.5)))
    else:
        P.rrect(250, CENTER - 200, 830, CENTER + 220, 30, CLOUD, outline=FUR2, w=10)          # Foto
        P.circ(540, CENTER + 30, 140, (240, 200, 170))
        for d in (-1, 1):
            P.circ(540 + d * 55, CENTER, 30, CLOUD); P.circ(540 + d * 55, CENTER, 17, (230, 50, 50))
        P.arc(540, CENTER + 60, 60, 20, 160, NIGHT, 8)
        fl = max(0, 1 - abs(u - .6) / .2)
        if fl > 0: P.circ(760, CENTER - 140, 60 * fl, (255, 255, 230), glow=(120, 120, 90))
        P.badge(540, CENTER - 300, "red eye = blood vessels", 50, HOOK, CLOUD, back(seg(u, 1.0, 1.5)))
