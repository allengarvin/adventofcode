#!/usr/bin/python3.11

import sys, argparse, operator, re
import networkx as nx
from math import dist
from functools import reduce
import operator as op
# hadn't touched networkx in years, had to relearn

def main(args):
    points = []
    with open(args.file) as fd:
        for line in fd:
            points.append(tuple([int(x) for x in line.strip().split(",")]))

    graph = nx.Graph()
    for i, p in enumerate(points):
        graph.add_node(i, pos=p)

    distances = {}

    pn = len(points)
    for i in range(pn):
        for j in range(i+1, pn):
            p1, p2 = points[i], points[j]
            distances[dist(p1,p2)] = (p1,p2)

    total = 10 if args.file == "08-test.txt" else 1000

    shortd = sorted(distances.keys())

    for i, sd in enumerate(shortd):
        p1, p2 = points.index(distances[sd][0]), points.index(distances[sd][1])
        graph.add_edge(p1, p2)

        # the stupid mistake that held me back for 90 minutes:
        #graph.add_edge(*distances[sd])
#        print(i, "adding", distances[sd], " | contiguous:", nx.number_connected_components(graph))
#        print(nx.is_connected(graph))
        #print("---")

        if i + 1 == total:
            circuits = list(nx.connected_components(graph))
            print(reduce(op.mul, [len(x) for x in sorted(circuits, key=len, reverse=True)][:3]))
        elif i + 1 > total and nx.is_connected(graph):
            print(reduce(op.mul, [x[0] for x in distances[sd]]))
            break

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="20XX Day {0} AOC: Playground".format(day))

    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
