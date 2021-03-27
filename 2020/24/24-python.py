#!/usr/local/bin/python3.7

import sys, os, argparse, re

def main(args):
    floor = dict()

    # Thanks boucher for regex parsing and idea for using complex ints
    tiles = [re.findall("[ns][ew]|e|w", h) for h in open(args.file)]
    shifts_c = { "ne" : 1 -1j, "se" : 1 + 1j, "nw" : -1 - 1j, "sw" : -1 + 1j, "w" : -2, "e" : 2 }

    for t in tiles:
        d = sum([shifts_c[x] for x in t])
        floor[d] = 1 - floor.get(d, 0)
    
    print("Problem 1: {0}".format(sum(floor.values())))

    for day in range(100):
        new_floor = dict()
        new_floor.update(floor)
        for p in floor.keys():
            new_floor.update({ p + p1 : floor.get(p + p1, 0) for p1 in shifts_c.values() })
    
        for p in new_floor:
            black_count = sum([floor.get(p + p1, 0) for p1 in shifts_c.values()])
            if new_floor[p]:
                if black_count == 0 or black_count > 2:
                    new_floor[p] = 0
            elif black_count == 2:
                new_floor[p] = 1

        for p in list(new_floor.keys()):
            if not new_floor[p]:
                del new_floor[p]
        floor = new_floor
            
        # print("Day {0}: {1}".format(day+1, sum(floor.values())))
    print("Problem 2: {0}".format(sum(floor.values())))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2020 Day {0} AOC: Lobby Layout".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
