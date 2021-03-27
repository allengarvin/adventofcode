#!/usr/bin/python3

def captcha(arr, offset):
    return sum([arr[n] if arr[n] == arr[(n+offset) % len(arr)] else 0 for n in range(len(arr))])
    
def main():
    vals = [int(x) for x in list(open("01-input.txt").read().strip())]
    print(captcha(vals, 1))
    print(captcha(vals, len(vals) // 2))

if __name__ == "__main__":
    main()
