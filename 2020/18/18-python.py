#!/usr/bin/python

import sys, os, argparse, operator, re

def flat_precedence(c):
    return 1

def rev_precedence(c):
    if c == "+" or c == "-":
        return 2
    if c == "*":
        return 1

def trad_precedence(c):
    if c == "+" or c == "-":
        return 1
    if c == "*":
        return 2

def to_postfix(s, precedence_type):
    postfix = ""
    stack = []

    def is_operator(c):
        return c == "*" or c == "-" or c == "+"

    #print "%-20s %-10s %-20s" % ("Infix", "Op stack", "Postfix")

    for i, ch in enumerate(s):
        if ch.isspace():
            continue

    #    print "%-20s %-10s %-20s" % (s[:i+1], "".join(stack), postfix)
        if ch.isdigit():
            postfix += ch
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            top = stack[-1]
            while top != "(":
                postfix += stack.pop()
                top = stack[-1]
            stack.pop()
        elif is_operator(ch):
            if len(stack):
                top = stack[-1]
                while len(stack) and is_operator(top) and precedence_type(ch) <= precedence_type(top):
                    postfix += stack.pop()
                    if len(stack):
                        top = stack[-1]
                stack.append(ch)
            else:
                stack.append(ch)
            
    while len(stack):
        postfix += stack.pop()

    #print "%-20s %-10s %-20s" % (s[:i+1], "".join(stack), postfix)
    return postfix

def evaluate(pf):
    stack = []

    for c in pf:
        if c.isdigit():
            stack.append(int(c))
        else:
            stack.append(eval("%d %s %d" % (stack.pop(), c, stack.pop())))
    return stack.pop()
            
def main(args):
    sum_2 = sum_1 = 0

    for line in open(args.file):
        line = line.strip()
        pf1 = to_postfix(line, flat_precedence)
        pf2 = to_postfix(line, rev_precedence)
        sum_1 += evaluate(pf1)
        sum_2 += evaluate(pf2)

    print("Problem 1: %d" % sum_1)
    print("Problem 2: %d" % sum_2)

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day 18 AOC: Operation Order")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    main(ap.parse_args())
    
