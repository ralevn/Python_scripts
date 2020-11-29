cards = input().split(' ')
shuff_number = int(input())

def shuffel(ilist):
    half = len(ilist) // 2
    tmp_list = []
    for i in range(half):
        tmp_list.append(ilist[i])
        tmp_list.append(ilist[i + half])
    return tmp_list

for _ in range(shuff_number):
    cards = shuffel(cards)

print(cards)