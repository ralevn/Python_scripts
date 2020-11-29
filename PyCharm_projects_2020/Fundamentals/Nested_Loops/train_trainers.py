juri_num = int(input())

presentation_name = ''
overall_mark = 0
presentation_num = 0

while presentation_name != 'Finish':
    presentation_name = input()
    tot_mark = 0
    if presentation_name == 'Finish':
        break
    for i in range(juri_num):
        mark = float(input())
        tot_mark += mark
        overall_mark += mark
        presentation_num += 1
    print(f'{presentation_name} - {tot_mark / juri_num:.2f}.')

print(f'Student\'s final assessment is {overall_mark / presentation_num:.2f}.')
