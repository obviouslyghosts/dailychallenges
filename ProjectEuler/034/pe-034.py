"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the
factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

*****
upper bound:
99999999 == 8*(9!) == 2903040
2903040 is 7 digits long, but requires an 8 digit number to create.
Every digit greater than 99999999 will then be less digits than it took
to produce.
"""

facts = dict() # only calculate the factorials of 0-9 once
lowerLimit = 3
upperLimit = "99999999"

def getFactorial(f):
    # return cached factorial if it exists
    if f in facts: return facts[f]
    t = 1
    for i in range(1,f+1): t*=i
    facts[f] = t # chache it
    return facts[f]

# set the upper limit
a = 0
for v in upperLimit:
    a += getFactorial(int(v))
upperLimit = a

solutions = list()

for i in range(lowerLimit, upperLimit):
    if i%100000 == 0: print(i) # follow along!
    ans = 0
    s = str(i)
    for v in s:
        ans += getFactorial(int(v))
    if ans == i:
        print("MATCH!")
        solutions.append(ans)

if len(solutions) < 0:
    print("no matchs :(")
else:
    print("the solution is: %s" % (sum(solutions)))
