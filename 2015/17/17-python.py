#!/usr/local/bin/python3.7

import sys, argparse
from itertools import chain, combinations

# straight from: https://docs.python.org/3/library/itertools.html#itertools-recipes
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def main(args):
    containers = [int(x) for x in open(args.file).readlines()]

    cnt1, cnt2 = 0, 0;
    minimal = len(containers) + 1

    for c in powerset(containers):
        if sum(c) == 150:
            cnt1 += 1
            if len(c) < minimal:
                minimal = len(c)
                cnt2 = 1
            elif len(c) == minimal:
                cnt2 += 1
                

    print("Part 1:", cnt1)
    print("Part 2:", cnt2)

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2015 Day {0} AOC: No Such Thing as Too Much".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
