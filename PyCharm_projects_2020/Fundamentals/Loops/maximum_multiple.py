divisor = int(input())
bound = int(input())

## понеже търсим мах. въртим от горе на долу

for i in range(bound, divisor , -1):
    if i % divisor == 0:
        print(i)
        break

