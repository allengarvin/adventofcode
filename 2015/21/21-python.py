#!/usr/local/bin/python3.7

import sys, argparse, operator, re
from functools import reduce

goods = [ [
      [ "Dagger",      8, 4, 0 ],
      [ "Shortsword", 10, 5, 0 ],
      [ "Warhammer",  25, 6, 0 ],
      [ "Longsword",  40, 7, 0 ],
      [ "Greataxe",   74, 8, 0 ],
    ], [
      [ "None",        0,  0, 0 ],
      [ "Leather",    13,  0, 1 ],
      [ "Chainmail",  31,  0, 2 ],
      [ "Splintmail", 53,  0, 3 ],
      [ "Bandedmail", 75,  0, 4 ],
      [ "Platemail",  102, 0, 5 ],
    ], [ # one hand
      [ "None",        0, 0, 0 ],
      [ "Damage +1",  25, 1, 0 ],
      [ "Damage +2",  50, 2, 0 ],
      [ "Damage +3", 100, 3, 0 ],
      [ "Defense +1", 20, 0, 1 ],
      [ "Defense +2", 40, 0, 2 ],
      [ "Defense +3", 80, 0, 3 ],
    ], [ # the other
      [ "None",        0, 0, 0 ],
      [ "Damage +1",  25, 1, 0 ],
      [ "Damage +2",  50, 2, 0 ],
      [ "Damage +3", 100, 3, 0 ],
      [ "Defense +1", 20, 0, 1 ],
      [ "Defense +2", 40, 0, 2 ],
      [ "Defense +3", 80, 0, 3 ],
    ]
]

def battle(b, p, verbose=False):
    turn = 0
    p_dam = p[1] - b[2] if p[1] - b[2] > 0 else 1
    b_dam = b[1] - p[2] if b[1] - p[2] > 0 else 1

    boss_death, left = divmod(b[0], p_dam)
    if not left:
        boss_death -= 1
    if p[0] - boss_death * b_dam <= 0:
        return False
    return True

def main(args):
    for line in open(args.file):
        if line.startswith("Hit Points: "):
            hp = int(line.split()[-1])
        if line.startswith("Damage: "):
            dam = int(line.split()[-1])
        if line.startswith("Armor: "):
            arm = int(line.split()[-1])

    my_hp = 100
    
    least_cost, most_cost = 0xffffffff, -1

    lengths = [len(x) for x in goods]
    for choice in range(reduce(operator.mul, lengths)):
        gear = [(choice // (lengths[3] * lengths[2] * lengths[1])) % lengths[0],
                (choice // (lengths[3] * lengths[2])) % lengths[1], 
                (choice // lengths[3]) % lengths[2],
                 choice % lengths[3]]
        if gear[2] > 0 and gear[2] == gear[3]:
            continue
        gear = [goods[i][j] for i, j in enumerate(gear)]
        my_cost, my_dam, my_arm = sum([g[1] for g in gear]), sum([g[2] for g in gear]), sum([g[3] for g in gear])

        winner = battle([hp, dam, arm], [my_hp, my_dam, my_arm])

        if winner:
            least_cost = min(my_cost, least_cost)
        else:
            most_cost = max(my_cost, most_cost)
        
    print("Part 1: {}".format(least_cost))
    print("Part 2: {}".format(most_cost))
    
if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2015 Day {0} AOC: RPG Simulator 20XX".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
