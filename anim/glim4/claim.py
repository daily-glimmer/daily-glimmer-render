"""claim.py <thema> <frage>  -> reserviert den nächsten freien Glim-Slot (ab 16.11., 08:30/18:00; 13:00 nur 16.–19.11.) im Repo, gibt Tag aus."""
import sys, os, subprocess, json, datetime
R = "/home/claude/daily-glimmer-render"; th, q = sys.argv[1], sys.argv[2]
def git(*a): return subprocess.run(["git", "-C", R] + list(a), capture_output=True, text=True)
for attempt in range(6):
    git("pull", "-q", "--rebase")
    have = set(os.listdir(f"{R}/claims"))
    qs = [json.load(open(f"{R}/claims/{f}")).get("frage", "").lower() for f in have]
    if q.lower() in qs: print("FRAGE_SCHON_RESERVIERT"); sys.exit(1)
    d = datetime.date(2026, 11, 16); tag = None
    while d <= datetime.date(2026, 11, 30) and not tag:
        for hm in (["0830", "1300", "1800"] if d.day <= 19 else ["0830", "1800"]):
            t = f"glim-{d.isoformat()}-{hm}"
            if f"{t}.json" not in have: tag = t; break
        d += datetime.timedelta(days=1)
    if not tag: print("KEIN_SLOT"); sys.exit(2)
    now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    json.dump({"thema": th, "frage": q, "lauf_start": now, "von": "Chat-Sitzung"}, open(f"{R}/claims/{tag}.json", "w"))
    git("add", f"claims/{tag}.json")
    git("commit", "-q", "-m", f"Claim {tag} ({th}, Chat-Sitzung)\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_01XFtfdftJTR23228UeH1hPJ")
    if git("-c", "push.negotiate=true", "push", "-q").returncode == 0: print(tag); sys.exit(0)
    git("reset", "-q", "--hard", "origin/main")
print("PUSH_FAIL"); sys.exit(3)
