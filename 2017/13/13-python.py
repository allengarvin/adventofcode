#!/usr/bin/python

import sys

def main():
    pairs = []

    # I ended up deleting all my part1 code which simulated it, after
    # realizing running it for part 2 would take days

    for l in open("../advent/13-input.txt"):
        i, j = map(int, l.split(": "))
        pairs.append( (i, j*2-2) )

    score = 0
    for n in xrange(0xffffffff):
        p = [ (n+a) % b for a,b in pairs ]
        if 0 not in p:
            break
        
    print "Part 2: ", n

main()
