#!/usr/local/bin/python3.7

import sys, argparse, operator, re, copy
import numpy as np

map_l = lambda x, y: 1 if x < y else (-1 if x > y else 0)

def adjust_velocity(moons):
    for i, m in enumerate(moons):
        adjusts = []
        for j, n in enumerate(moons):
            if i != j:
                moons[i][1] += [map_l(a,b) for a, b in zip(moons[i][0], moons[j][0])]

def adjust_positions(moons):
    for p, v in moons:
        p += v
        
def energy(moons):
    e = 0
    for p, v in moons:
        e += sum([abs(x) for x in p]) * sum([abs(y) for y in v])
    return e

def main(args):
    moons = [0] * 4
    for i, line in enumerate(open(args.file)):
        moons[i] = [np.array([int(x.split("=")[1].strip()) for x in line.strip("<>\n").split(", ")]), 
                    np.array([0,0,0])]

    orig = copy.deepcopy(moons)

    cycles = [-1,-1,-1]

    for i in range(1000000):
        adjust_velocity(moons)
        adjust_positions(moons)

        if i == 1000:
            print("Part 1:", energy(moons))

        for j in range(3):
            if [ (x[j], y[j]) for x, y in moons ] == [ (a[j], b[j]) for a, b in orig ]:
                if cycles[j] == -1:
                    cycles[j] = i + 1
        if -1 not in cycles:
            break
    print("Part 2:", np.lcm.reduce(cycles))
    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2019 Day {0} AOC: The N-Body Problem".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
