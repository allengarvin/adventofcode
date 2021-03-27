#!/usr/bin/python

from copy import deepcopy
import os, sys, itertools, string
from parse import parse

def main(argv):

#p=<-3770,-455,1749>, v=<-4,-77,53>, a=<11,7,-9>
#p=<1430,195,-903>, v=<-123,60,20>, a=<5,-5,1>

    lines = [l.strip() for l in open("../advent/20-input.txt").readlines()]
    particles = []


    count = 0
    for l in lines:
        parts = parse("p=<{}>, v=<{}>, a=<{}>", l)
        p = {
            "p" : map(int, parts[0].split(",")),
            "v" : map(int, parts[1].split(",")),
            "a" : map(int, parts[2].split(",")),
            "distance" : 0,
            "number" : count
        }
        count += 1
        particles.append(p)

    count = 0

    aparticles = deepcopy(particles)
    while True:
        least = 0x7fffffff
        least_num = -1

        for i, p in enumerate(aparticles):
            if aparticles[i] == 0:
                continue
            p["v"][0] += p["a"][0]
            p["v"][1] += p["a"][1]
            p["v"][2] += p["a"][2]

            p["p"][0] += p["v"][0]
            p["p"][1] += p["v"][1]
            p["p"][2] += p["v"][2]

            p["distance"] = sum(map(abs, p["p"]))

            if p["distance"] < least:
                least = p["distance"]
                least_num = i
        count += 1
        if count % 500 == 0:
            print "Maybe Answer 1:", least_num
            break

    count = 0
    while True:
        least = 0x7fffffff
        least_num = -1

        for i, p in enumerate(particles):
            if particles[i] == 0:
                continue
            p["v"][0] += p["a"][0]
            p["v"][1] += p["a"][1]
            p["v"][2] += p["a"][2]

            p["p"][0] += p["v"][0]
            p["p"][1] += p["v"][1]
            p["p"][2] += p["v"][2]

            p["distance"] = sum(map(abs, p["p"]))

            if p["distance"] < least:
                least = p["distance"]
                least_num = i

        collided = []
        for i, p in enumerate(particles):
            if p == 0:
                continue
            for j, q in enumerate(particles):
                if q == 0: continue
                if i == j: continue
                if p["p"] == q["p"]:
                    collided.append(i)
                    collided.append(j)

        count += 1
        if len(collided):
            new_particles = []
            #print "Round", count, "Collided: ", collided
            for i, p in enumerate(particles):
                if i not in collided:
                    new_particles.append(p)
            particles = new_particles
                
        #if count % 100 == 0:
        #    print("%5d %d %d %d sz=%d" % (count, least_num, least, particles[least_num]["number"], len(particles)))
        #print min(map(lambda x: x["distance"], particles))
        if count == 100:
            print "Maybe Answer 2:", len(particles)
            sys.exit(1)

            
        
        
        
        
    return 1

if __name__ == "__main__":
    main(sys.argv)
