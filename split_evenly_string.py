#!/bin/python3

"""
split string evenly:
https://www.hackerrank.com/challenges/merge-the-tools/problem
input string and a k - length of the substrings
the rest of the code removes duplicates preserving character order 
of original substring
"""


mstring, k = input(), int(input())

for i in [mstring[i:k+i] for i in range(0,len(mstring),k)]:
    tmpstr = ''
    for ch in i:
        if ch in tmpstr: continue
        tmpstr += ch
    print (tmpstr)
