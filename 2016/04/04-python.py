#!/usr/local/bin/python3.7

import sys, argparse, operator, re, parse, string

def valid1(room):
    p = parse.parse("{text}-{sec:d}[{cksum}]", room)
    text, sec, cksum = p["text"], p["sec"], p["cksum"]
    text_p = "".join(text.split("-"))
    if "".join(sorted([x for x in sorted(list(set(text_p)))], key=lambda a: text.count(a), reverse=True)[:5]) == cksum:
        return sec, text
    return 0, 0

def rot(room, sec):
    alpha = string.ascii_lowercase

    return "".join([alpha[(alpha.index(x) + sec) % 26] if x != "-" else " " for x in room])

def main(args):
    lines = open(args.file).read().strip().split("\n")

    real_rooms = []
    for r in lines:
        n, r = valid1(r)
        if n:
            real_rooms.append([n, r])

    print("Part 1:", sum([s for s, _ in real_rooms]))
    for s, r in real_rooms:
        if "northpole" in rot(r, s):
            print("Part 2:", s)
    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2016 Day {0} AOC: Security Through Obscurity".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
