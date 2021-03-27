#!/usr/local/bin/python3.7

import sys, argparse, operator, re
from parse import parse

def main(args):
    bot = dict()
    bot_rules = dict()
    output = dict()
    compares = dict()
    
    def fullbot():
        for b, i in bot.items():
            if len(i) == 2:
                return b
        return None
    
    def assign(bucket, num, val):
        if bucket == "bot":
            bot[num] = bot.get(num, []) + [val]
        else:
            output[num] = val

    def give_bot(bot_num):
        v1, v2 = bot[bot_num]
        v1, v2 = [v1, v2] if v2 > v1 else [v2, v1]
        compares[(v1,v2)] = bot_num
        
        r = bot_rules[bot_num]
        assign(r["low_dest"], r["lownum"], v1)
        assign(r["high_dest"], r["highnum"], v2)
        bot[bot_num] = []

    for line in open(args.file):
        p = parse("value {val:d} goes to bot {bot:d}\n", line)
        if p:
            assign("bot", p["bot"], p["val"])
        p = parse("bot {giver:d} gives low to {low_dest:w} {lownum:d} and high to {high_dest:w} {highnum:d}\n", line)
        if p:
            bot_rules[p["giver"]] = p
            
    f = fullbot()
    while f != None:
        give_bot(f)
        f = fullbot()

    print("Part 1:", compares[(17,61)])
    print("Part 2:", output[0] * output[1] * output[2])
    
        

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2016 Day {0} AOC: Balance Bots".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
