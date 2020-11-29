square_side = float(input())
tile_w, tile_l = float(input()), float(input())
bench_w, bench_l = float(input()), float(input())

work_area = ( square_side ** 2) - (bench_w * bench_l)
tile_num = work_area / (tile_l * tile_w)
work_time = tile_num * 0.2

print(f'{tile_num}\n {work_time}')

