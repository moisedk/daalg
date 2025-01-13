#include <stdio.h>
#include <assert.h>

int gcd(int m, int n) {
    if (n == 0) return m;
    return gcd(n, m % n);
}

int main() {
    assert(gcd(12, 60) == 12);
    assert(gcd(0, 12) == 12);
    assert(gcd(29, 17) == 1);


    printf("All test passed\n");
    printf("***********************************************\n");
}