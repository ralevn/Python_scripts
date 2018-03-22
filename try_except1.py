
try:
    f = open('text1.txt')
except Exception:
    print 'No you can\'t'
print '######################'
try:
    f = open('text1.txt')
except Exception as e:
    print e
print '######################'
try:
    f = open('text1.txt')
except IOError:
    print 'Check file name'
print '######################'
f = open('text1.txt')
print '######################'
