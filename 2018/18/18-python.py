#!/usr/bin/python3

import sys, argparse, copy

def display(yard):
    s = ""
    for y in range(50):
        line = [{0:'.',1:'|',2:'#'}[yard[i + y * 1j]] for i in range(50)]
        s += "".join(line) + "\n"
    return s
    
def change_state(pos, yard):
    neighbors = [ -1 - 1j, -1j, 1 - 1j,
                  -1     ,      1,
                  -1 + 1j,  1j, 1 + 1j ]

    state = yard[pos]

    surround = [yard.get(pos + n, 0) for n in neighbors if (pos + n) in yard]
    if state == 0 and surround.count(1) >= 3:
        return 1
    if state == 1 and surround.count(2) >= 3:
        return 2
    if state == 2 and (surround.count(1) == 0 or surround.count(2) == 0):
        return 0
    return state

def run_simulation(yard, tm):
    past_yards = [display(yard)]

    for m in range(tm):
        yard = { pos : change_state(pos, yard) for pos in yard.keys() }
        s = display(yard)
        if s in past_yards:
            cycle = m - past_yards.index(s) + 1
            past_yards = past_yards[past_yards.index(s):]
            return past_yards[(tm - m) % cycle - 1]
        else:
            past_yards.append(display(yard))
    return s
            
def score(yard_display):
    return yard_display.count("|") * yard_display.count("#")

def main(args):
    yard = dict()

    for j, line in enumerate(open(args.file)):
        line = line.strip()
        for i, c in enumerate(line):
            yard[i + j * 1j] = { '.' : 0, '|' : 1, '#' : 2 }[c]

    y = run_simulation(copy.deepcopy(yard), args.minutes)
    print(score(y))
    y = run_simulation(copy.deepcopy(yard), 1000000000)
    print(score(y))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2018 Day {0} AOC: Settlers of The North Pole".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    ap.add_argument("-m", "--minutes", help="# minutes", type=int, default=10)
    main(ap.parse_args())
    
