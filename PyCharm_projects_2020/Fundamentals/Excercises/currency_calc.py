sum = float(input())
inp_currency = input()

if inp_currency == 'BGN': inp_rate = 1
elif inp_currency == 'USD': inp_rate = 1.79549
elif inp_currency == 'EUR': inp_rate = 1.95583
else: inp_rate = 2.53405

out_currency = input()

if out_currency == 'BGN': out_rate = 1
elif out_currency == 'USD': out_rate = 1.79549
elif out_currency == 'EUR': out_rate = 1.95583
else: out_rate = 2.53405

def converter (i, o, q):
    return ((i / o) * q )

print (round (converter(inp_rate, out_rate, sum), 2))
