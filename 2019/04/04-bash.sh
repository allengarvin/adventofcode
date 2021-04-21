#!/bin/bash

function match2 () { 
    grep '\(.\)\1'
}

FILE1=$(mktemp)
seq $(tr - \  <04-input.txt) | grep $(seq -s* 0 9 | sed 's/\(.*\)/^\1*$/') |
    match2 > $FILE1

wc -l < $FILE1
sed 's/\(.\)\1\1\+//g' $FILE1 | match2 | wc -l
rm $FILE1
