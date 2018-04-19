#/bin/python3

"""
https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem
"""


import itertools
string,N = input().split()
num = int(N)
for i in sorted(itertools.combinations_with_replacement(sorted(string),num)):
    print(*i,sep='')
