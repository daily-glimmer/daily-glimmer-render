#!/bin/bash
# render.sh <topic> <style> <music> <mstart>  -> glim_<topic>.mp4 (60 fps)
# Fehlende Frames (z. B. nach OOM-Abbruch eines Workers) werden vor dem Mischen einzeln nachgerendert.
k=$1; st=$2; mu=$3; ms=$4
rm -rf $k/frames; mkdir -p $k/frames
s=$(date +%s)
GLIM_STYLE=$st python3 glim4.py $k $k/tl.json $k/frames 0 2 & GLIM_STYLE=$st python3 glim4.py $k $k/tl.json $k/frames 1 2 & wait
for try in 1 2; do
  miss=$(python3 -c "import json,os;d=json.load(open('$k/tl.json'));n=int(d['total']*60);s=set(os.listdir('$k/frames'));print(' '.join(str(i) for i in range(n) if 'f%05d.png'%i not in s))")
  [ -z "$miss" ] && break
  for i in $miss; do GLIM_STYLE=$st GLIM_FROM=$i GLIM_TO=$((i+1)) python3 glim4.py $k $k/tl.json $k/frames 0 1; done
done
[ -n "$miss" ] && { echo "$k FEHLENDE FRAMES" >> render.log; exit 1; }
python3 glim4-mix.py $k music/$mu.wav $ms 60 && echo "$k fertig in $(( $(date +%s)-s )) s" >> render.log
