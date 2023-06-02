class Library:
    def __init__(self, books = None):
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        if len(self.books) == 0:
            return 1
        else:
            last_book_id = self.books[-1]['id']
            return last_book_id + 1

    def get_index_by_book_id(self, book_id):
        for i in range(len(self.books)):
            if self.books[i]['id'] == book_id:
                return i
            raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()
    list_books = [{"id": 1, "name": "test_name_1", "pages": 200}, {"id": 2, "name": "test_name_2", "pages": 400}]
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки
    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1