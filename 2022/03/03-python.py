#!/usr/bin/python3

import sys, argparse, operator, re, string

def score(c):
    return ord(c)-96 if c in string.ascii_lowercase else ord(c)-64+26

def main(args):
    part1, part2 = 0, 0

    lines = [x.strip() for x in open(args.file)]
    elf_groups = [lines[i:i+3] for i in range(0, len(lines), 3)]
    sacks = [[x[:len(x)//2], x.strip()[len(x)//2:]] for x in lines]

    for s in sacks:
        for c in set.intersection(*[set(x) for x in s]):
            part1 += score(c)
    for e in elf_groups:
        for c in set.intersection(*[set(x) for x in e]):
            part2 += score(c)
    print(part1)
    print(part2)

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2022 Day {0} AOC: Rucksack Reorganization".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
