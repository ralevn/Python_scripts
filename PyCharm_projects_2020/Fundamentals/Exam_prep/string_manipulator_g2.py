string = input()

command = input()
while command != "Done":
    if command.split(' ')[0] == 'Change':
        char = command.split(' ')[1]
        new_char = command.split(' ')[2]
        string = string.replace(char, new_char)
        print(string)
    elif command.split(' ')[0] == 'End':
        substr = command.split(' ')[1]
        print(string.endswith(substr))
    elif command.split(' ')[0] == 'Includes':
        substr = command.split(' ')[1]
        if string.count(substr):
            print(True)
        else:
            print(False)
    elif command.split(' ')[0] == 'Uppercase':
        string = string.upper()
        print(string)
    elif command.split(' ')[0] == 'FindIndex':
        ix = command.split(' ')[1]
        print(string.find(ix))
    elif command.split(' ')[0] == 'Cut':
        start_ix = int(command.split(' ')[1])
        length = int(command.split(' ')[2])
        string = string[start_ix: start_ix + length]
        print(string)
    command = input()