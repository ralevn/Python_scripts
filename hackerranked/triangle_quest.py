#!/bin/python3
"""
More than 2 lines will result in 0 score. Do not leave a blank line also 
print(i*sum(10**j for j in range(i)))
"""
for i in range(1,int(input())): 
    print((10**i)*i//9)
