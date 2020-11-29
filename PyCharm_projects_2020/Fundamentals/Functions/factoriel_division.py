def factorial (n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

n1 = int(input())
n2 = int(input())

fn1, fn2 = factorial(n1), factorial(n2)

print(f'{fn1 / fn2:.2f}')