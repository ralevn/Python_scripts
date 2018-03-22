rows,cols = map(int,raw_input().split())
ch,text = ".|.","WELCOME"

for i in xrange(0,rows-1,2):
    print (ch*i + ch).center(cols,'-')
print text.center(cols,'-')
for i in reversed(xrange(0,rows-1,2)):
    print (ch*i + ch).center(cols,'-')
