category_names = input().split(', ')
n = int(input())

category_items = {}

for c in category_names:
    category_items[c] = []
tot_items = 0
tot_quality = 0


for _ in range(n):
    item = input().split(' - ')
    category = item[0]
    item_name = item[1]
    item_qqs = item[2]
    quantity = int(item_qqs.split(';')[0].split(':')[1])
    quality = int(item_qqs.split(';')[1].split(':')[1])
    category_items[category].append(item_name)
    tot_items += quantity
    tot_quality += quality

print(f'Count of items: {tot_items}')
print(f'Average quality: {tot_quality/len(category_names):.2f}')

for c, i in category_items.items():
    print(f'{c} -> {", ".join(i)}')