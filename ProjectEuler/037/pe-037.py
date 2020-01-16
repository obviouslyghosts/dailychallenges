"""
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

# 37
# 53
# 73
# 313
# 317
# 373
# 797
# 3137
# 3797

## this brute force checks every number
## start with 1 digit prime
## 1-9 on left, 1-9 on right -- ## keep primes
## previous answers, 1-9 on right, 1-9 on left


limit = 11 # only searching for 11 numbers
answers = set()
primes = set()


def primeCheck(n):
    n = int(n)
    if n == 1: return False
    ## even check
    if n%2<1: return False
    ## only check below square root!
    l = int(n**0.5)+1
    for i in range(3,l,2):
        if n%i <1: return False
    return True


def truncPrime(n):
    t = str(n)
    if not primeCheck(t[0]): return False
    for i in range(len(t)-1):
##        if not primeCheck( t[i+1:] ): return False
        if not primeCheck( t[:len(t)-(i+1)]): return False
    return True


for i in range(2, 10):
    if primeCheck(i):
        primes.add(i)

print(primes)

while limit > 0:
    newPrimes = set()
    for p in primes:
        for i in range(1,10):
            a = str(i)+str(p)
            if primeCheck( a ):
                newPrimes.add( a )
                if a not in answers and truncPrime( a ):
                    print("found: %s" % a)
                    print(len( primes ))
                    limit -= 1
                    answers.add( a )        
    primes = newPrimes
    print(len(primes))

##while limit > 0:
##    newPrimes = set()
##    for p in primes:
##        for i in range(1,10):
##            a = str(i)+str(p)
##            b = str(p)+str(i)
##            if primeCheck( a ):
##                newPrimes.add( a )
##                if a not in answers and truncPrime( a ):
##                    print("found: %s" % a)
##                    print(len( primes ))
##                    limit -= 1
##                    answers.add( a )
##            if primeCheck( b ):
##                newPrimes.add( b )
##                if b not in answers and truncPrime( b ):
##                    print("found: %s" % b)
##                    print(len( primes ))
##                    limit -= 1
##                    answers.add( b )
        
##    print(newPrimes)
##    primes = newPrimes

print(answers)
