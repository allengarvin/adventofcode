#!/usr/local/bin/python3.7

import sys, argparse, operator, re

class Elf:
    def __init__(self, n):
        self.number = n
        self.next = False
        self.previous = False

    def __repr__(self):
        return "Elf [{}]".format(self.number)
    
def setup(elf_numbers):
    for i in range(1, elf_numbers+1):
        e = Elf(i)
        if i == 1:
            first = e
        else:
            e.previous = previous
            previous.next = e
        previous = e

        if i == (elf_numbers) // 2 + 1:
            half = e

    e.next = first
    first.previous = e

    return first, half

def main(args):
    n = int(open(args.file).read())
    current, _ = setup(n)
            
    while current.next != current:
        # print("{} takes {}'s presents.".format(current, current.next))
        current.next = current.next.next
        current = current.next

    print("Part 1:", current.number)
    
    current, half = setup(n)

    evenodd = 1
    while current.next != current:
        before = half.previous
        before.next = half.next
        half.next.previous = before

        if evenodd:
            half = half.next.next
        else:
            half = half.next
        evenodd = 1 - evenodd
        current = current.next
    print("Part 2:", current.number)

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2016 Day {0} AOC: An Elephant Named Joseph".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
