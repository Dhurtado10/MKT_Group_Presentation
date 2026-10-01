#!/bin/bash
# usage: render.sh <pptx> <outdir>
S=/tmp/claude-0/-home-user-MKT-Group-Presentation/bf85d9c3-7cd1-5049-ad84-7cc82f78b5a1/scratchpad
rm -rf $S/out; mkdir -p $S/out; cp "$1" $S/out/d.pptx
(cd $S/out && soffice --headless --convert-to pdf d.pptx >/dev/null 2>&1 && pdftoppm -r ${2:-110} -png d.pdf s)
ls $S/out | head -20
