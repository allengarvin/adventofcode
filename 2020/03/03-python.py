#!/usr/bin/python

import sys, os, argparse, operator

def treecount(grid, slope):
    y = x = count = 0
    side = len(grid[0])
    
    while y < len(grid):
        count += grid[y][x]
        y, x = y + slope[0], (x + slope[1]) % side
    return count

def main(args):
    fd = open(args.file)
    grid = []
    for line in fd:
        grid.append([1 if x == "#" else 0 for x in list(line.strip())])

    print("Problem 1: %d" % treecount(grid, (1, 3)))
    print("Problem 2: %d" % reduce(operator.mul, [treecount(grid, (y,x)) for y, x in (1,1), (1,3), (1,5), (1,7), (2,1)]))

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day 3 AOC: Toboggan trajectory")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    main(ap.parse_args())
    
