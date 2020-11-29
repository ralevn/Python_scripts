import re

def calc_emoji(text):
    new_tex = text.strip(text[0])
    s = 0
    for ch in new_tex:
        s += ord(ch)
    return s

string = input()

pattern_emoji = r'.?(::|\*\*)[A-Z][a-z]{2,}\1'
raw_emojis = {}
for item in string.split():
    if re.match(pattern_emoji, item):
        emoji = re.match(pattern_emoji, item).group()
        raw_emojis[emoji] = calc_emoji(emoji)

digits = [int(ch) for ch in string if ord(ch) >= 48 and ord(ch) <= 57]

threshold = 1
for item in digits:
    threshold *= item

print(f'Cool threshold: {threshold}')
print(f'{len(raw_emojis)} emojis found in the text. The cool ones are:')

# print(raw_emojis)

for item, value in raw_emojis.items():
    if value > threshold:
        print(item)