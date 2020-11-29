pr_whisky, q_beer, q_wine, q_rakia, q_whiskey = float(input()), float(input()), float(input()), float(input()), float(input())

pr_rakia = pr_whisky / 2
pr_wine = pr_rakia * 0.60
pr_beer = pr_rakia * 0.20

total_sum = pr_whisky * q_whiskey + pr_rakia * q_rakia + pr_beer * q_beer + pr_wine * q_wine

print (f"%.2f" %(total_sum))

