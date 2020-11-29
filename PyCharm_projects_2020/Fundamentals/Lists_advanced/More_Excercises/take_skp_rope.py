def skip(n, string):
    new_string = string[n:]
    return new_string


def take(n, string):
    new_string = string[:n]
    return new_string


encrypted_string = input()

number_list = [int(ch) for ch in encrypted_string if 48 <= ord(ch) <= 57]
text_ = ''.join([ch for ch in encrypted_string if 48 > ord(ch) or ord(ch) > 57])

decrypted_string = ''

for i in range(len(number_list)):
    if i % 2 == 0:
        decrypted_string += take(number_list[i], text_)
        text_ = skip(number_list[i], text_)
    else:
        text_ = skip(number_list[i], text_)

print(decrypted_string)