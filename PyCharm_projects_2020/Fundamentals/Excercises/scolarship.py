income, grade, min_pay = float(input()), float(input()), float(input())

social_scolarship = 0.0
merit_scolarship = 0.0

if income < min_pay and grade > 4.5:
    social_scolarship = min_pay * 0.35

if grade >= 5.5:
    merit_scolarship = grade * 25

scolarship = max(social_scolarship, merit_scolarship)
# print (scolarship)

if scolarship == 0.0:
    print('You cannot get a scholarship!')
elif social_scolarship > merit_scolarship:
    print(f'You get a Social scholarship {int(scolarship)} BGN')
elif merit_scolarship >= social_scolarship:
    print(f'You get a scholarship for excellent results {int(scolarship)} BGN')

