#!/usr/bin/python

import os, sys, itertools, string, math


def main():
    banks = [int(x) for x in open("06-input.txt").read().split()]
    configurations = set(tuple(banks))

    cnt = 0
    state = 0
    part1 = False
    part2 = False

    while True:
        cnt += 1
        highest = 0
        for i, bl in enumerate(banks):
            if bl > banks[highest]:
                highest = i

        to_dist = banks[highest]
        banks[highest] = 0

        #print "Highest is cell %d with %d" % (highest+1, to_dist)

        if to_dist == 0:
            break
        elif to_dist < len(banks):
            amount = 1
        else:
            amount = int(round(float(to_dist) / float(len(banks))))
        

        for i in range(1, len(banks)+1):
            if to_dist == 0:
                break
            if i == len(banks):
                amount = to_dist
            to_dist -= amount

            #print "Adding %d to bank %d" % (amount, (highest + i) % len(banks) + 1)
            banks[(highest + i) % len(banks)] += amount
        if tuple(banks) in configurations:
            if not part1:
                print cnt
                part1 = True
                configurations = set(tuple(banks))
                cnt = -1
            else:
                print cnt
                sys.exit(1)
        else:
            configurations.add(tuple(banks))
        
    return 1

if __name__ == "__main__":
    main()
