def multiply_strings(string1, string2, n):
    s = 0
    for i in range(n):
        s += ord(string1[i]) * ord(string2[i])
    return s


def sum_remain(string, n):
    s = 0
    for i in range(1, n + 1):
        s += ord(string[len(string) - i])
    return s


strings = input().split(' ')
str1 = strings[0]
str2 = strings[1]

suma = 0
if len(str1) > len(str2):
    shorter = len(str2)
    remain = len(str1) - len(str2)
    suma = multiply_strings(str1, str2, shorter) + sum_remain(str1, remain)
elif len(str2) > len(str1):
    shorter = len(str1)
    remain = len(str2) - len(str1)
    suma = multiply_strings(str1, str2, shorter) + sum_remain(str2, remain)
else:
    number = len(str1)
    suma = multiply_strings(str1, str2, number)

print(suma)




