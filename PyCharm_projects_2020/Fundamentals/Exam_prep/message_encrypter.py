import re

numb = int(input())
pattern = r'(\*|@)([A-Z][a-z]{2,})\1: \[([A-Za-z])\]\|\[([A-Za-z])\]\|\[([A-Za-z])\]\|$'

for _ in range(numb):
    message = input()
    a_match = re.search(pattern, message)
    if a_match is not None:
        tag = a_match.group(2)
        n1 = a_match.group(3)
        n2 = a_match.group(4)
        n3 = a_match.group(5)
        print(f'{tag}: {ord(n1)} {ord(n2)} {ord(n3)}')
    else:
        print('Valid message not found!')

