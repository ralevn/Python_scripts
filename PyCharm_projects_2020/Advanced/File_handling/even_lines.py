def print_line(txt):
    lt = []
    words = [w for w in txt.split()]
    for w in words:
        word = list(w)
        lt.append(word)
    for w in lt:
        for i in range(len(w)):
            if w[i] in {"-", ",", ".", "!", "?"}:
                w[i] = '@'
    for w in lt[::-1]:
        print(''.join(w), end=' ')


file = open('text.txt', 'r')
ind = 0
while True:
    line = file.readline()
    if not line:
        break
    if ind % 2 == 0:
        print_line(line)
        print()
    ind += 1

file.close()


