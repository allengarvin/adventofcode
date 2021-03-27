#!/usr/bin/python3

from itertools import combinations

def divisible(arr):
    return [y // x for x, y in combinations(sorted(arr), 2) if y % x == 0][0]
    
if __name__ == "__main__":
    lines = [[int(x) for x in l.split()] for l in open("02-input.txt").readlines()]
    print(sum([max(l) - min(l) for l in lines]))
    print(sum(map(divisible, lines)))
