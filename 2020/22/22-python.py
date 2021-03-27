#!/usr/bin/python

import sys, os, argparse, operator, re, copy
from parse import parse

def score(players, winner):
    return sum([(len(players[winner]) - i) * x for i, x in enumerate(players[winner])])

def round(players):
    a, b = players[1].pop(0), players[2].pop(0)
    winner = [a,b].index(max([a,b]))+1
    return winner, a, b

def recurse_game(players, prev_orders, game):
    while players[1] and players[2]:
        for p1, p2 in prev_orders:
            if tuple(players[1]) == p1 or tuple(players[2]) == p2:
                return 1
        prev_orders += [ [ tuple(players[1]), tuple(players[2]) ] ]

        winner, a, b = round(players)
        if len(players[1]) >= a and len(players[2]) >= b:
            deckcopy = copy.deepcopy(players)
            deckcopy[1], deckcopy[2] = players[1][:a], players[2][:b]
            winner = recurse_game(deckcopy, [], game+1)
        else:
            winner = [a,b].index(max([a,b]))+1

        players[winner] += [a,b] if winner == 1 else [b,a]

    return winner

def main(args):
    p = [x.strip("\n").split("\n") for x in  open(args.file).read().split("\n\n")]
    players = dict([(parse("Player {:d}:", x[0])[0], map(int, x[1:])) for x in p])
    
    orig_deck = copy.deepcopy(players)

    while players[1] and players[2]:
         winner, a, b = round(players)
         players[winner] += sorted([a,b])[::-1]
    print("Problem 1: {0}".format(score(players, winner)))

    players = orig_deck
    winner = recurse_game(players, [], 1)
    print("Problem 2: {0}".format(score(players, winner)))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2020 Day {0} AOC: Crab Combat".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
