key = int(input())
n = int(input()) # number of lines

li_text = []

for i in range(n):
    ch = input()
    li_text.append(ch)

new_li_text = [chr(ord(ch) + key) for ch in li_text]

print(''.join(new_li_text))