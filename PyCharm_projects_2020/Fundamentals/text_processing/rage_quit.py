rq = input()

final_quit = []
tmp_tex = []
tmp_number = []
i = 0
result_text = ''

while i < len(rq):
    if not rq[i].isdigit():
        if not rq[i + 1].isdigit():
            tmp_tex.append(rq[i])
        else:
            tmp_tex.append(rq[i])
            final_quit.append(''.join(tmp_tex).upper())
            tmp_tex = []
    elif rq[i].isdigit():
        if i + 1 < len(rq):
            if not rq[i + 1].isdigit():
                tmp_number.append(rq[i])
                final_quit.append(int(''.join(tmp_number)))
                tmp_number = []
            else:
                tmp_number.append(rq[i])
        else:
            tmp_number.append(rq[i])
            final_quit.append(int(''.join(tmp_number)))
    i += 1

# print(final_quit)

for i in range(0, len(final_quit), 2):
        result_text += final_quit[i] * final_quit[i + 1]
print(f'Unique symbols used: {len(set(result_text))}')
print(result_text)