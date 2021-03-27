#!/usr/local/bin/python3.7

import sys, argparse
from itertools import combinations
from operator import mul
from functools import reduce

def main(args):
    nums = [int(x) for x in open(args.file)]

    for n in [2,3]:
        print("Problem {0}: {1}".format(n-1, reduce(mul, [x for x in combinations(nums, n) if sum(x) == 2020][0])))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2020 Day {0} AOC: Report repair".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
