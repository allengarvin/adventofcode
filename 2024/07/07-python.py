#!/usr/bin/python3.9

import sys, argparse, operator, itertools

def catenate(v1, v2):
    return int(str(v1) + str(v2))

def op_eval2(arr, ops, test_val):
    lval = arr[0]
    for i in range(len(arr)-1):
        lval = ops[i](lval, arr[i+1])
        if lval > test_val: # speed it up
            return -1
    return lval

def test_combs(test_val, arr, seps):
    combines = itertools.product(seps, repeat=len(arr)-1)
    for ops in combines:
        v = op_eval2(arr, list(ops), test_val)
        if v == test_val:
            return v
    return 0

def main(args):
    test_list = []
    for line in open(args.file):
        val, nums = line.strip().split(": ")
        test_list.append([int(val), [int(x) for x in nums.split()]])

    total1, total2 = 0, 0
    for test_val, nums in test_list:
        total1 += test_combs(test_val, nums, [operator.add, operator.mul])
        total2 += test_combs(test_val, nums, [operator.add, operator.mul, catenate])
    print(total1)
    print(total2)

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2024 Day {0} AOC: Bridge Repair".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
