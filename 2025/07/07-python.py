#!/usr/bin/python3

import sys, argparse, operator, re

    
    
def main(args):
    current_lines = []
    part1 = 0
    grid = []
    with open(args.file) as fd:
        for line in fd:
            line = line.strip()
            grid.append(line)
            if "S" in line:
                lines = set([line.index("S")])
            elif "^" in line:
                new_lines = set()
                for i, ch in enumerate(line):
                    if ch == "^" and i in lines:
                        part1 += 1
                        new_lines = new_lines.union(set([i-1,i+1]))
                    elif i in lines:
                        new_lines.add(i)
                lines = new_lines
    print(part1)
    
    cache = {}
    def path(y, x):
        if y + 1 == len(grid):
            return 1
        elif (y,x) in cache:
            return cache[(y,x)]
        elif grid[y][x] == "^":
            n = path(y + 1, x - 1) + path(y + 1, x + 1)
            cache[(y,x)] = n
            return n
    
        return path(y + 1, x)
    print(path(1, grid[0].index("S")))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="20XX Day {0} AOC: Laboratories".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
