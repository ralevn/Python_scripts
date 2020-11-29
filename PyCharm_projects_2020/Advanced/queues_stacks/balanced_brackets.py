def check_brackets(list_brackets):
    answer = True
    opening_brackets = []
    for br in list_brackets:
        if br == '{' or br == '(' or br == '[':
            opening_brackets.append(br)
        elif br == '}':
            if opening_brackets.pop() == '{':
                continue
            else:
                answer = False
                break
        elif br == ')':
            if opening_brackets.pop() == '(':
                continue
            else:
                answer = False
                break
        elif br == ']':
            if opening_brackets.pop() == '[':
                continue
            else:
                answer = False
                break
    return answer


brackets = list(input())

if len(brackets) % 2 != 0:
    print('NO')
    exit()

if check_brackets(brackets):
    print('YES')
else:
    print('NO')