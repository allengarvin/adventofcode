#!/usr/bin/python3

import sys, os, argparse, operator, re

def query_fuel(mass, recursive=False):
    f = mass // 3 - 2
    if f <= 0:
        return 0

    if recursive:
        return f + query_fuel(f, recursive=True)
    else:
        return f

def main(args):
    lines = [int(x.strip()) for x in open(args.file).readlines()]
    fuel_req1 = [query_fuel(x) for x in lines]
    print(sum(fuel_req1))

    fuel_req2 = [query_fuel(x, recursive=True) for x in lines]
    print(sum(fuel_req2))

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2019 Day 1 AOC: Tyranny of the Rocket Equation")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    args = ap.parse_args()
    main(args)
    
