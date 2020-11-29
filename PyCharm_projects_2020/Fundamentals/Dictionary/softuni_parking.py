n = int(input())
users = {}

for _ in range(n):
    entry = input().split()
    operation = entry[0]
    name = entry[1]

    if operation == 'register':
        license = entry[2]
        if name not in users:
            users[name] = license
            print(f'{name} registered {users[name]} successfully')
        else:
            print(f'ERROR: already registered with plate number {users[name]}')

    if operation == 'unregister':
        if name not in users:
            print(f'ERROR: user {name} not found')
        else:
            users.pop(name)
            print(f'{name} unregistered successfully')

for u in users:
    print(f'{u} => {users[u]}')