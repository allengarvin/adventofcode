#!/usr/local/bin/python3.7

import sys, argparse, operator, re, collections

def common(a, part1):
    return collections.Counter(a).most_common()[0 if part1 else -1][0]

def main(args):
    lines = [l.strip() for l in open(args.file)]
    columns = [common([x[i] for x in lines], True) for i in range(len(lines[0]))]
    print("Part 1:", "".join(columns))
    columns = [common([x[i] for x in lines], False) for i in range(len(lines[0]))]
    print("Part 2:", "".join(columns))
    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2016 Day {0} AOC: Signals and Noise".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
