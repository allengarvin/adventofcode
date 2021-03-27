#!/usr/local/bin/python3.7

import sys, os, argparse, operator, re

def r_eval(s):
    c_map = { "\\":"\\\\", '"':'\\"' }
    return '"{0}"'.format("".join([c_map[c] if c in c_map else c for c in s]))

def main(args):
    lines = [x.strip() for x in open(args.file)]
    print("Part 1: {0}".format(sum([len(x) - len(eval(x)) for x in lines])))
    print("Part 2: {0}".format(sum([len(r_eval(x)) - len(x) for x in lines])))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2015 Day {0} AOC: Matchsticks".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
