stud=[]
grades =[]
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    stud.append(name)
    grades.append(score)
sndgrade = min([g for g in grades if g != min(grades)])
sndnames = [nam for nam,scor in zip(stud,grades) if scor == sndgrade]
for i in sorted(sndnames):
    print i
