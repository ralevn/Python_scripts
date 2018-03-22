lst = [(x,x*x) for x in xrange(16) if x % 2 != 0]
print lst
dict = {x : x*x for x in xrange(16) if x % 2 != 0}
print dict
tup = (x for x in xrange(16) if x % 2 != 0)
print tup
for element in tup:
    print element, type(element)
