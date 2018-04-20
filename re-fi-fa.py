#!/bin/python3

import re
string = input()

pat = r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[AEIOUaeiou]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'
compre = re.compile(pat)

fa = compre.findall(string)
if not fa:
    print('-1')
else:
    for fi in compre.finditer(string):
        print(fi.group())
