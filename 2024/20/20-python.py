#!/usr/bin/python3

import sys, argparse

# based off of geekforgeeks algo
def can_construct(design, atoms):
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        for atom in atoms:
            if i >= len(atom) and design[i - len(atom):i] == atom:
                #dp[i] = dp[i] or dp[i - len(atom)]
                dp[i] += dp[i - len(atom)]
    
    return dp[n]

def main(args):
    fd = open(args.file)
    towels = fd.readline().strip().split(", ")
    _ = fd.readline()
    designs = []
    for line in fd:
        designs.append(line.strip())

    results = [ can_construct(test, towels) for test in designs ]

    print(len([x for x in results if x]))
    print(sum(results))


if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2024 Day {0} AOC: Linen Layout".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
