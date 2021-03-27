#!/bin/bash

total1=0
total2=0

cat ${1:-02-input.txt} | tr ':-' \ | while read a b c d; do 
    count=$(echo $d | tr -dc $c | wc -c)
    ((total1 += ($count >= $a && count <= $b) ))
    ((a--)); ((b--))
    if [[ (${d:$a:1} == $c && ${d:$b:1} != $c) || (${d:$a:1} != $c && ${d:$b:1} == $c) ]]; then
        ((total2 += 1))
    fi
    echo $total1
    echo $total2
done | tail -2      # stupid bash scoping


