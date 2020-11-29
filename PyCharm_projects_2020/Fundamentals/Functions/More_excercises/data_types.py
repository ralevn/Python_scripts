def make_int(val):
    return int(val) * 2

def make_real(val):
    return f'{float(val) * 1.5:.2f}'

def make_string(val):
    return f'${str(val)}$'

typ = input()
val = input()

if typ == 'int':
    print(make_int(val))
elif typ == 'real':
    print(make_real(val))
else:
    print(make_string(val))