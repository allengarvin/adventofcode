#!/usr/bin/python3

import sys

def dist(x): return abs(int(pos.real))

if __name__ == "__main__":
    steps = { "ne" : 1, "se" : 1+1j, "n" : -1j, "s" : 1j, "sw" : -1, "nw" : -1-1j }
    moves = [steps[x] for x in open("11-input.txt").read().strip().split(",")]

    pos, mx = 0, -1
    
    for m in moves:
        pos += m
        mx = max(dist(pos), mx)

    print(dist(pos))
    print(mx)
