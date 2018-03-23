#!/bin/python2.7

list1=['A','B','C']
# xrange and range define number of iteration if like (3) starts with 0 and end with 2
# starting number and number of iteration if like (1,3) will start from 1 to 3
# starting number, number of iteration and step to increase if like (1,10,2)
for i in xrange(3):
    print "For i = %d list1[%d] is %s"%(i,i,(list1[i]))
#"for" loops execute statements equallly indented with spaces
for j in xrange(0,3):
    print "For j = %d list1[%d] is %s"%(j,j,(list1[j]))
# Assign values to empty lists
list2=[]
for i in xrange(3):
    temp=raw_input("Enter value for list2[%d]:  "%i)
    list2.append(temp)
for j in xrange(0,3):
    print "For i = %d list2[%d] is %s"%(j,j,(list2[j]))
# Changing values to empty lists Ver2
print "Replacing values"
for i in xrange(3):
    list2[i]=raw_input("Enter value for list2[%d]:  "%i)
for j in xrange(0,3):
    print "For i = %d list2[%d] is %s"%(j,j,(list2[j]))
# Extend list
print ("These are now values for list2: %s and for list1: %s"%(list2,list1))
print ("Now inserting values in front of list")
for i in xrange(3):
    temp=raw_input("Enter value for list2[%d]:  "%i)
    list2.insert(i,temp)
print ("Now extending values or appending behind")
list2.extend(list1)
print ("These are now values for list2: %s and for list1: %s"%(list2,list1))
