#!/usr/bin/python3

# This *REALLY* needs refactoring

import sys, argparse, operator
from functools import reduce

class VMtest:
    def __init__(self, triple):
        self.registers = triple[0][:]
        self.operands = triple[1][1:]
        self.opcode = triple[1][0]
        self.result = triple[2][:]
        self.triple = triple
        self.possibles = {}
        self.test()

    def addr(self, r1, r2, r3): self.registers[r3] = self.registers[r1] + self.registers[r2]
    def addi(self, r1, v2, r3): self.registers[r3] = self.registers[r1] + v2
    def mulr(self, r1, r2, r3): self.registers[r3] = self.registers[r1] * self.registers[r2]
    def muli(self, r1, v2, r3): self.registers[r3] = self.registers[r1] * v2
    def banr(self, r1, r2, r3): self.registers[r3] = self.registers[r1] & self.registers[r2]
    def bani(self, r1, v2, r3): self.registers[r3] = self.registers[r1] & v2
    def borr(self, r1, r2, r3): self.registers[r3] = self.registers[r1] | self.registers[r2]
    def bori(self, r1, v2, r3): self.registers[r3] = self.registers[r1] | v2
    def setr(self, r1, _, r3):  self.registers[r3] = self.registers[r1]
    def seti(self, v1, _, r3):  self.registers[r3] = v1
    def gtir(self, v1, r2, r3): self.registers[r3] = 1 if v1 > self.registers[r2] else 0
    def gtri(self, r1, v2, r3): self.registers[r3] = 1 if self.registers[r1] > v2 else 0
    def gtrr(self, r1, r2, r3): self.registers[r3] = 1 if self.registers[r1] > self.registers[r2] else 0
    def eqir(self, v1, r2, r3): self.registers[r3] = 1 if v1 == self.registers[r2] else 0
    def eqri(self, r1, v2, r3): self.registers[r3] = 1 if self.registers[r1] == v2 else 0
    def eqrr(self, r1, r2, r3): self.registers[r3] = 1 if self.registers[r1] == self.registers[r2] else 0

    def test(self):
        opcodes = [ self.addr, self.addi, self.mulr, self.muli, 
                    self.banr, self.bani, self.borr, self.bori, 
                    self.setr, self.seti, 
                    self.gtir, self.gtri, self.gtrr, self.eqir, self.eqri, self.eqrr ]

        for op in opcodes:
            original = self.registers[:]
            op(*self.operands)
            if self.registers == self.result:
                self.possibles[str(op).split()[2].split(".")[1]] = op
            self.registers = original
        return len(self.possibles)

class VM:
    def __init__(self, opcodes, program):
        self.registers = [0,0,0,0]
        op_maps = { "addr" : self.addr, "addi" : self.addi, "mulr" : self.mulr,
                    "muli" : self.muli, "banr" : self.banr, "bani" : self.bani,
                    "borr" : self.borr, "bori" : self.bori, "setr" : self.setr, 
                    "seti" : self.seti, "gtir" : self.gtir, "gtri" : self.gtri, 
                    "gtrr" : self.gtrr, "eqir" : self.eqir, "eqri" : self.eqri, 
                    "eqrr" : self.eqrr }

        self.opcodes = { k : op_maps[v] for k, v in opcodes.items() }
        self.program = program

    def addr(self, r1, r2, r3): self.registers[r3] = self.registers[r1] + self.registers[r2]
    def addi(self, r1, v2, r3): self.registers[r3] = self.registers[r1] + v2
    def mulr(self, r1, r2, r3): self.registers[r3] = self.registers[r1] * self.registers[r2]
    def muli(self, r1, v2, r3): self.registers[r3] = self.registers[r1] * v2
    def banr(self, r1, r2, r3): self.registers[r3] = self.registers[r1] & self.registers[r2]
    def bani(self, r1, v2, r3): self.registers[r3] = self.registers[r1] & v2
    def borr(self, r1, r2, r3): self.registers[r3] = self.registers[r1] | self.registers[r2]
    def bori(self, r1, v2, r3): self.registers[r3] = self.registers[r1] | v2
    def setr(self, r1, _, r3):  self.registers[r3] = self.registers[r1]
    def seti(self, v1, _, r3):  self.registers[r3] = v1
    def gtir(self, v1, r2, r3): self.registers[r3] = 1 if v1 > self.registers[r2] else 0
    def gtri(self, r1, v2, r3): self.registers[r3] = 1 if self.registers[r1] > v2 else 0
    def gtrr(self, r1, r2, r3): self.registers[r3] = 1 if self.registers[r1] > self.registers[r2] else 0
    def eqir(self, v1, r2, r3): self.registers[r3] = 1 if v1 == self.registers[r2] else 0
    def eqri(self, r1, v2, r3): self.registers[r3] = 1 if self.registers[r1] == v2 else 0
    def eqrr(self, r1, r2, r3): self.registers[r3] = 1 if self.registers[r1] == self.registers[r2] else 0

    def run(self):
        for opcode, *operands in self.program:
            self.opcodes[opcode](*operands)
        return self.registers[0]

def parse_contents(contents):
    s = contents

    while "\n\n" in s:
        s = s[s.index("\n\n")+2:]

    change_states = contents[:len(contents)-len(s)-4]
    program = contents[-len(s):]

    changes = []
    for ch in change_states.split("\n\n"):
        a, b, c = ch.split("\n")
        a = a[9:-1]
        c = c[9:-1]

        changes.append([[int(x) for x in a.split(", ")],
                        [int(x) for x in b.split(" ")],
                        [int(x) for x in c.split(", ")]])

    prog = [[int(y) for y in x.split()] for x in program.strip().split("\n")]

    return changes, prog

def determine_opcodes(vms):
    opcodes = { i : None for i in range(16) }

    while None in opcodes.values():
        for i in [x for x in opcodes.keys() if not opcodes[x]]:
            triples = [x.triple for x in vms if x.opcode == i]
            t_vms = [VMtest(t) for t in triples]
            reduced = reduce(operator.__or__, [set(v.possibles.keys()) for v in t_vms]) 
            reduced -= set(opcodes.values())
            if len(reduced) == 1:
                op = reduced.pop()
                opcodes[i] = op
                vms = [x for x in vms if x.opcode != i]
                for v in vms:
                    if op in v.possibles:
                        v.possibles.pop(op)
    return opcodes
    
def main(args):
    contents = open(args.file).read()
    
    changes, program = parse_contents(contents)

    vms = [VMtest(x) for x in changes]
    print(len([None for x in vms if len(x.possibles) >= 3]))

    opcodes = determine_opcodes(vms)
    vm = VM(opcodes, program)
    print(vm.run())
    
                

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2017 Day {0} AOC: Chronal Classification".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
