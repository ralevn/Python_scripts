concealed_message = input()

line = input()
while line != 'Reveal':
    if line.split(':|:')[0] == 'InsertSpace':
        ix = int(line.split(':|:')[1])
        concealed_message_list = list(concealed_message)
        concealed_message_list.insert(ix, ' ')
        concealed_message = ''.join(concealed_message_list)
        print(concealed_message)
    elif line.split(':|:')[0] == 'Reverse':
        substring = line.split(':|:')[1]
        if substring in concealed_message:
            substring_rev = substring[::-1]
            concealed_message = concealed_message.replace(substring, '', 1)
            concealed_message = concealed_message + substring_rev
            print(concealed_message)
        else:
            print('error')
    elif line.split(':|:')[0] == 'ChangeAll':
        substring = line.split(':|:')[1]
        replacement = line.split(':|:')[2]
        concealed_message = concealed_message.replace(substring, replacement)
        print(concealed_message)
    line = input()

print(f'You have a new text message: {concealed_message}')