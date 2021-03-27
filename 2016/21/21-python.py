#!/usr/local/bin/python3.7

import sys, argparse, operator, re
from parse import parse

def swap(s, p1, p2):
    l = list(s)
    l[p1], l[p2] = l[p2], l[p1]
    return "".join(l)

def reverse(s, p1, p2):
    return s[:p1] + s[p1:p2+1][::-1] + s[p2+1:]

def swap_letter(s, p1, p2):
    return swap(s, s.index(p1), s.index(p2))

def rotate_left(s, steps):
    return s[steps:] + s[:steps]

def rotate_right(s, steps):
    return rotate_left(s, len(s) - steps)

def move(s, p1, p2):
    a, b = p1, p2
    if b > a:
        return s[:a] + s[a+1:b+1] + s[a] + s[b+1:]
    else:
        return s[:b] + s[a] + s[b:a] + s[a+1:]

def rmove(s, p1, p2):
    return move(s, p2, p1)

def rotate_letter(s, l):
    r = 1 + s.index(l)
    if r > 4:
        r += 1
    r %= len(s)
    return rotate_right(s, r)

def rrotate_letter(s, l):
    pass

def main(args):
    rules = []
    for line in open(args.file):
        p = parse("swap position {a:d} with position {b:d}\n", line)
        if p:
            rules.append([swap, swap, p["a"], p["b"]])
            continue

        p = parse("reverse positions {a:d} through {b:d}\n", line)
        if p:
            rules.append([reverse, reverse, p["a"], p["b"]])
            continue

        p = parse("swap letter {a:l} with letter {b:l}\n", line)
        if p:
            rules.append([swap_letter, swap_letter, p["a"], p["b"]])
            continue
        
        if line.endswith("1 step\n"):
            line = line[:-1] + "s\n"    # hack
        p = parse("rotate {dir:l} {s:d} steps\n", line)
        if p:
            if p["dir"] == "right":
                func = rotate_right
                rfunc = rotate_left
            else:
                rfunc = rotate_right
                func = rotate_left
            rules.append([func, rfunc, p["s"]])
            continue
        
        p = parse("move position {a:d} to position {b:d}\n", line)
        if p:
            rules.append([move, rmove, p["a"], p["b"]])
            continue

        p = parse("rotate based on position of letter {l:l}\n", line)
        if p:
            rules.append([rotate_letter, rrotate_letter, p["l"]])
            continue

        print("BAD RULE:", line)
        sys.exit(1)

    phrase = "abcdefgh"
    i = 0
    for r in rules:
        print(r)
        phrase = r[0](phrase, *r[2:])
        i += 1

    print("Part 1:", phrase)
        

    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2016 Day {0} AOC: Scrambled Letters and Hash".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
