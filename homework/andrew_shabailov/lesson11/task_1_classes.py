class Book:
    material = 'бумага'
    text = True

    def __init__(self, book_name: str, author: str, pages: int, isbn: str):
        self.book_name = book_name
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.is_reserved = False

    def details(self):
        if self.is_reserved:
            print(
                f'Название: {self.book_name}, Автор: {self.author}, '
                f'страниц: {self.pages}, материал: {self.material}, '
                f'зарезервирована'
            )
        else:
            print(
                f'Название: {self.book_name}, Автор: {self.author}, '
                f'страниц: {self.pages}, материал: {self.material}'
            )


martin_iden = Book('Мартин Иден', 'Джек Лондон', 448, '43243435')
idiot = Book('Идиот', 'Фёдор Достоевский', 640, '546547547')
war_and_peace = Book('Война и мир', 'Лев Толстой', 1274, '6756756757')
evgeny_onegin = Book('Евгений Онегин', 'Александр Пушкин', 224, '56756756756')
grandfather = Book('Дедушка', 'Николай Некрасов', 18, '4645654654')

martin_iden.is_reserved = True

books_list = [martin_iden, idiot, war_and_peace, evgeny_onegin, grandfather]

for book in books_list:
    book.details()


class SchoolBook(Book):
    def __init__(
        self,
        book_name: str,
        author: str,
        pages: int,
        isbn: str,
        subject: str,
        school_class: int,
        tasks: bool,
    ):
        super().__init__(book_name, author, pages, isbn)
        self.subject = subject
        self.school_class = school_class
        self.tasks = tasks

    def details2(self):
        if self.is_reserved:
            print(
                f'Название: {self.book_name}, Автор: {self.author}, '
                f'страниц: {self.pages}, предмет: {self.subject}, '
                f'класс: {self.school_class}, зарезервирована'
            )
        else:
            print(
                f'Название: {self.book_name}, Автор: {self.author}, '
                f'страниц: {self.pages}, предмет: {self.subject}, '
                f'класс: {self.school_class}'
            )


algebra = SchoolBook(
    'Алгебра',
    'Иванов',
    200,
    '111111',
    'Математика',
    9,
    True,
)

history = SchoolBook(
    'История древнего мира',
    'Петров',
    300,
    '11111222',
    'История',
    4,
    True,
)

psychology = SchoolBook(
    'Психология личности',
    'Сидоров',
    400,
    '11114411',
    'Психология',
    11,
    True,
)

geography = SchoolBook(
    'География морей',
    'Шпак',
    220,
    '1116111',
    'География',
    8,
    True,
)

physic = SchoolBook(
    'Физика машин',
    'Андреев',
    700,
    '77777',
    'Физика',
    11,
    True,
)

school_books_list = [
    algebra,
    history,
    psychology,
    geography,
    physic,
]

for school_book in school_books_list:
    school_book.details2()
