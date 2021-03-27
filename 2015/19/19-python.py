#!/usr/local/bin/python3.7

import sys, argparse, operator, re

def replace_n(s, to, fr, n):
    indexes = [i for i, _ in enumerate(s) if s[i:].startswith(to)]
    return s[:indexes[n]] + s[indexes[n]:].replace(to, fr, 1)
    
def main(args):
    fd = open(args.file)
    repl = list()
    for line in fd:
        line = line.strip()
        if line == "":
            med = next(fd).strip()
        else:
            repl.append(tuple(line.split(" => ")))

    molecules = set()
    for k, v in repl:
        for i, _ in enumerate(re.findall(k, med)):
            molecules.add(replace_n(med, k, v, i))
            
    print("Part 1:", len(molecules))

    repl = sorted(repl, key=lambda x: len(x[1]), reverse=True)
    cnt = 0
    while med != "e":
        for a, b in repl:
            while b in med:
                med = med.replace(b, a, 1)
                cnt += 1
    print("Part 2:", cnt)
    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2015 Day {0} AOC: Medicine for Rudolph".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
