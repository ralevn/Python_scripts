#!/bin/python3

"""
https://www.hackerrank.com/challenges/python-sort-sort/problem
"""


import sys

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    arr = []
    for arr_i in range(n):
       arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
       arr.append(arr_t)
    k = int(input().strip())

sortedList = sorted(arr, key=lambda athlet: athlet[k])
for i in range(len(arr)):
    print(*sortedList[i])


""" Editorial python2 solution
n,m = map(int,raw_input().split())
lst = []
for i in range(n):
    lst.append(map(int,raw_input().split()))
k = int(raw_input())    
print "\n".join(map(lambda x: " ".join(map(str, x)), sorted(lst, key = lambda x: x[k])))
"""
