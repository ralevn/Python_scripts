L, W, A = float(input()), float(input()), float(input())

hall_area = (L * 100) * (W * 100)
wardrobe_area = (A * 100) ** 2
bench_area = hall_area / 10

dancers = (hall_area - wardrobe_area - bench_area) / 7040

print (int(dancers))