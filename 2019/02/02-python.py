#!/usr/bin/python3

import sys, argparse, operator, re, typing

DEBUG=0

MODE_POSITION=0

ARG1=0
ARG2=1
ARG3=2

OP_ADD=1
OP_MUL=2
OP_HALT=99


class Intcode:
    class Opcode:
        
        def __init__(self, opcode, bytes, params, param_modes, address, computer=None):
            self.bytes = bytes
            self.base_opcode = opcode
            self.params = params
            self.param_modes = param_modes
            self.addr = address
            self.computer = computer
            #print("Opcode({}, {}, {}, {})".format(opcode, bytes, params, param_modes))

        def __repr__(self):
            s = "%04X    " % self.addr

            s += "%-4s\t" % { 1 : "ADD", 2 : "MUL", 3 : "IN",  4 : "OUT", 5 : "JZ",
                           6 : "JNZ", 7 : "SLT", 8 : "SEQ", 9 : "INCB", 99 : "HALT" }[ self.base_opcode ]

            operands = []
            for i in range(self.params):
                if self.param_modes[i] == MODE_POSITION:
                    operands.append("@" + str(self.bytes[1+i]))
                else:
                    print("BUG")
                    sys.exit(1)
            s += "\t".join([str(o) for o in operands])
            return s

        def __str__(self):
            return self.__repr__()

        def run_op(self, program: list, pc: int):
            opc = self.base_opcode
            operands = []
            literal_operands = []
    
            for i in range(self.params):
                if( self.param_modes[i] == MODE_POSITION ):
                    operands.append(program[self.bytes[i+1]])
                    literal_operands.append(self.bytes[i+1])

            self.computer.debug(self)
            # print("  operands:", operands)
            if opc == OP_ADD:
                program[literal_operands[ARG3]] = operands[ARG1] + operands[ARG2]
            elif opc == OP_MUL:
                program[literal_operands[ARG3]] = operands[ARG1] * operands[ARG2]
            elif opc == OP_HALT:
                return -1

            return pc + len(self.bytes)

    def __init__(self, program: list, noun=None, verb=None, input_queue=None):
        self._program_unmodified = program[:]
        self.program = program[:]
        self.pc = 0
        self.halted = False
        self.blocked = False

        if input_queue:
            self.input_queue = input_queue
        else:
            self.input_queue = []
        self.output_queue = []
        self.instructions = {}

        if noun:
            self.program[1] = noun
        if verb:
            self.program[2] = verb

    def debug(self, msg):
        if DEBUG:
            print(msg)

    def read_instruction(self):
        program = self.program

        opcode = program[self.pc]

        base_opcode = opcode % 100
        param_modes = [ (opcode // 100) % 10, (opcode // 1000) % 10, (opcode // 10000) % 10 ]
        params = { 1 : 3, 2 : 3, 3 : 1, 4 : 1, 5 : 2, 6 : 2, 7 : 3, 8 : 3, 9 : 1, 99 : 0 }[base_opcode]
        op_bytes = program[self.pc : self.pc + params + 1]

        if self.pc in self.instructions:
            op = self.instructions[self.pc]
            if op.bytes == op_bytes:
                return op
            else:
                debug("INTEREST: opcode/arguments changed @{}".format(self.pc))

        op_obj = self.Opcode(base_opcode, op_bytes, params, param_modes, self.pc, computer=self)
        self.instructions[self.pc] = op_obj
        return op_obj

    def byte_addr(self, addr: int):
        return self.program[addr]

    def run_program(self):
        self.pc = 0
        while not self.halted and not self.blocked:
            o = self.read_instruction()
            self.pc = o.run_op(self.program, self.pc)

            if self.pc == -1:
                self.halted = True
            #print(self.program)



def main(args):
    program_bytes = [int(x) for x in open(args.file).read().strip().split(",")]

    intcode_instance = Intcode(program_bytes, noun=12, verb=2)
    intcode_instance.run_program()
    print(intcode_instance.byte_addr(0))

    results = {}
    for noun, verb in [(x,y) for x in range(100) for y in range(100)]:
        intcode_instance = Intcode(program_bytes, noun=noun, verb=verb)
        intcode_instance.run_program()
        if intcode_instance.byte_addr(0) == 19690720:
            print(noun * 100 + verb)
            break
        
        

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2019 Day {0} AOC: Program alarm".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
