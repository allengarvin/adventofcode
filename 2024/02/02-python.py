#!/usr/bin/python3.9

import sys, argparse, collections

def safeP(diffs):
    return (all(i > 0 for i in diffs) or all(i < 0 for i in diffs)) and all(abs(i) >= 1 and abs(i) <= 3 for i in diffs)
    
def difference(x):
    return [x[i+1] - x[i] for i in range(len(x)-1)]

def main(args):
    data = [[int(x) for x in line.split()] for line in open(args.file).readlines()]
    cnt1, cnt2 = 0, 0
    for x in data:
        diffs = difference(x)
        if safeP(diffs):
            cnt1 += 1
            cnt2 += 1
        else:
            for i in range(len(x)):
                if safeP(difference(x[:i] + x[i+1:])):
                    cnt2 += 1
                    break
    print(cnt1)
    print(cnt2)


if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2024 Day {0} AOC: Red-Nosed Reports".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
