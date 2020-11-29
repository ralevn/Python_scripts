collection = {}

line = input()

while line != 'Statistics':
    if line.split('->')[0] == 'Add':
        user = line.split('->')[1]
        if user not in collection:
            collection[user] = []
        else:
            print(f'{user} is already registered')
    elif line.split('->')[0] == 'Send':
        user = line.split('->')[1]
        text = line.split('->')[2]
        collection[user].append(text)
    elif line.split('->')[0] == 'Delete':
        user = line.split('->')[1]
        if user not in collection:
            print(f'{user} not found!')
        else:
            collection.pop(user)
    line = input()

collection = sorted(collection.items(), key=lambda s: (-len(s[1]), s[0]))

print(f'Users count: {len(collection)}')
for user, mails in collection:
    print(user)
    for mail in mails:
        print(f' - {mail}')

