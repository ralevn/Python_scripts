from math import pi

radius = float(input())
## Alt + Enter with cursor on pi will import
surface = radius**2 * pi
circumvent = 2*pi*radius
print (f'{surface:.2f}')
print ('%.2f' % circumvent)