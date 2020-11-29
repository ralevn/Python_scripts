from math import ceil


def calc_bonus(att, lectures, bonus):
    bonus = ceil(att / lectures * (5 + bonus))
    return bonus


num_students = int(input())
count_lectures = int(input())
additional_bonus = int(input())
i = 0
students = []
while i <= num_students - 1:
    n = int(input())
    students.append(n)
    i += 1

bonus = []
max_bonus = 0
max_student = 0

for i in students:
    b = calc_bonus(i, count_lectures, additional_bonus)
    bonus.append(b)
    if max(bonus) == b:
        max_student = i
        max_bonus = b

print(f'Max Bonus: {max_bonus}.')
print(f'The student has attended {max_student} lectures.')

