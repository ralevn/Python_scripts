#!/bin/python3

"""
https://www.hackerrank.com/challenges/np-arrays/problem
"""

import numpy


def arrays(arr):
    rlst = arr[::-1]
    numpylst = numpy.array(rlst,float)
    return numpylst


arr = input().strip().split(' ')
result = arrays(arr)
print(result)


