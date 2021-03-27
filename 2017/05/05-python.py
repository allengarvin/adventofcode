#!/usr/bin/python

def main():
    orig_prog = map(int, open("../advent/05-input.txt").readlines())

    pc = 0
    steps = 0

    prog = orig_prog[:]
    while pc >= 0 and pc < len(prog):
        prev = pc
        pc += prog[pc]
        prog[prev] += 1
        steps += 1
    print "Answer 1:", steps

    pc = 0
    steps = 0
    prog = orig_prog[:]
    while pc >= 0 and pc < len(prog):
        prev = pc
        pc += prog[pc] 
        prog[prev] += 1 if prog[prev] < 3 else -1
        steps += 1
   
    print "Answer 2:", steps

if __name__ == "__main__":
    main()
