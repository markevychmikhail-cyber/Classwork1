import string

class Alphabet:
    """
    Клас представляє алфавіт для заданої мови.
    """

    def __init__(self, lang, letters):
        """
        Ініціалізує алфавіт заданої мови.

        :param lang: рядок з назвою мови
        :param letters: список літер алфавіту
        """
        self.lang = lang
        self.letters = list(letters)

    def print(self):
        """
        Виводить список літер алфавіту.
        """
        print(self.letters)

    def letters_num(self):
        """
        Повертає кількість літер у алфавіті.

        :return: int
        """
        return len(self.letters)

class EngAlphabet(Alphabet):
    """
    Клас англійського алфавіту.
    """
    _letters_num = 26

    def __init__(self):
        """
        Ініціалізує англійський алфавіт.
        """
        super().__init__('En', string.ascii_uppercase)

    def is_en_letter(self, letter):
        """
        Перевіряє, чи є літера англійською (у верхньому регістрі).

        :param letter: літера для перевірки
        :return: bool
        """
        return letter.upper() in self.letters

    def letters_num(self):
        """
        Повертає кількість літер в англійському алфавіті.

        :return: int
        """
        return self._letters_num

    @staticmethod
    def example():
        """
        Повертає приклад англійського тексту.

        :return: str
        """
        return "English Example:\nDon't judge a book by it's cover."