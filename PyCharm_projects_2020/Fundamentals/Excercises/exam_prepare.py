n_poor_scores = int(input())
failed_n = 0
problem_n = 0
tot_score = 0
last_prb_name = ''
is_failed = True

while failed_n < n_poor_scores:
    problem_name = input()
    if problem_name == 'Enough': is_failed = False; break
    score = int(input())
    if score <= 4:
        failed_n += 1
    tot_score += score
    problem_n += 1
    last_prb_name = problem_name
if is_failed: print (f'You need a break, {failed_n} poor grades.')
else: print (f'Average score: {tot_score / problem_n:.2f}\nNumber of problems: {problem_n}\nLast problem: {last_prb_name}')
