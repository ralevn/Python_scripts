"""
Input Format

The first line contains an integer N, the total number of students. 
 The second line contains the names of the columns in any order. 
 The next N lines contains the marks, IDs, name and , class under their respective column names.
SAMPLE INPUT
TESTCASE 01
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   


TESTCASE 02 
5
MARKS      CLASS      NAME       ID        
92         2          Calum      1         
82         5          Scott      2         
94         2          Jason      3         
55         8          Glenn      4         
82         2          Fergus     5
SAMPLE OUTPUT:
78.00
81.00

"""




from collections import namedtuple

N = int(raw_input())

resultList = ','.join(raw_input().split())
Student = namedtuple('Student', resultList)

marksum = 0
for i in xrange(N):
    result = raw_input().split()
    student = Student(*result)
    marksum += float(student.MARKS)

print '{:.2f}'.format(marksum/N)
