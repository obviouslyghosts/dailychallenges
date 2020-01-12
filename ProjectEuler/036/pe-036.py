"""
The decimal number, 585 = 1001001001^2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

# theyre always odd, because even will end with a 0 in binary

limit = 100
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
##    
##    # binary
##    b = bin(i)[2:]
##    print(b, b[::-1])

print(answers)
