"""
The decimal number, 585 = 1001001001^2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

limit = 100

for i in range(limit):
    # binary
    b = bin(i)[2:]
    print(b, b[::-1])
    
