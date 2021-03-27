#!/usr/bin/python3

import sys, argparse

def main(args):
    seq = [int(x) for x in args.nlist.split(",")]
    
    previous = { n: i for i, n in enumerate(seq) }
    
    # can we assume the leading numbers are unique?
    next_seq = 0
    cnt = len(seq)
    while True:
        last = { next_seq:cnt }
        next_seq = cnt - previous.get(next_seq, cnt)
        previous.update(last)
        cnt += 1

        if cnt + 1 == 2020:
            print("Problem 1:", next_seq)
        if cnt + 1 == 30000000:
            print("Problem 2:", next_seq)
            break

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="2020 Day 15 AOC: Rambunctious recitation")
    ap.add_argument("nlist", help="Numberlist", default="2,0,1,7,4,14,18",nargs="?")
    args = ap.parse_args()
    main(args)
    
