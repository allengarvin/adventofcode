#!/usr/bin/python

import sys, os, argparse, operator, re, itertools
from datetime import datetime
from parse import parse

def main(args):
    for line in open(args.file):
        p = parse("[{tm}] {rt}\n", line)
        dt = datetime.strptime(p["tm"], "%Y-%m-%d %H:%M")
        print dt

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2018 Day {0} AOC: FOO FOO".format(day))
    ap.add_argument("file", help="Input file", default="{0}-input.txt".format(day), nargs="?")
    main(ap.parse_args())
