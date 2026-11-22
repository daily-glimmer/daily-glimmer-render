#!/bin/bash
# render.sh <topic> <style> <music> <mstart>  -> glim_<topic>.mp4 (60 fps)
# Jede neue Schriftgröße kostet dauerhaft Speicher im Prozess (animierte Stempel/Pops -> mehrere GB, OOM).
# Daher rendert jeder Worker in Blöcken von 80 Frames mit frischem Prozess.
# Fehlende Frames (z. B. nach Abbruch) werden vor dem Mischen einzeln nachgerendert.
k=$1; st=$2; mu=$3; ms=$4
rm -rf $k/frames; mkdir -p $k/frames
s=$(date +%s)
N=$(python3 -c "import json;print(int(json.load(open('$k/tl.json'))['total']*60))")
work() { for ((a=0; a<N; a+=80)); do GLIM_STYLE=$st GLIM_FROM=$a GLIM_TO=$((a+80<N?a+80:N)) python3 glim4.py $k $k/tl.json $k/frames $1 2; done; }
work 0 & work 1 & wait
for try in 1 2; do
  miss=$(python3 -c "import os;s=set(os.listdir('$k/frames'));print(' '.join(str(i) for i in range($N) if 'f%05d.png'%i not in s))")
  [ -z "$miss" ] && break
  for i in $miss; do GLIM_STYLE=$st GLIM_FROM=$i GLIM_TO=$((i+1)) python3 glim4.py $k $k/tl.json $k/frames 0 1; done
done
[ -n "$miss" ] && { echo "$k FEHLENDE FRAMES" >> render.log; exit 1; }
python3 glim4-mix.py $k music/$mu.wav $ms 60 && echo "$k fertig in $(( $(date +%s)-s )) s" >> render.log
