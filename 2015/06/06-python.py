#!/usr/local/bin/python3.7

import sys, os, argparse, operator, re
from parse import parse

def range_iter(s):
    p = parse("{:d},{:d} through {:d},{:d}\n", s)
    for x in range(p[0], p[2]+1):
        for y in range(p[1], p[3]+1):
            yield x + y*1j
        
def main(args):
    grid = dict()

    instructions = open(args.file).readlines()

    for i in instructions:
        if i.startswith("turn on"):
            for n in range_iter(i[8:]):
                grid[n] = 1
        elif i.startswith("turn off"):
            for n in range_iter(i[9:]):
                grid[n] = 0
        elif i.startswith("toggle"):
            for n in range_iter(i[7:]):
                grid[n] = 1 - grid.get(n, 0)

    print("Part 1: {0}".format(sum(grid.values())))

    grid = dict()
    for i in instructions:
        if i.startswith("turn on"):
            for n in range_iter(i[8:]):
                grid[n] = grid.get(n, 0) + 1
        elif i.startswith("turn off"):
            for n in range_iter(i[9:]):
                val = grid.get(n, 0)
                if val:
                    grid[n] -= 1
        elif i.startswith("toggle"):
            for n in range_iter(i[7:]):
                grid[n] = grid.get(n, 0) + 2
    
    print("Part 2: {0}".format(sum(grid.values())))
        
    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2015 Day {0} AOC: Not Quite Lisp".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
