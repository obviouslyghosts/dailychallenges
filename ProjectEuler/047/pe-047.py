"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?
"""

# count up
# get prime factors
# save in queue if great

isSearching = True
ans = list()
limit = 3

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

def Factor(n, short):
    facs = list()
    if n <=1: return [1]
    for i in range(2,n):
        if n%i==0:
            facs.append(i)
            n=n//i
            if len(facs)>short: return[1]
    if len(facs) <1: return[1, n]
    return facs


num=1
while isSearching:
    factors = Factor(num,limit)
    if len(factors) == limit:
        if all([PrimeCheck(f) for f in factors]):
            print(num, "passed")
            ans.append(num)
        else:
            ans = list()
    else:
        ans = list()
    num += 1
    if len(ans)>=limit:isSearching = False
#

print("Complete")
print(ans)
