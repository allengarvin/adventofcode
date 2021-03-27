#!/usr/bin/python

import sys, os, argparse, operator, re
from parse import parse

def f_rule(str):
    r = { "type" : str.split(":")[0] }
    p = parse("{l1:d}-{h1:d} or {l2:d}-{h2:d}", str[str.index(":")+2:])
    r.update(p.__dict__["named"])
    return r

def f_my_ticket(str):
    return map(int, str.split(","))

def f_other_tickets(str):
    return map(int, str.split(","))

def all_invalid(ticket, rules):
    for i in ticket:
        validity = False

        for r in rules:
            if r["l1"] <= i <= r["h1"] or r["l2"] <= i <= r["h2"]:
                validity = True
        if not validity:
            return i
    return ticket

def solve(columns, rulesets):
    c_map = {}

    if len(rulesets) == 0:
        return {}
    for i, c in enumerate(columns):
        cnt = 0
        for k, v in rulesets.iteritems():
            if c.issubset(v):
                match_k = k
                cnt += 1
        if cnt == 1:
            c_map[i] = match_k
            del rulesets[match_k]
            c_map.update(solve(columns, rulesets))
    return c_map

def main(args):
    fd = open(args.file)

    parse_type = [ f_rule, f_my_ticket, f_other_tickets ]
    entries = [ [], [], [] ]
    parse_cnt = 0

    for line in fd:
        line = line.strip()
        if line == '':
            parse_cnt += 1
            continue
        if line == "your ticket:" or line == "nearby tickets:":
            continue

        entries[parse_cnt].append(parse_type[parse_cnt](line))

    rules, my_ticket, other_tickets = entries
    my_ticket = my_ticket[0]

    bad_nums = []
    potentially_valid = []

    invalid_map = [all_invalid(t, rules) for t in other_tickets]
    print("Problem 1: %d" % sum(filter(lambda x: isinstance(x, int), invalid_map)))
    all_tickets = [my_ticket] + filter(lambda x: isinstance(x, list), invalid_map)
    
    rulesets = {}
    for r in rules:
        rulesets[r["type"]] = set(range(r["l1"], r["h1"]+1)).union(set(range(r["l2"], r["h2"]+1)))

    columns = []
    for i, _ in enumerate(my_ticket):
        columns.append(set(zip(*all_tickets)[i]))

    column_map = solve(columns, rulesets)

    nums = []
    for k, v in column_map.iteritems():
        if v.startswith("departure"):
            nums.append(my_ticket[k])
    print("Problem 2: %d" % reduce(operator.mul, nums))
    
if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day X AOC: FOO FOO")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    main(ap.parse_args())
    
