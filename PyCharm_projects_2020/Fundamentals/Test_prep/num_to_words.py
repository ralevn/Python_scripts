num = int(input())
n1 = int(str(num)[0])
n2 = 0
if num > 9: n2 = int(str(num)[1])

# print (n1,n2)

one_digit = {0:'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
two_digit_1 = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
               17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
two_digit_2 = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

if num < 10:
    for i in one_digit:
        if num == i: print(one_digit[i]); exit()
elif 10 <= num < 20:
    for i in two_digit_1:
        if num == i: print(two_digit_1[i]); exit()
elif 20 <= num < 100:
    for i in two_digit_2:
        if n1 == i:
            d1 = two_digit_2[i]
            if n2 == 0: break
            for j in one_digit:
                if n2 == j:
                    d2 = one_digit[j]; break
elif num == 100: print('one hundred'); exit()

if n2 != 0:
    print(d1, d2)
else: print (d1)
