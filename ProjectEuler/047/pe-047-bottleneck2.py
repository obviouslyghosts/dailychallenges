import time
import cProfile
import pstats


primes = [2]

def PrimeCheck(n):
    n = int(n)
    if n == 1: return False
    if n == 2: return True
    if n%2<1: return False
    l = int(n**0.5)+1
    for i in range(3,l,2):
        if n%i <1: return False
    return True

def IsPrime(n):
    if n in primes: return True
    if len(primes)>0 and primes[-1] > n: return False
    i = primes[-1]
    while primes[-1] < n:
        if PrimeCheck(i+1):
            primes.append(i+1)
        i+=1
    if n in primes: return True
    return False

def PrimeFactor(n, short):
    if n<=1: return 0
    # facs = list()
    f = 0
    for i in range(2,n):
        if n%i==0:
            if not IsPrime(i): return 0
            # facs.append(i)
            f+=1
            n=n//i
            if f>short: return 0
    if f <1: return 0
    return f

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
    limit = 3
    ans = list()
    num=SetLowerBound( limit )
    print( num )
    # num = 130000
    searchMax = 40000

    while isSearching:
        if num%5000==0:print(num)
        factCount = PrimeFactor(num,limit)
        if factCount == limit:
            ans.append(num)
            if len(ans) == 1:
                fUpperCount = PrimeFactor(num+limit-1, limit)
                if fUpperCount == limit:
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
