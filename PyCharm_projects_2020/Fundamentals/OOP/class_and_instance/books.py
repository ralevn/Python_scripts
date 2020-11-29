class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{book1.title}, {book1.author}, {book1.pages}'

    def __repr__(self):
        return (book1.title, book1.author, book1.pages)


book1 = Book("Inception", "Gor Vidal", 460)

print('print(book1)           :', book1)
print("print(book1.__str__()) :", book1.__str__())
print("print(book1.__repr__()): ", book1.__repr__())
print(f'Title: {book1.title}\nAuthor: {book1.author}\nNumber of pages: {book1.pages}')


"""
!!!!
Difference between __str__ and __repr__ functions
1. __str__ must return string object whereas __repr__ can return any python expression.
2. If __str__ implementation is missing then __repr__ function is used as fallback. There is no fallback if __repr__ function implementation is missing.
3. If __repr__ function is returning String representation of the object, we can skip implementation of __str__ function.
"""