#!/bin/python3

"""
https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem
"""

import sys
def reverseNumb(numb):
    lstnumb=list(str(numb))
    revnumb=int(''.join(reversed(lstnumb)))
    return revnumb
    
def beautifulDays(i, j, k):
    # Complete this function
    bDays=[]
    for d in range(i,j+1):
        if (d - reverseNumb(d))%k == 0:
            bDays.append(d)
    return len(bDays)

if __name__ == "__main__":
    i, j, k = input().strip().split(' ')
    i, j, k = [int(i), int(j), int(k)]
    result = beautifulDays(i, j, k)
    print(result)
