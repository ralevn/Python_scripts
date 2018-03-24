#!/bin/python2.7
print "Hello World"
print "============"
ANS=24*6
txt='The answer of '
print txt,"24 x 6 is ",ANS
str1="ala "
str2="bala"
print str1+str2
TEXT=raw_input("Please enter a text longer that 15 characters: ")
while len(TEXT)<15:
      TEXT=raw_input("Please enter a text longer that 15 characters: ")
print "Actual text is: \"%s\"" %TEXT
print "the first letter is:  \"%s\"" %TEXT[0]
print "the second  letter is:  \"%s\""%TEXT[1]
print "There are %d characters in the text"%len(TEXT)
print "The first five characters in text are:  \"%s\""%TEXT[0:5]
print "The characters from 3d to 6th are:  \"%s\"" %TEXT[2:6]
## print backwards "-" negative value of the step 
## every item(charcter) in list has two indeces forward and backward
## forward start from 0 to end replaced with ":" and
## backward starting from -1 -2 etc to the begining replaced with ":"
print "Same reverse:   \"%s\"" %TEXT[5:1:-1]  
print "Same reverse:   \"%s\"" %TEXT[-1:-9:-1]  
print "Even characters:  \"%s\"" %TEXT[1::2]
print "Odd characters:  \"%s\"" %TEXT[0::2]
print "The last 5 characters are:  \"%s\""%TEXT[-5:]
print "Uppercase: \"%s\" and lower case:  \"%s\"" %(TEXT.upper(),TEXT.lower())
print "reverse:   \"%s\""%TEXT[::-1]
print "Print it vertically:"
for char in TEXT: print char
     
