#!/bin/python3

"""
https://www.hackerrank.com/challenges/python-time-delta/problem
"""


import sys, datetime

def time_delta(t1, t2):
    # Complete this function
    post = datetime.datetime.strptime(t1,"%a %d %b %Y %H:%M:%S %z")
    view = datetime.datetime.strptime(t2,"%a %d %b %Y %H:%M:%S %z")
    interval = post - view
    #print(t1,t2,post,view,interval, sep = "\n")
    return int(abs(interval.total_seconds()))

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        t1 = input().strip()
        t2 = input().strip()
        delta = time_delta(t1, t2)
        print(delta)



""" Editorial solution: 
from datetime import datetime

for i in range(int(input())):
    t1 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    print(abs(int((t1-t2).total_seconds())))
"""
