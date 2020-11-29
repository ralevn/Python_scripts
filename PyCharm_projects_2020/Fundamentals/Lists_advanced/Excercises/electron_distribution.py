def electrons_in_shell (n):
    return 2 * (n ** 2)


number_of_electrons = int(input())
result = []
shell = 1

while number_of_electrons >= electrons_in_shell(shell):
    if number_of_electrons - electrons_in_shell(shell) >= 0:
        result.append(electrons_in_shell(shell))
    number_of_electrons -= electrons_in_shell(shell)
    shell += 1

if number_of_electrons > 0:
    result.append(number_of_electrons)

print(result)