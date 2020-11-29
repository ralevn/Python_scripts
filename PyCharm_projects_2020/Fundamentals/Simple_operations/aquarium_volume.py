l_aquarium, w_aqarium, h_aquarium = float(input()), float(input()), float(input())
v_other = float(input())
water_litters = (l_aquarium * w_aqarium * h_aquarium) * 0.001 * ( 1 - v_other * 0.01 )

print(f"%.3f" %(water_litters))

# print ((l_aquarium * w_aqarium * h_aquarium) * 0.001 * ( 1 - v_other * 0.01 ))