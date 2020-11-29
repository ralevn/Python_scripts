numbers_dictionary = {}

line = input()
while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        if line not in numbers_dictionary:
            numbers_dictionary[number_as_string] = int(number)
    except ValueError:
        print("Must give integer")
    finally:
        line = input()


line = input()
while line != "Remove":
    try:
        print(numbers_dictionary[line])
    except KeyError:
        print("Number does not exist in dictionary")
    finally:
        line = input()


line = input()
while line != "End":
    try:
        numbers_dictionary.pop(line)
    except KeyError:
        print("Number does not exist in dictionary")
    finally:
        line = input()


print(numbers_dictionary)