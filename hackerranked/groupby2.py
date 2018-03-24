"""
You are given a string S. Suppose a character 'c' occurs consecutively X times in the string.
Replace these consecutive occurrences of the character 'c' with (X,c) in the string. 
For a better understanding of the problem, check the explanation. 

Input Format
A single line of input consisting of the string . 

Output Format 
A single line of output consisting of the modified string S.

Constraints
All the characters of S denote integers between 0 and 9. 

https://docs.python.org/2/library/itertools.html#itertools.groupby
"""




import itertools

S = raw_input()

for k, g in itertools.groupby(S):
    print (len(list(g)), int(k)),
