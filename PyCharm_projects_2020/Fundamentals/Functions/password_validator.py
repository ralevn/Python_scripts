def password_length (string):
    if 6 <= len(string) <= 10:
        return True
    else:
        return False

def password_digits (string):
    digits = 0
    for i in string:
        if 48 <= ord(i) <= 57:
            digits += 1
    if digits < 2:
        return False
    else:
        return True

def password_chars (string):
    is_valid = True
    for ch in string:
        if not ((48 <= ord(ch) <= 57) or
                (65 <= ord(ch) <= 90) or
                (97 <= ord(ch) <= 122)):
            is_valid = False
            break
    return is_valid


password = input()

if not password_length(password):
    print("Password must be between 6 and 10 characters")
if not password_chars(password):
    print("Password must consist only of letters and digits")
if not password_digits(password):
    print("Password must have at least 2 digits")

if password_length(password) and password_chars(password) and password_digits(password):
    print("Password is valid")