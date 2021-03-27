#!/usr/bin/python

import sys, os, argparse, operator, re, itertools, parse

class ElfClaim:
    def __init__(self, p):
        self.full = p.__dict__["named"]
        self.claim_no = p["cl"]
        self.ox = p["ox"]; self.oy = p["oy"]
        self.width = p["w"]; self.length = p["l"]

    def __contains__(self, p):                                  # unused, was using for debugging
        return self.ox <= p[0] <= self.ox + self.width and self.oy <= p[1] <= self.oy + self.length

    def size(self): return self.width * self.length

    def extent(self):
        return set((self.ox + x, self.oy + y) for x in xrange(self.width) for y in xrange(self.length))

    def __str__(self):
        return "#{cl:d} @ {ox:d},{oy:d}: {w:d}x{l:d}".format(**self.full)

    def __repr__(self):
        return str(self.claim_no)

def main(args):
    c = [parse.parse("#{cl:d} @ {ox:d},{oy:d}: {w:d}x{l:d}\n", l) for l in open(args.file)]

    fabric = dict()
    claims = []

    for p in c:
        ec = ElfClaim(p)
        claims.append(ec)
        for pnt in ec.extent():
            fabric[pnt] = fabric.get(pnt, []) + [ec.claim_no]
    print("Problem 1: {0}".format(len([k for k, v in fabric.items() if len(v) > 1])))

    for c in claims:
        if sum([c.claim_no] == x for x in fabric.values()) == c.size():
            print("Problem 2: {0}".format(c.claim_no))
            return


if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2018 Day {0} AOC: No Matter How You Slice It".format(day))
    ap.add_argument("file", help="Input file", default="{0}-input.txt".format(day), nargs="?")
    main(ap.parse_args())
