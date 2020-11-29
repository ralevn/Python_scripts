def check_validity(text: str):
    is_valid = True
    if not (3 <= len(text) <= 16):
        is_valid = False
        return is_valid
    for ch in text:
        if not (ch.isalnum() or ch == '-' or ch == '_'):
            is_valid = False
            break
    return is_valid


user_names = input().split(', ')

for word in user_names:
    if check_validity(word):
        print(word)

