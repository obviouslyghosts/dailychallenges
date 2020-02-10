"""
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
"""

upper = 10

ans = 0

for i in range(1,upper+1):
    ans += (i**i)

print(ans)
