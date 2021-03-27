#!/usr/bin/python

def main():
    steps = 303

    pc = 0
    grid = [0]

    for i in xrange(2018):
        pc = (pc + steps) % (i+1)
        grid = grid[:pc+1] + [i+1] + grid[pc+1:]

        pc = pc + 1

    print "Answer 1: ", grid[grid.index(2017)+1]

    pc = 0
    grid = [0]

    for i in xrange(50000000):
        pc = (pc + steps) % (i+1)
        if pc == 0:
            grid = [0,i+1]

        pc += 1
        
    print "Answer 2: ", grid[1]

if __name__ == "__main__":
    main()
