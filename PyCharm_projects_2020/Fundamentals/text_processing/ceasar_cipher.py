text = input()

encrypted_list = []
for i in range(len(text)):
    encrypted_list.append(chr(ord(text[i]) + 3))

encrypted_text = ''.join(encrypted_list)
print(encrypted_text)