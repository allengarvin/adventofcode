#!/usr/bin/python3

import sys, argparse, operator, re

def subseqs(s, k):
    n = len(s)
    start = 0
    result = []

    for needed in range(k, 0, -1):
        end = n - (needed - 1)
        pos = max(range(start, end), key=lambda x: s[x])
        result.append(s[pos])
        start = pos + 1

    return int(''.join(result))

def main(args):
    joltages, joltages2 = [], []

    with open(args.file) as fd:
        for line in fd:
            line = line.strip()

            joltages.append(subseqs(line, 2))
            joltages2.append(subseqs(line, 12))

        # first quick, naive solution. optimizing it was the way to go

#            left, leftpos = "/", -1
#            for i, x in enumerate(line[:-1]):
#                if x > left:
#                    left, leftpos = x, i
#                    right, rightpos = "/", i
#            for j, y in enumerate(line[leftpos+1:]):
#                if y > right:
#                    right, rightpos = y, j
#            
#            part2 = max(subseqs(line, 12))
#            print(part2)
#            
#
#            joltages.append(int((left + right).lstrip("0")))

    print(sum(joltages))
    print(sum(joltages2))

            
                

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2025 Day {0} AOC: Lobby".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
