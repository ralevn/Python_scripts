def palindrome(word, ix):
    if word == word[::-1]:
        return f'{word} is a palindrome'
    else:
        return f'{word} is not a palindrome'


print(palindrome("abcba", 0))
print(palindrome("peter", 0))

