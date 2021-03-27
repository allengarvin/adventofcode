#!/usr/local/bin/python3.7

import sys, os, argparse
from operator import mul
from functools import reduce

class Box:
    def __init__(self, d):
        self.dim = [int(x) for x in d.split("x")]
        self.sides = [mul(*p) for p in zip(self.dim, self.dim[1:] + self.dim[:1])]

    def paper(self):
        return 2 * sum(self.sides) + min(self.sides)
        
    def ribbon(self):
        return 2 * sum(sorted(self.dim)[:2]) + reduce(mul, self.dim)

def main(args):
    boxes = [Box(x) for x in open(args.file)]
    print("Part 1: {0}".format(sum([x.paper() for x in boxes])))
    print("Part 2: {0}".format(sum([x.ribbon() for x in boxes])))
    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2015 Day {0} AOC: I Was Told There Would Be No Math".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
