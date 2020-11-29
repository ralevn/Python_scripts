lists = [x.split() for x in input().split('|')[::-1]]

flattened = [num for sublist in lists for num in sublist]
print(' '.join(flattened))