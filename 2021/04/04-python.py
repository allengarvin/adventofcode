#!/usr/bin/python3

import sys, argparse, operator, re
import numpy as np
from io import StringIO

def win(boards, moves, firstp):

    for i, m in enumerate(moves):
        boards = [ b for b in boards if b is not None ]
        for j, b in enumerate(boards):
            cnt = len(boards)
            y, x = np.where(b == m)
            b[y, x] = -1

            full_row = np.any(np.all(b == -1, axis=1))
            full_col = np.any(np.all(b == -1, axis=0))

            if full_row or full_col:
                if firstp:
                    return int(sum(b[b != -1]) * m)
                else:
                    boards[j] = None
                if cnt == 1:
                    return int(sum(b[b != -1]) * m)

def main(args):
    flag = False

    boards = []

    with open(args.file) as fd:
        moves = [int(x) for x in fd.readline().strip().split(",")]
        fd.readline()
        s = ""
        for line in fd:
            if not line.strip():
                boards.append(np.loadtxt(StringIO(s)))
                s = ""
            else:
                s += line
    boards.append(np.loadtxt(StringIO(s)))
    print(win(boards, moves, True))
    print(win(boards, moves, False))
            
if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="20XX Day {0} AOC: Giant Squid".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
