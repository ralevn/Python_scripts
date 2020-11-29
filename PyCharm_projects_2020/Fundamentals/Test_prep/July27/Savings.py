month_income = float(input())
num_of_months = int(input())
personal_needs = float(input())

saved_money = month_income - ((0.30 * month_income) + personal_needs)

print(f'She can save {(saved_money / month_income) * 100:.2f}%\n{saved_money * num_of_months:.2f}')
