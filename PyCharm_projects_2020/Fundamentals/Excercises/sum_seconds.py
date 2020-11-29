sec1,sec2,sec3 = int(input()), int(input()), int(input())

def min_sec (s):
    return f'%2d:%02d' %(s // 60, s % 60)

print (min_sec(sec1 + sec2 + sec3))