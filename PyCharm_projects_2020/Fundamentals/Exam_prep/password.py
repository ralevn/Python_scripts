from re import match
n = int(input())

password_patter = r'^(.+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1$'

for _ in range(n):
    password = input()
    matched = match(password_patter, password)
    if matched is not None:
        encrypted_password = ''
        for i in range(2, 6):
            encrypted_password += matched.group(i)
        print(f'Password: {encrypted_password}')
    else:
        print('Try another password!')