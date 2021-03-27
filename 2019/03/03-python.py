#!/usr/bin/python3

import sys

def calc_path(moves):
    steps = {"U":-1j, "D":1j, "L":-1, "R":1}
    return [(steps[m[0]], int(m[1:])) for m in moves.split(",")]

def wire_path(moves):
    p, position, cnt = {}, 0, 1
    for m, n in moves:
        for i in range(1, n+1):
            position += m
            p[position] = cnt
            cnt += 1
    return p
        
def taxi(p):
    return abs(int(p.real)) + abs(int(p.imag))

def main(fn):
    wires = [calc_path(line.strip()) for line in open(fn)]
    points = [wire_path(w) for w in wires]
    intersections = points[0].keys() & points[1].keys()
    print(min([taxi(p) for p in intersections]))
    print(min([points[0][p] + points[1][p] for p in intersections]))

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    main(default_file if len(sys.argv) == 1 else sys.argv[1])
 
