work_days_in_month = int(input())
day_rate = float(input())
dollar_lv = float(input())

month_earnings = work_days_in_month * day_rate
year_earnings = month_earnings * 12 + month_earnings * 2.5
after_tax = year_earnings * 0.75

per_diem = (after_tax * dollar_lv) / 365

print(f'%.2f' %(per_diem))

