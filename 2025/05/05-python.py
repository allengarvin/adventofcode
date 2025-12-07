#!/usr/bin/python3

import sys, argparse, operator, re

# first attempt doing set unions blew up and froze my computer for a minute!
def range_union(ranges):
    ranges = sorted(ranges)

    total = 0
    c_sta, c_end = ranges[0]

    for sta, end in ranges[1:]:
        if sta <= c_end + 1:
            c_end = max(c_end, end)
        else:
            total += c_end - c_sta + 1
            c_sta, c_end = sta, end
    return total + c_end - c_sta + 1

def main(args):
    ranges = []
    
    ingredients = []
    with open(args.file) as fd:
        for line in fd:
            line = line.strip()
            if "-" in line:
                a, b = [int(x) for x in line.split("-")]
                ranges.append((a,b))
            elif line:
                ingredients.append(int(line))

    part1 = 0
    for i in ingredients:
        for r in ranges:
            if i in range(r[0], r[1]+1):
                part1 += 1
                break
    print(part1)
    print(range_union(ranges))
                
if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="20XX Day {0} AOC: Cafeteria".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
