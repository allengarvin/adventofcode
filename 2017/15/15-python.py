#!/usr/bin/python

import os, sys, itertools, string
from collections import deque

def main():
    a = 703
    b = 516
    a_factor = 16807
    b_factor = 48271

    count = 0
    #print "--Gen. A--  --Gen. B--"
    matches = 0
    a_match = 0

    dq_a = deque([])
    dq_b = deque([])

    b_flag = False
    a_flag = False
    a_count = 0
    while True:
        nul, a = divmod(a * a_factor, 2147483647)
        nul, b = divmod(b * b_factor, 2147483647)

        if not b_flag:
            if a % 4 == 0:
                dq_a.appendleft(a)
    
            if b % 8 == 0:
                dq_b.appendleft(b)

            if len(dq_a) and len(dq_b):
                if dq_a.pop() & 65535 == dq_b.pop() & 65535:
                    #print count+1, "match"
                    matches += 1
                count += 1

        if a & 65535 == b & 65535:
            a_match += 1
        if a_count == 40000000:
            print "Answer 1:", a_match
            a_flag = True
        a_count += 1

        if not b_flag and count == 5000000:
            print "Answer 2:", matches
            b_flag = True

        if a_flag and b_flag:
            return

if __name__ == "__main__":
    main()
