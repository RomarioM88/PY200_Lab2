class Book:
    def __init__(self, id, name, pages):
        self.id = id
        self.name = name
        self.pages = pages
    def __str__(self):
        return f'Книга "{self.name}"'
    def __repr__(self):
        return f'Book(id = {self.id!r}, name = {self.name!r}, pages = {self.pages!r})'

if __name__ == '__main__':
    book = Book(1, "NAME1", 200)
    book2 = Book(2, "NAME2", 500)
    array = [book, book2]
    for i in array:
        print(i)
    print(repr(array))