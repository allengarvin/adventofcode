#!/bin/bash

TMP=$(mktemp /tmp/aoc2020-05-XXXXXX)
tr FBRL 0110 < 05-input.txt | while read a; do echo $(( 2#$a )); done | sort -n > $TMP
cat $TMP > /tmp/aoc
tail -1 $TMP
for i in $(seq $(head -n 1 $TMP) $(tail -1 $TMP)); do grep -qL ^$i$ $TMP || break; done
echo $i
rm $TMP
