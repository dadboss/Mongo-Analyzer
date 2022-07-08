#!/bin/bash
tar zxvf $1
./keyhole --diag ./tmp/diagnostic.data/ > output.txt
awk -F'|' -v OFS="," '/^\+/{next} {for (i=2;i<NF;i++) {gsub(/^ *| *$/,"",$i); printf("\"%s\"%s",$i,i<(NF-1)?OFS:ORS)}}' output.txt >> out.txt
python pyscript.py