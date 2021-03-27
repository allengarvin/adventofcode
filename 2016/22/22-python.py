#!/usr/local/bin/python3.7

import sys, argparse, operator, re, itertools, heapq

# to get around ordering in the heap
class Position(complex):
    def __init__(self, n):
        self = n

    def __lt__(self, a): return 0 

def main(args):
    grid = dict()

    maxx = -1
    for line in open(args.file):
        d = re.findall("[0-9]+", line)
        if not d:
            continue
        x, y, *d, _ = [int(x) for x in d]
        pos = Position(x + y * 1j)
        grid[pos] = d
        maxx = max(x, maxx)
        if d[1] == 0:
            empty = pos

    total = 0
    use_map = set()
    for k1, k2 in itertools.permutations(grid.keys(), 2):
        a, b = grid[k1], grid[k2]
        if a[1] > 0 and a[1] <= b[2]:
            use_map.add((k1, k2))
    print("Part 1:", len(use_map))

    use_map.add(empty)

    distances = []
    visited = set()

    heapq.heappush(distances, (0, empty))
    dirs = [ -1j, 1, 1j, -1 ]

    while distances:
        dist, pos = heapq.heappop(distances)
        if pos == maxx:
            break

        adjacent = [Position(pos + d) for d in dirs if Position(pos+d) not in visited]
        for new_pos in adjacent:
            if new_pos in grid and (new_pos, empty) in use_map:
                heapq.heappush(distances, (dist+1, new_pos))
                visited.add(new_pos)
    # now the data is in maxx-1, 0
    # here we just observe we have to keep moving the empty node down,left,left,up,right until the data is in place
    print("Part 2:", dist + 5 * (maxx-1))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2016 Day {0} AOC: Grid Computing".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
