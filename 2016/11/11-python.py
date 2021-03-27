#!/usr/bin/python

import sys, re, itertools
from operator import and_, or_, xor

def mysplit(s):
    return re.split(", and | and |, ", s)

def main():
    floors = [0,0,0,0]
    things = []
    for l in map(lambda x: x.strip(), open("../advent-2016/11-input.txt").readlines()):
        fl, stuff = l.split(" contains ")
        stuff = stuff.rstrip(".")
        #print stuff
        
        fl_num = { "The first floor" : 0, "The second floor" : 1, "The third floor" : 2, "The fourth floor": 3 }[fl]
        floors[fl_num] = []
        if stuff == "nothing relevant":
            continue

        for t in mysplit(stuff):
            things.append(t)
            floors[fl_num].append(t)

    things = sorted(things)

    def convert_to_binary(contents):
        n = 0
        for i, what in enumerate(things):
            if what in contents:
                n |= 1 << i
        return n << 1

    floors = map(convert_to_binary, floors)

    floors[0] |= 1     
    
    def shorten(thing):
        return "".join(map(lambda x: x[0].upper(), thing.split(" ")[1:]))
    
    def display_floor(n):
        s = "E " if n & 1 else ". "

        for i, what in enumerate(things):
            s += shorten(what) if ((2**i)<<1) & n else ". "
            s += " "
        return s
            
    def display(fl):
        s = ""
        print fl
        for fn in range(4, 0, -1):
            s += "F" + str(fn) + " "
            f = fl[fn-1]

            s += "E " if f & 1 else ". "

            for i, what in enumerate(things):
                s += shorten(what) if ((2 ** i)<<1) & f else ". "
                s += " "
            s += "\n"
        print s

    def current_floor(floors_tmp):
        for i, w in enumerate(floors_tmp):
            if w & 1:
                return i
        print "NO ELEVATOR EXISTS. BUG. current_floor() call"
        sys.exit(1)

    def avail_to_move(floors_tmp):
        fl = current_floor(floors_tmp)

        items = []
        for i, what in enumerate(things):
            if floors_tmp[fl] & (1 << (i+1)):
                items.append(1 << (i+1))
        return map(lambda x: x[0] | x[1], itertools.combinations(items, 2)) + items

    def adjacent_floors(floors_tmp):
        fl = current_floor(floors_tmp)
        if fl == 0:
            return [1]
        elif fl == 3:
            return [2]
        else:
            return [fl-1, fl+1]

    def test_valid(fl, new):
        proposed_floor = fl | new

        generators = set([])
        chips = set([])
        for i, x in enumerate(things):
            if proposed_floor & (1 << (i+1)):
                if "generator" in x:
                    generators.add(x.split()[1])
                else:
                    chips.add(x.split()[1].split("-")[0])
                
        if len(generators - chips) and len(chips - generators):
            #print "Inval: ", display_floor(proposed_floor)
            return False
        else:
            #print "Valid: ", display_floor(proposed_floor)
            return True

    steps = { 0 : set( [tuple(floors) ] )  } 
    #steps = { 0 : set( [(16, 7, 8, 0) ] ) } 
    #steps = { 0 : set( [(21, 0, 10, 0)] ) }


    
    step = 1

    while True:
        steps[step] = set()
        print "====================", step, "=================="

        for i in steps[step-1]:
            fl = list(i)
            for f in adjacent_floors(fl):
                for m in avail_to_move(fl):
                    if test_valid(fl[f], m) and test_valid(fl[current_floor(fl)] ^ (m), 0):
                        new_fl = fl[:]
                        new_fl[current_floor(fl)] ^= (1 | m)
                        new_fl[f] |= (1 | m)
                        new_fl = tuple(new_fl)
                        for st in range(step):
                            if new_fl in steps[st]:
                                continue
                        if new_fl[3] == 2 ** (len(things) + 1) - 1:
                            display(new_fl)
                            print "WE WON", step
                            sys.exit(1)
                        steps[step].add(new_fl)
                        #display(new_fl)
            
        #print steps
        step += 1
        #print step

# Answer 2 is easy. Some experimentation found every extra two items on floor add 12 steps. I could optimize this
# but this problem has annoyed me long enough.
        

if __name__ == "__main__":
    main()
