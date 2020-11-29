passenger_number = int(input())
bus_stop_num = int(input())

for i in range(1, bus_stop_num + 1):
    dismount_passengers = int(input())
    mount_passagengers = int(input())
    if i % 2 != 0:
        mount_passagengers += 2
    else:
        dismount_passengers += 2
    passenger_number += (mount_passagengers - dismount_passengers)

print(f'The final number of passengers is : {passenger_number}')
