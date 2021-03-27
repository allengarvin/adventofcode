#!/usr/bin/python3

import sys

def query_fuel(mass, recursive=False):
    f = mass // 3 - 2
    if f <= 0:
        return 0

    if recursive:
        return f + query_fuel(f, recursive=True)
    else:
        return f

def main(fn):
    lines = [int(x.strip()) for x in open(fn).readlines()]
    fuel_req1 = [query_fuel(x) for x in lines]
    print(sum(fuel_req1))

    fuel_req2 = [query_fuel(x, recursive=True) for x in lines]
    print(sum(fuel_req2))

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    main(default_file if len(sys.argv) == 1 else sys.argv[1])
    
