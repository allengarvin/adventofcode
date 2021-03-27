#!/usr/local/bin/python3.7

import sys, argparse, operator, re

def distance(p):
    return int(abs(p.real) + abs(p.imag))

def main(args):
    moves = list()
    for m in open(args.file).read().strip().split(", "):
        t, n = 1 if m[0] == "R" else -1, int(m[1:])
        moves.append((t,n))


    part2 = False
    direction = 0
    pos = 0
    visited = dict()
    dirs = [ -1j, 1, 1j, -1 ]

    for m in moves:
        direction = (direction + m[0]) % 4
        if not part2: 
            for i in range(m[1]):
                adj = pos + dirs[direction] * i 
                visited[adj] = visited.get(adj, 0) + 1
                if visited[adj] > 1:
                    part2 = adj
        pos += m[1] * dirs[direction]
        
    print("Part 1:", distance(pos))
    print("Part 2:", distance(part2))

    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2016 Day {0} AOC: No Time for a Taxicab".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
