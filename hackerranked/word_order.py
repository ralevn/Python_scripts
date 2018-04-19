#!/bin/python3

"""
https://www.hackerrank.com/challenges/word-order/problem
"""


import collections
num = int(input())
od =collections.OrderedDict()


for i in range(num):
    word = input()
    if word in od: od[word] += 1
    else: od[word] = 1

print(len(od))
print(*od.values())
