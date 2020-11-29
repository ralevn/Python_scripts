numbers = [int(n) for n in input().split(', ')]

classified = {'Positive': [n for n in numbers if n >= 0],
              'Negative': [n for n in numbers if n < 0],
              'Even': [n for n in numbers if n % 2 == 0],
              'Odd': [n for n in numbers if n % 2 != 0]}

for key, value in classified.items():
    print(f"{key}: {', '.join(str(n) for n in value)}")