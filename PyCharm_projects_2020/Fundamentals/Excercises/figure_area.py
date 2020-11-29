from math import pi

figure_type = input()

def square_ar(a):
    print(f'%.3f' %(a ** 2))

def rectangle_ar (a,b):
    print(f'%.3f' %(a*b))

def circle_ar (r):
    print(f'%.3f' %((r**2)*pi))

def triangle_ar (a,h):
    print(f'%.3f' %((a * h) / 2))

if figure_type == 'square': a = float(input()); square_ar(a)
elif figure_type == 'rectangle':a,b = float(input()), float(input()); rectangle_ar (a,b)
elif figure_type == 'circle':r = float(input()); circle_ar (r)
else: a,h = float(input()), float(input()); triangle_ar(a,h)


