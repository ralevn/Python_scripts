M = int(raw_input())
lstM = map(int,raw_input().split())
N = int(raw_input())
lstN = map(int,raw_input().split())

setM = set(lstM)
setN = set(lstN)


lstout = list(setM.difference(setN))+ list(setN.difference(setM))

for i in sorted(lstout):
    print i
