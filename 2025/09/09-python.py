#!/usr/local/bin/python3

import sys, argparse, operator, re
from collections import deque
from matplotlib.path import Path
import pickle


def display(reds, greens):
    for y in range(9):
        row = ""
        for x in range(13):
            if (y, x) in reds:
                row += "#"
            elif (y, x) in greens:
                row += "@"
            else:
                row += "."
        print(row)

def outside_corner(p1, p2, p3):
    pts = [p1, p2, p3]

    # --- find the corner ---
    corner = None
    for i in range(3):
        y, x = pts[i]
        share_y = sum(1 for p in pts if p[0] == y)
        share_x = sum(1 for p in pts if p[1] == x)
        if share_y == 2 and share_x == 2:
            corner = pts[i]
            break

    if corner is None:
        raise ValueError("No L-shaped corner found.")

    cy, cx = corner

    # --- find the axes directions (from corner to each leg) ---
    others = [p for p in pts if p != corner]

    dy = sum((p[0] > cy) - (p[0] < cy) for p in others)  # sign of vertical leg
    dx = sum((p[1] > cx) - (p[1] < cx) for p in others)  # sign of horizontal leg

    # Normalize to ±1
    dy = 1 if dy > 0 else -1
    dx = 1 if dx > 0 else -1

    # --- interior point would be (cy + dy, cx + dx)
    #     exterior point is the OPPOSITE direction ---
    return (cy - dy, cx - dx)

def inside_corner(p1, p2, p3):
    pts = [p1, p2, p3]

    corner = None
    for i in range(3):
        y, x = pts[i]

        share_y = sum(1 for p in pts if p[0] == y)
        share_x = sum(1 for p in pts if p[1] == x)

        if share_y == 2 and share_x == 2:
            corner = pts[i]
            break

    if corner is None:
        print("ERROR: 3 adjacent points don't make L:", p1, p2, p3)
        sys.exit(1)
        raise ValueError("No L-shaped corner found.")

    cy, cx = corner

    others = [p for p in pts if p != corner]

    dy = sum((p[0] - cy) and (p[0] > cy) - (p[0] < cy) for p in others)
    dx = sum((p[1] - cx) and (p[1] > cx) - (p[1] < cx) for p in others)
    dy = 1 if dy > 0 else -1
    dx = 1 if dx > 0 else -1
    return (cy + dy, cx + dx)


def main(args):
    points = []
    greens = set()

    minmax = [0x80000000, 0x80000000, -1, -1]
    with open(args.file) as fd:
        for line in fd:
            points.append(tuple([int(x) for x in line.strip().split(",")][::-1]))
            y, x = points[-1]
            if y < minmax[0]: minmax[0] = y
            if x < minmax[1]: minmax[1] = x
            if y > minmax[2]: minmax[2] = y
            if x > minmax[3]: minmax[3] = x
        
    areas = {}
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points[i+1:]):
            y1, x1 = p1
            y2, x2 = p2

            areas[(abs(x2-x1)+1) * (abs(y2-y1)+1)] = (p1, p2)
    print(sorted(areas.keys())[-1])

    for i, p1 in enumerate(points):
        j = (i+1) % len(points)
        p2 = points[j]

        if p1[0] == p2[0]:
            for x in range(*sorted([p1[1]+1, p2[1]])):
                greens.add((p1[0], x))
        elif p1[1] == p2[1]:
            for y in range(*sorted([p1[0]+1, p2[0]])):
                greens.add((y, p1[1]))
        else:
            print("ERROR")
            sys.exit(1)
#    border_path = Path(points)
#    print(minmax)
#    for y in range(minmax[0], minmax[2]+1):
#        print(y, x)
#        for x in range(minmax[1], minmax[3]+1):
#            if border_path.contains_point((y, x)):
#                greens.add((y,x))
#
#    # stupid thing. It takes so long
#    with open("09-data.pickle", "wb") as fd:
#        pickle.dump(greens, fd, protocol=pickle.HIGHEST_PROTOCOL)
#    print("PICKLED")
#    #display(points, greens)
#        #print(f"{p1} connected to {p2}")
#

    interior_point = inside_corner(*points[:3])
    outside_point = outside_corner(*points[:3])

    print(f"Corner of {points[0]}, {points[1]}, {points[2]}: interior is {interior_point}")
    print(f"Corner of {points[0]}, {points[1]}, {points[2]}: outside is {outside_point}")

    border_set = set(points).union(greens)
    print(len(border_set))
    sys.exit(1)
    def floodfill(start):
        filled = set()
        q = deque([start])
    
        while q:
            p = q.popleft()
            if p in filled or p in border_set:
                continue
    
            filled.add(p)
    
            y, x = p
            for n in [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]:
                if n not in filled:
                    q.append(n)
        return filled
        
    filled = list(floodfill(interior_point))
    print(filled)
    #display(points, greens)

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="20XX Day {0} AOC: Movie Theater".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
