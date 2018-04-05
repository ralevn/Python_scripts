#!/bin/python3
'''
https://www.hackerrank.com/challenges/30-binary-numbers/problem
'''



import sys
import itertools

num = int(input().strip())
keys = []
groups = []
ii =[]

for k,n in itertools.groupby(bin(num)[2:]):
    keys.append(k)
    groups.append(list(n))
for i in groups:
    if i[0] == '1':
        ii.append(len(i))
print (max(ii))
