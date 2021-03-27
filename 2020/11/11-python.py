#!/usr/bin/python

import sys, os, argparse, operator, re

def square(c):
    return ["L", "#", "."][c]

def new_seat(adjacent_states, my_state, max):
    if 1 not in adjacent_states:
        return 1

    if adjacent_states.count(1) >= max:
        return 0

    return my_state

def tuple_add(t1, t2):
    return tuple(map(lambda i, j: i + j, t1, t2))

def adjacent(ferry, pos):
    deltas = [ (-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1) ]
    return filter(lambda x: x in ferry and ferry[x] == 0, [tuple_add(pos, x) for x in deltas])

def linear(ferry, pos):
    deltas = [ (-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1) ]

    lines = {p: [] for p in deltas}
    for d in deltas:
        new_pos = tuple_add(pos, d)
        while new_pos in ferry:
            if ferry[new_pos] == -1:
                new_pos = tuple_add(new_pos, d)
                continue
            lines[d].append(new_pos)
            break
    return reduce(operator.add, lines.values())

def print_map(ferry):
    lr = sorted(ferry.keys())[-1]
    mp = ""
    for y in range(lr[0]+1):
        mp += "".join([square(ferry[p]) for p in sorted(filter(lambda p: p[0] == y, ferry.keys()))]) + "\n"
    return mp

def one_turn(ferry, adjacents, max):
    new_map = dict()
    for q in ferry.keys():
        if ferry[q] == -1:
            new_map[q] = -1
            continue

        #adj = adjacent(ferry, q)
        adj = adjacents[q]

        new_map[q] = new_seat([ferry[p] for p in adj], ferry[q], max)

    return new_map
    
def execute(ferry, adjacency_map, max_seats):
    prev = print_map(ferry)
    while True:
        new_ferry = one_turn(ferry, adjacency_map, max_seats)
        mp = print_map(new_ferry)
 
        if mp == prev:
            return mp.count("#")
        ferry = new_ferry
        prev = print_map(ferry)

def main(args):
    fd = open(args.file)
    lines = [map(lambda y: -1 if y == "." else 0, list(x.strip())) for x in open(args.file).readlines()]

    ferry = dict()
    for y, row in enumerate(lines):
        for x, cell in enumerate(lines[y]):
            ferry[(y,x)] = cell
    orig_ferry = ferry.copy()

    adjacent_prob1 = { p: adjacent(ferry, p) for p in ferry.keys() }
    adjacent_prob2 = { p: linear(ferry, p) for p in ferry.keys() }

    print("Problem 1: %d" % execute(ferry, adjacent_prob1, 4))
    print("Problem 2: %d" % execute(ferry, adjacent_prob2, 5))

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day 11 AOC: Seating system")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    args = ap.parse_args()
    main(args)
    
