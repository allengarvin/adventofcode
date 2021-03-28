#!/usr/bin/python

def run(program, registers):
    pc = 0

    while pc in program.keys():
        i = program[pc][0]
        a = program[pc][1]

        if i == "hlf":
            registers[a[0]] /= 2
            pc += 1
            continue
        if i == "tpl":
            registers[a[0]] *= 3
            pc += 1
            continue
        if i == "inc":
            registers[a[0]] += 1
            pc += 1
            continue
        if i == "jmp":
            pc += int(a[0])
            continue
        if i == "jie" and registers[a[0]] % 2 == 0:
            pc += int(a[1])
            continue
        elif i == "jie":
            pc += 1
            continue
        if i == "jio" and registers[a[0]] == 1:
            pc += int(a[1])
            continue
        elif i == "jio":
            pc += 1
            continue
    return registers["b"]

def main(fn):
    program = dict()

    registers = { "a" : 0, "b" : 0 }
    lno = 0
    for line in open(fn):
        line = line.strip()
        instr = line[:3]
        argstr = line[4:]
        if "," in argstr:
            args = argstr.split(", ")
        else:
            args = [ argstr ]
        program[lno] = [ instr, args ]
        lno += 1

    print(run(program, { "a" : 0, "b" : 0 }))
    print(run(program, { "a" : 1, "b" : 0 }))

if __name__ == "__main__":
    main("23-input.txt")
