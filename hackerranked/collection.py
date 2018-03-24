from collections import Counter
shoeNum = int(raw_input())
shoeSizeLst = map(int,raw_input().split())
custNum = int(raw_input())
custDemand = [(0,0)]*(custNum)
for i in xrange(custNum):
    x,y = map(int,raw_input().split())
    custDemand[i] = (x,y)

shoeSizeCount = Counter(shoeSizeLst)
print shoeSizeCount
print shoeSizeCount.keys()
print shoeSizeCount.values()
print custDemand
for size in xrange(len(custDemand)):
    for price in xrange(2):
        print custDemand[size][price],
