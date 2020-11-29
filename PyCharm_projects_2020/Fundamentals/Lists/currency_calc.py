sum = float(input('Sum: '))
inp_currency = input('Input Currency: ')

#Test if Currency in BGN, USD, GBP, EUR
while inp_currency not in ['BGN', 'USD', 'GBP', 'EUR']:
    inp_currency = input('Input Currency: ')

if inp_currency == 'BGN': inp_rate = 1
elif inp_currency == 'USD': inp_rate = 1.79549
elif inp_currency == 'EUR': inp_rate = 1.95583
else: inp_rate = 2.53405

out_currency = input('Output Currency: ')
#Test if Currency in BGN, USD, GBP, EUR
while out_currency not in ['BGN', 'USD', 'GBP', 'EUR']:
    out_currency = input('Output Currency: ')

if out_currency == 'BGN': out_rate = 1
elif out_currency == 'USD': out_rate = 1.79549
elif out_currency == 'EUR': out_rate = 1.95583
else: out_rate = 2.53405

def converter (i, o, q):
    return ((i / o) * q )

print (round (converter(inp_rate, out_rate, sum), 2))