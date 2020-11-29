def list_manipulator(list_i, *args):
    operation = args[0]
    position = args[1]
    numbers = []
    for i in args[2:]:
        numbers.append(i)
    n = len(numbers)
    if operation == 'add'and position == 'end':
        return list_i + numbers
    elif operation == 'add' and position == 'beginning':
        return numbers + list_i
    elif operation == 'remove' and position == 'beginning':
        if n == 0:
            return list_i[1:]
        else:
            return list_i[args[2]:]
    elif operation == 'remove' and position == 'end':
        if n == 0:
            return list_i[:-1]
        else:
            return list_i[:-(args[2])]






print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))