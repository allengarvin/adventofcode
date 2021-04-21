#!/bin/bash

TMP=$(mktemp /tmp/aoc2020-05-XXXXXX)
(echo ibase=2; tr FBRL 0110 < 05-input.txt | sort ) | bc > $TMP
tail -1 $TMP
comm -13 $TMP <(seq $(sed -n '1p;$p' $TMP))
rm $TMP
