from datetime import date, datetime

i_date = datetime.strptime(input(),'%Y-%m-%d')

t_date = datetime.today()

if i_date < t_date: print(f'{(t_date -i_date).days} days passed')
else: print (f'{(i_date -t_date).days} days left')

