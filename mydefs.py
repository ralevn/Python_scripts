#!/bin/python2.7
""" Here I plan to save frequently used functions.
******************************************************************************
The following functions are just added as to test primfact(e)  fib(n)   fib2(n)
******************************************************************************"""
print "You just imported ",__name__,"  functions here: primfact(e), fib(n) and fib2(n)"
print "The value of __name__ is %s" %__name__

import os

def listf(d=None):
	"""prints the directory content. if no parametrs 
	are passed print current directory content"""
	if d:
		dir=str(d)
	else:
		dir=os.getcwd()
	for item in os.listdir(dir):
		print item

def primfact(e):
   """ print the primary numbers to the specified number as argument"""
   for n in range(2, e):
      for x in range(2, n):
         if n % x == 0:
            break
      else:
         print n, 

def fib(n):
    """ write Fibonacci series up to n """
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b


def fib2(n):
    """ return Fibonacci series up to n """
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
	
def findchars():
	text=raw_input("Enter the text: ")
	char=raw_input("Enter the character to be searched: ")
	positions=list()
	for i in range(text.find(char),text.rfind(char)+1):
		if text.find(char,i,i+1)!= -1:
			positions.append(i)
			print i,
		else:
			continue
	return positions
	
