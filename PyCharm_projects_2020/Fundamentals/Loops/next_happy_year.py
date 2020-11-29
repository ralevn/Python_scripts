year = int(input())

def check_year(text):
    is_found = True
    for i in range(0, len(text)):
        for j in range(i + 1, len(text) ):
            if text[i] == text[j]:
                is_found = False
                break
    return is_found

is_happy = False

while is_happy == False:
    year += 1
    is_happy = check_year(str(year))

print(year)