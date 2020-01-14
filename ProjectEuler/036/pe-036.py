"""
The decimal number, 585 = 1001001001^2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

# an even number will end with a 0 in binary, which cannon be reversed
# all solutions must be odd

limit = 1_000_000
answers = set()

def isPalindromic( f ):
    f = str(f)
    if f[0] == "0": return False
    if f == f[::-1]: return True
    return False

for i in range(1, limit, 2):
    if isPalindromic(i):
        b = bin(i)[2:]
        if isPalindromic(b):
            answers.add(i)

print(answers)
print("sum: %i" %( sum(answers) ))
