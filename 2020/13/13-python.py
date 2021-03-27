#!/usr/bin/python3

import sys, os, argparse, operator, re, functools
from egcd import egcd
 
def eq_func(t):
    c, p, o = t
    return o * c * (egcd(o, p)[1] % p)

def crt(congruences, primes):
    lcm = functools.reduce(operator.mul, primes)
    lcm_d = map(lambda x: lcm // x, primes)

    return sum(map(eq_func, zip(congruences, primes, lcm_d))) % lcm

def main(args):
    fd = open(args.file)
    departure = int(fd.readline())
    buses = [int(x) if x.isdigit() else x for x in fd.readline().strip().split(",") ]

    tm = departure

    prob1_unsolved = True
    while prob1_unsolved:
        for b in buses:
            if isinstance(b, int) and tm % b == 0:
                print("Problem 1: %d" % (b * (tm - departure)))
                prob1_unsolved = False
                break
        tm += 1

    congruences = list(filter(lambda x: x > -1, [ (p - n) % p if isinstance(p, int) else -1 for n, p in enumerate(buses)]))
    primes = list(filter(lambda x: isinstance(x, int), buses))

    print("Problem 2: %d" % crt(congruences, primes))

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day X AOC: Shuttle search")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    args = ap.parse_args()
    main(args)
    
