#!/usr/bin/python

import sys

def main():
    d = dict()
    for l in open("../advent/12-input.txt"):
        p = l.split(" <-> ")
        d[int(p[0])] = map(int, p[1].split(", "))

    total = d.keys()
    p = set([0])

    grp = []
    flag = False
    while True:
        prev = set()
        while True:
            to_eval = set()
            for n in p:
                nodes = d[n]
                for m in nodes:
                    if m not in p:
                        to_eval.add(m)
            p |= to_eval
            if p == prev:
                break
            else:
                prev = set(p)

        if not flag:
            print("Answer 1: %d" % len(p))
            flag = True

        grp.append(p)

        for i in p:
            total.remove(i)

        if len(total) == 0:
            print("Answer 2: %d" % len(grp))
            break
        p = set([total[0]])

if __name__ == "__main__":
    main()
