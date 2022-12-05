#!/usr/bin/python3

import sys, argparse

class Stacks:
    def __init__(self, n, lines):
        self.stacks = [""] * n
        for l in lines:
            crates = l[1::4]
            for i, c in enumerate(crates):
                if c != " ":
                    self.stacks[i] = c + self.stacks[i]

    def move_crates(self, cnt, frm, to, CrateMover9001):
        if CrateMover9001:
            self.stacks[to] = self.stacks[to] + self.stacks[frm][::-1][:cnt][::-1]
        else:
            self.stacks[to] = self.stacks[to] + self.stacks[frm][::-1][:cnt]
        self.stacks[frm] = self.stacks[frm][:-cnt]

    def final(self):
        return "".join([x[-1] for x in self.stacks])

def main(args):
    sl = []
    for line in open(args.file):
        line = line.rstrip()
        if "[" in line:
            sl.append(line)
        elif "1   2   3" in line:
            st1 = Stacks(len(line.split()), sl)
            st2 = Stacks(len(line.split()), sl)
        elif "move " in line:
            c, f, t = [int(x) for x in line[5:].split()[::2]]
            st1.move_crates(c, f-1, t-1, False)
            st2.move_crates(c, f-1, t-1, True)

    print(st1.final())
    print(st2.final())

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="20XX Day {0} AOC: Supply Stacks".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
