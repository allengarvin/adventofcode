#!/usr/bin/python

def main():
    lines = [x.strip().split() for x in open("../advent/04-input.txt").readlines()]
    
    count = 0
    acount = 0
    for l in lines:
        if len(set(l)) == len(l):
            count += 1
        anagrams = map(lambda x: "".join(sorted(list(x))), l)
        if len(set(anagrams)) == len(anagrams):
            acount += 1
    print "Answer 1:", count
    print "Answer 2:", acount
        
    return 1

if __name__ == "__main__":
    main()
