year = int(input()) + 1

# A set is an unordered collection with no duplicate elements.

while True:
    if len(set(str(year))) == len(str(year)):
        print(year)
        break
    else:
        year += 1

