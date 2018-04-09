#!/bin/python3

"""
https://www.hackerrank.com/challenges/insertionsort2/problem
"""

import sys

def insertionSort2(n, arr):
    # Complete this function
    for i in range(1, len(arr)):
        while i > 0 and temp < arr[i-1]:
            arr[i],arr[i-1] = arr[i-1],arr[i]
            i -= 1
        print (' '.join(str(i) for i in arr))
        
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort2(n, arr)
