reservation_day  = int(input())
reservation_month  = int(input())
accomodation_day = int(input())
accomodation_month = int(input())
leave_day = int(input())
leave_month = int(input())

price = 30.00
vacation_len = leave_day - accomodation_day


if accomodation_month > reservation_month:
    price = 25 * 0.8

# print(vacation_len, price)
print('Your stay from {0}/{1} to {2}/{3} will cost {4:.2f}'.format(accomodation_day, accomodation_month, leave_day, leave_month, (price * vacation_len)))