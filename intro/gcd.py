def gcd(m, n):
    if n == 0:
        return m
    return gcd(n, m % n)

def main():
    assert gcd(12, 60) == 12
    assert gcd(0, 343) == 343
    assert gcd(2, 0) == 2
    assert gcd(21, 7) == 7
    assert gcd(17, 17) == 17
    

if __name__ == '__main__':
    main()