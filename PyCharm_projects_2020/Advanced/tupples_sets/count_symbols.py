text = input()

chars = {}

for ch in text:
    if ch not in chars:
        chars[ch] = 1
    else:
        chars[ch] += 1

sorted_ch = dict(sorted(chars.items(), key=lambda i: (i[0])))

for ch, num in sorted_ch.items():
    print(f'{ch}: {num} time/s')