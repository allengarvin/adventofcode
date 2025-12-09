#!/usr/bin/python3

import sys, argparse, operator, re
from collections import Counter

def common(numbers, mostp):
    if len(numbers[0]) == 0:
        return ""
    return Counter([x[0] for x in numbers]).most_common()[0 if mostp else -1][0] + common([x[1:] for x in numbers], mostp)

def bfilter(numbers, mostp):
    if len(numbers) < 3:
        return sorted(numbers, reverse=mostp)[0]

    com = Counter([x[0] for x in numbers]).most_common()
    if len(com) == 2 and com[0][1] == com[1][1]:
        com = "1" if mostp else "0"
    else:
        com = com[0 if mostp else -1][0]
    return com + bfilter([x[1:] for x in numbers if x[0] == com], mostp)

def main(args):
    numbers = []
    with open(args.file) as fd:
        for line in fd:
            numbers.append(line.strip())

    print(int(common(numbers, True), 2) * int(common(numbers, False), 2))
    
    ox = bfilter(numbers, True)
    co = bfilter(numbers, False)
    print(int(ox, 2) * int(co, 2))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="20XX Day {0} AOC: Binary Diagnostic".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
