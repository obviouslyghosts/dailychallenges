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

# 9 = 7 + 2x1**2
# 15 = 7 + 2x2**2
# 21 = 2 + 2x3**2 <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 25 = 7 + 2x3**2
# 27 = 19 + 2x2**2
# 33 = 31 + 2x1**2
# 35 = 2 + 2x4**2
# 39 = 7 + 2x4**2
# 45 = 13 + 2x4**2
# 49 = 17 + 2x4**2

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
##        print(i)
        if PrimeCheck(i):
            b = int((num-i)/2)
##            print(b)
            b = b**0.5
##            print(b)
            if b.is_integer() and b > 0 and b < num:
                return i
    return -1

n = 3
while searching:
##    print(n)
    if not PrimeCheck(n):
##        print(n)
        p = ScanPrimes( n )
        print("%i = %i + 2x%i**2" %(n, p, int(((n-p)/2)**0.5)))
        lim -= 1
    if lim<=0: searching=False
    n += 2
