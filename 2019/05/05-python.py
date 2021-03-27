#!/usr/bin/python

import sys, os, argparse, operator, re

class INTCODE:
    tape = []
    pc = 0

    opcodes = dict()
    output = []
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
            #self.display_state()
        self.HALT = True

    def op_add(self, mode):
        tape = self.tape
        pc = self.pc

        if self.debug:
            print "op_add (mode=%d)" % mode, tape[pc:pc+4]

        mode1 = mode % 10 == 1
        mode2 = (mode / 10) % 10 == 1
        mode3 = (mode / 100) % 10 == 1

        if mode1 == 1:
            arg1 = tape[pc+1]
        else:
            arg1 = tape[tape[pc+1]]
        if mode2 == 1:
            arg2 = tape[pc+2]
        else:
            arg2 = tape[tape[pc+2]]
        dest = tape[pc+3]

        tape[dest] = arg1 + arg2
        print("op_add @%d <- %d (check: %d)" % (dest, arg1 + arg2, self.tape[dest]))
        self.pc += 4

    def op_mul(self, mode):
        tape = self.tape
        pc = self.pc
        if self.debug:
            print "op_mul (mode=%d)" % mode, tape[pc:pc+4]


        mode1 = mode % 10 == 1
        mode2 = (mode / 10) % 10 == 1
        mode3 = (mode / 100) % 10 == 1

        if mode1 == 1:
            arg1 = tape[pc+1]
        else:
            arg1 = tape[tape[pc+1]]
        if mode2 == 1:
            arg2 = tape[pc+2]
        else:
            arg2 = tape[tape[pc+2]]
        dest = tape[pc+3]

        self.tape[dest] = arg1 * arg2
        self.pc += 4

    def op_input(self, mode):
        tape = self.tape
        pc = self.pc

        arg1 = tape[pc+1]
        tape[arg1] = self.input[0]
        self.input = self.input[1:]

        if self.debug:
            print("input: %d => @%d" % (tape[arg1], arg1))

        self.pc += 2

    def op_output(self, mode):
        tape = self.tape
        pc = self.pc

        mode1 = mode % 10 == 1
        if mode1:
            arg1 = tape[tape[pc+1]]
        else:
            arg1 = tape[pc+1]
            
        self.output.append(arg1)

        if self.debug:
            print("input: %d => @%d" % (tape[arg1], arg1))

        self.pc += 2

    def __init__(self, tape, debug=False,input=[]):
        self.tape = list(tape)
        tape = self.tape
        self.pc = 0
        self.debug = debug
        self.input = input

        self.opcodes = {
            99 : self.op_halt,
             1 : self.op_add,
             2 : self.op_mul,
             3 : self.op_input,
             4 : self.op_output,
        }

        cnt = 0
        while True:
            op = tape[self.pc]
            if self.debug:
                print("PC=%d, op=%d" % (self.pc, op))

            opc = op % 100
            mode = op / 100

            if opc not in self.opcodes:
                print("COUNT %d" % cnt)
                raise Exception("unknown opcode @%d: %d" % (self.pc, opc))
                self.tape[0] = "X"
                break

            self.opcodes[opc](mode)
            cnt += 1

            if self.HALT:
                break

def init():
    print opcodes

def main(args):
    global tape

    tape = [int(x) for x in open(args.file).read().strip().split(",")]

    computer = INTCODE(tape, debug=True, input=[1])
    print("Problem 1: ", computer.output)
    

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2019 Day 5 AOC: Sunny with a Chance of Asteroids")
    ap.add_argument("-1", "--one", action="store_true", help="Problem 1")
    ap.add_argument("-2", "--two", action="store_true", help="Problem 2")
    ap.add_argument("-v", "--verbose", action="store_true", help="Debug")

    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    args = ap.parse_args()
    if not args.one and not args.two:
        args.one = args.two = True
    main(args)
    
