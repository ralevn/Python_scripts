students = {}
languages = {}

submission = input()
while submission != 'exam finished':
    if submission.count('-') == 2:
        user_name = submission.split('-')[0]
        language = submission.split('-')[1]
        points = int(submission.split('-')[2])
        if user_name not in students:
            students[user_name] = ''
            students[user_name] = points
        else:
            if students[user_name] <= points:
                students[user_name] = points
        if language not in languages:
            languages[language] = 0
        languages[language] += 1

    elif submission.count('-') == 1:
        user_name = submission.split('-')[0]
        if user_name in students:
            students.pop(user_name)
    submission = input()

sorted_students = sorted(students.items(), key=lambda s: (-s[1], s[0]))
sorted_languages = sorted(languages.items(), key=lambda l: (-l[1], l[0]))

print('Results:')
for s, p in sorted_students:
    print(f'{s} | {p}')
print('Submissions:')
for l, p in sorted_languages:
    print(f'{l} - {p}')

