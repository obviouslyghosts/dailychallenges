"""
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

limit = 1000
maxPer = 0
solution = list()
searching = True

for per in range(limit+1, 3, -1):
    answers = list()
    for a in range(1, per//3):
        for b in range(1, per-a):
            c = per-(a+b)
            if (((a*a)+(b*b) )**(.5) == per-(a+b)):
                answers.append([a,b,c])
    if len(answers) > len(solution):
        print("%i sets a new Record with %i solution(s)" %(per, len(answers)))
        solution = answers
        maxPer = per

print("%i has %i solutions!" %(maxPer, len(solution)))
print(solution)
