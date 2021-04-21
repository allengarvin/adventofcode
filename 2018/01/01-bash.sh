#!/bin/bash

# Part 1 only
sed 's/^+//;$!s/$/ +/' 01-input.txt | xargs | bc
