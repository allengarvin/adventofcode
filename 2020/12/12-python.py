#!/usr/bin/python3

from sys import argv

def rotate(point, rot):
    if rot > 0:
        rot = rot - 4
    return point * 1j**(-rot)       # complex plane rotations are great!

def answer(p):
    print(abs(int(p.real + p.imag)))

def main(input_file):
    dirs = [1j, -1, -1j, 1]
    movements = dict(zip("SWNE", dirs))
    pos, current_dir = 0, 0

    actions = [(a[0], (int(a[1:]) // 90) % 4 if a[0] in "LR" else int(a[1:])) for a in open(input_file).readlines()]
    for a, n in actions:
        if a in "NSEW":
            pos += movements[a] * n
        elif a == "F":
            pos += dirs[current_dir] * n
        elif a == "L": 
            current_dir = (current_dir + n) % 4
        if a == "R": 
            current_dir = (current_dir - n) % 4
    answer(pos)

    pos, current_dir, = 0, 0
    way = -1 + 10j
    movements = dict(zip("SWNE", dirs[::-1]))       # a little trickery to make the problem simpler

    for a, n in actions:
        if a in "NSEW":
            way += movements[a] * n
        elif a == "F": 
            pos += way * n
        elif a == "L": 
            way = rotate(way, -n)
        elif a == "R": 
            way = rotate(way, n)
    answer(pos)
        
if __name__ == "__main__":
    main(argv[1] if len(argv) > 1 else argv[0].split("-")[0] + "-input.txt")
    
