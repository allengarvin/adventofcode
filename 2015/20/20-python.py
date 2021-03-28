#!/usr/bin/python3

# Yes it's kind of a sieve of eratosthenes problem--if we can take all the factors, generate a powerset with
# repeating elements, it might be easier, but I'm going to brute force it, naively

def main(fn):
    upper_bound = int(open(fn).read().strip())
    arbitrary_limit = upper_bound // 20

    arr = [0] * arbitrary_limit
    for i in range(1, arbitrary_limit):
        for j in range(i, arbitrary_limit, i):
            arr[j] += i * 10

    for i, n in enumerate(arr):
        if n > upper_bound:
            print(i)
            break
    
    arr = [0] * arbitrary_limit
    for i in range(1, arbitrary_limit):
        for j in range(i, i*50+1 if i*50 < arbitrary_limit else arbitrary_limit, i):
            arr[j] += i * 11

    for i, n in enumerate(arr):
        if n > upper_bound:
            print(i)
            break

if __name__ == "__main__":
    main("20-input.txt")
