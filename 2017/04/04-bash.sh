#!/bin/bash
# part 1 only... have to think about anagram detection

while read line; do
    if ! echo $line | tr \  '\n' | sort | uniq -c | grep -v '^ *1\>' | grep -q ^; then
        echo FOO; 
    fi
done < 04-input.txt | wc -l
