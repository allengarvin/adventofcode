#!/usr/local/bin/python3.7

import sys, argparse, operator, re
from itertools import combinations
from functools import reduce

def prod(n): return reduce(operator.mul, n)

def least(nums, partitions):
    target = sum(nums) // partitions

    nums = sorted(nums)
    for i, n in enumerate(reversed(nums)):
        if sum(nums[::-1][:i]) >= target:
            min_size = i
            break

    min_qe = 0xffffffffffffffff
    for i in range(min_size, len(nums) - min_size):
        for c in combinations(nums, i):
            if sum(c) == target:
                min_qe = min(min_qe, prod(c))
        if min_qe < 0xffffffffffffffff:
            break

    return min_qe

def main(args):
    nums = [int(x) for x in open(args.file)]

    print("Part 1: {0}".format(least(nums, 3)))
    print("Part 2: {0}".format(least(nums, 4)))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2015 Day {0} AOC: It Hangs in the Balance".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
