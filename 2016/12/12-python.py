#!/usr/local/bin/python3.7

import sys, argparse, operator, re

class VM:
    ops1 = [ "inc", "dec" ]
    ops2 = [ "cpy", "jnz" ]

    def __init__(self, registers=[0,0,0,0]):
        self.reg = registers
        self.program_lines = []
        self.pc = 0
        self.debug = False

    def add_line(self, s):
        self.program_lines.append(s.strip())

    def rule_closure(self, p):
        instr, args = p.split(" ", 1)
        
        registers = self.reg

        if instr in self.ops1:
            op1 = ord(args) - 97

            def inc():
                if self.debug:
                    print("* ++ {} ({}->{})".format(chr(op1+97), registers[op1], registers[op1]-1))
                registers[op1] += 1
                self.pc += 1
            def dec():
                if self.debug:
                    print("* --{} ({}->{})".format(chr(op1+97), registers[op1], registers[op1]-1))
                registers[op1] -= 1
                self.pc += 1

            return eval(instr)
        if instr in self.ops2:
            arg1, arg2 = args.split()
            if arg1.isdigit() or arg1[0] == "-":
                op1 = int(arg1)
                op1_type = int
            else:
                op1 = ord(arg1) - 97
                op1_type = str

            if arg2.isdigit() or arg2[0] == "-":
                op2 = int(arg2)
                op2_type = int
            else:
                op2 = ord(arg2) - 97
                op2_type = str
        
            def cpy():
                if op1_type == int:
                    if self.debug:
                        print("* cpy {} [int] {}".format(op1, chr(op2+97)))
                    registers[op2] = op1
                else:
                    if self.debug:
                        print("* cpy {} [var:{}] {}".format(chr(op2+97), registers[op1], chr(op2+97)))
                    registers[op2] = registers[op1]
                self.pc += 1

            def jnz():
                if op1_type == int:
                    if self.debug:
                        print("* jnz {} [int] {}".format(op1, op2))
                    if op1 != 0:
                        self.pc += op2
                        return
                else:
                    if self.debug:
                        print("* jnz {} [var:{}] {}".format(chr(op1+97), registers[op1], op2))
                    if registers[op1] != 0:
                        self.pc += op2
                        return
                self.pc += 1

            return eval(instr)
        
    def register(self, r):
        return self.reg[ord(r)-97]

    def load_tape(self):
        self.program = []

        for p in self.program_lines:
            self.program.append(self.rule_closure(p))

    def step(self):
        self.program[self.pc]()

    def run(self):
        self.pc = 0
        while 0 <= self.pc < len(self.program):
            self.step()
   

        
def main(args):
    vm1 = VM()
    vm2 = VM(registers=[0,0,1,0])
    for l in open(args.file):
        vm1.add_line(l)
        vm2.add_line(l)

    vm1.load_tape()
    vm1.run()
    print("Part 1:", vm1.register("a"))
    vm2.load_tape()
    vm2.run()
    print("Part 2:", vm2.register("a"))
    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2016 Day {0} AOC: Leonardo's Monorail".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
