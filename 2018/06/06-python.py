#!/usr/bin/python

from string import ascii_uppercase as UCC
from string import ascii_lowercase as LCC

import sys

LC = list(UCC) + list(LCC)

def part1(coordinates):
    tmp = coordinates[0]
    bounds = [ tmp[0]-2, tmp[0]+2, tmp[1]-2, tmp[1]+2 ]
    for x,y in coordinates:
        if x < bounds[0]:
            bounds[0] = x -2
        if x > bounds[1]:
            bounds[1] = x +2
        if y < bounds[2]:
            bounds[2] = y -2
        if y > bounds[3]:
            bounds[3] = y +2
    
    rows = []
    for y in range(bounds[2], bounds[3]+1):
        row = ""
        for x in range(bounds[0], bounds[1]+1):
            if (x,y) in coordinates:
                row += LC[coordinates.index((x,y))]
            else:
                distances = [abs(x - x1) + abs(y - y1) for x1, y1 in coordinates]
                m = min(distances)
    
                if distances.count(m) > 1:
                    row += "."
                else:
                    row += LC[distances.index(min(distances))]
                    
        rows.append(row)
    totry = coordinates[:]
    area = {}
    for i, c in enumerate(LC[:len(totry)]):
        if c in rows[0] or c in rows[-1]:
            totry[i] = False
        for r in rows:
            if c == r[0] or c == r[-1]:
                totry[i] = False
                break
        if totry[i]:
            totry[i] = c
            area[c] = 0
            
    for r in rows:
        for c in totry:
            if c:
                area[c] += r.count(c)
    
    return sorted(area.iteritems(), key=lambda (k, v): (v, k))[-1][1]

def part2(coordinates):

    tmp = coordinates[0]
    
    bounds = [ tmp[0]-500, tmp[0]+50, tmp[1]-50, tmp[1]+50 ]
    for x,y in coordinates:
        if x < bounds[0]:
            bounds[0] = x -500
        if x > bounds[1]:
            bounds[1] = x +500
        if y < bounds[2]:
            bounds[2] = y -500
        if y > bounds[3]:
            bounds[3] = y +500
    
    rows = []
    
    cnt = 0;
    for y in range(bounds[2], bounds[3]+1):
        row = ""
        for x in range(bounds[0], bounds[1]+1):
            distances = [abs(x - x1) + abs(y - y1) for x1, y1 in coordinates]
            if sum(distances) < 10000:
                cnt += 1

    return cnt

def main():

    coordinates = []
    with open("06-real-input.txt") as fd:
        for k in fd.readlines():
            coordinates.append(tuple([int(x) for x in k.strip().split(", ")]))

    print(part1(coordinates))
    print(part2(coordinates))

    
if __name__ == "__main__":
    main()
