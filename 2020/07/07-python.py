#!/usr/bin/python

import sys, os, argparse, operator, re
from parse import parse

def traverse(type, maps):
    if type == "shiny gold":
        return True
    for t in maps[type]:
        if traverse(t[1], maps):
            return True
    return False

def traverse2(type, maps, cnt):
    count = 0

    for t in maps[type]:
        if len(maps[t[1]]):
            count += cnt * traverse2(t[1], maps, t[0])
        else:
            count += t[0] * cnt
    
    return count + cnt

def main(args):
    fd = open(args.file)

    maps = dict()
    for line in fd:
        line = line.strip().strip(".")
        left, right = line.split(" bags contain ")
        if "no other bags" in right:
            maps[left] = []
        else:
            right = [parse("{num} {type} bag", x.replace("bags", "bag")) for x in right.split(", ")]
            maps[left] = [(int(s["num"]), s["type"]) for s in right]

    count_one = 0

    for k in maps.keys():
        if traverse(k, maps) and k != "shiny gold":
            count_one += 1

    print("Problem 1: %d" % count_one)
    print("Problem 2: %d" % (traverse2("shiny gold", maps, 1) - 1))

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day X AOC: FOO FOO")
    ap.add_argument("-1", "--one", action="store_true", help="Problem 1")
    ap.add_argument("-2", "--two", action="store_true", help="Problem 2")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    args = ap.parse_args()
    if not args.one and not args.two:
        args.one = args.two = True
    main(args)
    
