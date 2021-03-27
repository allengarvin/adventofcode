#!/usr/local/bin/python3.7

import sys, argparse, operator, re
from fractions import Fraction

def count(space, pos):
    final = set()

    x1, y1 = pos
    for x2, y2 in space:
        if x1 == x2:
            if y1 < y2:
                final.add(0xffff)
            else:
                final.add(-0xffff)
            continue
        slope = Fraction(y2-y1, x2-x1)
        if x2 < x1:
            final.add((slope.numerator, slope.denominator, -1))
        else:
            final.add((slope.numerator, slope.denominator, 1))
        
    return len(final)

def main(args):
    space = set()
    for j, line in enumerate(open(args.file)):
        for i, c in enumerate(line.strip()):
            if c == "#":
                space.add((i,j))

    visible = dict()
    visible = { p : count(space, p) for p in space }
    print("Part 1:", visible[sorted(visible.keys(), key=lambda x: visible[x])[-1]])
        
        
    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2019 Day {0} AOC: Not Quite Lisp".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
