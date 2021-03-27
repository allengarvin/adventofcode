#!/usr/local/bin/python3.7

import sys, argparse, operator, re
from parse import parse
from itertools import permutations

def main(args):
    cities = set()
    distances = dict()
    for l in open(args.file):
        metric = parse("{:w} to {:w} = {:d}\n", l) 
        c1, c2, d = metric
        cities |= set([c1,c2])
        distances[(c1,c2)] = distances[(c2,c1)] = d
        
    biggest, least = -1, 0xffffff
    for p in permutations(cities, len(cities)):
        total = sum([distances[x] for x in zip(p, p[1:])])
        biggest = max(total, biggest)
        least = min(total, least)

    print("Part 1: {0}".format(least))
    print("Part 2: {0}".format(biggest))
    
if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2015 Day {0} AOC: All in a Single Night".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
