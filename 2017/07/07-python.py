#!/usr/bin/python

import os, sys, itertools, string
from parse import parse

def weights(root, progs, depth):
    pad = "  " * depth
    wt = progs[root][0]
    mywt = wt


    for i in progs[root][1]:
        wt += weights(i, progs, depth + 1)
    # print pad + root, " (%d) (%d)" % (mywt, wt)
    if depth == 0:
        return root
    return wt

def main(argv):
    progs = dict()

    for l in open("07-input.txt"):
        l = l.strip()
        if "->" in l:
            p = parse("{} ({}) -> {}", l)
            progs[p[0]] = [ int(p[1]), p[2].split(", ") ]
        else:
            p = parse("{} ({})", l)
            progs[p[0]] = [ int(p[1]), [] ]
        # print progs[p[0]]

    for i in progs.keys():
        flag = False
        for j in progs.keys():
            if i in progs[j][1]:
                flag = True
                break
        if flag:
            continue
        root = i
        break

    print weights(root, progs, 0)

if __name__ == "__main__":
    main(sys.argv)
