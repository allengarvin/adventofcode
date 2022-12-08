#!/usr/bin/python3

import sys, argparse, operator, re
from functools import reduce

def prod(x):
    return reduce(operator.mul, x, 1)

def main(args):
    grid = []
    part1, part2 = 0, [0, 0, 0, 0]
    for line in open(args.file):
        grid.append([int(x) for x in line.strip()])
    for y, row in enumerate(grid):
        for x, tree in enumerate(row):
            if y == 0 or x == 0 or y + 1 == len(grid) or x + 1 == len(row):
                part1 += 1
            else:
                to_edge = [
                        [True if t < tree else False for t in row[:x]][::-1],
                        [True if t < tree else False for t in row[x+1:]],
                        [True if t[x] < tree else False for t in grid[:y]][::-1],
                        [True if t[x] < tree else False for t in grid[y+1:]]
                    ]

                for e in to_edge:
                    if False not in e:
                        part1 += 1
                        break
                counts = [ 0 ] * 4
                p2c = 0
                for i, e in enumerate(to_edge):
                    for t in e:
                        p2c += 1
                        counts[i] += 1
                        if not t:
                            break
                # print(x, y, counts)
                if prod(counts) > prod(part2):
                    part2 = counts.copy()
                
    print(part1)
    print(prod(part2))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2022 Day {0} AOC: Treetop Tree House".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
