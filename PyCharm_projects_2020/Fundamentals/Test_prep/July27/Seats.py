num = int(input())
seat = ''

for i in range(num):
    ticket =input()
    if len(ticket) == 4:
        if  65 <= ord(ticket[0]) <= 90:
            seat = ticket[0] + ticket[1] + ticket [2]
            print(f'Seat decoded: {seat}')
        else:
            seat = ticket[3] + ticket[1] + ticket [2]
            print(f'Seat decoded: {seat}')
    else:
        seat = ticket[0] + str(ord(ticket[1]))
        print(f'Seat decoded: {seat}')
