def is_palindrome(text):
    return text[::-1]

string = input().split(' ')
searched_word = input()

found =[word for word in string if word == is_palindrome(word)]

print(found)
print(f'Found palindrome {found.count(searched_word)} times')