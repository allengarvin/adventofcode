#!/usr/bin/python3

import sys, argparse, re

def replace_all(s, r):
    for a, b in r: s = s.replace(a, b)
    return s

def calibrate(s):
    ns = re.sub("[a-z]", "", s)
    return int(ns[0] + ns[-1])
    
def main(args):
    total1, total2 = 0, 0

    values = open(args.file).read().strip().split("\n")
    cardinals =  [ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    replaces = [a+b+c for a,b,c in zip(cardinals, [str(x) for x in range(1,10)], cardinals)]

    print(sum([calibrate(x) for x in values]))
    print(sum([calibrate(replace_all(x, zip(cardinals, replaces))) for x in values]))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2023 Day {0} AOC: Trebuchet!".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
