#!/usr/bin/python

import os, sys, itertools, string
from copy import deepcopy

def display(grid):
    s = ""
    for j in range(25):
        for i in range(25):
            s += grid[(j,i)]
        print s
        s = ""

def main():
    grid = dict()

    lines = []
    for l in open("../advent/22-input.txt"):
        lines.append(list(l.strip()))

    for j in range(len(lines)):
        for i in range(len(lines[0])):
            grid[(j,i)] = lines[j][i]

    if len(lines) == 25:        # our input
        virus = (12,12)
    else:                       # test input
        virus = (4, 4)

    orig_virus = (virus[0], virus[1])
    orig_grid = deepcopy(grid)

    orientation = 0

    # 5231 isn't right, nor is 5834.
    count = 0
    infection_count = 0
    while True:
        if virus not in grid:
            grid[virus] = "."

        if grid[virus] == "#":
            orientation = (orientation + 1) % 4
            grid[virus] = "."
        else:
            orientation = (orientation - 1) % 4
            grid[virus] = "#"
            infection_count += 1
        if orientation == 0:
            virus = (virus[0] - 1, virus[1])
        elif orientation == 1:
            virus = (virus[0], virus[1] + 1)
        elif orientation == 2:
            virus = (virus[0] + 1, virus[1])
        else:
            virus = (virus[0], virus[1] - 1) 
        count += 1

#        display(grid)
        if count == 10000:
            print "Answer 1:", infection_count
            break

    grid = orig_grid
    orientation = 0
    virus = orig_virus

    infection_count = 0
    count = 0
    while True:
        if virus not in grid:
            grid[virus] = "."

        if grid[virus] == ".":
            orientation = (orientation - 1) % 4
            grid[virus] = "W"
        elif grid[virus] == "W":
            # orientation doesn't change
            grid[virus] = "#"
            infection_count += 1
        elif grid[virus] == "#":
            orientation = (orientation + 1) % 4
            grid[virus] = "F"
        elif grid[virus] == "F":
            orientation = (orientation + 2) % 4
            grid[virus] = "."

        if orientation == 0:
            virus = (virus[0] - 1, virus[1])
        elif orientation == 1:
            virus = (virus[0], virus[1] + 1)
        elif orientation == 2:
            virus = (virus[0] + 1, virus[1])
        else:
            virus = (virus[0], virus[1] - 1) 
        count += 1
        if count == 10000000:
            print "Answer 2:", infection_count
            break
    


if __name__ == "__main__":
    main()
