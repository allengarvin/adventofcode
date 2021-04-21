#!/bin/bash

function match2 () { 
    grep '\([0-9]\)\1'
}

FILE1=$(mktemp)
seq $(cat 04-input.txt | tr - \  ) | grep $(echo {0..9} | sed 's/^/^/;s/ /*/g;s/$/*$/') |
    match2 > $FILE1

cat $FILE1 | wc -l
sed 's/\([0-9]\)\1\1\+//g' $FILE1 | match2 | wc -l
rm $FILE1
