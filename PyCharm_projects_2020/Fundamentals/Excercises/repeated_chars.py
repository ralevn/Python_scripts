year = int(input())

def check_year(text):
    for i in range(0, len(text)):
        for j in range(i + 1, len(text) -1 ):
            if text[i] == text[j]:
                return True
            else:
                continue


is_happy = False

while is_happy == False:
    is_happy = check_year(str(year))
    year += 1

print(year)