#!/usr/bin/python

import sys, os, argparse, operator, re

class INTCODE:
    tape = []
    pc = 0

    opcodes = dict()
    HALT=False

    debug = False

    def display_state(self):
        tape = self.tape
        pc = self.pc

        max = -1
        for i in tape:
            if len(str(i)) > max:
                max = len(str(i))
        print ", ".join(["%*d" % (max, i) for i in tape])
        print ", ".join(["^" * max if i == pc else " " * max for i in range(len(tape))])


    def op_halt(self, mode):
        if self.debug:
            print("op_halt")
            self.display_state()
        self.HALT = True

    def op_add(self, mode):
        tape = self.tape
        pc = self.pc

        if self.debug:
            print("op_add (mode=%s)" % mode)
            self.display_state()

        arg1 = tape[pc+1]
        arg2 = tape[pc+2]
        dest = tape[pc+3]

        if mode == "position":
            if self.debug:
                print("ADD @%d(%d) + %d(%d) = %d => @%d" % (arg1, tape[arg1], arg2, tape[arg2], tape[arg1] + tape[arg2], dest))
            tape[dest] = tape[arg1] + tape[arg2]
        else:
            if self.debug:
                print("ADD %d + %d = %d => @%d" % (arg1, arg2, arg1 + arg2, dest))
            tape[dest] = arg1 * arg2
        self.pc += 4

    def op_mul(self, mode):
        tape = self.tape
        pc = self.pc

        if self.debug:
            print("op_mul (mode=%s)" % mode)
            self.display_state()
        arg1 = tape[pc+1]
        arg2 = tape[pc+2]
        dest = tape[pc+3]

        if mode == "position":
            if self.debug:
                print("MUL @%d(%d) * %d(%d) = %d => @%d" % (arg1, tape[arg1], arg2, tape[arg2], tape[arg1] * tape[arg2], dest))
            tape[dest] = tape[arg1] * tape[arg2]
        else:
            if self.debug:
                print("MUL %d * %d = %d => @%d" % (arg1, arg2, arg1 * arg2, dest))
            tape[dest] = arg1 * arg2

        self.pc += 4

    def __init__(self, tape, debug=False):
        self.tape = list(tape)
        self.pc = 0
        self.debug = debug

        self.opcodes = {
            99 : self.op_halt,
             1 : self.op_add,
             2 : self.op_mul,
        }

#        if self.debug:
#            self.display_state()
        while True:
            op = tape[self.pc]

            DE = op % 100
            C = (op / 100) % 10
            B = (op / 1000) % 10
            A = (op / 10000) % 10

            if DE not in self.opcodes:
                print("EXCEPTION: unknown opcode @%d: %d" % (self.pc, DE))
                self.tape[0] = "X"
                break

            self.opcodes[DE]("immediate" if B == 1 else "position")
            if self.HALT:
                break

def init():
    print opcodes

def main(args):
    global tape

    tape = [int(x) for x in open(args.file).read().strip().split(",")]

    tape[1] = 12
    tape[2] = 2
    computer = INTCODE(tape, debug=False)
    print("Problem 1: %d" % computer.tape[0])
    
    while True:
        for y in range(100):
            for x in range(100):
                tape[1], tape[2] = x, y
                computer = INTCODE(tape)

                if computer.tape[0] == 19690720:
                    print("Problem 2: %d" % (x*100 + y))
                    sys.exit(0)


if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2019 Day 2 AOC: Program alarm")
    ap.add_argument("-1", "--one", action="store_true", help="Problem 1")
    ap.add_argument("-2", "--two", action="store_true", help="Problem 2")
    ap.add_argument("-v", "--verbose", action="store_true", help="Debug")

    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    args = ap.parse_args()
    if not args.one and not args.two:
        args.one = args.two = True
    main(args)
    
