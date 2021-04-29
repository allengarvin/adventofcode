#!/usr/bin/python3

# arg this is getting really messy, perhaps I should rewrite the whole thing

import sys, argparse, operator, re, typing, itertools

DEBUG=0

MODE_POSITION=0
MODE_PARAMETER=1
MODE_RELATIVE=2

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
OP_INCB=9
OP_HALT=99

def jump_opcode(opc):
    return False
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
            s += "R=%-6d\t" % self.computer.relative

            s += "%05d  " % self.byte_list[0]

            s += "%-4s\t" % { 1 : "ADD", 2 : "MUL", 3 : "IN",  4 : "OUT", 5 : "JNZ",
                           6 : "JZ", 7 : "SLT", 8 : "SEQ", 9 : "INCB", 99 : "HALT" }[ self.base_opcode ]

            operands = []
            for i in range(self.params):
                if self.param_modes[i] == MODE_POSITION:
                    operands.append("@" + str(self.byte_list[1+i]))
                elif self.param_modes[i] == MODE_PARAMETER:
                    operands.append(" " + str(self.byte_list[1+i]))
                elif self.param_modes[i] == MODE_RELATIVE:
                    operands.append("r" + str(self.byte_list[1+i]))
            s += "\t".join([str(o) for o in operands])
            return s

        def __str__(self):
            return self.__repr__()

        def peek(self, memory_address: int):
            return self.computer.peek(memory_address)

        def poke(self, memory_address: int, new_byte: int):
            self.computer.poke(memory_address, new_byte)

        def run_op(self, program: dict, pc: int):
            opc = self.base_opcode
            operands = []
            literal_operands = []
    
            #print("params", self.params)
            #print("bytes", self.byte_list)
            #print("param_modes", self.param_modes)
            if not jump_opcode(opc):        # jumps may be to a non-existent location. We evaluate them later
                #print("FOO", opc)
                for i in range(self.params):
                    if self.param_modes[i] == MODE_POSITION:
                        literal_operands.append(self.byte_list[i+1])
                        operands.append(self.peek(self.byte_list[i+1]))
                    elif self.param_modes[i] == MODE_PARAMETER:
                        literal_operands.append(self.byte_list[i+1])
                        operands.append(self.byte_list[i+1])
                    elif self.param_modes[i] == MODE_RELATIVE:
                        operands.append(self.peek(self.computer.relative + self.byte_list[i+1]))
                        literal_operands.append(self.computer.relative + self.byte_list[i+1])
                        #print("relative, peeking at %d + %d = %d" % (self.computer.relative, self.byte_list[i+1], operands[-1]))
                        
                    else:
                        print("Unknown parameter mode")
                        exit(1)
            else:
                for i in range(self.params-1):
                    if self.param_modes[i] == MODE_POSITION:
                        operands.append(self.peek(self.byte_list[i+1]))
                        literal_operands.append(self.byte_list[i+1])
                    elif self.param_modes[i] == MODE_PARAMETER:
                        operands.append(self.byte_list[i+1])
                        literal_operands.append(self.byte_list[i+1])
                    elif self.param_modes[i] == MODE_RELATIVE:
                        operands.append(self.peek(self.computer.relative + self.byte_list[i+1]))
                        literal_operands.append(self.computer.relative + self.byte_list[i+1])
                    else:
                        print("Unknown parameter mode")
                        exit(1)

            self.computer.debug(self)
            self.computer.debug("                           Values:      " + "".join([" %-7s" % str(x) for x in operands]))

            #self.computer.debug(self.computer.program[63])

            if opc == OP_INCB:
                self.computer.relative += operands[ARG1]
            elif opc == OP_ADD:
                self.poke(literal_operands[ARG3], operands[ARG1] + operands[ARG2])
            elif opc == OP_MUL:
                self.poke(literal_operands[ARG3], operands[ARG1] * operands[ARG2])
            elif opc == OP_HALT:
                return -1
            elif opc == OP_INPUT:
                if self.computer.input_queue:
                    self.poke(literal_operands[ARG1], self.computer.input_queue.pop(0))
                else:
                    self.computer.blocked = True
                    return pc
            elif opc == OP_OUTPUT:
                self.computer.output_queue.append(operands[ARG1])
            elif opc == OP_JNZ:
                if operands[ARG1] != 0:
                    if self.param_modes[-1] == MODE_POSITION:
                        #print("Param_modes", self.param_modes)
                        #print("Jumping via position mode to @%d (real addr %d)" % (self.byte_list[-1], self.peek(self.byte_list[-1])))
                        #return self.peek(self.byte_list[-1])
                        return self.peek(self.byte_list[-1])
                    if self.param_modes[self.params-1] == MODE_PARAMETER:
                        #print("Jumping via parameter mode to %d" % self.byte_list[-1])
                        return self.byte_list[-1]
                    if self.param_modes[self.params-1] == MODE_RELATIVE:
                        return self.peek(self.computer.relative + self.byte_list[-1])
                    print("JNZ BUG")
                    exit(1)
            elif opc == OP_JZ:
                if operands[ARG1] == 0:
                    if self.param_modes[-1] == MODE_POSITION:
                        #print("Param_modes", self.param_modes)
                        #print("Jumping via position mode to @%d (real addr %d)" % (self.byte_list[-1], self.peek(self.byte_list[-1])))
                        return self.peek(self.byte_list[-1])
                    if self.param_modes[self.params-1] == MODE_PARAMETER:
                        #print("Jumping via parameter mode to %d" % self.byte_list[-1])
                        return self.byte_list[-1]
                    if self.param_modes[self.params-1] == MODE_RELATIVE:
                        return self.peek(self.computer.relative + self.byte_list[-1])
                    print("JZ BUG")
                    exit(1)
            elif opc == OP_SLT:
                if operands[ARG1] < operands[ARG2]:
                    self.poke(literal_operands[ARG3], 1)
                else:
                    self.poke(literal_operands[ARG3], 0)
            elif opc == OP_SEQ:
                if operands[ARG1] == operands[ARG2]:
                    self.poke(literal_operands[ARG3], 1)
                else:
                    self.poke(literal_operands[ARG3], 0)
            else:
                print("BYTES", self.byte_list, "opcode=", opc)
                print("BIG BUG NO OPCODE!!")
                exit(1)

            return pc + len(self.byte_list)

    def __init__(self, program: list, noun=None, verb=None):
        self.program = { addr : instr for addr, instr in enumerate(program) }
        self.pc = 0
        self.halted = False
        self.blocked = False
        self.relative = 0

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

    def peek(self, memory_address: int):
        if memory_address < 0:
            raise IndexException("negative memory address {}".format(memory_address))
        #print("peek @", memory_address, "=", self.program.get(memory_address, 0))
        return self.program.get(memory_address, 0)

    def poke(self, memory_address: int, new_byte: int):
        if memory_address < 0:
            raise IndexException("negative memory address {}".format(memory_address))
        self.program[memory_address] = new_byte

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
            
        #op_byte_list = program[self.pc : self.pc + params + 1]
        op_byte_list = [program[x] for x in range(self.pc, self.pc + params + 1)]

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

        while not self.halted:
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
                break

        if self.blocked:
            self.debug("Blocked waiting for input")

    def continue_run(self, input_queue=None):
        #print("Continuing at ", self.read_instruction(), "Input queue is", input_queue)

        if input_queue:
            self.input_queue += input_queue

        self.blocked = False
        while not self.halted:
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
                break




def main(args):
    program_bytes = [int(x) for x in open(args.file).read().strip().split(",")]

    computer = Intcode(program_bytes)
    computer.run_program(input_queue=[1])
    print(computer.output_queue[-1])

    computer = Intcode(program_bytes)
    computer.run_program(input_queue=[2])
    print(computer.output_queue[-1])

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2019 Day {0} AOC: Space Police".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
