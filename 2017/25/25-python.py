#!/usr/bin/python

# I was out of town, and exhausted before midnight, and had a busy Christmas,
#   so I couldn't do this until the next day

import os, sys, itertools, string
from collections import defaultdict
from parse import parse

def main(argv):


    begin_state = None
    steps = None

    current_state = None
    current_value = None

    state_instructions = dict()

    for l in open("../advent/25-input.txt").readlines():
        l = l.strip()
        if parse("Begin in state {}.", l):
            begin_state = parse("Begin in state {}.", l)[0]
        if parse("Perform a diagnostic checksum after {:d} steps.", l):
            steps = parse("Perform a diagnostic checksum after {:d} steps.", l)[0]
        if parse("In state {}:", l):
            current_state = parse("In state {}:", l)[0]
            state_instructions[current_state] = [ [None, None, None], [None, None, None] ]
        if parse("If the current value is {:d}:", l):
            current_value = parse("If the current value is {:d}:", l)[0]
        if "Move one slot to the right" in l:
            state_instructions[current_state][current_value][1] = 1
        if "Move one slot to the left" in l:
            state_instructions[current_state][current_value][1] = -1
        if parse("- Write the value {:d}.", l):
            state_instructions[current_state][current_value][0] = parse("- Write the value {:d}.", l)[0]
        if parse("- Continue with state {}.", l):
            tmp = parse("- Continue with state {}.", l)[0]
            state_instructions[current_state][current_value][2] = tmp
    
    tape = defaultdict(lambda: 0)
    current_pos = 0
    current_state = "A"

    #print state_instructions

    for st in xrange(steps):
        val, dir, state = state_instructions[current_state][tape[current_pos]]
        tape[current_pos] = val
        current_pos += dir
        current_state = state

        
    print "Answer 1:", sum(tape.values())
    
    # 576116 is too high

if __name__ == "__main__":
    main(sys.argv)
