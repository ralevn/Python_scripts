import re

line =input()

text = []
pattern = r"\d+"

while True:
    if line:
        text.append(line)
        line = input()
    else:
        break

text = ' '.join(text)
matches = re.findall(pattern, text)
print(' '.join(matches), end=' ')

