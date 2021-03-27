#!/usr/local/bin/python3.7

import sys, argparse, operator, re
import json

def recurse(js, redcheck=False):
    cnt = 0
    if isinstance(js, dict):
        for k, v in js.items():
            if redcheck and js[k] == "red":
                return 0
            cnt += recurse(v, redcheck=redcheck)
    elif isinstance(js, list):
        for v in js:
            cnt += recurse(v, redcheck=redcheck)
    elif isinstance(js, int):
        cnt += js

    return cnt
def main(args):
    js = json.load(open(args.file))
    print("Part 1: {0}".format(recurse(js)))
    print("Part 2: {0}".format(recurse(js, redcheck=True)))
    
if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2015 Day {0} AOC: JSAbacusFramework.io".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
