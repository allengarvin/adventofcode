#!/usr/bin/python3

import argparse, sys

def increasingp(lst):
    return len([n for n, x in enumerate(lst[1:]) if x > lst[n]])

def main(args):
    nums = [int(x) for x in open(args.file)]
    print("Problem 1: {}".format(increasingp(nums)))
    print("Problem 2: {}".format(increasingp([sum(nums[i:i+3]) for i in range(len(nums)-2)])))

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2021 Day 1 AOC: Sonar Sweep")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    main(ap.parse_args())
    
