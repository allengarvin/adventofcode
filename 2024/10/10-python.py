#!/usr/bin/python3

import sys, argparse, operator, re

def in_gridP(pos, grid):
    x, y = int(pos.real), int(pos.imag)
    return x >= 0 and y >= 0 and y < len(grid) and x < len(grid[0])

def grid_value(pos, grid):
    return grid[int(pos.imag)][int(pos.real)]

def count_paths(pos, grid, sval):
    if grid_value(pos, grid) == 9:
        return 1

    n, s, w, e = complex(0,-1), complex(0,1), complex(-1,0), complex(1,0)
    paths = 0
    for d in [n,s,e,w]:
        new_pos = pos+d
        if in_gridP(new_pos, grid) and grid_value(new_pos, grid) == sval+1:
            paths += count_paths(new_pos, grid, sval+1)
    return paths

def find_paths(pos, grid, sval, positions):
    if grid_value(pos, grid) == 9:
        return set([pos])

    n, s, w, e = complex(0,-1), complex(0,1), complex(-1,0), complex(1,0)
    for d in [n,s,e,w]:
        new_pos = pos+d
        if in_gridP(new_pos, grid) and grid_value(new_pos, grid) == sval+1:
            v = find_paths(new_pos, grid, sval+1, positions)
            positions = positions.union(v)
    return positions

def main(args):
    grid = []
    trailheads = []
    with open(args.file) as fd:
        for j, line in enumerate(fd):
            grid.append([int(x) for x in line.strip()])
            for i, n in enumerate(grid[-1]):
                if n == 0:
                    trailheads.append(complex(i, j))

    total1, total2 = 0, 0
    for pos in trailheads:
        v, c = find_paths(pos, grid, 0, set()), count_paths(pos, grid, 0)
        #print("From", pos, "we have a total of", len(v))
        total1 += len(v)
        total2 += c

    print(total1)
    print(total2)

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2024 Day {0} AOC: Hoof It".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())

