#!/usr/bin/python3

import sys, argparse, operator, re

def set_range(s):
    a, b = [int(x) for x in s.split("-")]
    return set(range(a, b+1))

def main(args):
    part1, part2 = 0, 0

    for line in open(args.file):
        e1, e2 = [set_range(x) for x in line.strip().split(",")]
        if e1.issubset(e2) or e2.issubset(e1):
            part1 += 1
        if e1.intersection(e2):
            part2 += 1
    print(part1)
    print(part2)

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2022 Day {0} AOC: Camp Cleanup".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
