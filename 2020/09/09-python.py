#!/usr/bin/python

import sys, argparse, itertools

def contiguous(arr):
    for i, j in itertools.combinations(list(range(len(arr)+1)), 2):
        if j - i > 1:
            yield arr[i:j]

def main(args):
    lines = [int(x.strip()) for x in open(args.file).readlines()]

    for n in range(args.queue, len(lines)):
        prev = lines[n - args.queue:n]
        if lines[n] not in map(sum, itertools.combinations(prev, 2)):
            print("Problem 1: %d" % lines[n])
            for arr in contiguous(lines[:n]):
                if sum(arr) == lines[n]:
                    print("Problem 2: %d" % sum(sorted(arr)[::len(arr)-1]))
                    sys.exit(0)

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day 9 AOC: Encoding error")
    ap.add_argument("-q", "--queue", help="Number for day-9-queue", type=int, default=25)
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    args = ap.parse_args()
    main(args)
    
