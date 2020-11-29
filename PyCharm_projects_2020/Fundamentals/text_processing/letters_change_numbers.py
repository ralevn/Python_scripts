def process_string(text):
    operation1 = 0
    operation2 = 0
    letter1 = text[0]
    letter2 = text[len(text) - 1]
    number = int(text[1:len(text) - 1])
    if 97 <= ord(letter1) <= 122:
        operation1 = number * small_alph[letter1]
    elif 65 <= ord(letter1) <= 90:
        operation1 = number / cap_alph[letter1]
    if 97 <= ord(letter2) <= 122:
        operation2 = operation1 + small_alph[letter2]
    elif 65 <= ord(letter2) <= 90:
        operation2 = operation1 - cap_alph[letter2]
    return operation2

small_alph = dict(enumerate('abcdefghijklmnopqrstuvwxyz', 1))
small_alph = dict((v,k) for k,v in small_alph.items())
cap_alph = dict(enumerate('abcdefghijklmnopqrstuvwxyz'.upper(), 1))
cap_alph = dict((v,k) for k,v in cap_alph.items())

strings = input().split()
res = 0
for st in strings:
    res += process_string(st)
print(f'{res:.2f}')