#!/usr/local/bin/python3.7

import sys, argparse, operator, re

def run_discs(discs):
    tm = 0
    while True:
        if not sum([(d[2] + i + tm) % d[0] for i, d in discs.items()]):
            break
        tm += 1
    return tm

def main(args):
    discs = {}
    high = -1
    for line in open(args.file):
        l = [int(x) for x in re.findall("[0-9]+", line)]
        high = l[0]
        discs[high] = l[1:4]

    print("Part 1:", run_discs(discs))
    discs[high+1] = [ 11, 0, 0 ]
    print("Part 2:", run_discs(discs))
        
if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2016 Day {0} AOC: Timing is Everything".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
