#!/usr/bin/python3

import sys, itertools

def main(fn):
    low, high = [int(x) for x in open(fn).read().split("-")]
    c1, c2 = 0, 0
    for i in range(low, high+1):
        s = str(i)
        if s != "".join(sorted(s)):
            continue
        groupings = [len(list(gr)) for _, gr in itertools.groupby(s)]
        if len([x for x in groupings if x > 1]):
            c1 += 1
            if 2 in groupings:
                c2 += 1

    print(c1)
    print(c2)

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    main(default_file if len(sys.argv) == 1 else sys.argv[1])

