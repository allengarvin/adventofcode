#!/usr/bin/python2

import sys, os, argparse, operator, re
from hashlib import md5

def main(args):
    i = 1
    p1 = False
    while True:
        hash = md5((args.key + str(i)).encode("utf-8")).hexdigest()
        if not p1 and hash.startswith("00000"):
            print("Part 1: {0}".format(i))
            p1 = True
        if hash.startswith("000000"):
            print("Part 2: {0}".format(i))
            break
        i += 1
    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2015 Day {0} AOC: The Ideal Stocking Stuffer".format(day))
    ap.add_argument("key", help="secret key", default="bgvyzdsv", nargs="?")
    main(ap.parse_args())
    
