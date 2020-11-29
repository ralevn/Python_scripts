import re

text_string = input()
pattern = r'(#|@)(?P<word1>[A-Za-z]{3,})\1\1(?P<word2>[A-Za-z]{3,})\1'


words = []
for m in re.finditer(pattern, text_string):
    words.append((m.group('word1'), m.group('word2')))
if len(words) == 0:
    print('No word pairs found!')
else:
    print(f'{len(words)} word pairs found!')


pairs = {}
for items in words:
    if items[1][::-1] == items[0]:
        pairs[items[0]] = items[1]

if len(pairs) == 0:
    print('No mirror words!')
else:
    l_text = []
    for key, value in pairs.items():
        element = f'{key} <=> {value}'
        l_text.append(element)
    print('The mirror words are:')
    text = ', '.join(l_text)
    print(text)