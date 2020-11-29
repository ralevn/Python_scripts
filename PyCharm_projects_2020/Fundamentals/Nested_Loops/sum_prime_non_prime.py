line_enetered = ''

def is_prime (n):
    if n <= 3:
        return True
    else:
        if n % 2 == 0:
            return False
        else:
            for i in range(2, n //2):
                if n % i == 0:
                    return False
                else:
                    continue
    return True


prime_sum = 0
non_prime_sum = 0

while line_enetered != 'stop':
    line_enetered = input()
    if line_enetered != 'stop':
        if int(line_enetered) < 0:
            print('Number is negative.')
            continue
        else:
            num = int(line_enetered)
        if is_prime(num):
            prime_sum += num
        else:
            non_prime_sum += num
print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')
