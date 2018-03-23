#!/bin/python2.7
# Slicing allows access one or more elements of a sequence
# Immutable sequences include tuples, strings, and bytes
a_tuple = ('a', 1, 2, (3, 4))
print "a_tuple: ",a_tuple
a_string = 'immutable'
print "a_string: ",a_string
a_bytes = b'sequence'
print "a_bytes: ",a_bytes,"\n"

# Mutable sequences include lists and bytearrays
a_list = [5, 6, 7, 8, (4, 5)]
print "a_list: ",a_list
a_byte_array = bytearray(b'mutable')
print "a_byte_array: ",a_byte_array,"\n"

# Accessing is allowed in all sequences
print('a_tuple[0] ->', a_tuple[0])
print('a_string[1] ->', a_string[1])
print('a_bytes[2] ->', a_bytes[2])
print('a_list[3] ->', a_list[3])
print('a_byte_array[4] ->', a_byte_array[4]),"\n"

# Negative indexes are from the end
print('a_tuple[-1] ->', a_tuple[-1])
print('a_string[-2] ->', a_string[-2])
print('a_bytes[-3] ->', a_bytes[-3])
print('a_list[-4] ->', a_list[-4])
print('a_byte_array[-5] ->', a_byte_array[-5]),"\n"

# Subslices can be accessed with two indexes
print('a_list[0:2] ->', a_list[0:2])
print('a_list[:2] ->', a_list[:2])
print('a_list[2:5] ->', a_list[2:5])
print('a_list[2:] ->', a_list[2:])
print('a_list[:] ->', a_list[:])
list_ref = a_list
print('a_list is list_ref ->', a_list is list_ref)
list_copy = a_list[:]
print('a_list is list_copy ->', a_list is list_copy)
