#!/usr/bin/python3

import sys, os, argparse, operator, re

def main(args):
    nums = sorted([int(n, 2) for n in open(args.file).read().translate(str.maketrans({"F":"0", "B":"1", "R":"1", "L":"0"})).splitlines()])
    print("Problem 1: %d" % nums[-1])
    print("Problem 2: %d" % list(set(range(nums[0], nums[-1])) - set(nums))[0])
        
if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day 5 AOC: Binary boarding")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    main(ap.parse_args())
    
