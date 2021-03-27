#!/usr/local/bin/python3.7

import sys, argparse, operator, re
from itertools import permutations

def happiest(people, relations):
    most = -1
    for i in permutations(people, len(people)):
        l = list(i)
        total_happiness = 0
        for p1, p2 in zip(i, i[1:] + i[:1]):
            total_happiness += relations[(p1,p2)] + relations[(p2,p1)]
        most = max(total_happiness, most)
    return most

def main(args):
    lines = [l.strip().replace("gain ", "").replace("lose ", "-").rstrip(".").split() for l in open(args.file)]
    relations = { (k[0], k[-1].strip(".")) : int(k[2]) for k in lines }
    people = set([l[0] for l in lines])

    print("Part 1: {0}".format(happiest(people, relations)))
    for p in people:
        relations[(p, "you")] = relations[("you", p)] = 0
    people.add("you")
    print("Part 2: {0}".format(happiest(people, relations)))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2015 Day {0} AOC: Knights of the Dinner Table".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
