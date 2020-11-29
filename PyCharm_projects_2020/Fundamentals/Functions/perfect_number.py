def find_divisors (n):
    divisor_list = [i for i in range(1, (n // 2) + 1) if n % i == 0]
    return divisor_list

number = int(input())

if sum(find_divisors(number)) == number:
    print('We have a perfect number!')
else:
    print('It\'s not so perfect.')