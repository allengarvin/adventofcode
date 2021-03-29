#!/usr/local/bin/python3.7

# NEED to rewrite for part 2

import sys, os, argparse, operator, re
from collections import deque

cnt = 1
revlist = list(range(1,10))[::-1]

def cycle(circle, args):
    global cnt

    if args.verbose:
        print("-- move {0}--".format(cnt))
        print(circle)

    try:
        pulled = circle.pop3()
    except:
        print("Count: ", cnt)
        print("Circle.cup:", circle.cup)
        sys.exit(1)

    pulled_num = [x.number for x in pulled]
    if args.verbose:
        print("pick up: {0}".format(" ".join(map(str, pulled))))
        print(circle)

    cup = circle.cup.number

    for i in range(1,6):
        c_try = (cup-i) % (1000000 if args.two else 10)
        if c_try and c_try not in pulled_num:
            dest = circle.ll_map[c_try]
            break

    if args.verbose:
        print("destination: {0}\n".format(dest))

    circle.insert3(dest, pulled)
    circle.set_cup(circle.cup.nref)
    if args.verbose:
        print
    cnt += 1
    if cnt % 10000 == 0:
        node_1 = circle.ll_map[1]
        print(cnt, node_1, node_1.nref, node_1.nref.nref)
    
    
class Element:
    is_cup = False
    debug = False
 
    def __init__(self, n):
        self.number = n
        self.pref = None
        self.nref = None

    def __str__(self): 
        if self.debug:
            return "({0} P:{1} N:{2})".format(self.number, self.pref, self.nref) if self.is_cup else "[{0} P:{1} N:{2}]".format(self.number, self.pref, self.nref)
        return "({0})".format(self.number) if self.is_cup else str(self.number)

    def __repr__(self): return self.__str__()

class LList:
    cup = None

    def __init__(self):
        self.start_node = None
        self.end_node = None
        self.ll_map = dict()

    def initialize(self, n):
        node = Element(n)
        self.end_node, self.start_node, self.cup = node, node, node
        self.ll_map[n] = self.start_node
        self.start_node.is_cup = True

    def append(self, n):
        if not self.start_node:
            self.initialize(n)
            return
        new_node = Element(n)
        self.ll_map[n] = new_node
        self.end_node.nref = new_node
        new_node.pref = self.end_node
        self.end_node = new_node

    def close_circle(self):
        self.end_node.nref = self.start_node
        self.start_node.pref = self.end_node

    def set_cup(self, n):
        if self.cup:
            self.cup.is_cup = False

        new_cup = self.ll_map[n.number]
        new_cup.is_cup = True
        self.cup = new_cup

        self.start_node = new_cup
        self.end_node = new_cup.pref
    
    def __iter__(self):
        n = self.start_node
        while True:
            yield n
            if n == self.end_node:
                break
            n = n.nref

    def index(self, n):
        return self.ll_map[n]

    def pop3(self):
        a = self.cup.nref
        b = a.nref
        c = b.nref
            
        self.cup.nref = c.nref
        c.nref.pref = self.cup
        a.pref = None
        c.nref = None
        return [a, b, c]

    def insert3(self, node, arr):
        a, b, c = arr
        a.pref = node
        c.nref = node.nref

        c.nref.pref = c
        node.nref = a

    def insert(self, num, el):
        num_e = self.ll_map[num]
        num_e.nref.pref = el
        el.nref = num_e.nref
        num_e.nref = el
        el.pref = num_e

    def __str__(self): return "cups: {0}".format(" ".join(map(str, list(self))))
    def __repr__(self): return self.__str__()

    def verify(self):
        prev = self.end_node
        for n in self:
            assert n.nref != n
            assert n.pref != n
            assert n.pref.nref == n
            assert n.nref.pref == n
        return True
            
    
def main(args):
    circle = LList()
    for x in str(args.label):
        circle.append(int(x))

    if not args.two and not args.one:
        args.one = True

    if args.two:
        for i in range(10, 1000001):
            circle.append(i)
    circle.close_circle()

    for i in range(10000000 if args.two else 100):
        cycle(circle, args)

    if args.one:
        print(circle)
        print("Problem 1: {0}".format("".join(map(lambda x: str(x.number), list(circle)))))
    else:
        print("{0},{1}".format(circle.ll_map[1].nref, circle.ll_map[1].nref.nref))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2020 Day {0} AOC: Crab Cups".format(day))
    ap.add_argument("-v", "--verbose", action="store_true", help="Print some output")
    ap.add_argument("-1", "--one", action="store_true", help="Problem 1")
    ap.add_argument("-2", "--two", action="store_true", help="Problem 2")
    ap.add_argument("label", help="Labeling", default=327465189, type=int, nargs="?")
    args = ap.parse_args()
    if args.one and args.two:
        print("In this problem, -1 and -2 are exclusive.")
        sys.exit(1)
    main(ap.parse_args())
    
