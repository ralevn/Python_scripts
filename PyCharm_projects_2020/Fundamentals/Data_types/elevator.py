persons = int(input())
elevator_capacity = int(input())

courses = int(persons / elevator_capacity)
left_persons = persons % elevator_capacity

if left_persons == 0:
    print(courses)
else:
    print(courses + 1)