#!/bin/bash
for file in `ls -1 testdata`; do
	./../separator_big5.pl testdata/${file} > testdata/seg_${file}
done
