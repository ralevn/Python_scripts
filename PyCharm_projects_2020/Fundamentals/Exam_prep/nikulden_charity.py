string = input()

command = input()
while command != 'Finish':
    if command.split(' ')[0] == 'Replace':
        curr_char = command.split(' ')[1]
        new_char = command.split(' ')[2]
        string = string.replace(curr_char, new_char)
        print(string)
    elif command.split(' ')[0] == 'Cut':
        start_ix = int(command.split(' ')[1])
        end_ix = int(command.split(' ')[2])
        if 0 <= start_ix <= end_ix <= len(string):
            substr = string[start_ix:end_ix + 1]
            string = string.replace(substr, '')
            print(string)
        else:
            print('Invalid indexes!')
    elif command.split(' ')[0] == 'Make':
        case = command.split(' ')[1]
        if case == 'Upper':
            string = string.upper()
            print(string)
        else:
            string = string.lower()
            print(string)
    elif command.split(' ')[0] == 'Check':
        string_1 = command.split(' ')[1]
        if string_1 in string:
            print(f'Message contains {string_1}')
        else:
            print(f'Message doesn\'t contain {string_1}')
    elif command.split(' ')[0] == 'Sum':
        start_ix = int(command.split(' ')[1])
        end_ix = int(command.split(' ')[2])
        if 0 <= start_ix <= end_ix <= len(string):
            substr = string[start_ix:end_ix + 1]
            sum = 0
            for ch in substr:
                sum += ord(ch)
            print(sum)
        else:
            print('Invalid indexes!')
    command = input()
