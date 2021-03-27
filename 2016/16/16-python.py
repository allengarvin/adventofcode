#!/usr/local/bin/python3.7

import sys, argparse, operator, re

def str_xor(s):
    return s.replace("0", "_").replace("1", "0").replace("_", "1")

def step(s):
    return s + "0" + str_xor(s[::-1])

def cksum(a):
    return "".join(["1" if a[i] == a[i+1] else "0" for i in range(0, len(a), 2)])

def transform(istate, ilen):
    while len(istate) < ilen:
        istate = step(istate)

    istate = istate[:ilen]
    c = cksum(istate)
    while len(c) % 2 == 0:
        c = cksum(c)
    return c

def main(args):
    istate = open(args.file).read().strip()
    print("Part 1:", transform(istate, 272))
    print("Part 2:", transform(istate, 35651584))
    
if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2016 Day {0} AOC: Dragon Checksum".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
