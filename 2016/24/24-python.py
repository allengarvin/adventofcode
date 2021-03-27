#!/usr/local/bin/python3.7

import sys, argparse, operator, re
from itertools import permutations, combinations
import networkx as nx

def main(args):
    grid_set = set()
    locations = dict()

    for y, line in enumerate(open(args.file)):
        for x, ch in enumerate(line.strip()):
            pos = x + y * 1j
            if ch.isdigit():
                locations[int(ch)] = pos
                ch = "."
            if ch == ".":
                grid_set.add(pos)
    directions = [ -1j, 1, 1j, -1 ]

    grid = nx.Graph()
    for p in grid_set:
        grid.add_node(p)
        for d in directions:
            if p + d in grid_set:
                grid.add_edge(p, p + d)
            
    distances = dict()
    for a, b in combinations(locations.items(), 2):
        distances[(a[0],b[0])] = distances[(b[0], a[0])] = len(nx.shortest_path(grid, a[1], b[1])) - 1

    min_dist = min_dist2 = 0xffffffff

    for perm in permutations(sorted(locations.keys())[1:], len(locations.keys())-1):
        dist = distances[(0, perm[0])]
        for i in range(len(perm)-1):
            dist += distances[(perm[i], perm[i+1])]
        p2_dist = dist + distances[(perm[-1], 0)]

        min_dist = min(min_dist, dist)
        min_dist2 = min(min_dist2, p2_dist)

    print("Part 1:", min_dist)
    print("Part 2:", min_dist2)
    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2016 Day {0} AOC: Air Duct Spelunking".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
