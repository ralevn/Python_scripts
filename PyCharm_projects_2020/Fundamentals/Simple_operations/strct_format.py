text='The architect {0} will need {1} hours to complete {2} project/s.'
name=input()
n_projects = int(input())

print(text.format(name,n_projects*3,n_projects))

# print('Architect %s will need %d hours to complete %d projects.' %(name, n_projects*3, n_projects))