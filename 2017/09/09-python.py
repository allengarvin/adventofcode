#!/usr/bin/python

import os, sys, itertools, string

def main():
    l = open("09-input.txt").read().strip()

    level = 0
    grp = 0
    score = 0

    scores = []

    garbage = False
    garbage_c = ""
    skip = False
    
    for ch in list(l):
        if ch == "!" and not skip:
            skip = True
        elif skip:
            skip = False
        elif garbage:
            if ch == ">":
                garbage = False
            else:
                garbage_c += ch
        elif ch == "<":
            garbage = True
        elif ch == "{":
            level += 1
            scores.append(level)
            grp += 1
        elif ch == "}":
            level -= 1
            score += scores.pop()

    #print "%-40s" % l, 
    print "Answer 1:", score
    print "Answer 2:", len(garbage_c)

if __name__ == "__main__":
    main()
