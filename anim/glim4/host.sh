#!/bin/bash
# host.sh <topic> <tag> <title>  -> pusht MP4 + Manifest, wartet auf Release, prüft URL
k=$1; tag=$2; title=$3; R=/home/claude/daily-glimmer-render
grep -q "^$k fertig" /home/claude/glim/render.log || { echo "NOT RENDERED $k"; exit 1; }
ffprobe -v error /home/claude/glim/glim_$k.mp4 || { echo "BROKEN $k"; exit 1; }
cd $R && git pull -q --rebase || exit 1
cp /home/claude/glim/glim_$k.mp4 glim/$tag.mp4
printf '{"passthrough": true, "title": "Glim explains: %s", "file": "glim/%s.mp4"}\n' "$title" "$tag" > manifests/$tag.json
git add glim/$tag.mp4 manifests/$tag.json
git commit -q -m "Glim $tag: $title

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01XFtfddKD54yJppGTJDcRR8"
ok=0; for n in 1 2 3 4 5; do git pull -q --rebase; if git -c push.negotiate=true push -q 2>/dev/null; then ok=1; break; fi; sleep 5; done
[ $ok = 1 ] || { echo "PUSH FAIL $tag"; exit 1; }
sha=$(git rev-parse HEAD); echo "pushed $sha"
url=https://github.com/daily-glimmer/daily-glimmer-render/releases/download/$tag/out.mp4
for i in $(seq 1 40); do
  sleep 10
  code=$(curl -sL -o /tmp/chk_$tag.mp4 -w '%{http_code}' $url)
  if [ "$code" = "200" ] && cmp -s /tmp/chk_$tag.mp4 /home/claude/glim/glim_$k.mp4; then echo "OK $url"; exit 0; fi
done
echo "FAIL $tag ($code)"; exit 1
