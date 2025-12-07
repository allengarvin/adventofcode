#!/usr/bin/python3

import sys, argparse, operator, re
import numpy as np
from io import StringIO
import operator as op
from functools import reduce

def cephalopod_numbers(col, w):
    nums = []
    for i in range(w):
        nums.append(int("".join([x[i] for x in col]).strip()))

    return nums
    
# ugh, fiddly!
def do_part2(grid):
    widths = []
    flag = False
    part2 = 0

    for ch in grid[-1]:
        if not flag: # first column
            flag = True
            i = 1
            continue
        if ch == " ":
            i += 1
            continue 
        else:
            widths.append(i-1)
            i = 1
    widths.append(i)

    start = 0
    column = []


    operators = [op.add if x == "+" else op.mul for x in grid[-1].strip().split()]

    for i, w in enumerate(widths):
        for line in grid[:-1]:
            column.append(line[start:start+w])
        real_column = cephalopod_numbers(column, w)
        part2 += reduce(operators[i], real_column)
        column = []
        start += w + 1

    return part2
        

def main(args):
    grid = ""
    grid2 = []
    with open(args.file) as fd:
        for line in fd:
            grid2.append(line[:-1]) # this'll probably break if windows line-endings
            line = line.lstrip()
            if line[0].isdigit():
                grid += line
            else:
                operators = [np.add if x == "+" else np.multiply for x in line.rstrip().split()]
    array = np.loadtxt(StringIO(grid))

    part1 = 0
    
    for i in range(array.shape[1]):
        #print(operators[i], array[:, i])

        col = array[:, i]
        #col2 = cephalopod_numbers(col)

        part1 += int(operators[i].reduce(col))

    print(part1)
    print(do_part2(grid2))
        
if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="20XX Day {0} AOC: Trash Compactor".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
