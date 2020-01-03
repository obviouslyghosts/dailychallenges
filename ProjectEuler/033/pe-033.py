"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is
correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
"""

ans = set()

def filterTrivial( ab, xy ):
    ab = str(ab)
    xy = str(xy)
    if ( ab[0] == xy[0] ): return False
    if ( ab[1] == xy[1] ): return False
    return True

def simpleReduce( ab, xy ):
    ab = str(ab)
    xy = str(xy)

    if ( xy[1] == "0" ): return ( 0 )
    if ( ab[0] == xy[1] ): return ( int( ab[1] ) / int( xy[0] ) )
    if ( ab[1] == xy[0] ): return ( int( ab[0] ) / int( xy[1] ) )

for xy in range(10, 100):
    for ab in range(10, xy+1):
        if filterTrivial( ab, xy ):
            if simpleReduce(ab,xy) == (ab/xy):
                print(ab,xy)
                ans.add( xy )
