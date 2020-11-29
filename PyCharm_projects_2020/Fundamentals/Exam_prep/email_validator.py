email = input()

line = input()

while line != 'Complete':
    if line == 'Make Upper':
        email = email.upper()
        print(email)
    elif line == 'Make Lower':
        email = email.lower()
        print(email)
    elif line.split()[0] == 'GetDomain':
        num = int(line.split(' ')[1])
        print(email[-num:])
    elif line == 'GetUsername':
        if '@' not in email:
            print(f'The email {email} doesn\'t contain the @ symbol.')
            line = input()
            continue
        else:
            print(email.split('@')[0])
    elif line.split()[0] == 'Replace':
        char = line.split()[1]
        print(email.replace(char, '-'))
    elif line == 'Encrypt':
        for ch in email:
            print(ord(ch), end=' ')
    line = input()