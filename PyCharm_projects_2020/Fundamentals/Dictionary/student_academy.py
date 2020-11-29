students = {}
graduated_students = {}

n = int(input())

tmp_list = []
for _ in range(n * 2):
    tmp_list.append(input())
for i in range(0, len(tmp_list), 2):
    name = tmp_list[i]
    grade = float(tmp_list[i + 1])
    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)

for st in students:
    if sum(students[st]) / len(students[st]) >= 4.5:
        graduated_students[st] = sum(students[st]) / len(students[st])

graduated_students = sorted(graduated_students.items(), key=lambda i: -i[1])

for st, gr in graduated_students:
    print(f'{st} -> {gr:.2f}')
