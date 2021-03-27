#!/usr/local/bin/python3.7

import sys, os, argparse

def transform(subject, keys, setloops):
    val = cnt = 1
    while True:
        val = (val * subject) % 20201227
        if keys:
            for i, k in enumerate(keys):
                if val == k:
                    return cnt, keys[1-i]
        elif cnt == setloops:
                return val
        cnt += 1
        
def main(args):
    keys = [int(n) for n in open(args.file)]

    m, k = transform(7, keys, False)
    print("Part 1: {0}".format(transform(k, [], m)))
    
if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2020 Day {0} AOC: Combo Breaker".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
