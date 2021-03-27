#!/usr/bin/python

import sys, os, argparse, operator, re
from parse import parse

def parse_line(str):
    p = parse("{0} (contains {1})\n", str)
    return set(p[0].split()), p[1].split(", ")

def main(args):
    foods = map(parse_line, open(args.file).readlines())

    allergens = set()
    ingredients = set()
    a_map = dict()

    for i, a in foods:
        allergens |= set(a)
        a_map.update( { x: a_map.get(x, []) + [i] for x in a } )
        ingredients.update(i)
            
    for a in allergens:
        a_map[a] = reduce(operator.and_, a_map[a]) 

    non_allergens = ingredients.copy()
    for k, a in a_map.items():
        non_allergens -= a

    print("Problem 1: {0}".format(sum([x in f for f, _ in foods for x in non_allergens])))

    while max([len(x) for x in a_map.values()]) > 1:
        for k, v in a_map.items():
            for l, u in a_map.items():
                if len(v) > 1 and len(u) == 1:
                    a_map[k] -= u
    print("Problem 2: {0}".format(",".join([a_map[x].pop() for x in sorted(a_map)])))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2020 Day 21 AOC: Allergen Assessment")
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
