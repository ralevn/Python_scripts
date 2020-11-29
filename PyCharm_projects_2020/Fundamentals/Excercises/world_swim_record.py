WR = float(input())
distance = float(input())
ivan_speed = float(input())

time_ideal = ivan_speed * distance
time_add = int(distance / 15) * 12.5
ivan_time = time_add + time_ideal
## print (time_ideal, time_add, ivan_time)

if ivan_time >= WR:
    print(f'No, he failed! He was {ivan_time - WR:.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.')