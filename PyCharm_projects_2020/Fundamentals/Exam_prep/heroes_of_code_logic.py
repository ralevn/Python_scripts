def substitute(string, substring, subst):
    while string.count(substring) != 0:
        string = string.replace(substring, subst)
    return string

string = input()

line = input()
while line != 'Done':
    if line.split(' ')[0] == 'TakeOdd':
        string = [string[i] for i in range(len(string)) if i % 2 != 0]
        string = ''.join(string)
        print(string)
    elif line.split(' ')[0] == 'Cut':
        ix_1 = int(line.split(' ')[1])
        length = int(line.split(' ')[2])
        ix_2 = ix_1 + length
        substr = string[ix_1: ix_2]
        string = string.replace(substr, '', 1)
        print(string)
    elif line.split(' ')[0] == 'Substitute':
        substr = line.split(' ')[1]
        newsubstr = line.split(' ')[2]
        if substr in string:
            string = string.replace(substr, newsubstr)
            print(string)
        else:
            print('Nothing to replace!')
    line = input()

print(f'Your password is: {string}')
