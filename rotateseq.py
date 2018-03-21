def lrotate():
    l,n = raw_input().split()
    llen,nu = int(l),int(n)
    lst=[x for x in xrange(1,llen+1)]
    llst = lst[nu:]+lst[:nu]
    for i in llst:
        print i,

