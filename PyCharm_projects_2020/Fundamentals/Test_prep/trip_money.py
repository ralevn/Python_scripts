bitcoin_n, chin_ioan, commission = float(input()), float(input()), float(input())

bitcoin_rate_lv = 1168
chin_ioan_rate_usd = 0.15
lv_dollar = 1.76
lv_eur = 1.95

ch_i_lv = (chin_ioan_rate_usd * chin_ioan) * lv_dollar
#print(ch_i_lv)

bitcoin_i_lv = bitcoin_n * bitcoin_rate_lv
#print(bitcoin_i_lv)

commission_perc = commission /100

sum_lv = ch_i_lv + bitcoin_i_lv
sum_eur = sum_lv / lv_eur
sum_received = sum_eur - (sum_eur * commission_perc)
print(f'%.2f' %(sum_received))
