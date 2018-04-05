"""
https://www.hackerrank.com/challenges/introduction-to-regex/problem
"""


def checkForNotAllowed(string):
    allowed = set('0123456789+-.')
    answer = 'True'
    for chr in string:
        if chr not in allowed:
            answer = 'False'
            break
        elif chr == '+' or chr == '-':
            if string.find(chr) != 0:
                answer = 'False'
                break
        elif string.count('.') != 1:
            answer = 'False'
    print (answer)
            
        
num = int(input())
for i in range(num):
    string = input()
    checkForNotAllowed(string)

