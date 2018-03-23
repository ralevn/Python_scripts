"""A module for demonstrating exceptions."""

def convert(s):
    "Convert to an integer"""
    try:
        x = int(s)
        print("Conversion success!!!\n")
    except ValueError:
        print("Converion failed!\n")
        x = -1
    return x
