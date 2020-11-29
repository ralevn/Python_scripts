ticket_num = ''
counter = 0

min_wait = 0
min_ticket = ''
min_price = 0

while ticket_num != 'End':
    ticket_num = input()
    if ticket_num != 'End':
        price = float(input())
        wait_min = int(input())
    if counter == 0:
        min_wait = wait_min
        min_ticket = ticket_num
        min_price = price
    else:
        if wait_min < min_wait:
            min_wait = wait_min
            min_ticket = ticket_num
            min_price = price
    counter += 1

hh = min_wait // 60
mm = min_wait % 60
price_lv = min_price * 1.96

print (f'Ticket found for flight {min_ticket} costs {price_lv:.2f} leva with {hh}h {mm}m stay')


