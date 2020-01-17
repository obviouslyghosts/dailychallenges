"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and
5, giving the pandigital, 918273645, which is the concatenated product of 9
and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""
##smallest = 123456789
largest = 987654321
digits = 10 # 1-9

def checkPanDigital ( v, b ):
    s = str(v)
    if len(s) < b-1: return False
    if len(s) > b-1 : return False
    for i in range(1,b):
        if not (len([x for x in s if x == str(i)]) == 1):
            return False
    return True

searching = True
n = 2
answer = 0

while searching:
    if n%100 == 0: print(n) # keep track of search
    m = 1
    a = ""
    building = True
    while building:
        if len(a+ str(n*m))>9:
            building = False
        else:            
            a+= str(n*m)
            m+=1
    if checkPanDigital( a, digits ):
        if int(a) > answer:
            print("FOUND ONE! %s" %(a))
            answer = int(a)
    if int(a) > largest:
        searching = False
    n+=1

print( answer )
