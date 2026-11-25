# TikTok-„Fact Snap“ (Prototyp 21.11.): 2 Sätze, Loop-Ende, Szenen aus lemmings.py
exec(open(os.path.join(HERE, "topics", "lemmings.py")).read(), globals())
_SC = SC
def SC(i, P, t, u):
    if i == 0: _SC(0, P, t, u + .6)
    else:
        _SC(4, P, t, u + 2.0)
        P.stamp(540, CENTER - 290, "MYTH", seg(u, .1, .5), rot=-10)
