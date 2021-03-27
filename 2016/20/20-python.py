#!/usr/local/bin/python3.7

import sys, argparse, operator, re

def main(args):
    pairs = [ sorted([int(x) for x in line.split("-")]) for line in open(args.file)]
    pairs = sorted(pairs, key=lambda x: x[0])

    allowed = []
    i = 0
    while True:
        for a, b in pairs:
            if a <= i <= b:
                i = b + 1
        if i >= 2**32:
            break
        allowed.append(i)
        i += 1

    print("Part 1:", allowed[0])
    print("Part 2:", len(allowed))
    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2016 Day {0} AOC: Firewall Rules".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
