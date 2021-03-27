#!/usr/local/bin/python3.7

# I don't know how I solved this originally. This is a rewrite from scratch. Probably better than the original.

import sys, argparse
from functools import reduce
from operator import mul
import numpy as np

def comb_to(max_n, elements, prefix=[]):
    if( elements == 2 ):
        for i in range(1, max_n):
            yield prefix + [i, max_n - i]
    else:
        for i in range(1, max_n):
            for c in comb_to(max_n-i, elements-1, prefix=prefix + [i]):
                yield c
    
    
def main(args):
    ingredients = [ np.array([int(y) for _, y in [c.split() for c in b.split(", ")]])
                    for _, b in [ l.strip().split(": ") for l in open(args.file).readlines()] ]

    max1 = max2 = -1
    for c in comb_to(100, len(ingredients)):
        cookie = reduce(mul, [x if x > 0 else 0 for x in sum([x * c[i] for i, x in enumerate(ingredients)])[:-1]])
        if cookie:
            max1 = max(max1, cookie)
            if sum([x[-1] * c[i] for i, x in enumerate(ingredients)]) == 500:
                max2 = max(max2, cookie)
    print("Part 1:", max1)
    print("Part 2:", max2)


if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2015 Day {0} AOC: Science for Hungry People".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
