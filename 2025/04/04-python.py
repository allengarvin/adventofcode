#!/usr/bin/python3

import sys, argparse, operator, re

def cell_clear(grid, y, x):
    cnt = 0
    if y > 0:
        cnt += sum(grid[y-1][0 if x == 0 else x-1:x+2])
    if x > 0:
        cnt += grid[y][x-1]
    if x < len(grid[y]) -1:
        cnt += grid[y][x+1]
    if y < len(grid)-1:
        cnt += sum(grid[y+1][0 if x == 0 else x-1:x+2])
    return cnt < 4
        
def iterate(grid):
    cells_accessible = []
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            if cell == 1:
                if cell_clear(grid, y, x):
                    cells_accessible.append((y,x))
    return cells_accessible

def print_grid(grid):
    newpic = ""
    for y, line in enumerate(grid):
        for x, cell in enumerate(line):
            newpic += "@" if cell else "."
        newpic += "\n"
    print(newpic)

def main(args):
    grid = []
    with open(args.file) as fd:
        for line in fd:
            grid.append([1 if s == "@" else 0 for s in line.strip()])

    part1, part2 = None, 0

    to_clear = iterate(grid)
    if not part1:
        part1 = len(to_clear)
    while len(to_clear):
        for pair in to_clear:
            y, x = pair
            grid[y][x] = 0
        # print_grid(grid)
        part2 += len(to_clear)
        to_clear = iterate(grid)
    print(part1)
    print(part2)

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2025 Day {0} AOC: Printing Department".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
