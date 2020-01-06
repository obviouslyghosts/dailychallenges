"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the
factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

facts = dict()
lowerLimit = 3
upperLimit = 1000000

def getFactorial(f):
    if f in facts:
        #print("cached")
        return facts[f]
    t = 1   
    for i in range(1,f+1):
        t*=i
    facts[f] = t
    return facts[f]


solutions = set()
for i in range(lowerLimit, upperLimit):
    ans = 0
    s = str(i)
    for v in s:
        ans += getFactorial(int(v))
    if ans == i:
        print("MATCH!")
        solutions.add(ans)

if len(solutions) > 0:
    for s in solutions:
        print(s)
else:
    print("no matchs :(")
