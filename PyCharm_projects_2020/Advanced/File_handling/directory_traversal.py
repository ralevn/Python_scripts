import os

current_dir = os.getcwd()
files = os.listdir(current_dir)
for item in files:
    if os.path.isdir(item):
        files.remove(item)

f_types = {}

for file in files:
    ext = os.path.splitext(file)[-1]
    if ext not in f_types:
        f_types[ext] = []
    else:
        f_types[ext].append(file)

with open('report.txt', 'w') as report_file:
    for typ, f_list in f_types.items():
        report_file.write(f'\n{typ}\n')
        for f in f_list:
            report_file.write(f'- - - {f}\n')