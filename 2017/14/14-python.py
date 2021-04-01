#!/usr/bin/python

# My original 2017 solution--needs to be rewritten

import os, sys, itertools, string
from operator import xor
from functools import reduce

def hex2bin(s):
    return bin(int(s, 16))[2:].zfill(128)

def hash(input_str):
    length = 256

    input = [ord(p) for p in list(input_str)] + [17, 31, 73, 47, 23]
    nums = list(range(length)) 

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

    return "".join(map(lambda x: "%02x" % x, hash))

def showmap(s):
    return s.replace("0", ".").replace("1", "#")

def adjacent(y, x):
    adj = []

    if y > 0:
        adj.append( (y-1,x) )
    if y < 127:
        adj.append( (y+1,x) )
    if x > 0:
        adj.append( (y,x-1) )
    if x < 127:
        adj.append( (y,x+1) )
    return adj

def fill(m, y, x):
    m[y] = m[y][:x] + "1" + m[y][x+1:]
    for j, i in adjacent(y, x):
        if m[j][i] == "#":
            m = fill(m, j, i)
    return m

def part2(a):
    count = 0

    while True:
        flag = False
        for y in range(128):
            if "#" not in a[y]:
                continue
            x = a[y].index("#")
            a = fill(a, y, x)
            count += 1
            flag = True
            break
    
        if flag:
            a = map(lambda x: x.replace("1", "."), a)
            continue
        break
    print(count)


def main(fn):
    init_seed = open(fn).read().strip()
    score = 0

    smap = []
    for i in range(128):
        seed = init_seed + "-%d" % i
        h = hash(seed)
        score += hex2bin(h).count("1")
        smap += [showmap(hex2bin(h))]
        
    print(score)
    part2(smap)
    return 0

if __name__ == "__main__":
    main("14-input.txt" if len(sys.argv) == 1 else sys.argv[1])
