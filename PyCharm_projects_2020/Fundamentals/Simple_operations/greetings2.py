f_name, s_name, age = input(), input(), int(input())
#### 1st method
text = f"{f_name} {s_name} {age - 10}"
print(text)
#### 2nd method
print('my name is %20s %s and I am %d old' % (f_name, s_name, age + 5))
#### 3d Method
print("Once upon a time {0} also know as {1}. \nWhen he was already {2} happened something".format(f_name, s_name, age))
#### 4th Method
story = "there once was him: {0} {1}. he was at that time {2} years old.\n Then {0} was a strong young man"
print(story.format(f_name, s_name, age))
