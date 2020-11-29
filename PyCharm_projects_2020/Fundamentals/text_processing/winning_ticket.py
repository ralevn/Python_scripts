import re

def check_validity(text):
    is_valid = True
    if len(text) < 20:
        is_valid = False
    return is_valid

def check_match(text):
    is_match = False
    text1 = text[:len(text) // 2]
    text2 = text[len(text) // 2:]
    pattern = r'\${6,}|\^{6,}|\@{6,}|\#{6,}'
    match1 = re.findall(pattern, text1)
    match2 = re.findall(pattern, text2)
    if len(''.join(match1)) >= 6 and len(''.join(match2)) >= 6:
        is_match = True
    return is_match


def count_win(text1, text2):
    max = n1 = n2 = 0
    c = c1 = c2 = ''
    for ch in ['$', '^', '@', '#']:
        if text1.count(ch) >= 6:
            n1 = text1.count(ch)
            c1 = ch
        if text2.count(ch) >= 6:
            n2 = text2.count(ch)
            c2 = ch
    if n1 >= n2:
        max = n1
        c = c1
    else:
        max = n2
        c = c2
    return max, c

collection = input().split(', ')

for ticket in collection:
    if not check_validity(ticket):
        print('invalid ticket')
        continue
    elif not check_match(ticket):
        print(f'ticket {ticket} - no match')
        continue
    elif check_match(ticket):
        part1 = ticket[:len(ticket) // 2]
        part2 = ticket[len(ticket) // 2:]
        if count_win(part1, part2)[0] < 10:
            print(f'ticket "{ticket}" - {count_win(part1, part2)[0]}{count_win(part1, part2)[1]}')
        else:
            print(f'ticket "{ticket}" - {count_win(part1, part2)[0]}{count_win(part1, part2)[1]} Jackpot!')
