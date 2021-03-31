#!/usr/bin/python3

import sys, argparse, string

def reduce(chem):
    volatile = [x + x.upper() for x in string.ascii_lowercase]
    volatile += [x[::-1] for x in volatile]

    match = True
    while match:
        for v in volatile:
            if v in chem:
                chem = chem.replace(v, "")
        match = False
        for v in volatile:
            if v in chem:
                match = True
    return chem
    
# immutable strings makes this a bit slow (9 seconds). Should I rewrite for a bytearray?
def main(args):
    chemical = open(args.file).read().strip()
    
    print(len(reduce(chemical)))
    part2 = { let : len(reduce(chemical.replace(let, "").replace(let.upper(), "")))
                for let in string.ascii_lowercase }
    print(min(part2.values()))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2018 Day {0} AOC: Alchemical Reduction".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
