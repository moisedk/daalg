""" Find the square root of x"""
def sqrt(x):
    PRECISION = 1e-12
    y_0 = x / 2 if x > 1.0 else 1.0
    while True:
        y = (y_0 + x/y_0)/2
        if abs(y - y_0) < PRECISION:
            return y
        y_0 = y
    return y_0

""" Returns the gcd(m, n) using Euclid's algorithm """
def euclid_gcd(m, n):
    if n == 0:
        return m
    return euclid_gcd(n, m % n)

""" Return the gcd(m, n) using a linear decrement method and checking every possibility from 1 to min(m, n)"""
def linear_gcd(m, n):
    if m == 0 or n == 0:
        return m | n
    t = min(m, n)
    while t > 0:
        if m % t == n % t == 0:
            return t
        t -= 1
    return 1
""" Returns the gcd(m,n) using the prime factoring methods """
def prime_gcd(m, n):
    assert m != 0 or n != 0 # Not both 0
    if m == 0 or n == 0:
        return m | n # Returns whichever is not 0, if one is 0
    """ Returns all the primes less than N using Sieve of Eratosthenes' algorithm """
    def sieve(N):
        nums = [i for i in range(N)]
        for p in range(2, N):
            if nums[p] != 0:
                j = p * p
                while j < N:
                    nums[j] = 0
                    j += p # Mark all the multiples of p as non primes
        return list(filter(lambda x: x != 0, nums[2:]))
    
    """ Returns the prime factors of N """
    def factorize(N):
        factors = {}
        primes = sieve(N)
        for p in primes:
            while N % p == 0:
                if p in factors:
                    factors[p] += 1
                else:
                    factors[p] = 1
                N /= p
        return factors
    
    m_factors = factorize(m)
    n_factors = factorize(n)

    gdc = 1
    for factor in m_factors:
        if factor in n_factors:
            gdc *= factor ** min(m_factors[factor], n_factors[factor])
    return gdc
        
def main():
    print("********************Testing...************************")

    assert euclid_gcd(24, 144) == 24
    assert euclid_gcd(1, 144) == 1
    assert euclid_gcd(24, 0) == 24
    assert euclid_gcd(0, 5) == 5   

    assert linear_gcd(24, 144) == 24
    assert linear_gcd(1, 144) == 1
    assert linear_gcd(24, 0) == 24
    assert linear_gcd(0, 5) == 5

    assert prime_gcd(24, 144) == 24
    assert prime_gcd(1, 144) == 1
    assert prime_gcd(24, 0) == 24
    assert prime_gcd(0, 5) == 5
    
    print("********************All Tests Passed************************")

if __name__ == '__main__':
    main()