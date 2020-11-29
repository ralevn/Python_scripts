last_sector = input()
rows_A = int(input())
odd_row_seats = int(input())

even_row_seats = odd_row_seats + 2
last_sector_ascii = ord(last_sector)
sec_num = 0
seat_num = 0

for sec in range(65, last_sector_ascii + 1):
    for row in range(1, rows_A + 1 + sec_num):
        if row % 2 != 0:
            for seat in range(97, 97 + odd_row_seats):
                print(f'{chr(sec)}{row}{chr(seat)}')
                seat_num += 1
        elif row % 2 == 0:
            for seat in range(97, 97 + even_row_seats):
                print(f'{chr(sec)}{row}{chr(seat)}')
                seat_num += 1
    sec_num += 1

print(seat_num)

