"""
It was proposed by Christian Goldbach that every odd composite number can be
written as the sum of a prime and twice a square.

9 = 7 + 2×1**2
15 = 7 + 2×2**2
21 = 3 + 2×3**2
25 = 7 + 2×3**2
27 = 19 + 2×2**2
33 = 31 + 2×1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a
prime and twice a square?
"""

searching = True
lim = 10

def PrimeCheck(n):
    n = int(n)
    if n == 1: return False
    if n == 2: return True
    ## even check
    if n%2<1: return False
    ## only check below square root!
    l = int(n**0.5)+1
    for i in range(3,l,2):
        if n%i <1: return False
    return True

def ScanPrimes( i ):
    num = i
    for i in range(1, i, 1):
        if PrimeCheck(i):
            b = (num-i)/2
            b = b**0.5
            if b.is_integer() and b > 0 and b < num:
                return i
    return -1

n = 3
while searching:
    if not PrimeCheck(n):
        p = ScanPrimes( n )
        if p < 0:
            print("BROKE")
            print("%i = %i + 2x%i**2" %(n, p, int(((n-p)/2)**0.5)))
            searching = False
    n += 2
