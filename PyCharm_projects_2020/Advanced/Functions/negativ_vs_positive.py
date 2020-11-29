def seprate(lista):
    listp = [p for p in lista if p >= 0]
    listn = [n for n in lista if n < 0]
    return sum(listn), sum(listp)


def compare(n, p):
    abs_n = abs(n)
    abs_p = abs(p)
    if abs_n > abs_p:
        print('The negatives are stronger than the positives')
    elif abs_p > abs_n:
        print('The positives are stronger than the negatives')


number_list = [int(i) for i in input().split(' ')]

negatives, positives = seprate(number_list)

print(negatives, positives, sep='\n')
compare(negatives, positives)
