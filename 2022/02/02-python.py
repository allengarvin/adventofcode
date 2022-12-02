#!/usr/bin/python3

import sys, argparse, operator, re

def main(args):
    score_grid = [ [0, 1, -1], [ -1, 0, 1], [1, -1, 0] ]
    part1 = 0
    part2 = 0
    for line in open(args.file):
        e, p = line.strip().split()
        en, pn = ord(e)-65, ord(p)-88
        p2n = score_grid[en].index([-1,0,1][pn])
        part1 += (score_grid[en][pn]+1)*3 + pn + 1
        part2 += (score_grid[en][p2n]+1)*3 + p2n + 1

    print(part1)
    print(part2)

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2022 Day {0} AOC: Rock Paper Scissors".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
