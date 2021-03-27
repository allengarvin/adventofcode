#!/usr/local/bin/python3.7

import sys, argparse, operator, re

# triangular numbers! There may be a more deterministic way to get n^p1 (mod p2), but I'll bruteforce it
def main(args):
    place = [int(x.rstrip(",.")) for i, x in enumerate(open(args.file).read().split()) if i == 15 or i == 17]
    start_of_row = (sum(place)-1) * (sum(place)-2) // 2 + 1

    start, p1, mod_p = 20151125, 252533, 33554393
    for i in range(start_of_row + place[1] - 2):
        start = (start * p1) % mod_p

    print("Part 1:", start)

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2015 Day {0} AOC: Let It Snow".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
