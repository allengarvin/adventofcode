#!/usr/local/bin/python3.7

import sys, os, argparse, operator, re

def main(args):
    instr = [-1 if x == ")" else 1 for x in open(args.file).readline().strip()]
    print("Part 1: {0}".format(sum(instr)))
    for i, x in enumerate(instr):
        instr[i] = x if i == 0 else instr[i-1] + x
    print("Part 2: {0}".format(instr.index(-1)+1))
    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2015 Day {0} AOC: Not Quite Lisp".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
