"""
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
"""

limit = 10
upper = int('9'*10)
ans = 0

for i in range(1,limit+1):
    a = str(i**i)
    print(a)
    a = int(a[len(a)-limit:])
    print(a)
    ans += a
    ans = str(ans)
    ans = int(ans[len(ans)-limit:])

print(ans)
