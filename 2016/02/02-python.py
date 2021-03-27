#!/usr/local/bin/python3.7

import sys, argparse, operator, re

def eval_instr(grid, pos, instr):
    directions = { "U" : -1j, "R" : 1, "D" : 1j, "L" : -1 }

    for i in instr:
        if pos + directions[i] in grid:
            pos += directions[i]
    return grid[pos], pos

def run_code(grid, starting_pos, instructions):
    code = ""
    pos = starting_pos
    for x in instructions:
        n, pos = eval_instr(grid, pos, x)
        code += str(n)

    return code
    
def main(args):
    instructions = [l.strip() for l in open(args.file)]
    grid = dict()

    for i in range(1, 10):
        grid[((i-1) % 3) + (i-1) // 3 * 1j] = i

    print("Part 1:", run_code(grid, 1 + 1j, instructions))

    g2_pos = [ 2+0j, 1+1j, 2+1j, 3+1j, 0+2j, 1+2j, 2+2j, 3+2j, 4+2j, 1+3j, 2+3j, 3+3j, 2+4j ]
    grid = {}
    for i, p in enumerate(g2_pos):
        grid[p] = "{:X}".format(i+1)

    print("Part 2:", run_code(grid, 2 + 2j, instructions))
            

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2016 Day {0} AOC: Bathroom Security".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
