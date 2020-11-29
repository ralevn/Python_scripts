def is_awsome(name):
    return name == 'python'  ## returns True only if supplied name == 'python'

programing_languages = ['c++', 'java script', 'java', 'c#', 'python']

filter(is_awsome, programing_languages) ## every item in the iterable is passed as argument to the function

good_languages = list(filter(is_awsome, programing_languages))

print(programing_languages, good_languages)