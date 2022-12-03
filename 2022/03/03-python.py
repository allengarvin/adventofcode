#!/usr/bin/python3

import sys, argparse, operator, re, string

def score(c):
    return ord(c)-96 if c in string.ascii_lowercase else ord(c)-64+26

def intersect(set_list):
    sc = 0
    for s in set_list:
        for c in set.intersection(*[set(x) for x in s]):
            sc += score(c)
    return sc

def main(args):
    lines = [x.strip() for x in open(args.file)]
    elf_groups = [lines[i:i+3] for i in range(0, len(lines), 3)]
    sacks = [[x[:len(x)//2], x.strip()[len(x)//2:]] for x in lines]

    print(intersect(sacks))
    print(intersect(elf_groups))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2022 Day {0} AOC: Rucksack Reorganization".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
