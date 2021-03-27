#!/usr/bin/python

import sys, os, argparse, operator, re, itertools, math
from parse import parse

def tuple_add(t1, t2):
    return tuple(map(lambda i, j: i + j, t1, t2))

class Point:
    pos = [0, 0]
    vel = [0, 0]

    def __init__(self, s):
        self.pos = map(int, s[s.find("<", 1)+1:s.find(">", 1)].split(","))
        self.vel = map(int, s[s.find("<", s.find("velocity"))+1:s.find(">", s.find("velocity"))].split(","))

    def __str__(self):
        return "[p=<{0:d}, {1:d}>-".format(*self.pos) + "v=<{0:d}, {1:d}>]".format(*self.vel)

    def __repr__(self):
        return str(self)

    def time(self, n):
        return tuple_add(self.pos, [self.vel[0] * n, self.vel[1] * n])
    
def draw_points(points, min):
    np = [p.time(min) for p in points]
    x_range = sorted([x for x,y in np])
    y_range = sorted([y for x,y in np])

    x0, x1 = x_range[0], x_range[-1] + 1
    y0, y1 = y_range[0], y_range[-1] + 1

    print("Problem 1:")
    for j in range(y0, y1):
        line = ""
        for i in range(x0, x1):
            line += "#" if (i, j) in np else " "
        print line

    print("Problem 2: {0}".format(min))

def main(args):
    points = [Point(line.strip()) for line in open(args.file)]

    extents = dict()

    for i in range(15000):
        np = [p.time(i) for p in points]
        x_range = sorted([x for x,y in np])
        y_range = sorted([y for x,y in np])
        extents[i] = math.sqrt((x_range[-1] - x_range[0])**2 + (y_range[-1] - y_range[0])**2)

    ranges = sorted(extents, key=lambda x: extents[x])
    draw_points(points, ranges[0])
    #print ranges[0], extents[ranges[0]], extents[ranges[-1]]
        

    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2018 Day {0} AOC: FOO FOO".format(day))
    ap.add_argument("file", help="Input file", default="{0}-input.txt".format(day), nargs="?")
    main(ap.parse_args())
