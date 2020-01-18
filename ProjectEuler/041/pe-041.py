"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and
is also prime.

What is the largest n-digit pandigital prime that exists?
"""
import itertools

largest = "987654321"
n = list(itertools.permutations(largest, len(largest)))
digits = 10

def checkPanDigital ( v, b ):
    s = str(v)
    if len(s) < b-1: return False
    if len(s) > b-1 : return False
    for i in range(1,b):
        if not (len([x for x in s if x == str(i)]) == 1):
            return False
    return True

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
    upperLimit = int( str(limit)[::-1])
    for i in n:
        i = int("".join(k for k in i))
        if primeCheck(i):
            print("FOUND!")
            return i
    return 0

print("searching for pandigital Primes...")
answer = panDigitalPrime(largest)
print(answer)