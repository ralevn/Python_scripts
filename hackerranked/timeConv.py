#!/bin/python3

"""
https://www.hackerrank.com/challenges/time-conversion/problem
"""


import os
import sys

def timeConversion(s):
    HH = s[0:2] 
    period = s[-2:] 

    if period == 'AM': 
        if HH == '12':
            convtime = '00' + s[2:-2] 
        else: 
            convtime = s[0:-2] 
    elif period == 'PM':
        HH = s[0:2]
        if HH == '12':
            convtime = s[0:-2]
        else:
            convtime = str(int(HH) + 12) + s[2:-2]
    return convtime

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
