#!/usr/bin/python

import os, sys, itertools, string
from collections import deque

def main():
    instructions = []
    register_list = [
        {"queue" : deque([]), "deadlock" : False, "sends" : [] },
        {"queue" : deque([]), "deadlock" : False, "sends" : [] },
    ]

    for l in open("../advent/18-input.txt"):
        cmd = l.strip().split()
        if cmd[1].islower():
            register_list[0][cmd[1]] = 0
            register_list[1][cmd[1]] = 1
        if len(cmd) == 3 and cmd[2].islower():
            register_list[0][cmd[2]] = 0
            register_list[1][cmd[2]] = 1
        instructions.append(cmd)

    def eval_register(pc_num, arg, registers):
        if arg.islower():
            return registers[arg]
        return int(arg)

    pcs = [ 0, 0 ]

    def execute(pc_num):
        pc = pcs[pc_num]
        registers = register_list[pc_num]

        if registers["deadlock"]:
            if len(registers["queue"]) == 0:
                return
            #print "*** Breaking deadlock"
            registers["deadlock"] = False

        cmd = instructions[pc][0]
        arg1 = instructions[pc][1]
        if len(instructions[pc]) == 3:
            arg2 = instructions[pc][2]
        else:
            arg2 = None
        #print "Executing ", cmd, arg1, arg2
        if cmd == "set":
            registers[arg1] = eval_register(pc_num, arg2, registers)
        if cmd == "add":
            registers[arg1] += eval_register(pc_num, arg2, registers)
        if cmd == "mul":
            registers[arg1] *= eval_register(pc_num, arg2, registers)
        if cmd == "mod":
            registers[arg1] %= eval_register(pc_num, arg2, registers)
        if cmd == "rcv":
            if len(registers["queue"]) == 0:
                registers["deadlock"] = True
                #print "Machine", pc_num, "is in deadlock"
                return
            registers[arg1] = registers["queue"].pop()

        flag = False
        if cmd == "jgz":
            if eval_register(pc_num, arg1, registers) > 0:
                pcs[pc_num] += eval_register(pc_num, arg2, registers)
                flag = True
        if cmd == "snd":
            val = eval_register(pc_num, arg1, registers)
            #print "Sending", val, "from pc", pc_num, "to", 1-pc_num
        
            register_list[pc_num]["sends"].append(val)
            register_list[1 - pc_num]["queue"].appendleft(val)
        if not flag:
            pcs[pc_num] += 1


    while True:
        execute(0)
        execute(1)
        if register_list[1]["deadlock"] and register_list[0]["deadlock"]:
            break

    #print "Program 0 sent", len(register_list[0]["sends"])
    #print "Program 1 sent", len(register_list[1]["sends"])
    print "Answer 2: ", len(register_list[1]["sends"])

if __name__ == "__main__":
    main()
