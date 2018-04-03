#!/bin/python3

"""
https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
"""

import collections

N =int(input())
phonebook = {}

for i in range(N):
    k,v = input().split()
    phonebook[k] = v
for i in range(N):
    name = input()
    if name in phonebook: 
        phone = phonebook[name]
        print (name + '=' + str(phone))
    else: print ('Not found')
