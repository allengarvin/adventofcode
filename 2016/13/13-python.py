#!/usr/local/bin/python3.7

import sys, argparse, operator, re
import networkx as nx

def openp(pos, num):
    x = int(pos.real)
    y = int(pos.imag)
    if x < 0 or y < 0:
        return False
    return "{:b}".format(x**2 + 3*x + 2*x*y + y + y**2 + num).count("1") % 2 == 0
    
def adjacent(pos, num, visited):
    moves = [ -1j, 1, 1j, -1 ]

    return { pos + m for m in moves if openp(pos + m, num) and pos + m not in visited }

def main(args):
    num = int(open(args.file).read())

    moves = [ -1j, 1, 1j, -1 ]

    visited = { 1 + 1j }
    leading_edge = visited
    step = 0

    while 31 + 39j not in visited:
        new_edge = set()
        for i in leading_edge:
            new_edge |= adjacent(i, num, visited)
        visited |= leading_edge
        leading_edge = new_edge
        if step == 50:
            answer = len(visited)
        step += 1

    print("Part 1:", step)
    print("Part 2:", answer)
            
    
    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2016 Day {0} AOC: A Maze of Twisty Little Cubicles".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
