#!/usr/local/bin/python3.7

import sys, os, argparse, operator, re

class Gate:
    value = None
    func = None
    shift_value = None

    def __init__(self, s, wires):
        self.wires = wires
        self.instr, self.id = s.split(" -> ")

        if self.instr.isdigit():
            self.value = int(self.instr)
            self.wires.update({self.id : self.value})
            self.registers = []

        elif "AND" in s:
            self.func = lambda x, y: x & y
            self.registers = self.instr.split(" AND ")

            # These only occur for 'AND' in my input
            if self.registers[0].isdigit():
                self.func = eval("lambda x: {0} & x".format(self.registers[0]))
                self.registers = self.registers[1:]

        elif "OR" in s:
            self.func = lambda x, y: x | y
            self.registers = self.instr.split(" OR ")

        elif "NOT" in s:
            self.func = lambda x: ~x & 65535
            self.registers = [self.instr[4:]]

        elif "LSHIFT" in s:
            reg, self.shift_value = self.instr.split(" LSHIFT ")
            self.shift_value = int(self.shift_value)
            self.registers = [reg]
            self.func = lambda x: (x << self.shift_value) & 65535

        elif "RSHIFT" in s:
            reg, self.shift_value = self.instr.split(" RSHIFT ")
            self.shift_value = int(self.shift_value)
            self.registers = [reg]
            self.func = lambda x: (x >> self.shift_value) & 65535
        elif self.instr.isalpha():
            self.registers = [self.instr]
            self.func = lambda x: x
        else:
            print("Bad instruction:", s)
            sys.exit(1)

    def dependencies(self):
        for r in self.registers:
            if r not in self.wires:
                return True
        return False

    def execute(self):
        # print("Executing:", self)
        assert self.value == None
        for r in self.registers:
            assert r in self.wires
        if len(self.registers) == 1:
            a = self.wires[self.registers[0]]
            self.value = self.func(a)
        else:
            a, b = self.wires[self.registers[0]], self.wires[self.registers[1]]
            self.value = self.func(a, b)
        self.wires[self.id] = self.value

    def __repr__(self):
        if self.value != None:
            return "{0}={1}".format(self.id, self.value)

        return "{0} -> {1}".format(self.instr, self.id)

def run_simulation(fn, wire_a=None):
    wires = dict()
    instructions = [Gate(l.strip(), wires) for l in open(fn)]

    if wire_a:
        wires["b"] = wire_a
        for i in instructions:
            if i.id == "b":
                i.value = wire_a

    still_left = [g for g in instructions if g.value == None]
    while still_left:
        for g in [g for g in still_left if g.dependencies() == False]:
            g.execute()
        left = [g for g in instructions if g.value == None]
        if left == still_left:
            print("Infinite loop detection")
            print("Wires:", wires)
            #print("Left:", left)
            for g in left:
                for k in wires.keys():
                    if k in g.registers:
                        print(g.__repr__())
            #print("\n".join([x.__repr__() for x in left]))
            sys.exit(1)
        still_left = left
    return wires["a"]

def main(args):
    part1 = run_simulation(args.file)
    print("Part 1: {0}".format(part1))
    part2 = run_simulation(args.file, wire_a=part1)
    print("Part 2: {0}".format(part2))
    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2015 Day {0} AOC: Some Assembly Required".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
