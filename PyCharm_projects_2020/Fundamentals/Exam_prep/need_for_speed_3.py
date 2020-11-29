number_of_cars = int(input())

cars = {}
for _ in range(number_of_cars):
    line = input()
    car = line.split('|')[0]
    mileage = int(line.split('|')[1])
    fuel = int(line.split('|')[2])
    cars[car] = [mileage, fuel]

command = input()
while command != 'Stop':
    if command.split(' : ')[0] == 'Drive':
        car = command.split(' : ')[1]
        distance = int(command.split(' : ')[2])
        fuel = int(command.split(' : ')[3])
        if fuel > cars[car][1]:
            print("Not enough fuel to make that ride")
        else:
            cars[car][0] += distance
            cars[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        if cars[car][0] >= 100000:
            print(f"Time to sell the {car}!")
            cars.pop(car)

    if command.split(' : ')[0] == 'Refuel':
        car = command.split(' : ')[1]
        fuel = int(command.split(' : ')[2])
        if fuel + cars[car][1] > 75:
            amount = 75 - cars[car][1]
        else:
            amount = fuel
        cars[car][1] += amount
        print(f"{car} refueled with {amount} liters")

    if command.split(' : ')[0] == 'Revert':
        car = command.split(' : ')[1]
        kilometers = int(command.split(' : ')[2])
        if cars[car][0] - kilometers < 10000:
            cars[car][0] = 10000
        else:
            cars[car][0] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

    command = input()

ordered_cars = sorted(cars.items(), key=lambda s: (-s[1][0], s[0]))
for car, values in ordered_cars:
    print(f'{car} -> Mileage: {values[0]} kms, Fuel in the tank: {values[1]} lt.')
