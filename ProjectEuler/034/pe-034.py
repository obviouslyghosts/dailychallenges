"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the
factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

0 1
1 1
2 2
3 6
4 24
5 120
6 720
7 5040
8 40320
9 362880

145
40585

3000000 = 7d

"""

facts = dict()
lowerLimit = 500000
upperLimit = 600000

def getFactorial(f):
    if f in facts:
        #print("cached")
        return facts[f]
    t = 1
    for i in range(1,f+1):
        t*=i
    facts[f] = t
    return facts[f]


solutions = list()
##i = lowerLimit
##while i < upperLimit:
##    if i%100000 == 0: print(i)
##    ans = 0
##    s = str(i)
##    for v in s:
##        ans += getFactorial(int(v))
##    print(i, ans)
##    if ans > i:
##        print("too big")
##        c = str( int(s[0])+1 )
##        
##        if s[0]=="0": s = "1"+s
##        i = int(s)
##    else:
##        if ans == i:
##            print("MATCH!")
##            solutions.append(ans)
##        i+=1
##            
        
for i in range(lowerLimit, upperLimit,5):
    if i%100000 == 0: print(i)
    ans = 0
    s = str(i)
    for v in s:
        ans += getFactorial(int(v))
    print(i, ans)
    if ans == i:
        print("MATCH!")
        solutions.append(ans)

if len(solutions) > 0:
    for s in solutions:
        print(s)
else:
    print("no matchs :(")
