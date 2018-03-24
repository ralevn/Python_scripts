def print_formatted(number):
    # your code goes here
    bl = len(bin(number))-2
    for i in xrange(1,number+1):
        print "{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i,w=bl)
