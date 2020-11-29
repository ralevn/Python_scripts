import re

num = int(input())
line_pattern = r'!([A-Z][a-z]{2,})!:\[([a-zA-Z]{8,})\]'
compiled_regex = re.compile(line_pattern)


for _ in range(num):
    line = input()
    matches = compiled_regex.match(line)
    if matches:
        command = matches.group(1)
        message = matches.group(2)
        encrypted_message = [ord(ch) for ch in message]
        print(f'{command}:', *encrypted_message)
    else:
        print('The message is invalid')