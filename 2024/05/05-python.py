#!/usr/bin/python3

import sys, argparse

def check_valid(row, rules):
    for i, p in enumerate(row):
        for q in row[i+1:]:
            if q not in rules:
                continue
            if p in rules[q]:
                return False
    return True

# REALLY ugly
def order_invalid(row, rules):
    new_row = []
    flat = sorted({num for values in rules.values() for num in values})
    while row:
        p = row[0]

        continue_flag = False
        for j, q in enumerate(row):
            if j == 0:
                continue
            if q not in rules:
                break
            if p in rules[q]:
                row = row[1:j+1] + [p] + row[j+1:]
                continue_flag = True
                break
        if continue_flag:
            continue
        new_row.append(row[0])
        row = row[1:]
    while not check_valid(new_row, rules):
        # oddly, this only got hit on the test output (once), but none at all on the real input
        print("BUGGGGGGGGGGGGGGGGGGGGGGGG")
        new_row = order_invalid(new_row, rules)
    return new_row

def main(args):
    rules = {}
    updates = []
    for line in open(args.file):
        line = line.strip()
        if "|" in line:
            a, b = [int(x) for x in line.split("|")]
            if a in rules:
                rules[a].append(b)
            else:
                rules[a] = [b]
        elif "," in line:
            updates.append([int(x) for x in line.split(",")])

    invalid, valid = [], []
    for u_row in updates:
        if check_valid(u_row, rules):
            valid.append(u_row[len(u_row)//2])
        else:
            new_row = order_invalid(u_row, rules)
            invalid.append(new_row[len(u_row)//2])
       
    print(sum(valid))
    print(sum(invalid))

if __name__ == "__main__":
    day = sys.argv[0].split("-")[0]
    ap = argparse.ArgumentParser(description="20XX Day {0} AOC: Print Queue".format(day))
    ap.add_argument("file", help="Input file", default=day + "-input.txt", nargs="?")
    main(ap.parse_args())
    
