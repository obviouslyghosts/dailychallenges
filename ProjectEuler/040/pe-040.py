"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

searching = True
d = "" ## the string
n = 0 ## the next digit to add, 1,2,3,4,...
maxString = 1000000

while searching:
    n += 1
    d += str(n) ## concatentate the digits
    ## check if the string is long enough
    if len(d) >= maxString: searching = False

## multiply the answer
ans = 1
for i in range(7):
    ans *= int(d[(10**i)-1])

print(len(d))
print(ans)
