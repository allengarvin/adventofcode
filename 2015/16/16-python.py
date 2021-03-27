#!/usr/local/bin/python3.7

import sys, argparse, operator, re

def test_sues(aunts, part2=False):
    gift = {
        "children" : 3,
        "cats" : 7,
        "samoyeds" : 2,
        "pomeranians" : 3,
        "akitas" : 0,
        "vizslas" : 0,
        "goldfish" : 5,
        "trees" : 3,
        "cars" : 2,
        "perfumes" : 1,
    }
    
    for a, m in aunts.items():
        skip = True
        for k, v in m.items():
            if part2:
                if (k == "cats" or k == "trees"):
                    if v <= gift[k]:
                        skip = False
                        break
                    else:
                        continue
                elif (k == "pomeranians" or k == "goldfish"):
                    if v >= gift[k]:
                        skip = False
                        break
                    else:
                        continue
                elif gift[k] != v:
                    skip = False
            
            elif gift[k] != v:
                skip = False
        if not skip:
            continue
        return a

def main(args):
    aunts = dict()
    for line in open(args.file):
        sue, attr = line.strip().split(": ", 1)
        aunts[int(sue.split()[1])] = {x.split(": ")[0] : int(x.split(": ")[1]) for x in attr.split(", ")}

    print("Part 1: {0}".format(test_sues(aunts)))
    print("Part 2: {0}".format(test_sues(aunts, part2=True)))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2015 Day {0} AOC: Aunt Sue".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
