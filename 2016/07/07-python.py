#!/usr/local/bin/python3.7

import sys, argparse, operator, re, itertools, string

def test_abba(abba, parts):
    for p in parts:
        for a in abba:
            if a in p:
                return True
    return False

def test_aba(aba, outer_parts, inner_parts):
    for f, b in aba.items():
        for p in outer_parts:
            if f in p:
                for q in inner_parts:
                    if b in q:
                        return True

    return False

def main(args):
    ips = [l.strip() for l in open(args.file)]

    abba = list()
    aba = dict()
    for a, b in itertools.combinations(string.ascii_lowercase, 2):
        abba.append(a+b+b+a)
        abba.append(b+a+a+b)

        aba[a+b+a] = b+a+b
        aba[b+a+b] = a+b+a
        
    cnt1 = cnt2 = 0
    for i in ips:
        if test_abba(abba, re.split("\[[^]]*\]", i)) and not test_abba(abba, re.findall("\[[^]]*\]", i)):
            cnt1 += 1

        if test_aba(aba, re.split("\[[^]]*\]", i), re.findall("\[[^]]*\]", i)):
            cnt2 += 1
    print("Part 1:", cnt1)
    print("Part 2:", cnt2)
    

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2016 Day {0} AOC: Internet Protocol Version 7".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
