number = float(input())
output = number * 2.54
print(output)
print (round(output,2))
print (f'%.3f' % output)
print (f'{output:.4f}')
# multiple placeholders

print (f'%.5f  and number is: %.2f' %(output, number))