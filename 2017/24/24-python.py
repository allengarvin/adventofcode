#!/usr/bin/python

import sys

recur_depth = 0
recur_depth_val = 0

def chain(tup, lines, lvl, val, depth):
    global recur_depth, recur_depth_val

    start = filter(lambda x: x[0] == tup[1] or x[1] == tup[1], lines)

    max_val = val
    for i in start:
        avail = lines[:]
        avail.remove(i)
        if i[0] == tup[1]:
            max_val = max(chain(i, avail, lvl+1, val + sum(i), depth + 1), max_val)
        else:
            max_val = max(chain((i[1],i[0]), avail, lvl+1, val + sum(i), depth + 1), max_val)
    if depth == recur_depth:
        recur_depth_val = max(recur_depth_val, max_val)
    elif depth > recur_depth:
        recur_depth = depth
        recur_depth_val = max_val
       
        
    return max_val
            

def main(argv):
    lines = []
    for l in open("../advent/24-input.txt").readlines():
        t = tuple(map(int, l.strip().split("/")))
        lines.append(t)

    start = filter(lambda x: x[0] == 0 or x[1] == 0, lines)

    max_val = -1
    for i in start:
        avail = lines[:]
        avail.remove(i)
        max_val = max(chain(i, avail, 0, sum(i), 0), max_val)
    print "Answer 1:", max_val
    print "Answer 2:", recur_depth_val
        
    return 1

if __name__ == "__main__":
    main(sys.argv)
