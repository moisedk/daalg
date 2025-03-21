#!/bin/python3
import time
# Computes the a^n mod m (for arbitrarily large values of n)
def modexponent(a, n, m):
    if m == 1:
        return 0
    r = 1
    while n > 0:
        r = (a * r) % m
        n -= 1
    return r
def modexposquare(a, n, m):
    if m == 1:
        return 0
    r = 1
    a = a % m
    while n > 0:
        if n & 1:
            r = (r * a) % m
        a = (a * a ) % m
        n >>= 1
    return r

def main():
    s1 = time.time()
    r1 = modexponent(3, 100000000, 97)
    s2 = time.time()
    ds = s2 - s1
    print(r1)
    print(ds)
    
    t1 = time.time()
    r1 = modexposquare(3, 1000000, 97)
    t2 = time.time()
    dt = t2 - t1
    print(r1)
    print(dt)

    print(ds / dt)

if __name__ == '__main__':
    main()