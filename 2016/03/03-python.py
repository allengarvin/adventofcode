#!/usr/local/bin/python3.7

import sys, argparse, operator, re
from itertools import permutations
import numpy as np

def valid(triangle):
    for t in permutations(triangle, 3):
        if sum(*[t[:2]]) <= t[2]:
            return False
    return True

def main(args):
    triangles = [[int(y) for y in line.strip().split()] for line in open(args.file)]
    triangles2 = []

    for i, t in enumerate(triangles):
        if (i + 1) % 3 == 0:
            for t2 in np.rot90(triangles[i-2:i+1], k=1, axes=(1,0)):
                triangles2.append(list(t2))
    
    print("Part 1:", sum([valid(t) for t in triangles]))
    print("Part 2:", sum([valid(t) for t in triangles2]))
    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2016 Day {0} AOC: Squares With Three Sides".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
