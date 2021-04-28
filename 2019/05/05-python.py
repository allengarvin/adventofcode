#!/usr/bin/python3

import sys, argparse, operator, re, typing

DEBUG=0

MODE_POSITION=0
MODE_PARAMETER=1

ARG1=0
ARG2=1
ARG3=2

OP_ADD=1
OP_MUL=2
OP_INPUT=3
OP_OUTPUT=4
OP_JNZ=5
OP_JZ=6
OP_SLT=7
OP_SEQ=8
OP_HALT=99

def jump_opcode(opc):
    return opc in [OP_JZ, OP_JNZ ]

class Intcode:
    class Opcode:
        
        def __init__(self, opcode, byte_list, params, param_modes, address, computer=None):
            self.byte_list = byte_list
            self.base_opcode = opcode
            self.params = params
            self.param_modes = param_modes
            self.addr = address
            self.computer = computer
            #print("Opcode({}, {}, {}, {})".format(opcode, byte_list, params, param_modes))

        def __repr__(self):
            s = "%04X    " % self.addr

            s += "%05d  " % self.byte_list[0]

            s += "%-4s\t" % { 1 : "ADD", 2 : "MUL", 3 : "IN",  4 : "OUT", 5 : "JNZ",
                           6 : "JZ", 7 : "SLT", 8 : "SEQ", 9 : "INCB", 99 : "HALT" }[ self.base_opcode ]

            operands = []
            for i in range(self.params):
                if self.param_modes[i] == MODE_POSITION:
                    operands.append("@" + str(self.byte_list[1+i]))
                else:
                    operands.append(" " + str(self.byte_list[1+i]))
            s += "\t".join([str(o) for o in operands])
            return s

        def __str__(self):
            return self.__repr__()

        def run_op(self, program: list, pc: int):
            opc = self.base_opcode
            operands = []
            literal_operands = []
    
            #print("params", self.params)
            #print("bytes", self.byte_list)
            #print("param_modes", self.param_modes)
            if not jump_opcode(opc):        # jumps may be to a non-existent location. We evaluate them later
                for i in range(self.params):
                    if( self.param_modes[i] == MODE_POSITION ):
                        operands.append(program[self.byte_list[i+1]])
                        literal_operands.append(self.byte_list[i+1])
                    if( self.param_modes[i] == MODE_PARAMETER ):
                        operands.append(self.byte_list[i+1])
                        literal_operands.append(self.byte_list[i+1])
            else:
                for i in range(self.params-1):
                    if( self.param_modes[i] == MODE_POSITION ):
                        operands.append(program[self.byte_list[i+1]])
                        literal_operands.append(self.byte_list[i+1])
                    if( self.param_modes[i] == MODE_PARAMETER ):
                        operands.append(self.byte_list[i+1])
                        literal_operands.append(self.byte_list[i+1])

            self.computer.debug(self)
            if opc == OP_ADD:
                program[literal_operands[ARG3]] = operands[ARG1] + operands[ARG2]
            elif opc == OP_MUL:
                program[literal_operands[ARG3]] = operands[ARG1] * operands[ARG2]
            elif opc == OP_HALT:
                return -1
            elif opc == OP_INPUT:
                #print("input_queue", self.computer.input_queue)
                if self.computer.input_queue:
                    program[literal_operands[ARG1]] = self.computer.input_queue.pop(0)
                else:
                    self.computer.blocked = True
                    return pc
            elif opc == OP_OUTPUT:
                self.computer.output_queue.append(operands[ARG1])
            elif opc == OP_JNZ:
                if operands[ARG1] != 0:
                    if self.param_modes[-1] == MODE_POSITION:
                        #print("Param_modes", self.param_modes)
                        #print("Jumping via position mode to @%d (real addr %d)" % (self.byte_list[-1], program[self.byte_list[-1]]))
                        return program[self.byte_list[-1]]
                    if self.param_modes[self.params-1] == MODE_PARAMETER:
                        #print("Jumping via parameter mode to %d" % self.byte_list[-1])
                        return self.byte_list[-1]
                    print("JNZ BUG")
                    exit(1)
            elif opc == OP_JZ:
                if operands[ARG1] == 0:
                    if self.param_modes[-1] == MODE_POSITION:
                        #print("Param_modes", self.param_modes)
                        #print("Jumping via position mode to @%d (real addr %d)" % (self.byte_list[-1], program[self.byte_list[-1]]))
                        return program[self.byte_list[-1]]
                    if self.param_modes[self.params-1] == MODE_PARAMETER:
                        #print("Jumping via parameter mode to %d" % self.byte_list[-1])
                        return self.byte_list[-1]
                    print("JZ BUG")
                    exit(1)
            elif opc == OP_SLT:
                if operands[ARG1] < operands[ARG2]:
                    program[literal_operands[ARG3]] = 1
                else:
                    program[literal_operands[ARG3]] = 0
            elif opc == OP_SEQ:
                if operands[ARG1] == operands[ARG2]:
                    program[literal_operands[ARG3]] = 1
                else:
                    program[literal_operands[ARG3]] = 0
            else:
                print("BYTES", self.byte_list, "opcode=", opc)
                print("BIG BUG NO OPCODE!!")
                exit(1)

            return pc + len(self.byte_list)

    def __init__(self, program: list, noun=None, verb=None):
        self._program_unmodified = program[:]
        self.program = program[:]
        self.pc = 0
        self.halted = False
        self.blocked = False

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
        if base_opcode == 99 or (base_opcode > 0 and base_opcode < 10):
            params = { 1 : 3, 2 : 3, 3 : 1, 4 : 1, 5 : 2, 6 : 2, 7 : 3, 8 : 3, 9 : 1, 99 : 0 }[base_opcode]
        else:
            print("PC bug, landed on pc=%d (contents=%d) which is not an opcode" % (self.pc, program[self.pc]))
            exit(1)
        param_modes = [ (opcode // 100) % 10, (opcode // 1000) % 10, (opcode // 10000) % 10 ]
        param_modes = param_modes[:params]
            
        op_byte_list = program[self.pc : self.pc + params + 1]

        if self.pc in self.instructions:
            op = self.instructions[self.pc]
            if op.byte_list == op_byte_list:
                return op
            else:
                debug("INTEREST: opcode/arguments changed @{}".format(self.pc))

        op_obj = self.Opcode(base_opcode, op_byte_list, params, param_modes, self.pc, computer=self)
        self.instructions[self.pc] = op_obj
        return op_obj

    def byte_addr(self, addr: int):
        return self.program[addr]

    def run_program(self, input_queue=None):
        self.pc = 0

        if input_queue:
            self.input_queue += input_queue

        while not self.halted and not self.blocked:
            o = self.read_instruction()
            self.pc = o.run_op(self.program, self.pc)

            if self.pc == -1:
                self.halted = True
            #print(self.output_queue)
            #print(self.program)
            if self.pc > len(self.program):
                print("BUG: jumped beyond memory")
                exit(1)

        if self.blocked:
            self.debug("Blocked waiting for input")



def main(args):
    program_bytes = [int(x) for x in open(args.file).read().strip().split(",")]

    intcode_instance = Intcode(program_bytes)
    intcode_instance.run_program(input_queue=[1])
    print(intcode_instance.output_queue[-1])

    intcode_instance = Intcode(program_bytes)
    intcode_instance.run_program(input_queue=[5])
    print(intcode_instance.output_queue[-1])
        

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2019 Day {0} AOC: Sunny with a Chance of Asteroids".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
