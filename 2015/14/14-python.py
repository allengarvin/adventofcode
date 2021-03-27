#!/usr/local/bin/python3.7

import sys, argparse, operator, re

def main(args):
    deer = {k[0] : [int(k[3])] * int(k[6]) + [0] * int(k[13]) for k in [l.split() for l in open(args.file)]}
    most = -1
    for k, v in deer.items():
        d, r = divmod(2503, len(v))
        most = max(most, d * sum(v) + sum(v[:r]))
    print("Part 1: {0}".format(most))

    deer_scores = {k : 0 for k in deer.keys()}
    deer_distances = {k : 0 for k in deer.keys()}
    for i in range(2503):
        for d in deer.keys():
            deer_distances[d] += deer[d][i % len(deer[d])]
        deer_scores[max(deer_distances.items(), key=operator.itemgetter(1))[0]] += 1
    print("Part 2: {0}".format(max(deer_scores.values())))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2015 Day {0} AOC: Reindeer Olympics".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
