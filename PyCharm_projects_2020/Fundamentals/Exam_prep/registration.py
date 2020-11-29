import re

num = int(input())
user_pattern = r'U\$([A-Z][a-z]{2,})U\$'
password_pattern = r'P@\$([a-zA-Z]{5,}\d+)P@\$'
success = 0

for i in range(num):
    registration = input()
    user = re.findall(user_pattern, registration)
    password = re.findall(password_pattern, registration)
    if len(user) > 0 and len(password) > 0:
        print("Registration was successful")
        print(f'Username: {user[0]}, Password: {password[0]}')
        success += 1
    else:
        print('Invalid username or password')

print(f'Successful registrations: {success}')