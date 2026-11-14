#!/bin/bash
# sheet.sh <topic> <style>  -> Testframes je Satz + Kontaktbogen <topic>/sheet.png
k=$1; st=$2
secs=$(python3 -c "import json;d=json.load(open('$k/tl.json'));print(','.join(str(round(l['start']+min(2.2,l['dur']*.6),2)) for l in d['lines']))")
rm -rf $k/test; mkdir -p $k/test
GLIM_STYLE=$st GLIM_ONLY=$secs python3 glim4.py $k $k/tl.json $k/test || exit 1
ffmpeg -y -loglevel error -pattern_type glob -i "$k/test/t*.png" -vf "scale=360:-1,tile=6x1" -frames:v 1 $k/sheet.png
