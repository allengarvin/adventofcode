#!/usr/bin/python

import sys, argparse, operator, itertools, collections

def main(args):
    lines = [x.strip() for x in open(args.file).readlines()]
    counters = [collections.Counter(x).values() for x in lines]
    print("Problem 1: {0}".format(reduce(operator.mul, [sum([y in x for x in counters]) for y in [2,3]])))

    for a, b in itertools.combinations(lines, 2):
        common = filter(lambda p: p[0] == p[1], zip(a,b))
        if len(common) == len(a) - 1:
            print("Problem 2: {0}".format("".join([x for x,y in common])))
            break

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2018 Day {0} AOC: Inventory Management System".format(day))
    ap.add_argument("file", help="Input file", default="{0}-input.txt".format(day), nargs="?")
    main(ap.parse_args())
