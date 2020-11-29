def get_stock(raw):
    data = raw.split(' ')
    dict = {}
    for i in range(0, len(data), 2):
        key = data[i]
        value = int(data[i + 1])
        dict[key] = value
    return dict


stock = get_stock(input())
searched_products = input().split(' ')

for i in searched_products:
    if i not in stock or stock[i] == 0:
        print(f'Sorry, we don\'t have {i}')
    else:
        print(f'We have {stock[i]} of {i} left')