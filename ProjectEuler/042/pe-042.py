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
import codecs # special characters

alpha = [i for i in string.ascii_lowercase]
triangles = [1]

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

w = "hello"

print(triangleNumberCheck(wordScore(w)))


# import csv
# import os
# import codecs # special characters

# f = 'C:/Users/Work/Desktop/test.csv'
# fPath = os.path.abspath(os.curdir)
# print(fPath)


def ReadFile(filePath):
    # check that its actual a file path
    if os.path.isfile(filePath):
        print("lets do this")
        #
        # fPath = os.path.dirname(filePath)
        # fPath = os.path.join(fPath, folder)

        # check if the path exists
        # if not os.path.isdir(fPath):
        #     # the path needs to be created
        #     os.mkdir(fPath)

        with open(filePath, newline='') as openFile:
            # fData = csv.reader(openFile, delimiter=',')
            fData = openFile.readlines()
            print(len(fData))
            # it reads as a single line... :(
            # and it's keeping all the "" and ,
            for d in fData:
                print(d)
    else:
        print("not a file")

f = r"C:\Users\Ryan\Projects\ObviouslyGhosts\CODE\dailychallenges\ProjectEuler\042\p042_words.txt"
# f = "Hello"
ReadFile( f )
