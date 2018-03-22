formula = raw_input("Formula for y = : ")

for x in xrange(0,40,5):
    print "x =",x, ": y =", eval(formula)
