#!/usr/bin/python3

import sys, argparse, operator, re

def main(args):
    fd = open(args.file)
    elves = [[]]
    for line in fd:
        if line.strip().isdecimal():
            elves[-1].append(int(line))
        else:
            elves.append([])
    sums = sorted([sum(x) for x in elves])
    print(sums[-1])
    print(sum(sums[-3:]))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2022 Day {0} AOC: Calorie Counting".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
