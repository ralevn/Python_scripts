class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(self.name, other.surname)

    def __repr__(self):
        return f'{self.name} {self.surname}'


class Group:
    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        people_sum = self.people + other.people
        new_name = f'{self.name}+{other.name}'
        return Group(new_name, people_sum)

    def __getitem__(self, item):
        return self.people[item]

    def __str__(self):
        text = f'Group {self.name} with members {", ".join(str(p) for p in self.people)}'

    def __repr__(self):
        return self.people

p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group


print(p0, p1, p2, p3, p4, sep="\n")
print("=" * 10)
print(len(first_group))
print(second_group)
print(third_group[0])
for person in third_group:
    print(person)