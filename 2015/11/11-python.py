#!/usr/local/bin/python3.7

import sys, argparse, operator, re
from functools import reduce
from string import ascii_lowercase as lowerc

# base-26 conversion from stack overflow "Excel" base:
def divmod_26(n):
    a, b = divmod(n, 26)
    if b == 0:
        return a - 1, b + 26
    return a, b

def to_26(num):
    chars = []
    while num > 0:
        num, d = divmod_26(num)
        chars.append(lowerc[d - 1])
    return ''.join(reversed(chars))

def from_26(chars):
    return reduce(lambda r, x: r * 26 + x + 1, map(lowerc.index, chars), 0)

class PasswdValidator:
    def __init__(self):
        self.pairs = "|".join(["".join(x) for x in zip(lowerc,lowerc)])
        self.seqs = "|".join([lowerc[i:i+3] for i, l in enumerate(lowerc[:-2])])

    def validate(self, p):
        if "i" in p or "o" in p or "l" in p:
            return False
        if len(re.findall(self.pairs, p)) < 2:
            return False
        if not re.findall(self.seqs, p):
            return False
        return True
            
def main(args):
    num = from_26(args.oldpass)
    p = PasswdValidator()
    cnt = 0

    while True:
        num += 1
        test_pass = to_26(num)
        if p.validate(test_pass):
            if cnt == 0:
                print("Part 1: {0}".format(test_pass))
                cnt += 1
            elif cnt == 1:
                print("Part 2: {0}".format(test_pass))
                break

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2015 Day {0} AOC: Not Quite Lisp".format(day))
    ap.add_argument("oldpass", help="Old password", default="cqjxjnds", nargs="?")
    main(ap.parse_args())
    
