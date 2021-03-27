#!/usr/bin/python

import os, sys, itertools, string
import numpy as np
from math import sqrt
from copy import deepcopy

def display2d(t):
    s = []
    for i in t:
        s.append("".join(i))

    return "\n".join(s)

def display(t):
    s = []
    for i in t:
        s.append("".join(i))

    return "/".join(s)

def rot90(p):
    return tuple(map(tuple, tuple(np.rot90(p))))

def flip(p):
    return tuple(map(tuple, tuple(p[::-1])))

def transform(rules, b):
    bt = map(list, b.split("/"))

    tried = []
    for j in [1,2]:
        for i in range(4):
            btmp = display(bt)
            tried.append(btmp)
            if btmp in rules.keys():
                return rules[btmp]
            bt = rot90(bt)
        bt = flip(bt)

    print "BUG BUG BUG ", b, "Not in rules"
    print "\n".join(tried)
    sys.exit(1)
        
def main():
    start = [
        ".#.",
        "..#",
        "###",
    ]

    rules = dict()
    for l in open("../advent/21-input.txt"):
        p = l.strip().split(" => ")
        rules[ p[0] ] = p[1]

    count = 0
    while True:
        blocks = []

        #print "Round", count, "starting with", start
        if len(start[0]) % 2 == 0:
            for j in range(0, len(start[0]), 2):
                for i in range(0, len(start[0]), 2):
                    block = start[j][i] + start[j][i+1] + "/" + \
                            start[j+1][i] + start[j+1][i+1]
                    blocks.append(block)
        else:
            for j in range(0, len(start[0]), 3):
                for i in range(0, len(start[0]), 3):
                    block = start[j][i] + start[j][i+1] + start[j][i+2] + "/" + \
                            start[j+1][i] + start[j+1][i+1] + start[j+1][i+2] + "/" + \
                            start[j+2][i] + start[j+2][i+1] + start[j+2][i+2]
                    blocks.append(block)
        
        newblocks = []
        #print "Split as", blocks
        for b in blocks:
            bnew = transform(rules, b)
            newblocks.append(bnew)
        
        if count == 0:
            start = newblocks[0].split("/")
        else:
            start = []
            b_sqrt = int(sqrt(len(newblocks)))
            for j in range(b_sqrt):
                tmp = []
                for i in range(b_sqrt):
                    if i == 0:
                        tmp = newblocks[j*b_sqrt+i].split("/")
                    else:
                        for k, row in enumerate(newblocks[j*b_sqrt+i].split("/")):
                            tmp[k] += row
                start += tmp

        count += 1
            
        lights = len("".join(start).replace(".", ""))
        #print " ", count, "Lights: ", lights

        if count == 5:
            print "Answer 1:", lights
        if count == 18:
            print "Answer 2:", lights
            sys.exit(1)
            
    return 1

if __name__ == "__main__":
    main()
