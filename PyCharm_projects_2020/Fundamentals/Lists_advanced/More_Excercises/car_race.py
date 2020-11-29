def car_time(lista):
    sum_time = 0
    for item in lista:
        if item != 0:
            sum_time += item
        else:
            sum_time *= 0.8
    return round(sum_time, 2)


times = [float(n) for n in input().split(' ')]

half = (len(times) // 2)
left_car = times[:half]
right_car = times[:half:-1]

winner = ''
winner_time = 0.0

if car_time(left_car) < car_time(right_car):
    winner = 'left'
    winner_time = car_time(left_car)
elif car_time(right_car) < car_time(left_car):
    winner = 'right'
    winner_time = car_time(right_car)

print(f'The winner is {winner} with total time: {winner_time}')