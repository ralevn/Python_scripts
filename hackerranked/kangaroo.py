#!/bin/python3

"""
https://www.hackerrank.com/challenges/kangaroo/problem

difference betwen both kangaroos is (x2 - x1) - (i*v1 -i*v2)
where "i" is the number of jumps
"""



import sys

def kangaroo(x1, v1, x2, v2):
    # Complete this function
    posDiff =((x2 - x1) - (i*v1 - i*v2) for i in range(10000))
    ans = 'NO'
    for pd in posDiff:
        if pd > 0: continue
        elif pd == 0: ans = 'YES'
        else: break
    return ans

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)

""" Editorial Solution (Python2 ):
x1, v1, x2, v2 = map(int, raw_input().split())
X = [x1, v1]
Y = [x2, v2]
back = min(X, Y)
fwd = max(X, Y)
dist = fwd[0] - back[0]

while back[0] < fwd[0]:
    back[0] += back[1]
    fwd[0] += fwd[1]
    if fwd[0] - back[0] >= dist:
        break

print ["NO", "YES"][back[0] == fwd[0]]
"""
