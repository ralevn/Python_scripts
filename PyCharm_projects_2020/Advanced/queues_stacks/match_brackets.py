text = input()
opening_brackets = []

for i in range(len(text)):
    if text[i] == "(":
        opening_brackets.append(i)              ## keep the index of opening brackets
    elif text[i] == ")":
        start_index = opening_brackets.pop()    ## the start index will be = the last entered "(" and popped out
        print(text[start_index:i + 1])          ## print everything from last entered/remained "(" to current index
