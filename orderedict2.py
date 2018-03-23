# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections
import itertools
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

def count_items(groups):
    return (len(i) for i in groups)

sales = get_items(N)

for i,j in collections.Counter(sales).items():
    print i[0], i[1]*j