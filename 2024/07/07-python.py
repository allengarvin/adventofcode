#!/usr/bin/python3.9

import sys, argparse, operator
from itertools import product

def catenate(v1, v2):
    return int(str(v1) + str(v2))

# works fine on first problem!
def op_eval(arr, ops):
    if len(arr) == 2:
        return ops[0](arr[0], arr[1])
    else:
        return ops[-1](arr[-1], op_eval(arr[:-1], ops[:-1]))

def op_eval2(arr, ops, test_val):
    lval = arr[0]
    for i in range(len(arr)-1):
        lval = ops[i](lval, arr[i+1])
        if lval > test_val: # speed it up
            return -1
    return lval

def print_ops(test_val, arr, seps, v):
    s = f" {test_val} ?= {arr[0]} "
    m = { operator.mul : "*", operator.add : "+", catenate : "||" }
    for i in range(len(arr)-1):
        s += f"{m[seps[i]]} {arr[i+1]} "
    print(s,"->", v)

def test_combs(test_val, arr, seps):
    combines = product(seps, repeat=len(arr)-1)
    for ops in combines:
        #v = op_eval(arr, list(ops))
        v = op_eval2(arr, list(ops), test_val)
        #print_ops(test_val, arr, ops, v)
        if v == test_val:
            return True

def main(args):
    test_list = []
    for line in open(args.file):
        val, nums = line.strip().split(": ")
        test_list.append([int(val), [int(x) for x in nums.split()]])

    total1, total2 = 0, 0
    for test_val, nums in test_list:
        if test_combs(test_val, nums, [operator.add, operator.mul]):
            total1 += test_val
        if test_combs(test_val, nums, [operator.add, operator.mul, catenate]):
            total2 += test_val
    print(total1)
    print(total2)

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2024 Day {0} AOC: Bridge Repair".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
