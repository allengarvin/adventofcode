#!/usr/bin/python3

import sys, argparse, re

def multiples(npt):
    return sum([int(x) * int(y) for x, y in [expr[4:expr.index(")")].split(",") for expr in re.findall(r'mul\(\d+,\d+\)', npt)]])

def main(args):
    npt = open(args.file).read()
    print(multiples(npt))

    sum = 0
    state = True
    while re.search(r'mul\(\d+,\d+\)', npt):
        if "don't()" in npt:
            sum += multiples(npt[:npt.index("don't()")])
            npt = npt[npt.index("don't()")+1:]
            state = False
            if "do()" in npt:
                npt = npt[npt.index("do()")+1:]
                state = True
        else:
            break
    if state == True:
        sum += multiples(npt)
    print(sum)

if __name__ == "__main__":
    day =sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2024 Day {0} AOC: Mull It Over".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
