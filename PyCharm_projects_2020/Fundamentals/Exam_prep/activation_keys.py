activation_key = input()
raw_key = activation_key

line = input()
while line != 'Generate':
    if line.split('>>>')[0] == 'Contains':
        substr = line.split('>>>')[1]
        if substr in activation_key:
            print(f'{activation_key} contains {substr}')
        else:
            print('Substring not found!')
    elif line.split('>>>')[0] == 'Flip':
        up_low = line.split('>>>')[1]
        start_ix = int(line.split('>>>')[2])
        end_ix = int(line.split('>>>')[3])
        if (0 <= start_ix <= end_ix) and (start_ix <= end_ix <= len(activation_key)):
            old_substr = activation_key[start_ix:end_ix]
            new_substr = old_substr
            if up_low == 'Upper':
                new_substr = old_substr.upper()
            elif up_low == 'Lower':
                new_substr = old_substr.lower()
            activation_key = activation_key.replace(old_substr, new_substr)
        print(activation_key)
    elif line.split('>>>')[0] == 'Slice':
        start_ix = int(line.split('>>>')[1])
        end_ix = int(line.split('>>>')[2])
        if (0 <= start_ix <= end_ix) and (start_ix <= end_ix <= len(activation_key)):
            substr = activation_key[start_ix:end_ix]
            activation_key = activation_key.replace(substr, '')
        print(activation_key)
    line = input()

print(f'Your activation key is: {activation_key}')