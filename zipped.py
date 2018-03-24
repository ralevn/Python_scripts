"""
Input Format

The first line contains  and  separated by a space. 
 The next  lines contains the space separated marks obtained by students in a particular subject. 

Output Format

Print the averages of all students on separate lines.
The averages must be correct up to  decimal place.

Sample Input

5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5

Sample Output

90.0 
91.0 
82.0 
90.0 
85.5   

"""

studNum,subjNum = map(int,raw_input().split())
subjLst =[]

for i in xrange(subjNum):
    subjLst.append(raw_input().split())

for i in zip(*subjLst):
    print sum(map(float,i))/subjNum
