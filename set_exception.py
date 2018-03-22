"""
Task

You have a non-empty set , and you have to execute N commands given in N lines.
The commands will be pop, remove and discard. 

Input Format

The first line contains integer n, the number of elements in the set s. 
 The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9. 
 The third line contains integer N, the number of commands.
 The next N lines contains either pop, remove and/or discard commands followed by their associated value.

Output Format

Print the sum of the elements of set s on a single line.
"""

n = int(raw_input())
s = set(map(int,raw_input().split()))
n1 = int(raw_input())

for i in xrange(n1):
    f = raw_input().split()
    if f[0] == 'remove':
        try:
            s.remove(int(f[1]))
        except Exception:
            continue
    elif f[0] == 'discard':
        s.discard(int(f[1]))
    else:
        s.pop()
print sum(list(s))
