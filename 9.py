class Book:
    """
    Клас, що представляє книгу з назвою, автором та унікальним ідентифікатором.
    """
    next_id = 1

    def __init__(self, title, author):
        """
        Ініціалізує книгу.
        :param title: Назва книги
        :param author: Автор книги
        """
        self.title = title
        self.author = author
        self.book_id = Book.next_id
        Book.next_id += 1

    def __str__(self):
        """
        Рядкове представлення книги.
        :return: Форматований рядок
        """
        return f"[{self.book_id}] '{self.title}' - {self.author}"


class Reader:
    """
    Клас, що представляє читача бібліотеки.
    """
    next_id = 1

    def __init__(self, name):
        """
        Ініціалізує читача.
        :param name: Ім'я читача
        """
        self.name = name
        self.reader_id = Reader.next_id
        Reader.next_id += 1
        self.borrowed_books = []

    def borrow_book(self, book):
        """
        Додає книгу до списку взятих книг.
        :param book: Об'єкт Book
        """
        self.borrowed_books.append(book)

    def return_book(self, book):
        """
        Видаляє книгу зі списку взятих книг.
        :param book: Об'єкт Book
        """
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)


class Library:
    """
    Клас для управління бібліотекою — книги, читачі, видача і повернення.
    """

    def __init__(self):
        """
        Створює порожню бібліотеку.
        """
        self.books = {}
        self.readers = {}
        self.borrowed = {}  # book_id: reader_id

    def add_book(self, book):
        """
        Додає книгу у бібліотеку.
        :param book: Об'єкт Book
        """
        self.books[book.book_id] = book

    def register_reader(self, reader):
        """
        Реєструє нового читача.
        :param reader: Об'єкт Reader
        """
        self.readers[reader.reader_id] = reader

    def lend_book(self, book_id, reader_id):
        """
        Видає книгу читачеві, якщо можливо.
        :param book_id: ID книги
        :param reader_id: ID читача
        """
        if book_id not in self.books:
            print(f"Книга з ID {book_id} не існує.")
            return
        if reader_id not in self.readers:
            print(f"Читач з ID {reader_id} не зареєстрований.")
            return
        if book_id in self.borrowed:
            print(f"Книга '{self.books[book_id].title}' вже видана.")
            return
        reader = self.readers[reader_id]
        book = self.books[book_id]
        reader.borrow_book(book)
        self.borrowed[book_id] = reader_id
        print(f"Книга '{book.title}' видана {reader.name}.")

    def accept_return(self, book_id, reader_id):
        """
        Приймає повернення книги від читача.
        :param book_id: ID книги
        :param reader_id: ID читача
        """
        if book_id not in self.borrowed:
            print(f"Книга з ID {book_id} не була видана.")
            return
        if self.borrowed.get(book_id) != reader_id:
            print(f"Книга з ID {book_id} не у читача {reader_id}.")
            return
        reader = self.readers[reader_id]
        book = self.books[book_id]
        reader.return_book(book)
        del self.borrowed[book_id]
        print(f"Книга '{book.title}' повернена до бібліотеки.")

    def show_available_books(self):
        """
        Показує всі доступні книги.
        """
        available = [book for book_id, book in self.books.items() if book_id not in self.borrowed]
        print("Доступні книги:")
        for book in available:
            print(book)

    def show_borrowed_books(self):
        """
        Показує всі видані книги з вказанням читача.
        """
        print("Видані книги:")
        for book_id, reader_id in self.borrowed.items():
            book = self.books[book_id]
            reader = self.readers[reader_id]
            print(f"{book} -> {reader.name}")

if __name__ == '__main__':
    # Створюємо бібліотеку
    lib = Library()

    # Додаємо книги
    b1 = Book("1984", "George Orwell")
    b2 = Book("Кобзар", "Тарас Шевченко")
    b3 = Book("Майстер і Маргарита", "М.Булгаков")
    b4 = Book("To Kill a Mockingbird", "Harper Lee")
    for b in (b1, b2, b3, b4):
        lib.add_book(b)

    # Реєструємо читачів
    r1 = Reader("Аліса")
    r2 = Reader("Богдан")
    lib.register_reader(r1)
    lib.register_reader(r2)

    # Видаємо книги
    lib.lend_book(b1.book_id, r1.reader_id)       # 1984 -> Аліса
    lib.lend_book(b2.book_id, r2.reader_id)       # Кобзар -> Богдан
    lib.lend_book(b3.book_id, r2.reader_id)       # Майстер і Маргарита -> Богдан

    # Спроба видати вже видану книгу
    lib.lend_book(b1.book_id, r2.reader_id)       # 1984 вже видана

    # Показати доступні книги
    lib.show_available_books()

    # Показати видані книги (детально)
    lib.show_borrowed_books()

    # Один читач повертає книгу
    lib.accept_return(b2.book_id, r2.reader_id)   # Богдан повертає "Кобзар"

    # Доступні книги після повернення
    lib.show_available_books()