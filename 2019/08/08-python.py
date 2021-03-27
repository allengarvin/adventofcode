#!/usr/local/bin/python3.7

import sys, argparse, operator, re

def main(args):
    size = (25,6)
    img_str = open(args.file).read().strip()
    layer_size = size[0] * size[1]
    layers = [img_str[x:x + layer_size] for x in range(0, len(img_str), layer_size)]

    least = sorted(layers, key=lambda x: x.count("0"))[0]
    print("Part 1: {0}".format(least.count("1") * least.count("2")))
    layers = [[int(x) for x in s] for s in layers]

    img = [[x[i] for x in layers if x[i] != 2] for i in range(layer_size)]
    print("Part 2:")
    for y in range(size[1]):
        print("".join([" " if img[y * size[0] + x][0] == 0 else "#" for x in range(size[0])]))
    
    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2019 Day {0} AOC: Not Quite Lisp".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
