#!/usr/bin/python3

import sys, argparse, operator, re

def main(args):
    p1 = False
    line = open(args.file).read().strip()
    for i in range(4, len(line)):
        if not p1 and len(set(line[i-4:i])) == 4:
            p1 = True
            print("part1", i)
        if len(set(line[i-14:i])) == 14:
            print("part2", i)
            break

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2022 Day {0} AOC: Tuning Trouble".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
