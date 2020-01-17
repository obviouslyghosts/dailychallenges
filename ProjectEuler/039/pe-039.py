"""
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

per = 120

for a in range(1, per):
    for b in range(1, per-a):
        c = per-(a+b)
        if (((a*a)+(b*b) )**(.5) == per-(a+b)):
            print(a,b,c)
