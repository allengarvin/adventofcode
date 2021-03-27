#!/usr/bin/python

import sys, os, argparse, operator, re
from parse import parse

def flatten(t):
    flat_list = []
    for sublist in t:
        for item in sublist:
            flat_list.append(item)
    return flat_list

def cycle(number, pattern, iteration):
    p = flatten([[x] * (iteration+1) for x in pattern])
    print p
    print [x * p[i % len(p)] for i, x in enumerate(number)]
    
def main(args):
    number = map(int, list(open(args.file).read().strip()))
    print cycle(number, [0,1,0,-1], 0)
    print cycle(number, [0,1,0,-1], 1)
    print cycle(number, [0,1,0,-1], 2)
    print number

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2020 Day {0} AOC: FOO FOO".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
