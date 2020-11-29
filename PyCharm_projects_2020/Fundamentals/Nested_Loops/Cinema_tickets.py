students_tickets = 0
standard_tickets = 0
kid_ticket = 0

while True:
    Film_title = input()
    if Film_title == 'Finish':
       break
    free_seats = int(input())
    ticket_count = 0
    for i in range(free_seats):
        ticket_type = input()
        if ticket_type == 'student': students_tickets += 1
        elif ticket_type == 'standard': standard_tickets += 1
        elif ticket_type == 'kid': kid_ticket += 1
        elif ticket_type == 'End' or ticket_type == 'Finish':
            break
        ticket_count += 1
    full = (ticket_count / free_seats) * 100
    print(f'{Film_title} - {full:.2f}% full.')

total_tickets = students_tickets + standard_tickets + kid_ticket

print(f'Total tickets: {total_tickets}')
print(f'{(students_tickets/total_tickets) * 100:.2f}% student tickets.')
print(f'{(standard_tickets / total_tickets) * 100:.2f}% standard tickets.')
print(f'{(kid_ticket / total_tickets) * 100:.2f}% kids tickets.')