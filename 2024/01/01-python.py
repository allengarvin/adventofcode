#!/usr/bin/python3.9

import sys, argparse, collections

def main(args):
    data = [map(int, line.split()) for line in open(args.file).readlines()]
    a, b = map(sorted, zip(*data))
    print(sum([abs(x-y) for x,y in zip(a, b)]))
    c = collections.Counter(b)
    print(sum([num * c.get(num, 0) for num in a]))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2024 Day {0} AOC: Historian Hysteria".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
