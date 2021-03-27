#!/usr/local/bin/python3.7

import sys, os, argparse, operator, re, string

def nice1(s):
    if len(re.findall("[aeiou]", s)) < 3:
        return False
    if sum([l+l in s for l in string.ascii_lowercase]) == 0:
        return False
    if sum([x in s for x in ["ab", "cd", "pq", "xy"]]):
        return False
    return True

def nice2(s):
    con1 = con2 = False
    for i, c in enumerate(s):
        if c == s[i+2:i+3]:
            con1 = True
        if s[i:i+2] in s[i+2:]:
            con2 = True
    return con1 and con2

def main(args):
    strings = [x.strip() for x in open(args.file)]
    
    print("Part 1: {0}".format(sum([nice1(s) for s in strings])))
    print("Part 2: {0}".format(sum([nice2(s) for s in strings])))
    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2015 Day {0} AOC: Doesn't He Have Intern-Elves For This?".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
