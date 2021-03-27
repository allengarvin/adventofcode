#!/usr/bin/python3

import sys

def new_state(pos, grid):
    x, y = int(pos.real), int(pos.imag)
    n = [x-1 + (y-1) * 1j, x + (y-1) * 1j, x+1 + (y-1) * 1j,
         x-1 + (y  ) * 1j,                 x+1 + (y  ) * 1j,
         x-1 + (y+1) * 1j, x + (y+1) * 1j, x+1 + (y+1) * 1j ]

    on = sum([grid.get(x, 0) for x in n])

    if grid[pos]:
        return 1 if (on == 2 or on == 3) else 0
    else:
        return 1 if (on == 3) else 0

def main(fn):
    map1 = {}
    corners = [0, 99, 99j, 99+99j ]

    for y, line in enumerate(open(fn)):
        for x, ch in enumerate(line.strip()):
            map1[x + y * 1j] = 1 if ch == "#" else 0

    map2 = map1.copy()
    for c in corners:
        map2[c] = 1

    for i in range(100):
        map1 = { p : new_state(p, map1) for p in map1.keys() }
        map2 = { p : 1 if p in corners else new_state(p, map2) for p in map2.keys() }

    print(sum(map1.values()))
    print(sum(map2.values()))
        
if __name__ == "__main__":
    main("18-input.txt" if len(sys.argv) == 1 else sys.argv[1])
    

