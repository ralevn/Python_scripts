def version_to_number(vers):
    return int(''.join(vers.split('.')))


def number_to_version(n):
    return '.'.join([ch for ch in str(n)])


version = input()

number = version_to_number(version)
new_version = number_to_version(number + 1)

print(new_version)
