#!/usr/bin/python3

import sys, argparse, operator, functools

def main(args):
    threshold = { "red" : 12, "green" : 13, "blue" : 14 }
    colors = threshold.keys()

    total1, total2 = 0, 0

    for g, line in enumerate(open(args.file)):
        line = line.strip()
        g += 1

        game_good = list()
        minimum = { i : 0 for i in colors }
        for d in map(lambda lst: {b : int(a) for a, b in [x.split() for x in lst.split(", ")]}, line.split(": ")[1].split("; ")):

            d = { i : (d[i] if i in d else 0) for i in colors}

            game_good += [d[i] <= threshold[i] for i in colors]

            for i in colors:
                minimum[i] = max(d[i], minimum[i])
            
        if functools.reduce(operator.__and__, game_good):
            total1 += g
        total2 += functools.reduce(operator.mul, minimum.values())
    print(total1)
    print(total2)

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2023 Day {0} AOC: Cube Conundrum".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
