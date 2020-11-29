char_nums = int(input())

sum = 0

for i in range(char_nums):
    ch = input()
    sum += ord(ch)

print(f'The sum equals: {sum}')

