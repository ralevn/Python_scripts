import re

def decrypt(key, text):
    t_list = list(text)
    decrypted_list = []
    decrypted_text = ''
    for ch in t_list:
        decrypted_list.append(chr(ord(ch)+key))
        decrypted_text = ''.join(decrypted_list)
    return decrypted_text

pattern = r'^([#$%\*&])([a-zA-Z]+)\1=(\d+)!!(.+)$'

while True:
    line = input()
    a_match = re.match(pattern, line)
    if a_match is None:
        print(f'Nothing found!')
    else:
        name = a_match.group(2)
        number = int(a_match.group(3))
        geohashcode = a_match.group(4)
        if len(geohashcode) != number:
            print(f'Nothing found!')
        else:
            print(f'Coordinates found! {name} -> {decrypt(number, geohashcode)}')
            exit()