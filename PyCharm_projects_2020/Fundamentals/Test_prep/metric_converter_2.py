len = float(input())
inp_unit, out_unit = input().lower(), input().lower()

if inp_unit == 'km':
    m  = 1000
elif inp_unit == 'm':
    m = 1
elif inp_unit == 'cm':
    m = 0.01
elif inp_unit == 'mm':
    m = 0.001
elif inp_unit == 'in':
    m = 1 / 39.3700787
elif inp_unit == 'ft':
    m = 1 / 3.2808399
elif inp_unit == 'yd':
    m = 1 / 1.0936133
elif inp_unit == 'mi':
    m = 1 / 0.000621371192

km =   0.001 * m
cm =   100   * m
mm =   1000  * m
inch = 39.3700787 * m
ft =   3.2808399  * m
yd =   1.0936133  * m
mi =   0.000621371192 * m

if out_unit == 'km':
    result = len * km
elif out_unit == 'm':
    result = len * m
elif out_unit == 'cm':
    result = len * cm
elif out_unit == 'mm':
    result = len * mm
elif out_unit == 'in':
    result = len * inch
elif out_unit == 'ft':
    result = len * ft
elif out_unit == 'yd':
    result = len * yd
elif out_unit == 'mi':
    result = len * mi

print(result)