"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

limit = 1_000_000 #million
answers = list()

# count up to limit
# check if in answers - skip if it is
# check if prime
# if prime, offset by one and recheck
# if back at begining, save to answer list
## (save all of them!)

print(len(answers))
