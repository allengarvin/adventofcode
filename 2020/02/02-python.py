#!/usr/bin/python

import sys, os, argparse
from parse import parse
from operator import xor

def main(args):
    a, b = 0, 0
    for line in open(args.file).readlines():
        p = parse("{low:d}-{high:d} {let:1w}: {passwd:w}\n", line)
        ns = argparse.Namespace(**p.__dict__["named"])
        a += ns.low <= ns.passwd.count(ns.let) <= ns.high
        b += xor(ns.passwd[ns.low-1] == ns.let, ns.passwd[ns.high-1] == ns.let)
    print("Problem 1: {0}".format(a))
    print("Problem 2: {0}".format(b))

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day 2 AOC: Password philosophy")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    main(ap.parse_args())
    
