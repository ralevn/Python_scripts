num_tables, l_tables, w_tables = int(input()), float(input()), float(input())

area_covers = (l_tables + 0.60) * (w_tables + 0.60)
area_carr = (l_tables / 2) **2

cost_covers = area_covers * 7
cost_carr = area_carr * 9

price_usd = (cost_covers + cost_carr) * num_tables

print (f'%.2f USD\n%.2f BGN' %(price_usd, price_usd *1.85))