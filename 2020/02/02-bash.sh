#!/bin/bash

PART2=$(mktemp /tmp/aoc2020-02-2.XXXXXXX)
sed 's/[-:]/ /g' 02-input.txt | while read a b c d; do
    echo $d | tr -dC $c | egrep "$c{$a,$b}" | egrep -v "$c{$(($b+1))}"
    ((a--)); ((b--))
    echo ${d:$a:1}${d:$b:1} | tr -dC $c | grep '^.$' >> $PART2
done | wc -l

wc -l <$PART2
rm -f $PART2

