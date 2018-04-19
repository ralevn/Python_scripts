#!/bin/python3

"""
https://www.hackerrank.com/challenges/iterables-and-iterators/problem
"""


import itertools
n = int(input())
lst = input().split()
k = int(input())
numa = 0
numcombs = 0

combs = itertools.combinations(lst,k)
for c in combs:
    if c.count('a') != 0:
        numa += 1
    numcombs += 1
print('{:5f}'.format(numa/numcombs))
