#!/usr/local/bin/python3.7

import sys, argparse, operator, re

def decompress(s, recurse):
    pos = 0
    cnt = 0

    while pos < len(s):
        if s[pos] == "(":
            end = s.find(")", pos)

            l, n = [int(x) for x in s[pos+1:end].split("x")]
            t = s[end+1:end+1+l]
            ln = l

            if recurse:
                ln = decompress(s[end+1:end+1+l], True)
                cnt += ln * n
            else:
                cnt += ln * n
            pos = end + 1 + l
        else:
            pos += 1
            cnt += 1

    return cnt

def main(args):
    s = open(args.file).read().strip()

    print("Part 1:", decompress(s, False))
    print("Part 2:", decompress(s, True))
    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2016 Day {0} AOC: Explosives in Cyberspace".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
