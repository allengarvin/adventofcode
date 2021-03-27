#!/usr/bin/python

from datetime import datetime as DT
import os, sys, itertools, string

def main():
    instructions = open("../advent/16-input.txt").readline().strip().split(",")
    programs = string.ascii_lowercase[:16]

    original = programs
    limit = 10 ** 9

    count = 0
    def cycle(p):
        for l in instructions:
            if l[0] == "s":
                n = -int(l[1:])
                p = p[n:] + p[:n]
            elif l[0] == "x":
                a, b = sorted(map(int, l[1:].split("/")))
                p = p[:a] + p[b] + p[a+1:b] + p[a] + p[b+1:]
            elif l[0] == "p":
                a, b = sorted(map(lambda x: p.index(x), l[1:].split("/")))
                p = p[:a] + p[b] + p[a+1:b] + p[a] + p[b+1:]
        return p

    while True:
        programs = cycle(programs)

        if count == 0:
            print("Answer 1: {0}".format(programs))
        count += 1
        if programs == original:
            break
    for i in xrange(limit % count):
        programs = cycle(programs)
    
    print("Answer 2: {0}".format(programs))
            

if __name__ == "__main__":
    main()
