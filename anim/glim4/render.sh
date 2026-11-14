#!/bin/bash
# render.sh <topic> <style> <music> <mstart>  -> glim_<topic>.mp4 (60 fps)
k=$1; st=$2; mu=$3; ms=$4
rm -rf $k/frames; mkdir -p $k/frames
s=$(date +%s)
GLIM_STYLE=$st python3 glim4.py $k $k/tl.json $k/frames 0 2 & GLIM_STYLE=$st python3 glim4.py $k $k/tl.json $k/frames 1 2 & wait
python3 glim4-mix.py $k music/$mu.wav $ms 60 && echo "$k fertig in $(( $(date +%s)-s )) s" >> render.log
