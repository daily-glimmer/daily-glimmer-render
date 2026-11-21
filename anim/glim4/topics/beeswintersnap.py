# Fact Snap (TikTok-Kurzfassung) zu topics/beeswinter.py: Szene 0 = Frage, Szene 1 = Auflösung (Szene 1) mit Stempel
exec(open(os.path.join(HERE, "topics", "beeswinter.py")).read(), globals())
_SC_FULL = SC
def SC(i, P, t, u):
    if i == 1:   # Badges unten nicht unter den großen Schluss-Glim legen
        _b = P.badge
        P.badge = lambda x, y, *a, **kw: _b(x, min(y, CENTER + 400), *a, **kw)
    _SC_FULL(0 if i == 0 else 1, P, t, u)
WOW = (1,)
