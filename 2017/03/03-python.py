#!/usr/bin/python

from math import sqrt, ceil, floor

sq_pos = dict()

def square_positions(n):
    xcnt = 0
    ycnt = -1

    base = [0,0]

    for i in range(1, int(ceil(sqrt(n)))+1):
        sq_pos[i] = tuple([base[0] * (-1 if (xcnt % 2) else 1), base[1] * (1 if (ycnt % 2) else -1) ])
        
        xcnt = (xcnt + 1) % 2
        ycnt = (ycnt + 1) % 2
        if xcnt == 0:
            base[0] += 1
        if ycnt == 0:
            base[1] += 1

def position(n):
    if n == 1: return (0,0)
    if n == 2: return (1,0)
    if n == 3: return (1,-1)
    if n == 4: return (0,-1)

    cl = int(ceil(sqrt(n)))
    fl = int(floor(sqrt(n)))

    fl_pos = sq_pos[fl]
    cl_pos = sq_pos[cl]

    if fl**2 == n:
        return fl_pos

    dist = cl**2 - fl**2 + 1

    if n - fl ** 2 <= dist/2:
        # we adjust the vertical
        if fl_pos[1] > 0:
            return (fl_pos[0]+1, fl_pos[1] - ((n-1) - fl**2))
        else:
            return (fl_pos[0]-1, fl_pos[1] + ((n-1) - fl**2))
    else:
        # Here we use the horizontal
        if cl_pos[1] > 0:
            return (cl_pos[0] - fl + (n % (cl**2 - fl)), cl_pos[1])
        else:
            return (cl_pos[0] + fl - (n % (cl**2 - fl)), cl_pos[1])

input = int(open("03-input.txt").read())

square_positions(input)

def adjacents(pos):
    x, y = pos[0], pos[1]
    return [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]
        
print "Answer 1: ", sum(map(abs, position(input)))
squares = { (0,0) : 1 }

i = 2
while True:
    pos = position(i)
    total = 0
    for adj in adjacents(pos):
        if adj in squares:
            total += squares[adj]
    squares[pos] = total
    if total > input:
        break
    
    i += 1

print "Answer 2: ", total



        
