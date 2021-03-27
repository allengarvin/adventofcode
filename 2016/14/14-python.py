#!/usr/local/bin/python3.7

import sys, argparse, operator, re, string
from hashlib import md5

def md5hash(osalt, times):
    salt = osalt
    for n in range(times):
        hash = md5(salt.encode("ascii")).hexdigest()
        salt = hash

    return hash

def run_problem(original_salt, part1):
    n3 = {x : [] for x in string.hexdigits[:16]}
    n5 = {x : [] for x in string.hexdigits[:16]}

    ndx = 0

    while True:
        hash = md5hash("{:s}{:d}".format(original_salt, ndx), 1 if part1 == True else 2017)
        dupe3 = []
        for k, v in n3.items():
            if k*3 in hash:
                dupe3.append(hash.index(k))
            if k*5 in hash:
                n5[k].append(ndx)

        if len(dupe3):
            n3[hash[min(dupe3)]].append(ndx)

        ndx += 1

        if ndx % 1000 == 0:
            keys = []
            for k, v in n5.items():
                for v5 in v:
                    for v3 in n3[k]:
                        if v3 > v5 - 1000 and v3 < v5 and v3 not in keys:
                            keys.append(v3)
            if len(keys) > 64:
                keys = sorted(keys)
                break

    return keys

def main(args):
    original_salt = open(args.file).read().strip()


    print("Part 1:", run_problem(original_salt, True)[-1])
    print("Part 1:", run_problem(original_salt, False)[-1])

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2016 Day {0} AOC: One-Time Pad".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
