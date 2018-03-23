#!/bin/python2.7
""" Contains class person with __init__ , __call__ and display methods
functions for adding (add)and displaying tabulated data (tabulate)"""

class person ():
	""" __init__ , __call__ and display methods"""
	
	data=[]
	allinst=0
		
	def __init__(self):
	""" initializing object of class person and updating the list with objects 
	as well as the total number of items """
		self.name = raw_input ("Name: ")
		self.age = int(raw_input ("Age: "))
		person.allinst +=1
		self.ind = person.allinst
		person.data.append((self.name,self.age,self.ind))
		
	def __call__(self):
		print "Following values were assigned: %s, %s" %(self.name,self.age)
		return [self.name,self.age]
			
	def display(self):
		print "Your values are:\nName:\t%s\nAge:\t%s" %(self.name, self.age)
		
	
def add():
	""" if a variable is created with this function it will update the list with objects
	as well as the total number of items but it will not be an object of class person"""
	person.name = raw_input ("Name: ")
	person.age = int(raw_input ("Age: "))
	person.allinst +=1
	person.ind=person.allinst
	person.data.append((person.name,person.age,person.ind))

def tabulate():
	print "%s\t%s\t%s" %('Name','Age','Memeber Num')
	for i in range(len(person.data)):
		j=0
		print "%s\t%d\t%d" %(person.data[i][j],person.data[i][j+1],person.data[i][j+2])
