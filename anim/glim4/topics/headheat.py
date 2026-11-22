# Thema: Do you lose most of your body heat through your head?  (Mythos-Format, MYTH in Satz 2, FACT in Satz 6)
# Quellen: Vreeman & Carroll, BMJ 2008;337:a2769 "Festive medical myths" (Kopf ~10 % der Wärme, entspricht etwa
# seinem Anteil an der Körperoberfläche; Mythos aus US-Army-Versuch mit Arktisanzügen ohne Mütze).
CENTER = 1050
SKINC, HAT, SUIT, SNOW = (245, 200, 165), (230, 80, 90), (70, 110, 170), (242, 247, 252)
COLD, WARM = (90, 150, 230), (240, 90, 70)
PAL = ((60, 90, 150), (170, 200, 235))
HI = {"most", "head?", "myth!", "ten", "percent", "share", "skin,", "army", "hats.", "covered!", "cozy!"}
WOW = (1,)

def snowy(P, t, y=CENTER + 380):
    P.rrect(-20, y, W + 20, H + 50, 0, SNOW)
    for j in range(25): P.circ((j * 131 + t * 25) % W, (j * 197 + t * 70) % 1000 + CENTER - 650, 5 + j % 3, (255, 255, 255))

def person(P, x, y, s, t, hat=True, suit=SUIT, glow_head=0., glow_body=0.):
    """Figur (Kopfmitte bei x, y)."""
    if glow_body > 0: P.rrect(x - 190 * s, y + 110 * s, x + 190 * s, y + 560 * s, 100 * s, lc((255, 210, 180), WARM, .5 * glow_body))
    P.rrect(x - 160 * s, y + 130 * s, x + 160 * s, y + 540 * s, 90 * s, suit)
    if glow_head > 0: P.circ(x, y, 175 * s, lc((255, 210, 180), WARM, .5 * glow_head), glow=(int(150 * glow_head), int(60 * glow_head), int(40 * glow_head)))
    P.circ(x, y, 140 * s, SKINC)
    if hat:
        P.d.chord([*P.c.p(x - 150 * s, y - 170 * s), *P.c.p(x + 150 * s, y + 80 * s)], 180, 360, fill=HAT)
        P.rrect(x - 155 * s, y - 60 * s, x + 155 * s, y - 20 * s, 20 * s, CLOUD); P.circ(x, y - 175 * s, 30 * s, CLOUD)
    else:
        P.d.chord([*P.c.p(x - 140 * s, y - 145 * s), *P.c.p(x + 140 * s, y + 20 * s)], 180, 360, fill=(110, 75, 50))
    for ex in (-50, 50): P.circ(x + ex * s, y + 10 * s, 13 * s, NIGHT)
    for ex in (-80, 80): P.ell(x + ex * s, y + 50 * s, 20 * s, 12 * s, (250, 150, 140))
    P.arc(x, y + 50 * s, 40 * s, 20, 160, NIGHT, 7 * s)

def heatwaves(P, x, y, t, k):
    if k <= .02: return
    for j in range(3):
        q = (t * .8 + j / 3) % 1
        xx = x + (j - 1) * 70
        P.line([(xx + math.sin(q * 9) * 12, y - q * 180), (xx + math.sin(q * 9 + 1) * 12, y - q * 180 - 50)], lc(WARM, (255, 220, 150), q), 10 * k * (1 - q))

def SC(i, P, t, u):
    if i == 0:
        snowy(P, t); person(P, 540, CENTER - 60, 1.0, t, hat=False)
        heatwaves(P, 540, CENTER - 230, t, 1.)
        P.text(820, CENTER - 230, "?", 160 * back(seg(u, .5, 1.0)), GLIM)
    elif i == 1:
        snowy(P, t); person(P, 380, CENTER - 60, .9, t, hat=False)
        k = eout(seg(u, .8, 2.0))
        P.circ(820, CENTER + 60, 150, (40, 60, 100))
        P.d.pieslice([*P.c.p(670, CENTER - 90), *P.c.p(970, CENTER + 210)], -90, -90 + 36 * k, fill=HOOK)
        P.badge(820, CENTER + 260, "about 10%", 56, HOOK, CLOUD, back(seg(u, 1.8, 2.3)))
        P.stamp(560, CENTER - 300, "MYTH", seg(u, .25, .7), rot=-6)
    elif i == 2:
        person(P, 540, CENTER - 170, .9, t, hat=False, glow_head=.6, glow_body=.6)
        P.badge(540, CENTER + 450, "every bare spot loses heat", 50, NIGHT, CLOUD, back(seg(u, 1.4, 1.9)))
    elif i == 3:
        snowy(P, t)
        for j, x in enumerate((300, 780)):
            person(P, x, CENTER - 60, .75, t, hat=False, suit=(200, 205, 215))
        P.badge(540, CENTER - 330, "old army test", 58, NIGHT, CLOUD, back(seg(u, .4, .9)))
        P.badge(540, CENTER + 470, "warm suits, no hats", 54, GLIM, NIGHT, back(seg(u, 1.6, 2.1)))
    elif i == 4:
        snowy(P, t); person(P, 540, CENTER - 60, .95, t, hat=False, suit=(200, 205, 215), glow_head=eio(seg(u, .5, 1.5)))
        heatwaves(P, 540, CENTER - 230, t, eio(seg(u, .5, 1.5)))
        P.badge(540, CENTER + 480, "only part left bare", 54, HOOK, CLOUD, back(seg(u, 1.6, 2.1)))
    else:
        snowy(P, t); person(P, 380, CENTER - 40, .9, t, hat=True)
        P.stamp(780, CENTER - 290, "FACT", seg(u, .3, .7), col=HOPE, rot=8)
