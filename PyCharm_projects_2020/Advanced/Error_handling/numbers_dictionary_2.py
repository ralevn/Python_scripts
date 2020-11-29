numbers_dictionary = {}

try:
    line = input()
    while line != "Search":
        number_as_string = line
        number = int(input())
        if line not in numbers_dictionary:
            numbers_dictionary[number_as_string] = int(number)
        line = input()

    line = input()
    while line != "Remove":
        print(numbers_dictionary[line])
        line = input()

    line = input()
    while line != "End":
        numbers_dictionary.pop(line)
        line = input()
except ValueError:
    print("Variable must be integer")
except KeyError:
    print("Number is not in dictionary")

finally:
    print(numbers_dictionary)