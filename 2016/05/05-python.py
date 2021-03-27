#!/usr/local/bin/python3.7

import sys, argparse, operator, re

def main(args):
    open(args.file)
    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2016 Day {0} AOC: How About a Nice Game of Chess?".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
