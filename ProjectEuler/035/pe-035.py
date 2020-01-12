"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
import time

## Improve by flagging primes to be checked later,
## so that we only pass through all the digits once

start = time.time()

limit = 1_000_000 #million
answers = {2} #start with 2


def primeCheck(n):
    ## even check
    if n%2<1: return False
    ## only check below square root!
    l = int(n**0.5)+1
    for i in range(3,l,2):
        if n%i <1: return False
    return True



for i in range(3, limit, 2):
    if (i not in answers) and (primeCheck(i)):
        # this is a unique prime
        temp = {i}
        isCircle = True
        # loop through each combination
        for j in range(len(str(i))-1):
            k = int(str(i)[j+1:] + str(i)[:j+1])
            if (isCircle) and (k not in answers) or (k not in temp):
                if primeCheck(k):
                    temp.add(k)
                else:
                    isCircle = False
        if isCircle:
            print("%i is new, unique circle prime" % (i) )
            # add all of the primes to the the answers
            for a in temp:
                answers.add(a)

print(len(answers))
print(time.time()-start)
