#!/usr/local/bin/python3.7

import sys, argparse, operator, re
from itertools import groupby

def look_say(s):
    result = ""
    for a, b in groupby(s):
        result += "{0}{1}".format(len(list(b)),a)
    
    return result

def main(args):
    l_str = args.start
    for i in range(1,51):
        l_str = look_say(l_str)
        if i == 40:
            print("Part 1: {0}".format(len(l_str)))
        if i == 50:
            print("Part 2: {0}".format(len(l_str)))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2015 Day {0} AOC: Elves Look, Elves Say".format(day))
    ap.add_argument("start", help="Start string", default="1113122113", nargs="?")
    main(ap.parse_args())
    
