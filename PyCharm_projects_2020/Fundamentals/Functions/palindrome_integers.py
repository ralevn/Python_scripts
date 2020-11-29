def is_palindrome (n):
    n_list = [int(n) for n in str(n)]
    checks = []
    for i in range(len(n_list) // 2):
        if n_list[i] == n_list[-(i + 1)]:
            checks.append(1)
        else:
            checks.append(0)
    if checks.count(1) == len(checks):
        return True
    else:
        return False

numbers = [int(n) for n in input().split(', ')]

for i in numbers:
    print(is_palindrome(i))
