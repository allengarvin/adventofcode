#!/usr/bin/python

import sys, os, argparse, operator, re
from parse import parse

def apply_mask1(num, mask):
    num |= mask[0]
    num &= mask[1]
    return num

def apply_mask2(addr, num, mask, core):
    masks = [0]
    for n, b in enumerate(mask[0]):
        if b == "X":
             for m in masks[:]:
                 masks.append(m | (2**(35-n)))
        
    for m in masks:
        core[addr | m] = num

def problem1(fn):
    core = dict()
    mask = [ 0, 0xfffffffff]

    for line in open(fn):
        line = line.strip()

        if line.startswith("mask"):
            mask = [ 0, 0xfffffffff]
            for n, bit in enumerate(list(line.split(" = ")[1])):
                if bit.isdigit():
                    if bit == "1":
                        mask[0] |= 2**(35-n)
                    elif bit == "0":
                        mask[1] ^= 2**(35-n)
        if line.startswith("mem"):
            mem = parse("mem[{:d}] = {:d}", line)
            core[mem[0]] = apply_mask1(mem[1], mask)

    return sum(core.values())

def problem2(fn):
    core = dict()
    for line in open(args.file):
        line = line.strip()

        if line.startswith("mask"):
            m = line.split(" = ")[1]
            mask = [["X" if x == "X" else 0 for x in list(m)], 0]
            for n, bit in enumerate(list(m)):
                if bit.isdigit() and bit == "1":
                    mask[1] |= 2**(35-n)
        if line.startswith("mem"):
            addr, num = parse("mem[{:d}] = {:d}", line)
            addr |= int(m.replace("X", "0"), 2)
            addr &= 0xfffffffff & int(m.replace("0", "1").replace("X", "0"),2)
            apply_mask2(addr, num, mask, core)
    return sum(core.values())

def main(args):
    print("Problem 1: %d" % problem1(args.file))
    print("Problem 2: %d" % problem2(args.file))

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day 14 AOC: Docking data")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    args = ap.parse_args()
    main(args)
    
