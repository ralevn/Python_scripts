names = input().split(', ')

# [print(f'{name} -> {len(name)}') for name in names]
# output = [(f'{name} -> {len(name)}') for name in names]

print(', '.join([f'{name} -> {len(name)}' for name in names]))