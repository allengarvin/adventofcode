#!/usr/bin/python

import sys, argparse

def to_bin(s):
    return int(s, 2)

LIMIT=50000000000

def next_generation(rules, state):
    new_state = dict()

    mn, mx = min(state.keys()) - 5, max(state.keys()) + 5
    for i in range(mn, mx):
        mask = to_bin("".join([state.get(x, "0") for x in range(i-2, i + 3)]))

        if rules[mask] == "1":
            new_state[i] = "1"
    return new_state
        
def main(args):
    state, rest = open(args.file).read().replace("#", "1").replace(".", "0").split("\n\n")
    original_state = state.strip("initial state: ")
    
    rules = { k : '0' for k in range(2**5) }
    for a, b in [x.split(" => ") for x in rest.strip().split("\n")]:
        rules.update({ to_bin(a) : b })
    
    state = { i : c for i, c in enumerate(original_state) if c == "1" }

    for i in range(1, 21):
        state = next_generation(rules, state)

    print(sum(state.keys()))

    state = { i : c for i, c in enumerate(original_state) if c == "1" }

    prev = sum(state.keys())
    prev_diff = None

    for i in range(1, 1000):
        state = next_generation(rules, state)
        ssum = sum(state.keys())

        # stabalizes after ~92
        if prev_diff != None:
            if ssum - prev == prev_diff:
                print(ssum + (LIMIT - i) * prev_diff)
                return
        prev_diff = ssum - prev
        prev = sum(state.keys())

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="2017 Day {0} AOC: Subterranean Sustainability".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
