#!/bin/python3

"""
https://www.hackerrank.com/challenges/picking-numbers/problem
My improvement of original idea taken from vshah12 (10Q)
input is a list of integers
Editorial solution:
===================
from collections import Counter
n, arr = input(), Counter(map(int, raw_input().split()))
print reduce(lambda y, x:max(arr[x] + arr[x + 1], y), range(100), -1)
"""



import sys

def pickingNumbers(a):
    # Complete this function
    max=0
    for i in set(a):
        a1=a.count(i)
        #print(a1)
        a0=a.count(i-1)
        a1=a1+a0
        if a1 > max:
            #print(a2,a1,max)
            max=a1
    return max
    

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    result = pickingNumbers(a)
    print(result)
