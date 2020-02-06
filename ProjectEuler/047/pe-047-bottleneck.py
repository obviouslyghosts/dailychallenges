import time
import cProfile
import pstats


primes = list()

def PrimeCheck(n):
    n = int(n)
    if n == 1: return False
    if n == 2: return True
    if n%2<1: return False
    l = int(n**0.5)+1
    for i in range(3,l,2):
        if n%i <1: return False
    return True

def PrimeFactor(n, short):
    if n<=1: return[1]
    facs = list()
    for i in range(2,n):
        if n%i==0:
            if not PrimeCheck(i):
                # print(i,"not prime")
                return [1]
            facs.append(i)
            n=n//i
            if len(facs)>short: return[1]
    if len(facs) <1: return[1, n]
    return facs

def Factor(n, short):
    if n <=1: return [1]
    facs = list()
    for i in range(2,n):
        if n%i==0:
            facs.append(i)
            n=n//i
            if len(facs)>short: return[1]
    if len(facs) <1: return[1, n]
    return facs

def SetLowerBound( d ):
    p = list()
    n = 2
    while len(p) < d:
        if PrimeCheck(n):
            p.append(n)
        n+=1
    n = 1
    for i in p:
        n *= i
    return n

def Main():
    isSearching = True
    limit = 4
    ans = list()
    num=SetLowerBound( limit )
    print( num )
    num = 130000
    searchMax = 40000

    while isSearching:
        if num%5000==0:print(num)
        factors = PrimeFactor(num,limit)
        if len(factors) == limit:
            ans.append(num)
            if len(ans) == 1:
                fUpper = PrimeFactor(num+limit-1, limit)
                if len(fUpper) == limit:
                    ans.append(num)
                else:
                    ans = list()
                    num += limit-1
        else: ans = list()
        num += 1
        if len(ans)>=limit:isSearching = False
        # if num >= searchMax: isSearching = False
    #
    print("Complete")
    print(ans)

profile = cProfile.Profile()
profile.runcall(Main)
ps = pstats.Stats(profile)
ps.print_stats()
