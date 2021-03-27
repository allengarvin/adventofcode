#!/usr/bin/python

import sys, os, argparse
from itertools import product

def tuple_add(t1, t2):
    return tuple(map(lambda i, j: i + j, t1, t2))

def surround(p):
    s = set(map(lambda x: tuple_add(p, x), product(*[[-1,0,1]]*len(p))))
    s.remove(p)
    return s
    
def toggle(active, dimensions):
    new_space = set()

    for p in active:
        new_space = new_space.union(surround(p))
    new_space -= active

    new_active = set()
    new_inactive = set()
    for p in active:
        if 2 <= len(surround(p) & active) <= 3:
            new_active.add(p)
        else:
            new_inactive.add(p)
    for p in new_space:
        if len(surround(p) & active) == 3:
            new_active.add(p)
        else:
            new_inactive.add(p)
        
    return new_active - new_inactive

def main(args):
    threespace = set()
    fourspace = set()

    fd = open(args.file)
    for i, line in enumerate(open(args.file).readlines()):
        for j, char in enumerate(list(line.strip())):
            if char == '#':
                threespace.add((j, i, 0))
                fourspace.add((j, i, 0, 0))

    for i in range(6):
        threespace = toggle(threespace, 3)
        fourspace = toggle(fourspace, 4)
    print("Problem 1: {0}".format(len(threespace)))
    print("Problem 2: {0}".format(len(fourspace)))
        

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day 17 AOC: Conway cubes")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    main(ap.parse_args())
    
