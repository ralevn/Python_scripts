bands = {}
played = {}

line = input()
while line != 'start of concert':
    if line.split('; ')[0] == 'Add':
        name = line.split('; ')[1]
        members = line.split('; ')[2].split(', ')
        if name not in bands:
            bands[name] = members
        else:
            for m in members:
                if m not in bands[name]:
                    bands[name].append(m)
    elif line.split('; ')[0] == 'Play':
        name = line.split('; ')[1]
        time = int(line.split('; ')[2])
        if name not in played:
            played[name] = time
        else:
            played[name] += time
        if name not in bands:
            bands[name] = []
    line = input()

ordered_played = sorted(played.items(), key=lambda s: (-s[1], s[0]))
total_time = 0
for t in played.values():
    total_time += t
print(f'Total time: {total_time}')
for n, t in ordered_played:
    print(f'{n} -> {t}')

band_name = input()
print(band_name)
for n in bands[band_name]:
    print(f'=> {n}')