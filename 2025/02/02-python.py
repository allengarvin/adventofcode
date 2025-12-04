#!/usr/bin/python3

import sys, argparse, operator, re

def check_repeats(s):
    return s in (s + s)[1:-1]

def check_id(s):
    return len(s) % 2 == 0 and s[:len(s)//2] * 2 == s
    #return s[:len(s)//2] == s[len(s)//2:]

def main(args):
    part1, part2 = 0, 0
    for pairs in open(args.file).read().rstrip().split(","):
        a, b = [int(x) for x in pairs.split("-")]
        for i in range(a, b+1):
            si = str(i)
            if check_id(si):
                part1 += i
            if check_repeats(si):
                part2 += i 
    print(part1)
    print(part2)
        

    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2025 Day {0} AOC: Gift Shop".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
