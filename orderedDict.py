import collections

N = int(raw_input())

def get_items(N):
    name = []
    price = []

    for i in xrange(N):
        tmp =raw_input().split()
        price.append(int(' '.join(tmp[-1:])))
        name.append(' '.join(tmp[:-1]))
    item=zip(name,price)
    return item

sales = get_items(N)

for i in sales:
    print i

total_sales = collections.OrderedDict()
for n,p in sales:
    total_sales[n] = p
    print total_sales



