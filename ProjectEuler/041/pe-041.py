"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and
is also prime.

What is the largest n-digit pandigital prime that exists?
"""
import itertools

largest = 987654321

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

def panDigitalPrime(limit):
    limit = str(limit)
    for i in range( len(limit) ):
        # starting at the largest, and counting down
        # check all permutations of the pandigital number
        for d in itertools.permutations(limit[i:], len(limit[i:])):
            d = int("".join(k for k in d))
            if primeCheck(d):
                return d
    return 0

print("searching for pandigital Primes...")
answer = panDigitalPrime(largest)
print(answer)
