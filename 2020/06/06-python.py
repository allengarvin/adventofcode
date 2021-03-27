#!/usr/bin/python

import sys, os, argparse, operator

def main(args):
    answers1 = [set(x.replace("\n", "")) for x in open(args.file).read().split("\n\n")]
    print("Problem 1: %d" % sum(map(lambda x: len(set(x)), answers1)))

    answers2 = [map(set, x.split()) for x in open(args.file).read().split("\n\n")]
    print("Problem 2: %d" % sum([len(reduce(operator.and_, x)) for x in answers2]))

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day 6 AOC: Custom customs")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    main(ap.parse_args())
    
