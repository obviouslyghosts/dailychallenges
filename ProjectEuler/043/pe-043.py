"""
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

import itertools

largest = "9876543210"
answers = set()
primes =[2,3,5,7,11,13,17]

def sliceable( digits ):
    digits = str( digits )
    for i in range((len(digits)//3)*2):
        d = int( digits[i+1:i+4] )
##        print(digits, d, primes[i])
        if ( d % primes[i] ) != 0: return False
##        if not primeCheck( digits[i+1:i+3]): return False
    ## string slice across, check if (%n+1) == 0
    ## if the whole string can do this, then save it out!
    print( digits )
    return True



for d in itertools.permutations(largest, len(largest)):
    d = int("".join(k for k in d))
    if sliceable( d ):
        answers.add( d )

print( answers )
ans = sum([a for a in answers])
print( ans )
