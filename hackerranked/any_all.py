#!/bin/pyhton3

"""
https://www.hackerrank.com/challenges/any-or-all/problem
"""


num = int(input())
lst = input().split()

print (all(int(n)>0 for n in lst) and any(n[::-1]==n for n in lst))
