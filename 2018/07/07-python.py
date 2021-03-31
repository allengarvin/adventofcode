#!/usr/bin/python3

import sys, os, argparse, operator, re, copy
from parse import parse

OFFSET=60
WORKERS=5

def requirements(fd):
    components = dict()

    for line in fd:
        a, b = parse("Step {} must be finished before step {} can begin.", line)
        components[a] = components.get(a, set())
        components[b] = components.get(b, set()) | set([a])
    return components

def main(args):
    req = requirements(open(args.file))

    part1 = copy.deepcopy(req)
    code = ""
    while( part1 ):
        possible = sorted([k for k, v in part1.items() if not v])
        for p in possible:
            part1.pop(p)
            for k, v in part1.items():
                if p in v:
                    v.remove(p)
        code += "".join(possible)

    print(code)

    code = ""
    part2 = req.copy()
    work = dict()
    seconds = 0

    while part2 or work:
        for w in list(work.keys()):
            work[w] -= 1
            if work[w] == 0:
                work.pop(w)
                code += w
                for k, v in part2.items():
                    if w in v:
                        v.remove(w)

        possible = sorted([k for k, v in part2.items() if not v])
        for p in possible:
            if len(work) == WORKERS:
                break
            part2.pop(p)
            work[p] = OFFSET + ord(p) - 64

        if not work:
            continue

        if not work and not part2:
            break
        seconds += 1

    print(seconds)


if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2017 Day {0} AOC: The Sum of Its Parts".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
