#!/usr/bin/python

import sys, os, argparse, operator, re

def execute(tape):
    loop_detect = [0] * len(tape)

    pc = 0
    acc = 0
    completed = False

    while True:
        if pc >= len(tape):
            completed = True
            break
        elif loop_detect[pc] == 1:
            break
        loop_detect[pc] += 1 

        op, arg = tape[pc]
        if op == "nop":
            pc += 1
        elif op == "acc":
            acc += arg
            pc += 1
        elif op == "jmp":
            pc += arg

    return (acc, completed)

def main(args):
    instr = []
    tape = []
    for line in open(args.file).readlines():
        instr = line.split()[0]
        arg = int(line.strip().split()[1])
        tape.append((instr, arg))

    print("Problem 1: %d" % execute(tape)[0])
        
    changes = []
    for i, t in enumerate(tape):
        if t[0] == "nop" or t[0] == "jmp":
            changes.append(i)
    for n in changes:
        new_tape = tape[:]
        if new_tape[n][0] == "nop":
            new_tape[n] = ("jmp", new_tape[n][1])
        else:
            new_tape[n] = ("nop", new_tape[n][1])

        acc, comp = execute(new_tape)
        if comp == True:
            print("Problem 2: %d" % acc)

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day 8 AOC: Handheld halting")
    ap.add_argument("-1", "--one", action="store_true", help="Problem 1")
    ap.add_argument("-2", "--two", action="store_true", help="Problem 2")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    args = ap.parse_args()
    if not args.one and not args.two:
        args.one = args.two = True
    main(args)
    
