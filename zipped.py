studNum,subjNum = map(int,raw_input().split())
subjLst =[]

for i in xrange(subjNum):
    subjLst.append(raw_input().split())

for i in zip(*subjLst):
    print sum(map(float,i))/subjNum