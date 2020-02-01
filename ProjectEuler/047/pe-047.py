"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors
each. What is the first of these numbers?
"""

# count up
# get prime factors
# save in queue if great

isSearching = True
lim = 1000
ans = list()
n=1

def HasPrimeFactors(n):
    for i in range(2,)
    return False

while isSearching:
    if HasPrimeFactors(n):
        ans.append(n)
    elif len(ans)>0:
        ans = list()
    n+=1
    lim -=1
    if len(ans)>=4:searching = False
    if lim <=0: isSearching = False

print("Complete")
print(ans)
