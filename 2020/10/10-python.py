#!/usr/bin/python

import sys, os, argparse, operator, re, itertools
from itertools import chain, combinations

def combs(l):
    return [1,1,2,4,7][len(l)-1]

def main(args):
    adaptors = sorted([int(x) for x in open(args.file).readlines()])

    a_range = [0] + adaptors + [adaptors[-1]+3]
    grouped = sorted([j-i for i, j in zip(a_range[:-1], a_range[1:])])
    grouped = map(len, [list(j) for i, j in itertools.groupby(grouped)])
    print(reduce(operator.mul, grouped))

    contiguous = [[0]]
    ptr = 0
    for i in range(1, len(a_range)):
        if a_range[i] - a_range[i-1] == 1:
            contiguous[ptr].append(a_range[i])
        else:
            contiguous.append([a_range[i]])
            ptr += 1
    #print(contiguous)
    print(reduce(operator.mul, map(combs, contiguous)))
        

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day 10 AOC: Adaptor Array")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    args = ap.parse_args()
    main(args)
    
