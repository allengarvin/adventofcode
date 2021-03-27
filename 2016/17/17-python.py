#!/usr/bin/python

import os, sys, itertools, string
from hashlib import md5


def door_open(ch):
    if ch == "b" or ch == "c" or ch == "d" or ch == "e" or ch == "f":
        return 1
    return 0

# Order: up, down, left, right

orig_salt = 0
least_path = 100
most_path = -1
winner = None
loser = None

def display(hash):
    return "%s%s%s%s" % (("U" if door_open(hash[0]) else "-"), ("D" if door_open(hash[1]) else "-"), ("L" if door_open(hash[2]) else "-"), ("R" if door_open(hash[3]) else "-"))

def go(salt, pos, depth):
    global orig_salt
    global least_path, most_path
    global winner

    if depth > 1000:
        return

    hash = md5("%s" % (salt)).hexdigest()

    if pos == [3, 3]:
        #print "WINNER: %d " % (len(salt) - len(orig_salt)), salt[len(orig_salt):]
        if min(depth, least_path) < least_path:
            least_path = min(depth, least_path)
            winner = salt[len(orig_salt):]
        if (len(salt) - len(orig_salt)) > most_path:
            most_path = len(salt) - len(orig_salt)
            loser = salt[len(orig_salt):]
        return

    dirs = map(door_open, list(hash[0:4]))
    if pos[0] == 0:
        dirs[2] = 0
    if pos[0] == 3:
        dirs[3] = 0
    if pos[1] == 0:
        dirs[0] = 0
    if pos[1] == 3:
        dirs[1] = 0

    #print ">" * depth, pos, dirs, salt, hash[0:4], display(hash[0:4]), salt[len(orig_salt):]
    possibles = "UDLR"
    possible_deltas = [ [0, -1], [0, 1], [-1, 0], [1, 0] ]

    for d in range(len(dirs)):
        if dirs[d] == 1:
            go( salt + possibles[d], [ pos[0] + possible_deltas[d][0], pos[1] + possible_deltas[d][1] ], depth + 1 )
        
    
def main(argv):
    global orig_salt

    if len(argv) != 2:
        print("Usage: %s salt" % argv[0])
        sys.exit(1)

    salt = argv[1]
    orig_salt = salt

    go(salt, [0,0], 1)
    print "Answer 1:", winner
    print "Answer 2:", most_path
    return 1

if __name__ == "__main__":
    main(sys.argv)
