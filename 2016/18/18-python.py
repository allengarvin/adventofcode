#!/usr/local/bin/python3.7

import sys, argparse, operator, re, string

def main(args):
    break1, break2 = 40, 400000

    to_binary = str.maketrans(".^", "01")
    s = open(args.file).read().strip().translate(to_binary)
    log = len(s)

    row = int(s, 2)

    i = 1
    total = 0

    while True:
        total += log - "{:b}".format(row, log=log).count("1")

        row = ((row ^ (row>>1)) ^ (row ^ (row<<1))) & (2 ** log - 1)
        if i == break1:
            print("Part 1:", total)
        if i == break2:
            print("Part 2:", total)
            return
        i += 1
        

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2016 Day {0} AOC: Like a Rogue".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
