def calc_emoji(text):
    s = 0
    for ch in text:
        s += ord(ch)
    return s


import re
string = input()
pattern_emoji = r'(::|\*\*)([A-Z][a-z]{2,})\1'
digits = [int(ch) for ch in string if 48 <= ord(ch) <= 57]

raw_emojis = re.findall(pattern_emoji, string)
#print(re.match(pattern_emoji, string))
#print(raw_emojis)

emodjis = {}
for item in raw_emojis:
    emodjis[item[1]] = [calc_emoji(item[1]), item[0]]
#print(emodjis)

threshold = 1
for item in digits:
    threshold *= item

print(f'Cool threshold: {threshold}')
print(f'{len(raw_emojis)} emojis found in the text. The cool ones are:')

for item, value in emodjis.items():
    if value[0] > threshold:
        print(f'{value[1]}{item}{value[1]}')
