#!/bin/bash

# ha ha ha, I don't know if this is brilliant or what: 
# https://bobcopeland.com/blog/2012/10/goto-in-bash/
function goto
{
    label=$1
    cmd=$(sed -n "/$label:/{:a;n;p;ba};" $0 | grep -v ':$')
    eval "$cmd"
    exit
}

mapfile num < 01-input.txt
for j in ${num[@]}; do for i in ${num[@]}; do ((2020 == $j + $i)) && echo $(($j * $i)) && goto part2; done; done

part2:
for k in ${num[@]}; do for j in ${num[@]}; do for i in ${num[@]}; do 
    ((2020 == $k + $j + $i)) && echo $(($k * $j * $i)) && goto finished; 
done; done; done

finished:
