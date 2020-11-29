def caps_encrypt(char, key):
    if ord(char) + key <= 90:
        return chr(ord(char) + key)
    elif ord(char) + key > 90:
        return chr(ord(char) + key - 26)

def small_encrypt(char, key):
    if ord(char) + key <= 122:
        return chr(ord(char) + key)
    elif ord(char) + key > 122:
        return chr(ord(char) + key - 26)


import re
pattern = r'(^[A-Z][a-z \']+):([A-Z ]+)'
caps = [chr(a) for a in range(65, 91)]
smalls = [chr(a) for a in range(97, 123)]

line = input()
while line != 'end':
    a_match = re.match(pattern, line)
    if a_match is not None:
        artist = a_match.group(1)
        song = a_match.group(2)
        key = len(artist)
        a_list = list(line)
        encrypted_list = []
        for ch in a_list:
            if ch in caps:
                encrypted_list.append(caps_encrypt(ch, key))
            elif ch in smalls:
                encrypted_list.append(small_encrypt(ch, key))
            elif ch == ' ':
                encrypted_list.append(' ')
            elif ch == "'":
                encrypted_list.append("'")
            elif ch == ":":
                encrypted_list.append("@")
        encrypted_text = ''.join(encrypted_list)
        print(f'Successful encryption: {encrypted_text}')
    else:
        print('Invalid input!')
    line = input()