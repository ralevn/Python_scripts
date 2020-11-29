# import re

# pattern_1 = r'\d+'
# pattern_2 = r'([A-Za-z ]+)([\-|\s| ]*)([\d|/|-|\+]+)'
contacts = {}
contact = input().split('-')
while len(contact) == 2:
    name = contact[0]
    number = contact[1]
    contacts[name] = number
    contact = input().split('-')

n = int(contact[0])

for _ in range(n):
    search_name = input()
    if search_name in contacts:
        print(f'{search_name} -> {contacts[search_name]}')
    else:
        print(f'Contact {search_name} does not exist.')