#!/usr/local/bin/python3.7

import sys, argparse, operator, re

def ancestor(orbits, a, b):
    for i in orbits[a]:
        if i in orbits[b]:
            return i

def main(args):
    parents = dict()

    o_map = dict()
    for line in open(args.file):
        a, b = line.strip().split(")")
        o_map[a] = o_map.get(a, []) + [ b ]
        parents[b] = a

    cnt = 0
    orbits = dict()

    for k, v in parents.items():
        orbits[k] = [v]
        p = parents[v] if v in parents else None
        while p:
            orbits[k] += [p]
            p = parents[p] if p in parents else None

    print("Part 1:", sum([len(v) for v in orbits.values()]))
    a, b, c = parents["YOU"], parents["SAN"], ancestor(orbits, "YOU", "SAN")
    print("Part 2:", len(orbits[a]) + len(orbits[b]) - 2 * len(orbits[c]))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2019 Day {0} AOC: Universal Orbit Map".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
