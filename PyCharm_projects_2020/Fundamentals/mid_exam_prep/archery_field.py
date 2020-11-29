field = [int(n) for n in input().split('|')]

def find_index_right(start, length, listi):
    ind = (start + length) % len(listi)
    return ind

def find_index_left(start, length, listi):
    ind = len(listi) - (len(listi) - ((start - length) % len(listi)))
    return ind
