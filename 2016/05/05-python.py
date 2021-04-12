#!/usr/local/bin/python3.7

import sys, argparse
from hashlib import md5

def main(args):
    seed = open(args.file).read().strip()

    pos, i = 0, 0
    passwd1, passwd2 = "", [None] * 8

    while pos < 8 or None in passwd2:
        hash = md5((seed + str(i)).encode("utf-8")).hexdigest()
        if hash.startswith("00000"):
            passwd1 += hash[5]
            ndx = int(hash[5], 16)
            if ndx < 8 and not passwd2[ndx]:
                passwd2[ndx] = hash[6]
                print(hash, passwd2)
            pos += 1
        i += 1
    print(passwd1[:8])
    print("".join(passwd2))
    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2016 Day {0} AOC: How About a Nice Game of Chess?".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
