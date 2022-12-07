#!/usr/bin/python3

import sys, argparse, operator, re

def main(args):
    dirs = { }

    for line in open(args.file):
        line = line.strip()
        if line[0] == "$":
            if line[2:4] == "cd":
                d = line.split()[2]
                if d == "/":
                    dir_ptr = dirs
                elif d == "..":
                    dir_ptr = dir_ptr[".."]
                else:
                    dir_ptr = dir_ptr[d]
            elif line[2:] == "ls":
                continue
        elif re.match("^\d+ [a-z.]+$", line):
            sz, name = line.split()
            dir_ptr[name] = int(sz)
        elif re.match("^dir [a-z.]+$", line):
            _, name = line.split()
            dir_ptr[name] = { ".." : dir_ptr }

    sizes = {}
    def du(dirs, cwd):
        sz = 0
        for k, v in dirs.items():
            if k == "..":
                continue
            if type(v) == int:
                sz += v
            else:
                sz += du(v, cwd + [k])
        sizes["/".join(cwd)] = sz
        return sz

    part1 = 0
    du(dirs, [""])
    p2_deletions = {}
    for k, v in sizes.items():
        if v <= 100000:
            part1 += v
        if sizes[""] - v <= 70000000 - 30000000:
            p2_deletions[k] = v

    print(part1)
    print(min(p2_deletions.values()))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2022 Day {0} AOC: No Space Left On Device".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
