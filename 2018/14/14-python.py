#!/usr/bin/python3

import sys, argparse

def round(score, a, b):
    score += [int(x) for x in str(score[a] + score[b])]
    return [(x + score[x] + 1) % len(score) for x in [a,b]]

def main(args):
    score = [3, 7]
    a, b = 0, 1

    initial = open(args.file).read().strip()
    initial_int = int(initial)
    initial_arr = [int(x) for x in initial]
    initial_len = len(initial)
    last = initial_arr[-1]

    while True:
        a, b = round(score, a, b)
        if len(score) == initial_int + 10:
            print("".join([str(x) for x in score[-10:]]))
        if score[-1] == last or score[-2] == last:  #naive optimization
            if score[-initial_len-1:-1] == initial_arr:
                print(len(score) - initial_len - 1)
                break
            if score[-initial_len:] == initial_arr:
                print(len(score) - initial_len)
                break
    
if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2018 Day {0} AOC: Chocolate Charts".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
