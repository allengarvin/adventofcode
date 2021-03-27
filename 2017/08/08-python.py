#!/usr/bin/python3

import re

def main():
    registers = dict()
    instr = [(x.replace("inc", "+=").replace("dec", "-="), y.strip()) for x, y in [line.split(" if ") for line in open("08-input.txt")]]

    highest = 0

    for cmd, cond in instr:
        var1, rest1 = cmd.split(" ", 1)
        var2, rest2 = cond.split(" ", 1)
        if eval("registers.get('{}', 0) {}".format(var2, rest2)):
            registers[var1] = registers.get(var1, 0)
            exec("registers['{}'] {}".format(var1, rest1))

            if registers[var1] > highest:
                highest = registers[var1]

    print(max(registers.values()))
    print(highest)

if __name__ == "__main__":
    main()
