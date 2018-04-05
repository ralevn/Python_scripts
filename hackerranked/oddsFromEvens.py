def process(string):
    odds = []
    evens = []
    lstr = list(string)
    for i in range(len(string)):
        if i == 0 or i%2 == 0:
            evens.append(lstr[i])
        else:
            odds.append(lstr[i])
    print (''.join(evens),''.join(odds),sep=' ',end='\n')

num = int(input())
for i in range(num):
    string = input()
    process(string)
