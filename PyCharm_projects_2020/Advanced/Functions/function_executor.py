def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

def func_executor(*args):
    result = []
    for t in args:
        func = t[0]
        arguments = t[1]
        result.append(func(*arguments))
    return result

print(func_executor((sum_numbers, (1, 2)),
                    (multiply_numbers, (2, 4)),
                    (sum_numbers, (4, 7)),
                    (multiply_numbers, (20, 4))
                    )
      )