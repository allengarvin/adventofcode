#!/usr/local/bin/python3.7

import sys, argparse, operator, re
from parse import parse
import numpy as np

def display(grid):
    cnt = 0

    s = ""
    for y in range(len(grid)):
        s += "".join(["#" if grid[y][x] else "." for x in range(len(grid[y]))]) + "\n"

    return s.count("#"), s.strip()

def main(args):
    maxx, maxy = 50, 6
    grid = np.zeros((maxy,maxx), dtype=int)

    instructions = []
    for line in open(args.file):
        a, b = [int(x) for x in re.findall(r"[0-9]+", line)]
        if "rect" in line:
            for x in range(a):
                for y in range(b):
                    grid[y][x] = 1
        if "rotate row" in line:
            grid[a,:] = np.concatenate((grid[a,:][-b:], grid[a,:][:-b]))
        if "rotate column" in line:
            grid[:,a] = np.concatenate((grid[:,a][-b:], grid[:,a][:-b]))
    
    cnt, txt = display(grid)
    print("Part 1:", cnt, "\nPart 2:")
    print(txt)
            

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2016 Day {0} AOC: Two-Factor Authentication".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
