#!/usr/bin/python

import os, sys, itertools, string
from collections import deque

def main():
    instructions = []
    register_list = { "a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, }

    for l in open("23-input.txt"):
        cmd = l.strip().split()
        instructions.append(cmd)

    def eval_register(pc_num, arg, registers):
        if arg.islower():
            return registers[arg]
        return int(arg)

    #print register_list

    pcs = [ 0, 0 ]

    mul_count = 0
    pc_num = 0
    while True:
        pc = pcs[pc_num]
        if pc < 0 or pc >= len(instructions):
            break

        cmd = instructions[pc][0]
        arg1 = instructions[pc][1]
        if len(instructions[pc]) == 3:
            arg2 = instructions[pc][2]
        else:
            arg2 = None
        #print "Executing ", cmd, arg1, arg2
        if cmd == "set":
            register_list[arg1] = eval_register(pc_num, arg2, register_list)
        if cmd == "sub":
            register_list[arg1] -= eval_register(pc_num, arg2, register_list)
        if cmd == "mul":
            register_list[arg1] *= eval_register(pc_num, arg2, register_list)
            mul_count += 1

        flag = False
        if cmd == "jnz":
            if eval_register(pc_num, arg1, register_list) != 0:
                jump_val = eval_register(pc_num, arg2, register_list)
                pcs[pc_num] += jump_val
                if jump_val != 2:
                    #print "Jumping to ", instructions[pcs[pc_num]]
                    #print register_list
                    pass
                flag = True
        if not flag:
            pcs[pc_num] += 1
        if pcs[pc_num] == 24:
            #print register_list
            break
        #print register_list
    print mul_count


if __name__ == "__main__":
    main()
