len, width = float(input()), float(input())

rows_num = len // 1.2 ## маса 40см + място 80см
# print(rows_num)

col_num = ((width -1) // 0.7) ## - 1м коридор делено на дължината на масата
# print(col_num)

work_place_n = (col_num * rows_num) -3

print(int(work_place_n))

