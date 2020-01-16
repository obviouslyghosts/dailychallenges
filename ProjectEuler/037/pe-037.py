"""
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each
stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

## start with set containing 1-digit primes
## add 1-9 to the left of the primes
## if it is prime: keep it in new list, and test for trunc
## replace primes with new list, repeat


limit = 11
answers = set()
primes = set()


def primeCheck(n):
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


def truncPrime(n):
    t = str(n)
    ## if the first digit isn't prime, it wont work, and this is quick
    if not primeCheck(t[0]): return False
    for i in range(len(t)-1):
        if not primeCheck( t[:len(t)-(i+1)]): return False
    return True

## set initial prime list
for i in range(3, 10):
    if primeCheck(i):
        primes.add(i)

while limit > 0:
    newPrimes = set()
    for p in primes:
        for i in range(1,10):
            ## add 1-9 to the front, and test for prime
            a = str(i)+str(p)
            if primeCheck( a ):
                newPrimes.add( a )
                if a not in answers and truncPrime( a ):
                    print("found: %s" % a)
                    limit -= 1
                    answers.add( a )        
    primes = newPrimes
    print(len(primes))

print(answers)
s = 0
for a in answers:
    s+= int(a)
print(s)
