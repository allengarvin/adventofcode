#!/usr/bin/python3

import sys, os, argparse, operator, re, copy
from parse import parse

class Tape:
    def __init__(self, tape):
        self.tc = 0
        self.tape = tape

    def read(self):
        val = self.tape[self.tc]
        self.tc += 1
        return val

    def rewind(self):
        self.tc = 0

    def part1(self):
        total = 0

        children = self.read()
        metadata = self.read()

        for i in range(children):
            total += self.part1()

        for i in range(metadata):
            total += self.read()
        return total

    def part2(self):
        total = 0

        children = self.read()
        metadata = self.read()
        cvals = [0] * children

        if children:
            for i in range(children):
                cvals[i] = self.part2()

            for i in range(metadata):
                ref = self.read()
                if ref > 0 and ref < children + 1:
                    total += cvals[ref-1]
        else:
            for i in range(metadata):
                total += self.read()

        return total
            
def main(args):
    tape = Tape([int(x) for x in open(args.file).read().split()])

    print(tape.part1())
    tape.rewind()
    print(tape.part2())

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2017 Day {0} AOC: Memory Maneuver".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
