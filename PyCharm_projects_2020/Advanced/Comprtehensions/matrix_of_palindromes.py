rows, cols = (int(n) for n in input().split())

matrix = [[f'{chr(97 + r)}{chr(97 + r + c)}{chr(97 + r)}' for c in range(cols)] for r in range(rows)]
[print(' '.join(row)) for row in matrix]
