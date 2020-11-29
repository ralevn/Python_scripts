from math import ceil

width_hall = float(input())
length_hall = float(input())
bar_side = float(input())
dansing = (width_hall * length_hall) * 0.19

free_space = (width_hall * length_hall) - (bar_side ** 2) - dansing

number_of_guests = ceil(free_space / 3.2)

print(number_of_guests)