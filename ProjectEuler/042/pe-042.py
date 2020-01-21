"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle words?
"""

import string
import os
import csv

alpha = [i for i in string.ascii_lowercase] #abc...xyz
triangles = [1]

file = "p042_words.txt"
path = os.path.abspath(os.curdir)
filePath = os.path.join(path, file)


def wordScore( word ):
    score = 0
    for letter in word:
        score += alpha.index(letter)+1
    return score

def triangleNumberCheck( number ):
    while triangles[-1] < number:
        n = len(triangles)+1
        triangles.append( 0.5 * n * ( n + 1 ) )
    if number in triangles: return True
    return False


ans = 0
if os.path.isfile(filePath):
    print("lets do this")

    with open(filePath, newline='') as openFile:
        reader = csv.reader(openFile, delimiter=',')
        for row in reader:
            for word in row:
                score = wordScore(word.lower())
                if triangleNumberCheck(score):
                    print(word)
                    ans+=1
else:
    print("not a file")

print(ans)
