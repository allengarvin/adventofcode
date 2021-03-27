#!/usr/bin/python

import os, sys, itertools, string

def main():

    lines = []
    maze = []
    for l in open("../advent/19-input.txt"):
        lines.append(l.strip("\n"))
        maze.append(list(l.rstrip("\n")))

    pos = [0, maze[0].index("|")]
    dir = [1,0]

    letters = []

    def adjacents(y, x, prev):
        adj = []
        if y > 0:
            adj.append( [y-1, x] )
        if x > 0:
            adj.append( [y, x-1] )
        if x < len(maze[0]) - 1:
            adj.append( [y, x+1] )
        if y < len(maze) - 1:
            adj.append( [y+1, x] )

        adj.remove(prev)
        ##print "DIM", len(maze), len(maze[0])
        #print y, x, adj
        for j, i in adj[:]:
            #print j, i
            if maze[j][i] == " ":
                adj.remove([j,i])
        return adj


    prev = []
    steps = 0

    while True:
        here = maze[pos[0]][pos[1]]
        if here.isupper():
            letters.append(here)
        elif here == "+":
            adj = adjacents(pos[0], pos[1], prev[:])
            if len(adj) > 1:
                print "".join(letters)
                print "BUG MULT ADJ at ", pos[0], pos[1]
                print map(lambda x: "<%c>" % maze[x[0]][x[1]], adj)
                print "Here: %s" % maze[pos[0]][pos[1]]
                print "Prev: ", prev
                for i in range(pos[0]-3, pos[0]+3):
                    print "".join(maze[i][pos[1]-3:pos[1]+3])
                print adj
                sys.exit(1)
            if len(adj) == 0:
                break
            new_place = adj[0]
            dir = [new_place[0] - pos[0], new_place[1] - pos[1]]
        elif here != "-" and here != "|":
            print "Answer 1:", "".join(letters)
            print "Answer 2:", steps
            #print "BUG BUG BUG we got off track"
            #print "Here: %s" % maze[pos[0]][pos[1]]
            #print "Prev: ", prev
#            for i in range(pos[0]-3, pos[0]+3):
#                print "".join(maze[i][pos[1]-3:pos[1]+3])
            sys.exit(1)
        prev = pos[:]
        pos[0] += dir[0]
        pos[1] += dir[1]
        steps += 1
        #print "POSITION: ", pos, "DIR:", dir, "PREVIOUS:", prev
        if pos[0] < 0 or pos[1] < 0:
            break
        
            
        
        
    return 1

if __name__ == "__main__":
    main()
