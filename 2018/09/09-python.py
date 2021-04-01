#!/usr/bin/python3

from parse import parse
import sys, argparse

class LListNode:
    def __init__(self, number, prv=None, nxt=None):
        self.prv = prv or self
        self.nxt = nxt or self
        self.prv.nxt = self
        self.nxt.prv = self
        self.number = number

class LList:
    def __init__(self):
        self.size = 0
        self.current = None

    def insert(self, n):
        if self.size == 0:
            self.current = LListNode(n)
            self.size = 1
        else:
            self.size += 1
            self.current = LListNode(n, self.current, self.current.nxt)

        if n == 0:
            self.zero = self.current
            
    def pop(self):
        if self.size == 0:
            raise IndexError("pop() on empty list")

        self.current.prv.nxt = self.current.nxt
        self.current.nxt.prv = self.current.prv

        num = self.current.number
        self.current = self.current.nxt
        self.size -= 1
        return num

    def move(self, offset):
        n = self.current
        for _ in range(abs(offset)):
            n = n.prv if offset < 0 else n.nxt
        self.current = n
            
def part1(pl, high):
    scores = { x : 0 for x in range(pl) }

    circle = LList()
    circle.insert(0)

    for i in range(0, high):
        player = i % pl
        if (i+1) % 23 == 0:
            circle.move(-7)
            scores[player] += i + circle.pop() + 1
        else:
            circle.move(1)
            circle.insert(i+1)

    print(max(scores.values()))

def main(args):
    players, last_marble = parse("{:d} players; last marble is worth {:d} points\n", open(args.file).read())
    part1(players, last_marble)
    part1(players, last_marble * 100)

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2017 Day {0} AOC: Marble Mania".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
