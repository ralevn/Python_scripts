followers = {}

line = input()
while line != 'Log out':
    if line.split(':')[0] == 'New follower':
        user = line.split(':')[1]
        if user not in followers:
            followers[user] = [0, 0]
    elif line.split(':')[0] == 'Like':
        user = line.split(':')[1]
        cnt = int(line.split(':')[2])
        if user not in followers:
            followers[user] = [cnt, 0]
        else:
            followers[user][0] += cnt
    elif line.split(':')[0] == 'Comment':
        user = line.split(':')[1]
        if user not in followers:
            followers[user] = [0, 1]
        else:
            followers[user][1] += 1
    elif line.split(':')[0] == 'Blocked':
        user = line.split(':')[1]
        if user not in followers:
            print(f'{user} doesn\'t exist.')
        else:
            followers.pop(user)
    line = input()

ordered_followers = sorted(followers.items(), key=lambda s: (-s[1][0], s[0]))

print(f'{len(followers)} followers')
for u, l in ordered_followers:
    print(f'{u}: {l[0] + l[1]}')
