"""
Lists 

onsider a list (list = []). You can perform the following commands: 
nsert i e: Insert integer e at position i. 
rint: Print the list. 
emove e: Delete the first occurrence of integer e. 
ppend e: Insert integer e at the end of the list. 
ort: Sort the list. 
op: Pop the last element from the list. 
reverse: Reverse the list. 

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the types listed above. 
Iterate through each command in order and perform the corresponding operation on your list. 

Input Format 
The first line contains an integer, n, denoting the number of commands.  
Each line i of the n subsequent lines contains one of the commands described above. 

Constraints 
The elements added to the list must be integers. 

Output Format 
For each command of type print, print the list on a new line. 

Enter your code here. Read input from STDIN. Print output to STDOUT 
"""
if __name__ == '__main__':
    N = int(raw_input())
    lst=[]
    for i in xrange(N):
        a = raw_input().split()
        if len(a) == 3:
            eval("lst." + a[0] + "(" + a[1] + "," + a[2] + ")")
        elif len(a) == 2:
            eval("lst." + a[0] + "(" + a[1] + ")") 
        elif a[0] == "print":
            print lst
        else:
            eval("lst." + a[0] + "()")
