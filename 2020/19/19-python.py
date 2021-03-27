#!/usr/bin/python

import sys, os, argparse, operator, copy

def match(rules, msg, r, d):
    #print " " * d + "* match('{0}') {1}".format(msg, str(r))
    if len(r) == 0:
        return msg == ""
    left, r = r[0], r[1:]
    next_r = rules[left]

    if isinstance(next_r, str):
        # print " " * d, msg[1:], ",".join(map(str, r))
        if len(msg) == 0:
            return False
        return msg[0] == next_r and match(rules, msg[1:], r, d+1)
    # print " " * d, msg, "next=", ",".join(map(str, next_r)), "current=", ",".join(map(str, r))
    return reduce(operator.or_, [match(rules, msg, x + r, d+1) for x in next_r])
    
def main(args):
    rule_lines, messages = map(lambda x: x.splitlines(), open(args.file).read().split("\n\n"))
    rules1 = dict()

    for r in rule_lines:
        l, r = r.split(": ")
        if '"' in r:
            rules1[int(l)] = r.strip('"')
        else:
            rules1[int(l)] = [map(int, x.split()) for x in r.split(" | ")]

    rules2 = copy.deepcopy(rules1)
    rules2[8] = [[42], [42, 8]]
    rules2[11] = [[42, 31], [42, 11, 31]]

    cnt1 = cnt2 = 0
    for msg in messages:
        if match(rules1, msg, [0], 0):
            cnt1 += 1
        if match(rules2, msg, [0], 0):
            cnt2 += 1
    print("Problem 1: %d" % cnt1)
    print("Problem 2: %d" % cnt2)
        

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    default_file = day + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day {0} AOC: Monster Messages".format(day))
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    main(ap.parse_args())
    
