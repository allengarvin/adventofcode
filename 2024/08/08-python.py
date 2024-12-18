#!/usr/bin/python3

import sys, argparse, itertools

def show_grid(grid, antennae):
    pic = ""
    for j, row in enumerate(grid):
        for i, n in enumerate(row):
            flag = False
#            for k, v in antennae.items():
#                if complex(i, j) in v:
#                    pic += k
#                    flag = True
            if flag:
                continue
            if n == 0:
                pic += "."
            elif n == 1:
                pic += "#"
        pic += "\n"
    print(pic)

def main(args):
    antennae = {}
    grid, grid2 = [], []

    for j, row in enumerate(open(args.file)):
        grid2.append([0] * len(row.strip()))
        grid.append([0] * len(row.strip()))
        for i, ch in enumerate(row.strip()):
            if ch == ".":
                continue
            if ch in antennae:
                antennae[ch].append(complex(i, j))
            else:
                antennae[ch] = [complex(i, j)]

    for freq, locations in antennae.items():
        for a, b in itertools.combinations(locations, 2):
            if b.imag > a.imag:
                a, b = b, a
            anode1, anode2 = a+(a-b), b+(b-a)
            if anode1.real < 0 or anode1.imag < 0 or anode1.real >= len(grid[0]) or anode1.imag >= len(grid):
                pass
            else:
                grid[int(anode1.imag)][int(anode1.real)] = 1
            if anode2.real < 0 or anode2.imag < 0 or anode2.real >= len(grid[0]) or anode2.imag >= len(grid):
                pass
            else:
                grid[int(anode2.imag)][int(anode2.real)] = 1

            n1 = a
            while not (n1.real < 0 or n1.imag < 0 or n1.real >= len(grid[0]) or n1.imag >= len(grid)):
                grid2[int(n1.imag)][int(n1.real)] = 1
                n1 += a-b
            n2 = b
            while not (n2.real < 0 or n2.imag < 0 or n2.real >= len(grid[0]) or n2.imag >= len(grid)):
                grid2[int(n2.imag)][int(n2.real)] = 1
                n2 += b-a
    
    print(sum([sum(x) for x in grid]))
    print(sum([sum(x) for x in grid2]))


if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2024 Day {0} AOC: Resonant Collinearity".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
