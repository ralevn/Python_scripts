hh, mm = int(input()), int(input())

if 0 <= mm < 45:
    mm = mm + 15
elif hh != 23:
    hh = hh + 1
    mm = mm + 15 -60
else:
    hh = 0
    mm = mm + 15 - 60

print (f'%d:%02d' %(hh,mm))

