def sum_numbers(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def add_and_subtract(n1, n2, n3):
    temp_n = sum_numbers(n1, n2)
    return subtract(temp_n, n3)

n1 = int(input())
n2 = int(input())
n3 = int(input())

print(add_and_subtract(n1, n2, n3))
