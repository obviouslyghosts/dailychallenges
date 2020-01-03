"""
We shall say that an n-digit number is pandigital if it makes use of all the
digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through
5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
"""

def checkPanDigital ( v, b ):
    s = str(v)
    if len(s) > b-1 : return False
    for i in range(1,b):
        if not (len([x for x in s if x == str(i)]) == 1):
            return False
    return True

ans = set()
limit = 99999 ## probably don't need to go higher than this
digits = 10 # 1-9

for a in range(1,limit):
    ## second loop:
    ## set lower bound to a, to remove duplicates
    ## set upper bound with consideration to digit count of a
    z = 10**(len(str(a))-1)
    for b in range(a,limit//z): 
        c = a*b
        if checkPanDigital(str(a)+str(b)+str(c), digits):
            print(a,b,c)
            ans.add(c)
print(ans)
print(sum(ans))
