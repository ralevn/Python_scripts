def decipher(word):
    ch_li = [i for i in word if 48 <= ord(i) <= 57]
    ch_1 = chr(int(''.join(ch_li)))
    new_word = [ch for ch in word if 48 > ord(ch) or ord(ch) > 57]
    new_word.insert(0, ch_1)
    new_word[1], new_word[-1] = new_word[-1], new_word[1]
    return new_word


text_list = input().split(' ')

for i in text_list:
    print(''.join(decipher(i)), end=' ')