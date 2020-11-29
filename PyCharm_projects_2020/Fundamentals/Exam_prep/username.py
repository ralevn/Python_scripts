username = input()

command = input()
while command != 'Sign up':
    if command.split(" ")[0] == 'Case':
        if command.split(" ")[1] == 'upper':
            username = username.upper()
        else:
            username = username.lower()
        print(username)
    elif command.split(" ")[0] == 'Reverse':
        start_ix = int(command.split(" ")[1])
        end_ix = int(command.split(" ")[2])
        if (0 <= start_ix <= end_ix) and (start_ix <= end_ix < len(username)):
            string = username[start_ix: end_ix + 1]
            print(string[::-1])
        else:
            command = input()
            continue
    elif command.split(" ")[0] == 'Cut':
        substring = command.split(" ")[1]
        if substring in username:
            username = username.replace(substring, '')
            print(username)
        else:
            print(f'The word {username} doesn\'t contain {substring}.')
    elif command.split(" ")[0] == 'Replace':
        char = command.split(" ")[1]
        for c in username:
            if c == char:
                username = username.replace(c, '*')
        print(username)
    elif command.split(" ")[0] == 'Check':
        char = command.split(" ")[1]
        if char not in username:
            print(f'Your username must contain {char}.')
        else:
            print('Valid')
    command = input()