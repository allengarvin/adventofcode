#!/usr/bin/python

import sys, os, argparse, operator, re, parse, itertools, math

NORTH=0
EAST=1
SOUTH=2
WEST=3

def opposite(dir):
    return { NORTH : SOUTH, EAST : WEST, WEST : EAST, SOUTH : NORTH }[dir]

class Tile:
    number = False
    sides = None
    attaches = False
    attach_sides = False
    attach_map = False
    literal = False

    def to_bin(self, s):
        return "".join("1" if x == "#" else "0" for x in s)

    def setup(self, grid):
        top = self.to_bin(grid[0])
        right = self.to_bin([x[-1] for x in grid])
        left = self.to_bin([x[0] for x in grid])
        bottom = self.to_bin(grid[-1])

        self.sides = [top, right, bottom, left]
        self.top, self.right, self.bottom, self.left = self.sides
        self.nsides = map(lambda x: int(x, 2), self.sides)
        self.osides = map(lambda x: int(x[::-1], 2), self.sides)
        self.allsides = set(self.nsides + self.osides)

        self.array = grid

    def __init__(self, s):
        lines = s.split("\n")
        h, t = lines[0], lines[1:]
        p = parse.parse("Tile {no:d}:", h)
        self.attaches = []
        self.attach_sides = []
        self.number = p["no"]
        self.attach_map = dict()

        self.setup(t)


    def __str__(self):
        if len(self.attach_map):
            prefix = "*"
        else:
            prefix = ""
        return prefix + "[{0}[ N:{1:4d} E:{2:4d} S:{3:4d} W: {4:4d} ]]".format(self.number, *self.nsides)

    def __repr__(self): return self.__str__()

    def rot90(self):
        assert len(self.attach_map) == 0
            
        self.array = ["".join(list(x)) for x in list(zip(*self.array[::-1]))]
        self.setup(self.array)
        return self

    def flip_x(self):
        assert len(self.attach_map) == 0

        self.array = [x[::-1] for x in self.array]
        self.setup(self.array)
        return self

    def in_side(self, s):
        return any(s in x for x in self.attach_sides)

    def setup_nw_corner(self):
        assert len(self.attach_sides) == 2

        while not self.in_side(self.nsides[EAST]) or not self.in_side(self.nsides[SOUTH]):
            self.rot90()

    def attach_side(self, dir):
        my_side = self.nsides[dir]
        #print self, "attach_side({0})".format(dir)

        #print self.attaches
        for t in self.attaches:
            if my_side in t.allsides:
                break
        assert my_side in t.allsides            # Should only trigger if bug
        if t.nsides[opposite(dir)] != my_side:
            for i in range(4):
                t.rot90()
                if t.nsides[opposite(dir)] == my_side:
                    break
            if t.nsides[opposite(dir)] != my_side:
                t.flip_x()
                for i in range(4):
                    t.rot90()
                    if t.nsides[opposite(dir)] == my_side:
                        break
        assert t.nsides[opposite(dir)] == my_side       # hopefully no bugs?
        self.attach_map[dir] = t
        t.attach_map[opposite(dir)] = self
        return t
                
        
        
def main(args):
    tiles = dict()
    for x in open(args.file).read().split("\n\n"):
        if x == "": break   # last 
        t = Tile(x)
        tiles[t.number] = t

    for a, b in itertools.product(tiles, tiles):
        if a == b:
            continue
        x, y = tiles[a], tiles[b]

        if len(x.allsides & y.allsides):
#            print a, b, "=", x.allsides & y.allsides

            if y not in x.attaches: 
                x.attaches.append(y)
                x.attach_sides.append(x.allsides & y.allsides)
            if x not in y.attaches: 
                y.attaches.append(x)
                y.attach_sides.append(x.allsides & y.allsides)
        
    corners = filter(lambda x: len(x.attaches) == 2, tiles.values())
    print("Problem 1: {0}".format(reduce(operator.mul, [t.number for t in corners])))

    #print corners[0].attaches
    #print corners[0].osides

    if "test" in args.file:
        for c in corners:
            if c.number == 1951:
                start_corner = c
                c.flip_x()
                start_corner.setup_nw_corner()
    else:
        start_corner = corners[0]
        start_corner.setup_nw_corner()

    t = start_corner
    side_len = int(math.sqrt(len(tiles)))
    #print "SQUARE SIDE", side_len
    for y in range(side_len):
        left = t
        for x in range(side_len-1):
            #print "---->", t.number
            n = t.attach_side(EAST)
            #print t, "->attach->", n
            t = n

        if y == side_len-1:
            break
        #print "NEW ROW"
        n = left.attach_side(SOUTH)
        #print left, "->attach->", n
        t = n

    x = start_corner
    y = start_corner

    final_grid = []
    while y:
        start_left = x
        for i in range(1, 9):
            line = ""
            x = start_left
            while x:
                line += x.array[i][1:-1]
                x = x.attach_map.get(EAST, False)
            final_grid.append(line)
        y = y.attach_map.get(SOUTH, False)
        x = y

    find_monsters(final_grid)

def print_grid(grid):
    ln = ""
    for row in grid:
        ln += "".join(["#" if x else " " for x in row]) + "\n"
    return ln

def grid_rot90(grid):
    return [list(x) for x in zip(*grid[::-1])]

def flip_grid(grid):
    return [x[::-1] for x in grid]

def count_monsters(grid):
    # monster has 15 hashes
    monster = [ "                  # ",
                "#    ##    ##    ###",
                " #  #  #  #  #  #   ",
    ]

    nm = []
    for j, row in enumerate(monster):
        nm += filter(lambda a: a != -1, [(j, i) if x == "#" else -1 for i, x in enumerate(row)])

    cnt = 0
    for y in range(len(grid)-2):
        for x in range(len(grid[0])-19):
            cnt += all([grid[y+j][x+i] for j, i in nm])
    return cnt

def find_monsters(grid):
    ng = []

    for row in grid:
        ng.append([1 if x == "#" else 0 for x in row])
    total_hash = print_grid(ng).count("#")

    for i in range(3):
        for j in range(2):
            ng = grid_rot90(ng)
            cnt = count_monsters(ng)     
            if cnt:
                print("Problem 2: {0}".format(total_hash - cnt * 15))
                sys.exit(0)
        ng = flip_grid(ng) 
            
    

if __name__ == "__main__":
    default_file = sys.argv[0].split("-")[0] + "-input.txt"
    ap = argparse.ArgumentParser(description="2020 Day 20 AOC: Jurassic Jigsaw")
    ap.add_argument("file", help="Input file", default=default_file, nargs="?")
    main(ap.parse_args())
    
