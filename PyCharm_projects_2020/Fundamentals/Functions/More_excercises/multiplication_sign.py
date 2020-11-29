negatives = 0

n1 = int(input())
if n1 < 0:
    negatives += 1
elif n1 == 0:
    print('zero')
    exit()
n2 = int(input())
if n2 < 0:
    negatives += 1
elif n2 == 0:
    print('zero')
    exit()
n3 = int(input())
if n3 < 0:
    negatives += 1
elif n3 == 0:
    print('zero')
    exit()
if negatives % 2 == 0:
    print('positive')
else:
    print('negative')