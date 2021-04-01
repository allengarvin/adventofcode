#!/usr/bin/python

import sys, os, argparse, operator, re, itertools

class Fuel_cell:

    def __init__(self, ser, pos):
        x, y = pos

        self.position = (x,y)
        self.serial = ser
        self.rack_id = x + 10
        self.power = self.rack_id * y
        self.power += self.serial
        self.power *= self.rack_id
        self.power = (self.power % 1000) / 100
        self.power -= 5

    def __repr__(self):
        return "Fuel cell at {0}, grid serial number {1}: power level {2}".format(str(self.position), self. serial, self.power)

        
        
def main(args):
    serial = args.serial

    fuels = { (x,y) : Fuel_cell(serial, (x,y)) for x in range(1, 301) for y in range(1, 301) }
    max_squares = { (x,y) : sum([fuels[(x+i, y+j)].power for i in range(3) for j in range(3)]) for x in range(1,301-3) for y in range(1,301-3) }
    max_power = sorted(max_squares.keys(), key=lambda x: max_squares[x])[-1]
    print("Problem 1: {0}".format(max_power))

    max = -1
    max_dial = -1
    max_coord = False
    for dial in range(1, 301):
        max_squares = { (x,y) : sum([fuels[(x+i, y+j)].power for i in range(dial) for j in range(dial)]) for x in range(1,301-dial) for y in range(1,301-dial) }
        tmp_coord = sorted(max_squares.keys(), key=lambda x: max_squares[x])[-1]
        tmp_max = max_squares[tmp_coord]

        if tmp_max > max:
            max_dial = dial
            max_coord = tmp_coord
            max = tmp_max
        print "curr dial: ", dial, "    ", max, "answer:", max_coord, max_dial

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2018 Day {0} AOC: Chronal Charge".format(day))
    ap.add_argument("serial", help="serial for puzzle", type=int, default=3463, nargs="?")
    main(ap.parse_args())
