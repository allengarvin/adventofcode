#!/usr/bin/python

import sys, os, argparse, operator, re, itertools

def main(args):
    nums = map(int, open(args.file).readlines())
    print("Problem 1: {0}".format(sum(nums)))

    frequency = 0
    seen = {}
    n = 0

    while True:
        frequency += nums[n % len(nums)]
        if seen.get(frequency, 0):
            print("Problem 2: {0}".format(frequency))
            break
        seen[frequency] = 1
        n += 1

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2018 Day {0} AOC: Chronal Calibration".format(day))
    ap.add_argument("file", help="Input file", default="{0}-input.txt".format(day), nargs="?")
    main(ap.parse_args())
