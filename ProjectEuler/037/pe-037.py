"""
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

## this brute force checks every number
## im only interested 

limit = 10 # only searching for 11 numbers
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

n = 11 # single digit primes don't count, 10 +1

def truncPrime(n):
    t = str(n)
    for i in range(len(t)-1):
        if not primeCheck( t[i+1:] ): return False
        if not primeCheck( t[:len(t)-(i+1)]): return False
    return True





while limit > 0:
    if primeCheck( n ):
        primes.add(n)
        if truncPrime( n ):
            limit -=1
            answers.add( n )
            print(n)
    n += 2
print(n)
print(answers)
print(len(primes))
