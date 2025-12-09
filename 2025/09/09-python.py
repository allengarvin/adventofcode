#!/usr/bin/python3

import sys, argparse, operator, re

def main(args):
    points = []
    with open(args.file) as fd:
        for line in fd:
            points.append(tuple([int(x) for x in line.strip().split(",")]))

    areas = {}
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points[i+1:]):
            x1, y1 = p1
            x2, y2 = p2

            areas[(abs(x2-x1)+1) * (abs(y2-y1)+1)] = (p1, p2)
    print(sorted(areas.keys())[-1])
            
if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="20XX Day {0} AOC: Movie Theater".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
