import doctest

class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        """
        Инициализация экземпляра класса.
        :param name: Название книги
        :param author: Автор книги
        Пример:
        >>> test_book = Book("Пиши, сокращай", "М. Ильяхов")
        """
        self._name = name
        self._author = author

    def __str__(self):
        """
        Метод возвращает строку для чтения.
        Пример:
        >>> test_book = Book("Пиши, сокращай", "М. Ильяхов")
        >>> print(test_book)
        """
        return f"Книга {self._name}; Автор {self._author}"

    def __repr__(self):
        """
        Метод возвращает строку, показывающую, как может быть инициализирован экземпляр.
        Пример:
        >>> test_book = Book("Пиши, сокращай", "М. Ильяхов")
        >>> print(repr(test_book))
        """
        return f"{self.__class__.__name__}(name = {self._name!r}, author = {self._author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

class PaperBook(Book):
    """ Класс бумажной книги. Является подклассом базовой книги """

    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализация экземпляра класса.
        :param name: Название книги
        :param author: Автор книги
        :param pages: Количество страниц книги
        Пример:
        >>> test_paper = PaperBook("Пиши, сокращай", "М. Ильяхов", 200)
        """
        super().__init__(name, author)
        if isinstance(pages, int):
            if pages > 0:
                self._pages = pages
            else:
                raise ValueError("Число страниц должно быть положительным числом")
        else:
            raise TypeError("Количество страниц должно быть типа int")

    @property
    def pages(self):
        return self._pages

    def __str__(self):
        """
        Метод возвращает строку для чтения. Метод был перегружен в связи с появлением нового атрибута.
        Пример:
        >>> test_paper = PaperBook("Пиши, сокращай", "М. Ильяхов", 200)
        >>> print(test_paper)
        """
        s_str = super().__str__()
        return f"{s_str}; Страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name = {self._name!r}, author = {self._author!r}, duration = {self._pages!r})"

class AudioBook(Book):
    """ Класс аудио книги. Является подклассом базовой книги """

    def __init__(self, name: str, author: str, duration: float):
        """
        Инициализация экземпляра класса.
        :param name: Название книги
        :param author: Автор книги
        :param duration: Продолжительность аудио книги
        Пример:
        >>> test_audio = AudioBook("Пиши, сокращай", "М. Ильяхов", 200.00)
        """
        super().__init__(name, author)
        if isinstance(duration, float):
            if duration > 0:
                self._duration = duration
            else:
                raise ValueError("Продолжительность должна быть положительным числом")
        else:
            raise TypeError("Продолжительность должно быть типа float")

    @property
    def duration(self):
        return self._duration

    def __str__(self):
        """
        Метод возвращает строку для чтения. Метод был перегружен в связи с появлением нового атрибута.
        Пример:
        >>> test_audio = AudioBook("Пиши, сокращай", "М. Ильяхов", 200.00)
        >>> print(test_audio)
        """
        s_str = super().__str__()
        return f"{s_str}; Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name = {self._name!r}, author = {self._author!r}, duration = {self._duration!r})"

if __name__ == "__main__":
    test_book = Book("Пиши, сокращай", "М. Ильяхов")
    test_paper = PaperBook("Пиши, сокращай", "М. Ильяхов", 200)
    test_audio = AudioBook("Пиши, сокращай", "М. Ильяхов", 200.00)
    print(repr(test_paper))
    doctest.testmod()
    pass
    
