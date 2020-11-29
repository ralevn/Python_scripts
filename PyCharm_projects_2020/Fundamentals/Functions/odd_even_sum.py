def odd_even_sum (str_n):
    odds = [int(n) for n in str_n if int(n) % 2 != 0]
    evens = [int(n) for n in str_n if int(n) % 2 == 0]
    return sum(odds), sum(evens)

n = input()

print(f'Odd sum = {odd_even_sum(n)[0]}, Even sum = {odd_even_sum(n)[1]}')