def exchange (ind, lis):
    if ind > len(lis) - 1 or ind < 0:
        print('Invalid index')
    else:
        return [v for i, v in enumerate(lis) if i > ind] + [v for i, v in enumerate(lis) if i <= ind]

def max_min_even_odd (cmd, ev_od, lis):
    if cmd == 'max' and ev_od == 'even':
        if len([n for n in lis if n % 2 == 0]) == 0:
            print('No matches')
        else:
            max_even = max([n for n in lis if n % 2 == 0])
            max_even_index = max([i for i, v in enumerate(lis) if v == max_even])
            return max_even_index
    elif cmd == 'min' and ev_od == 'even':
        if len([n for n in lis if n % 2 == 0]) == 0:
            print('No matches')
        else:
            min_even = min([n for n in lis if n % 2 == 0])
            min_even_index = max([i for i, v in enumerate(lis) if v == min_even])
            return min_even_index
    elif cmd == 'max' and ev_od == 'odd':
        if len([n for n in lis if n % 2 != 0]) == 0:
            print('No matches')
        else:
            max_odd = max([n for n in lis if n % 2 != 0])
            max_odd_index = max([i for i, v in enumerate(lis) if v == max_odd])
            return max_odd_index
    elif cmd == 'min' and ev_od == 'odd':
        if len([n for n in lis if n % 2 != 0]) == 0:
            print('No matches')
        else:
            min_odd = min([n for n in lis if n % 2 != 0])
            min_odd_index = max([i for i, v in enumerate(lis) if v == min_odd])
            return min_odd_index

def first_last_even_odd (cmd, cnt, ev_od, lis):
    count = int(cnt)
    if count > len(lis) :
        print('Invalid count')
    elif cmd == 'first' and ev_od == 'even':
        return [n for n in lis if n % 2 == 0][:count]
    elif cmd == 'first' and ev_od == 'odd':
        return [n for n in lis if n % 2 != 0][:count]
    elif cmd == 'last' and ev_od == 'even':
        return [n for n in lis if n % 2 == 0][-count:]
    elif cmd == 'last' and ev_od == 'odd':
        return [n for n in lis if n % 2 != 0][-count:]


listi = [int(n) for n in input().split(' ')]
command_li = [word for word in input().split(' ')]

while command_li[0] != 'end':
    if command_li[0] == 'exchange':
        if exchange(int(command_li[1]), listi) is not None:
            listi = exchange(int(command_li[1]), listi)
    elif command_li[0] == 'max' or command_li[0] == 'min':
        if max_min_even_odd(command_li[0], command_li[1], listi) is not None:
            print(max_min_even_odd(command_li[0], command_li[1], listi))
    elif command_li[0] == 'first' or command_li[0] == 'last':
        if first_last_even_odd(command_li[0], command_li[1], command_li[2], listi) is not None:
            print(first_last_even_odd(command_li[0], command_li[1], command_li[2], listi))
    command_li = [word for word in input().split(' ')]

print(listi)