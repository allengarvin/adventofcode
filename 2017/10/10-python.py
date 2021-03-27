#!/usr/bin/python

import os, sys, itertools, string
from operator import xor

def main():

    length = 256
    # input_str = "3,4,1,5"
    input_str = "106,118,236,1,130,0,235,254,59,205,2,87,129,25,255,118"

    orig_input = map(int, input_str.split(","))
    orig_nums = list(range(length))

    input = [ord(p) for p in list(input_str)] + [17, 31, 73, 47, 23]
    nums = list(range(length)) 

    cur = 0
    skip = 0
    for i in orig_input:
        tmp = []
     
        for j in range(i):
            tmp.append(orig_nums[(cur + j) % length])
        tmp = tmp[::-1]
        for j in range(i):
            orig_nums[(cur+j) % length] = tmp[j]
     
        cur = (cur + i + skip) % length
        skip += 1
    print "Answer 1:", orig_nums[0] * orig_nums[1]

    cur = 0
    skip = 0

    for a in range(64):
        for i in input:
            tmp = []
        
            for j in range(i):
                tmp.append(nums[(cur + j) % length])
            tmp = tmp[::-1]
            for j in range(i):
                nums[(cur+j) % length] = tmp[j]
        
            cur = (cur + i + skip) % length
            skip += 1

    hash = []
    for i in range(0, 256, 16):
        hash += [reduce(xor, nums[i:i+16])]

    print "Answer 2:", "".join(map(lambda x: "%02x" % x, hash))


    return 1

if __name__ == "__main__":
    main()
