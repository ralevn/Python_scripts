""" Да се напише програма, която чете две цели числа n и l, въведени от потребителя, и генерира по азбучен ред
всички възможни пароли, които се състоят от следните 5 символа:
 Символ 1: цифра от 1 до n;
 Символ 2: цифра от 1 до n;
 Символ 3: малка буква измежду първите l букви на латинската азбука;
 Символ 4: малка буква измежду първите l букви на латинската азбука;
 Символ 5: цифра от 1 до n, по-голяма от първите 2 цифри. """

n, l = int(input()), int(input())
max_letter = 97 + l

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(97, max_letter):
            for m in range(97, max_letter):
                for p in range(1, n + 1):
                    if p > i and p > j:
                        print(f'{i}{j}{chr(k)}{chr(m)}{p}', end=' ')