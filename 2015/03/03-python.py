#!/usr/bin/python3

import sys, os, argparse, operator, re

def main(args):
    d = { ">":1, "<":-1, "^":-1j, "v":1j }
    dirs = [d[x] for x in open(args.file).readline().strip()]
    
    homes = { 0 : 1 } 
    pos = 0
    for x in dirs:
        pos += x
        homes[pos] = homes.get(pos, 0) + 1
    
    print("Part 1: {0}".format(len(homes)))

    homes = { 0 : 1 }
    rpos = pos = 0
    for i, x in enumerate(dirs):
        if i % 2:
            rpos += x
            homes[rpos] = homes.get(rpos, 0) + 1
        else:
            pos += x
            homes[pos] = homes.get(pos, 0) + 1

    print("Part 2: {0}".format(len(homes)))

if __name__ == "__main__":
    homes = { 0 : 1 } 
    pos = 0
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2015 Day {0} AOC: Perfectly Spherical Houses in a Vacuum".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
